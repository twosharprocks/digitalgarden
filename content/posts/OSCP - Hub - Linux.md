---
title: OSCP - Hub - Linux
created: 2026-01-26
updated: 2026-01-22
status: seed
draft: false
tags:
  - cyber-security
Related: "[[Cybersecurity]]"
---
# Hub
This was a bit of an odd one that required more than a few reverts. Identifying that FuguForum was the target (not barracuda as initially suspected) was a nice realisation that I'm picking up on the details that I need to, and that searching for exploits is becoming a more common and clear thing to do. 

What was really frustrating was finding that none of those exploit actually work, and then needing to dig into the website to write a reverse shell into page. So much of this box didn't work properly, and what should have been straight forward was unnecessarily difficult - not because it was secure, but because it simply wasn't working properly. Even once I managed to get a shell, there was no way to upgrade it to full TTY, so once I had root through a binary exploit, I was still stuck with a shitty shell.

If this was for real, I would have spent a lot longer on it making sure I could get much easier access (the website was wide open anyway) but even getting the basics seemed way harder than it should have been because of things not working.

# Resolution summary
- Scanned with NMap
- Identified website on port 8082
- Set admin credentials, uploaded reverse shell to "About" page
- Navigated to "About" page and caught reverse shell as `root`
- Printed `proof.txt` from `/root` folder
## Improved skills
- Creating reverse shells for webpages running lsp (lua)
- Finding and testing exploits
- Finding alternative ways to establish shell without a public exploit
## Used tools
- nmap
- netcat
- revshells.com

---
# Information Gathering
Scanned all TCP ports:
```bash
sudo nmap -sC -sV -oN hub.nmap 192.168.228.25 -v
```

Enumerated open TCP ports:
```bash
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
| ssh-hostkey: 
|   3072 c9:c3:da:15:28:3b:f1:f8:9a:36:df:4d:36:6b:a7:44 (RSA)
|   256 26:03:2b:f6:da:90:1d:1b:ec:8d:8f:8d:1e:7e:3d:6b (ECDSA)
|_  256 fb:43:b2:b0:19:2f:d3:f6:bc:aa:60:67:ab:c1:af:37 (ED25519)
80/tcp   open  http     nginx 1.18.0
|_http-server-header: nginx/1.18.0
|_http-title: 403 Forbidden
| http-methods: 
|_  Supported Methods: GET HEAD POST
8082/tcp open  http     Barracuda Embedded Web Server
| http-methods: 
|   Supported Methods: OPTIONS GET HEAD PROPFIND PATCH POST PUT COPY DELETE MOVE MKCOL PROPPATCH LOCK UNLOCK
|_  Potentially risky methods: PROPFIND PATCH PUT COPY DELETE MOVE MKCOL PROPPATCH LOCK UNLOCK
|_http-title: Home
|_http-favicon: Unknown favicon MD5: FDF624762222B41E2767954032B6F1FF
| http-webdav-scan: 
|   Server Type: BarracudaServer.com (Posix)
|   Allowed Methods: OPTIONS, GET, HEAD, PROPFIND, PATCH, POST, PUT, COPY, DELETE, MOVE, MKCOL, PROPFIND, PROPPATCH, LOCK, UNLOCK
|   Server Date: Sat, 05 Oct 2024 04:56:13 GMT
|_  WebDAV type: Unknown
|_http-server-header: BarracudaServer.com (Posix)
9999/tcp open  ssl/http Barracuda Embedded Web Server
| ssl-cert: Subject: commonName=FuguHub/stateOrProvinceName=California/countryName=US
| Subject Alternative Name: DNS:FuguHub, DNS:FuguHub.local, DNS:localhost
| Issuer: commonName=Real Time Logic Root CA/organizationName=Real Time Logic LLC/countryName=US
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2019-07-16T19:15:09
| Not valid after:  2074-04-18T19:15:09
| MD5:   6320:2067:19be:be32:18ce:3a61:e872:cc3f
|_SHA-1: 503c:a62d:8a8c:f8c1:6555:ec50:77d1:73cc:0865:ec62
| http-methods: 
|   Supported Methods: OPTIONS GET HEAD PROPFIND PATCH POST PUT COPY DELETE MOVE MKCOL PROPPATCH LOCK UNLOCK
|_  Potentially risky methods: PROPFIND PATCH PUT COPY DELETE MOVE MKCOL PROPPATCH LOCK UNLOCK
|_http-server-header: BarracudaServer.com (Posix)
|_http-favicon: Unknown favicon MD5: FDF624762222B41E2767954032B6F1FF
| http-webdav-scan: 
|   Server Type: BarracudaServer.com (Posix)
|   Allowed Methods: OPTIONS, GET, HEAD, PROPFIND, PATCH, POST, PUT, COPY, DELETE, MOVE, MKCOL, PROPFIND, PROPPATCH, LOCK, UNLOCK
|   Server Date: Sat, 05 Oct 2024 04:56:14 GMT
|_  WebDAV type: Unknown
|_http-title: Home
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

---
# Enumeration
## Port 22 - SSH (OpenSSH 8.4p1)
No enumeration conducted
## Port 80 - HTTP (nginx 1.18)
- Navigated to `192.168.228.25:80` with FireFox 
  `403 Forbidden` for nginix/1.18.0
![OSCP Hub Linux Image1](/images/OSCP%20-%20Hub%20-%20Linux%20-%20image1.png)
## Port 8082 - HTTP (Barracuda Web Server)
- Navigated to `192.168.228.25:8082` with FireFox
  Default landing page for FuguHub, redirected to "set Administrator Account"
  Set admin account as `admin:password`
  ![OSCP Hub Linux Image2](/images/OSCP%20-%20Hub%20-%20Linux%20-%20image2.png)
## Port 9999 - HTTP (Barracuda Web Server)
No enumeration conducted

---
# Exploitation
## Malicious File Upload
- Used newly set admin credentials to "Customize Server"
![OSCP Hub Linux Image3](/images/OSCP%20-%20Hub%20-%20Linux%20-%20image3.png)
- Added lsp payload to About page for reverse shell
![OSCP Hub Linux Image4](/images/OSCP%20-%20Hub%20-%20Linux%20-%20image4.png)
- Navigated to "About" page and caught reverse shell with Netcat listener
![OSCP Hub Linux Image5](/images/OSCP%20-%20Hub%20-%20Linux%20-%20image5.png)
- Attempted to print `proof.txt` in `/root` directory
![OSCP Hub Linux Image6](/images/OSCP%20-%20Hub%20-%20Linux%20-%20image6.png)
---
# Trophy & Loot
`proof.txt` = `ffeee8550bcb0d874f6f01a7c072b9aa`

