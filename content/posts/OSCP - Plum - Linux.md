---
title: OSCP - Plum - Linux
created: 2026-01-26
updated: 2025-10-28
status: seed
draft: false
tags:
  - cyber-security
Related: "[[Cybersecurity]]"
---
# Plum
This one was relatively easy to achieve initial access on, but enumerating the target once I had initial access was frustrating. I'd learned on the previous box that I could pull up locally stored mail by visiting `/var/mail` but hadn't quite realised that it should be part of my standard privesc process. 

Anyway, once I got the nudge from the walkthrough to check mail, it became straight-forward to switch to root and grab the flag, but 100% an important lesson in seeing the `var/mail/www-data` in the `Linpeas` output and being sure to read the mail incase there's anything important or useful (like credentials) saved there.

# Resolution summary
-  Ran Nmap to identify ports `22` & `80`
- Visited html (`80`) & identified `pluxml`
- Password-guess access to admin console, navigated to "Static Pages"
- Replaced static page content with PHP reverse shell script
- Visited static page address and received reverse shell
- Enumerated target, identified `var/mail/www-data`
- Viewed `var/mail/www-data` and identified credentials for `root`
- Switched user to `root` with found credentials and printed `proof.txt`
## Improved skills
- Enumerating local files
- Finding Proof-of-Concept exploits
## Used tools
- nmap
- gobuster
- revshells.com
- linpeas.sh

---
# Information Gathering
Scanned all TCP ports:
```bash
sudo nmap -sC -sV -oN plum.nmap 192.168.164.28 -v
```

Enumerated open TCP ports:
```bash
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
| ssh-hostkey: 
|   3072 c9:c3:da:15:28:3b:f1:f8:9a:36:df:4d:36:6b:a7:44 (RSA)
|   256 26:03:2b:f6:da:90:1d:1b:ec:8d:8f:8d:1e:7e:3d:6b (ECDSA)
|_  256 fb:43:b2:b0:19:2f:d3:f6:bc:aa:60:67:ab:c1:af:37 (ED25519)
80/tcp open  http    Apache httpd 2.4.56 ((Debian))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: PluXml - Blog or CMS, XML powered !
|_http-server-header: Apache/2.4.56 (Debian)
|_http-favicon: Unknown favicon MD5: 2D58FC0104110AF4C9BE979DFD8FD83C
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
---
# Enumeration
## Port 22 - SSH (OpenSSH 7.9p1)
No enumeration conducted
## Port 80 - HTTP (Apache)
- Navigated to `http://192.168.164.28:80` and identified `Pluxml`
![OSCP Plum Linux Image1](/images/OSCP%20-%20Plum%20-%20Linux%20-%20image1.png)
	- Potentially vulnerable to CVE-2022-25018
	- Potentially vulnerable to CVE-2024-22636
- Ran `gobuster dir -u http://192.168.164.28 -w //usr/share/dirb/wordlists/big.txt` to identify other web directories
![OSCP Plum Linux Image2](/images/OSCP%20-%20Plum%20-%20Linux%20-%20image2.png)
- Navigated to `http://192.168.164.28:80/core/admin` then password guessed credentials `admin:admin` for administrator panel access
![OSCP Plum Linux Image3](/images/OSCP%20-%20Plum%20-%20Linux%20-%20image3.png)

---
# Exploitation
- Navigated to "Static pages" (http://192.168.164.28/core/admin/statiques.php) and selected "Edit" for static page 001
![OSCP Plum Linux Image4](/images/OSCP%20-%20Plum%20-%20Linux%20-%20image4.png)
- Replaced PHP code with reverse shell script and saved page
![OSCP Plum Linux Image5](/images/OSCP%20-%20Plum%20-%20Linux%20-%20image5.png)
- Started netcat listener with `nc -nvlp 4444` then navigated to `http://192.168.164.28/index.php?static1/static-1` and caught reverse shell
![OSCP Plum Linux Image6](/images/OSCP%20-%20Plum%20-%20Linux%20-%20image6.png)
- Navigated to home directory of `www-data` and ran `cat /var/www/local.txt` to print `7d958bdaf701e8151b53669070f6cfc2`
![OSCP Plum Linux Image7](/images/OSCP%20-%20Plum%20-%20Linux%20-%20image7.png)
---
# Privilege Escalation
## Local Enumeration
- Ran `cat /etc/passwd` to identify any other users
![OSCP Plum Linux Image8](/images/OSCP%20-%20Plum%20-%20Linux%20-%20image8.png)
- Ran `sudo -l` and identified `www-data` requires password to run `sudo`
![OSCP Plum Linux Image9](/images/OSCP%20-%20Plum%20-%20Linux%20-%20image9.png)
- Downloaded `linpeas.sh` to target machine and ran `./linpeas.sh`
![OSCP Plum Linux Image10](/images/OSCP%20-%20Plum%20-%20Linux%20-%20image10.png)
- Identified files with interesting permissions
![OSCP Plum Linux Image11](/images/OSCP%20-%20Plum%20-%20Linux%20-%20image11.png)
- Identified interesting SGIDs
![OSCP Plum Linux Image12](/images/OSCP%20-%20Plum%20-%20Linux%20-%20image12.png)
- Interesting files in others home
![OSCP Plum Linux Image13](/images/OSCP%20-%20Plum%20-%20Linux%20-%20image13.png)
## Privilege Escalation vector
- Identified `exim4` as mail service, so navigated to `/var/mail` to check any available mail
![OSCP Plum Linux Image14](/images/OSCP%20-%20Plum%20-%20Linux%20-%20image14.png)
- Identified and viewed mail for user `www-data` with command `cat /var/mail/www-data`
![OSCP Plum Linux Image15](/images/OSCP%20-%20Plum%20-%20Linux%20-%20image15.png)
- Identified credentials `root:6s8kaZZNaZZYBMfh2YEW`
- Ran `su root` to switch user to `root` with found credentials, and ran `cat /root/proof.txt` to print `cc1ebf8f904c8fcdc19afe9026e75ceb`
![OSCP Plum Linux Image16](/images/OSCP%20-%20Plum%20-%20Linux%20-%20image16.png)

---
# Trophy & Loot
`local.txt` = `7d958bdaf701e8151b53669070f6cfc2`
`root.txt` = `cc1ebf8f904c8fcdc19afe9026e75ceb`
