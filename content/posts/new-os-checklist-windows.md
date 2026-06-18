---
title: New OS Checklist
created: 2025-12-29
updated: 2026-02-24
status: seed
draft: false
tags:
  - Cybersecurity
Related:
---
Related: Personal

---


# Windows
Format
- *Reset*: Settings > System > Recovery
- *USB Install* 

Run
- [ ] O&O ShutUp10++
- [ ] Chocolatey
## Chocolatey
*Initial Install* 
- Run Powershell as Administrator*
```
Set-ExecutionPolicy Bypass -Scope Process -Force
```

```
[System.Net.ServicePointManager]::SecurityProtocol = `
[System.Net.ServicePointManager]::SecurityProtocol -bor 3072; `
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

```
- IMPORTANT: Close PowerShell completely 
- Reopen PowerShell, verify version
```
choco --version
```

*Install Apps*: 
```
choco install Chrome vlc obsidian notepadplusplus steam vscode greenshot -y
```
Standard Apps: Chrome googledrive vlc obsidian notepadplusplus steam vscode greenshot 

*Upgrade All Apps*
```
choco upgrade all -y
```

*Search for Apps*:
```
choco search git
```

*List Installed Chocolatey Apps*:
```
choco list --local-only
```

*Unistall*: 
```
choco uninstall vlc -y
```
# Other Apps 
- Brave Browser

---
**This also reminds me of**... 

---
# References

