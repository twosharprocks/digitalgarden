---
title: OSCP - Codo - Linux
created: 2026-01-26
updated: 2026-01-22
status: seed
draft: false
tags:
  - cyber-security
related: "[[Cyber Security]]"
---
# Codo
Interesting experience just slowly working through this over the day. Having the walkthrough as a reference is handy, although I should have done more enumeration to identify everything `linpeas` was providing. Helpful experience updating the cheatsheet for fully interactive TTS too - most references just use `python` when pretty much everyone/thing is using `python3`, so be sure to watch out for that when copy/pasting from references.

Keep revshells.com handy too, and keep practicing with msfvenom too, as a lot of your holdup today was trying to find the right reverse shell for php, when you should have just been able to pull it up in a heartbeat

# Resolution summary
- Port scan with Nmap, ID 22 & 80
- Found default CodoForum install - password guessed admin admin credentials
- Modified global settings to allow php upload
- Used CodoForum exploit for RCE to achieve local shell
- Upgraded shell to fully interactive TTS
- Enumerated to ID user `offsec`
- Ran `linpeas.sh` to find password `FatPanda123`
- Successfully password sprayed `FatPanda123` to switch to root user
## Improved skills
- Identifying vulnerable services
- Finding credentials through LinPeas enumeration

## Used tools
- nmap
- gobuster

---

# Information Gathering
Scanned all TCP ports:
```bash
sudo nmap -sC -sV -oN codo-nmap 192.168.210.23
```

Enumerated open TCP ports:
```bash
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 62:36:1a:5c:d3:e3:7b:e1:70:f8:a3:b3:1c:4c:24:38 (RSA)
|   256 ee:25:fc:23:66:05:c0:c1:ec:47:c6:bb:00:c7:4f:53 (ECDSA)
|_  256 83:5c:51:ac:32:e5:3a:21:7c:f6:c2:cd:93:68:58:d8 (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-title: All topics | CODOLOGIC
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 09:49
Completed NSE at 09:49, 0.00s elapsed
Initiating NSE at 09:49
Completed NSE at 09:49, 0.00s elapsed
Initiating NSE at 09:49
Completed NSE at 09:49, 0.00s elapsed
Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 23.33 seconds
           Raw packets sent: 2006 (88.240KB) | Rcvd: 7 (292B)
```

---
# Enumeration
## Port 22 - SSH (OpenSSH 8.2p1)
No enumeration conducted
## Port 80 - HTTP (Apache)
- Navigated to `192.168.210.23` to find Codologic default installation page
	- Username "admin"
	- CodoForum v5.1 has RCE vulnerability ([CVE-2022-31854](https://pentest-tools.com/vulnerabilities-exploits/codoforum-51-arbitrary-file-upload_3201))
![OSCP Codo Linux Image1](/images/OSCP%20-%20Codo%20-%20Linux%20-%20image1.png)
-  Found login page, tested credentials `admin:admin`, successfully logged in
![OSCP Codo Linux Image2](/images/OSCP%20-%20Codo%20-%20Linux%20-%20image2.png)
---
# Exploitation
- Accessed admin panel at `http://192.168.210.23/admin/`
![OSCP Codo Linux Image3](/images/OSCP%20-%20Codo%20-%20Linux%20-%20image3.png)
- Modified Global settings to allow php upload
![OSCP Codo Linux Image4](/images/OSCP%20-%20Codo%20-%20Linux%20-%20image4.png)
- Started netcat listener: `nc -nvlp 4444`
- Uploaded php with reverse shell to admin avatar
![OSCP Codo Linux Image5](/images/OSCP%20-%20Codo%20-%20Linux%20-%20image5.png)
- Caught reverse shell with netcat
![OSCP Codo Linux Image6](/images/OSCP%20-%20Codo%20-%20Linux%20-%20image6.png)
---
# Lateral Movement to user
## Local Enumeration
- Enumerated passwd file with `cat /etc/passwd` to find `offsec` user
![OSCP Codo Linux Image7](/images/OSCP%20-%20Codo%20-%20Linux%20-%20image7.png)
- Checked binaries with `find / -perm -4000 2>/dev/null`
![OSCP Codo Linux Image8](/images/OSCP%20-%20Codo%20-%20Linux%20-%20image8.png)
- Uploaded & ran `linpeas.sh`
![OSCP Codo Linux Image9](/images/OSCP%20-%20Codo%20-%20Linux%20-%20image9.png)
- Found cleartext password `FatPanda123`
![OSCP Codo Linux Image10](/images/OSCP%20-%20Codo%20-%20Linux%20-%20image10.png)
---
# Privilege Escalation

## Privilege Escalation vector
- Attempted to `su`to users `offsec` and `root` using password `FatPanda123`
![OSCP Codo Linux Image11](/images/OSCP%20-%20Codo%20-%20Linux%20-%20image11.png)
---
# Trophy & Loot
- Navigated to `/root` and printed available txt files
![OSCP Codo Linux Image12](/images/OSCP%20-%20Codo%20-%20Linux%20-%20image12.png)
`email2.txt` = `MTWlkW`
`root.txt` = `bbe0a8834e7c29db8c1a2813c6907ba6`

