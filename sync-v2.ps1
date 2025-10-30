# PowerShell Script for Windows — Option B (master as source, hostinger as deploy)
# - Copies from Obsidian "1 - Published" into Hugo /content/posts
# - Commits source to master
# - Builds the site
# - Publishes ONLY /public to branch `hostinger` via subtree split

# ---------- Config ----------
$sourcePath      = 'C:\Users\Josh\My Drive\Vaults\Digital-Garden\1 - Published'
$destinationPath = 'C:\Users\Josh\Documents\garden\content\posts'
$repoUrl         = 'https://github.com/twosharprocks/digitalgarden.git'
$deployBranch    = 'hostinger'
$sourceBranch    = 'master'
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

# ---------- Helper ----------
function Assert-Command($name) {
  if (-not (Get-Command $name -ErrorAction SilentlyContinue)) {
    throw "Required command not found on PATH: $name"
  }
}

# ---------- Start ----------
# 0) Run from the repo root (where .git lives). If the script is in the repo, lock to it.
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $ScriptDir
Write-Host "Working directory: $(Get-Location)"

# 1) Preconditions
Assert-Command git
Assert-Command hugo
Assert-Command robocopy

if (-not (Test-Path -LiteralPath $sourcePath))      { throw "Source path missing: $sourcePath" }
if (-not (Test-Path -LiteralPath $destinationPath)) { throw "Destination path missing: $destinationPath" }

# 2) Ensure we’re inside a Git repo with origin set
if (-not (git rev-parse --is-inside-work-tree 2>$null)) {
  Write-Host "Initializing git repo..."
  git init
}
if (-not ((git remote 2>$null) -contains 'origin')) {
  Write-Host "Adding remote origin -> $repoUrl"
  git remote add origin $repoUrl
}

# 3) Pull latest (don’t fail if branch missing remotely yet)
git fetch origin --prune
try {
  git checkout -B $sourceBranch origin/$sourceBranch
} catch {
  Write-Host "Remote $sourceBranch not found; creating local $sourceBranch."
  git checkout -B $sourceBranch
}

# 4) Copy Obsidian → Hugo (mirror; delete removed files)
Write-Host "Syncing Obsidian → Hugo: `"$sourcePath`" → `"$destinationPath`""
$srcCount = (Get-ChildItem -LiteralPath $sourcePath -File -Recurse | Measure-Object).Count
Write-Host "Source files: $srcCount"

robocopy $sourcePath $destinationPath *.* /MIR /NFL /NDL /NP /R:1 /W:1
if ($LASTEXITCODE -lt 0 -or $LASTEXITCODE -gt 7) { throw "Robocopy failed with code $LASTEXITCODE" }

# 5) Commit source on master
git status --porcelain=v1
git add -A

# If there are staged changes, commit & push
$staged = git diff --cached --name-only
if ($staged) {
  $stamp = Get-Date -Format "yyyy-MM-dd HH:mm"
  git commit -m "Source update from Obsidian → Hugo ($stamp)"
  git push -u origin $sourceBranch
} else {
  Write-Host "No source changes to commit on $sourceBranch."
}

# 6) Build site
Write-Host "Running Hugo build..."
hugo
if ($LASTEXITCODE -ne 0) { throw "Hugo build failed with code $LASTEXITCODE" }

# 7) Publish ONLY /public to hostinger via subtree
#    This creates a temporary branch from the /public subtree and force-pushes it to $deployBranch
Write-Host "Publishing /public → $deployBranch (subtree split)..."
# Clean up any old temp branch if present
if ((git branch --list _deploy_tmp) -ne $null) { git branch -D _deploy_tmp | Out-Null }

git subtree split --prefix public -b _deploy_tmp
git push -f origin _deploy_tmp:$deployBranch
git branch -D _deploy_tmp

# 8) Show remote info for sanity
git remote show origin

Write-Host "Done: source pushed to '$sourceBranch' and site deployed to '$deployBranch'."
