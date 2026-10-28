[CmdletBinding()]
param(
    [string]$VaultPath = (Join-Path $env:USERPROFILE 'My Drive\Vaults\Digital-Garden'),
    [switch]$SkipPush
)

# Keep the old entry point, using the same privacy checks as the main publisher.
& (Join-Path $PSScriptRoot 'sync.ps1') @PSBoundParameters
exit $LASTEXITCODE
