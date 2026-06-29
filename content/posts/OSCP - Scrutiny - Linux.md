---
title: OSCP - Scrutiny - Linux
created: 2026-01-26
updated: 2025-10-02
status: seed
draft: false
tags:
  - cyber-security
Related: "[[Cyber Security]]"
---
# Scrutiny
This whole box felt like a whole lot of enumeration - digging through files to find SSH keys and cleartext passwords. Probably the biggest lesson I learned out of it however was how to setup and run python libraries in a virtual environment! 

The exploit required `urllib3 faker` to run, and `python3` kept throwing the `externally managed` error that drove me crazy awhile back when I was trying to install the `bzz` library - I must have found another way around that, but this time around I actually dug into what this error was all about. Turns out `python` likes to run it's external libraries in a self-contained virtual environment, and while there is an override pretty much everyone on stackoverflow was screaming that it'd break the system.

So with that in mind, I managed to follow some straight forward instructions on starting the virtual environment: move to the environment folder, then `python -m venv my-venv` and `source bin/activate`. Installing libraries and running python is 10x easier now that I have that setup, and the exploit worked perfectly once it was in there.

Couple of really handy tricks for enumeration in this box too, which I definitely gleaned from the Youtube walkthrough. 
- Keep an eye out for SSH keys being accidentally committed to Git (and use `ssh2john` before you try to crack them)
- Running `find / -name local.txt -type f 2>/dev/null` to find the local flag is genius & definitely being saved to my desktop quick reference
- Checking everyone's mail in `/var/mail` was interesting too
- Make sure you're checking every folder with `ls -lah` so you catch those sneaky hidden files

Interesting box all round, but also an important lesson in stepping away for the night when you feel yourself flagging. You'd done three boxes yesterday, and with this one you were starting a 4th after dinner and a few drinks. It's the same as playing Doom Eternal - you can feel yourself getting tired as you get stuck on a specific checkpoint, so rather than pushing on and getting worse what you really need is to do is step away and give your eyes/hands/brain a solid rest by sleeping.
# Resolution summary
- Ran Nmap to identify ports `22`, `25` & `80`
- Visited http (`80`) & identified `Onlyrands.com` website
- Identified `teams.onlyrands.com` and modified `/etc/hosts` to access
- Identified `TeamCity v2023.05.4` and exploit to create new user
- Ran exploit and gained access to admin panel
- Enumerated user files and found private SSH key for `marcot`
- Cracked SSH key with `ssh2john` and `john`
- Logged into `marcot` with cracked password and 
- Enumerated `marcot` mail (`/var/mail/marcot`), found cleartext credentials for `matthewa`
- Switched user to `matthewa` and viewed home directory with `ls -lah`
- Found hidden file in `matthewa` home directory, provided cleatext credential for `briand`
- Switched user to `briand` and found user had `sudo` privileges to run `systemctl` on  `teamcity-server.service` as `root` and without a password
- Used systemctl to start `teamcity-server.service` and ran `!sh` to establish shell as `root`
## Improved skills
- File and mail enumeration
- Cracking SSH keys with `ssh2john`
## Used tools
- Nmap
- john
- ssh2john

---
# Information Gathering
Scanned all TCP ports:
```bash
sudo nmap -sC -sV -oN scrutiny.nmap 192.168.215.91 -v
```

Enumerated open TCP ports:
```bash
PORT    STATE  SERVICE VERSION
22/tcp  open   ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 62:36:1a:5c:d3:e3:7b:e1:70:f8:a3:b3:1c:4c:24:38 (RSA)
|   256 ee:25:fc:23:66:05:c0:c1:ec:47:c6:bb:00:c7:4f:53 (ECDSA)
|_  256 83:5c:51:ac:32:e5:3a:21:7c:f6:c2:cd:93:68:58:d8 (ED25519)
25/tcp  open   smtp    Postfix smtpd
|_smtp-commands: onlyrands.com, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, SMTPUTF8, CHUNKING
80/tcp  open   http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: OnlyRands
| http-methods: 
|_  Supported Methods: GET HEAD
443/tcp closed https
Service Info: Host:  onlyrands.com; OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

---
# Enumeration
## Port 22 - SSH (OpenSSH 7.9p1)
No enumeration conducted
## ## Port 25 - SMTP (Postfix)
- Created a list of potential email addresses (domain @onlyrands.com) in `usernames.txt` then ran `smtp-user-enum -U usernames.txt -t 192.168.215.91` to enumerate common SMTP usernames
![OSCP Scrutiny Linux Image1](/images/OSCP%20-%20Scrutiny%20-%20Linux%20-%20image1.png)
## Port 80 - HTTP (nginx 1.18)
- Navigated to `http://192.168.215.91:80`
![OSCP Scrutiny Linux Image2](/images/OSCP%20-%20Scrutiny%20-%20Linux%20-%20image2.png)
- Navigated to `http://192.168.215.91/teams.onlyrands.com`
![OSCP Scrutiny Linux Image3](/images/OSCP%20-%20Scrutiny%20-%20Linux%20-%20image3.png)
- Edited `/etc/hosts` file so `192.168.215.91  teams.onlyrands.com`
![OSCP Scrutiny Linux Image4](/images/OSCP%20-%20Scrutiny%20-%20Linux%20-%20image4.png)
- Navigated to `teams.onlyrands.com` and identified `TeamCity v2023.05.4`
![OSCP Scrutiny Linux Image5](/images/OSCP%20-%20Scrutiny%20-%20Linux%20-%20image5.png)
- Attempted password guessing with `admin:admin` & `admin:password`
![OSCP Scrutiny Linux Image6](/images/OSCP%20-%20Scrutiny%20-%20Linux%20-%20image6.png)
---
# Exploitation
- Identified exploit `CVE-2024-27198-RCE.py` from [https://github.com/W01fh4cker/CVE-2024-27198-RCE/tree/main] - copied to local machine and ran `python3 /media/sf_Kali-Shared/Boxes/PG/Linux/Scrutiny/CVE-2024-27198-RCE.py -t http://teams.onlyrands.com` - Tested multiple commands without success
![OSCP Scrutiny Linux Image7](/images/OSCP%20-%20Scrutiny%20-%20Linux%20-%20image7.png)
- Logged into `teams.onlyrands.com` with credentials `cmnsjvgh:yhMNlvZ5b8` produced by exploit
![OSCP Scrutiny Linux Image8](/images/OSCP%20-%20Scrutiny%20-%20Linux%20-%20image8.png)
- Checked Freelancer builds and identified `id_rsa` removed from `Marco Tillman`
![OSCP Scrutiny Linux Image9](/images/OSCP%20-%20Scrutiny%20-%20Linux%20-%20image9.png)
- Identified and copied OPENSSH Private Key for user `marcot`
![OSCP Scrutiny Linux Image10](/images/OSCP%20-%20Scrutiny%20-%20Linux%20-%20image10.png)
- Used `ssh2john` to create `id_rsa.hash` of SSH private key then cracked with `john` to find credentials `marcot:cheer`
![OSCP Scrutiny Linux Image11](/images/OSCP%20-%20Scrutiny%20-%20Linux%20-%20image11.png)
- Ran `ssh -i id_rsa marcot@192.168.117.91` and logged in with credentials `marcot:cheer`
![OSCP Scrutiny Linux Image12](/images/OSCP%20-%20Scrutiny%20-%20Linux%20-%20image12.png)
---
# Lateral Movement to user
## Local Enumeration
- Ran `cat /etc/passwd` to identify users
![OSCP Scrutiny Linux Image13](/images/OSCP%20-%20Scrutiny%20-%20Linux%20-%20image13.png)
- Navigated to `/home/freelancers` and identified 5th user `williamw`
![OSCP Scrutiny Linux Image14](/images/OSCP%20-%20Scrutiny%20-%20Linux%20-%20image14.png)
- Attempted access to other `/freelancers`
![OSCP Scrutiny Linux Image15](/images/OSCP%20-%20Scrutiny%20-%20Linux%20-%20image15.png)
- Ran `linpeas.sh`
![OSCP Scrutiny Linux Image16](/images/OSCP%20-%20Scrutiny%20-%20Linux%20-%20image16.png)
- Identified vulnerable to CVE-2021-2560
![OSCP Scrutiny Linux Image17](/images/OSCP%20-%20Scrutiny%20-%20Linux%20-%20image17.png)
- Identified Mail
![OSCP Scrutiny Linux Image18](/images/OSCP%20-%20Scrutiny%20-%20Linux%20-%20image18.png)
- Ran `find / -name local.txt -type f 2>/dev/null` to find & then printed `local.txt`
![OSCP Scrutiny Linux Image19](/images/OSCP%20-%20Scrutiny%20-%20Linux%20-%20image19.png)
- Ran `cat /var/mail/marcot` and identified credentials `matthewa:IdealismEngineAshen476`
![OSCP Scrutiny Linux Image20](/images/OSCP%20-%20Scrutiny%20-%20Linux%20-%20image20.png)
## Lateral Movement vector
- Used credentials `matthewa:IdealismEngineAshen476` to login via SSH
![OSCP Scrutiny Linux Image21](/images/OSCP%20-%20Scrutiny%20-%20Linux%20-%20image21.png)
---
# Privilege Escalation
## Local Enumeration
- Navigated to `~/` and ran `ls -lah` to view all file permissions
![OSCP Scrutiny Linux Image22](/images/OSCP%20-%20Scrutiny%20-%20Linux%20-%20image22.png)
- Identified hidden file `.~` and ran `cat .~` to view, identifying credentials `briand:RefriedScabbedWasting502`
![OSCP Scrutiny Linux Image23](/images/OSCP%20-%20Scrutiny%20-%20Linux%20-%20image23.png)
## Privilege Escalation vector
- Ran `su briand` with password `RefriedScabbedWasting502` to switch to user `briand` 
![OSCP Scrutiny Linux Image24](/images/OSCP%20-%20Scrutiny%20-%20Linux%20-%20image24.png)
- Ran `sudo -l` and identified no password required to run `/usr/bin/systemctl status teamcity-server.service` as `root`
![OSCP Scrutiny Linux Image25](/images/OSCP%20-%20Scrutiny%20-%20Linux%20-%20image25.png)
- Identified [GTFObins](https://gtfobins.github.io/gtfobins/systemctl/) for `systemctl` run as `sudo`. Ran `sudo /usr/bin/systemctl status teamcity-server.service` to start `teamcity-server.service` then `!sh` to establish shell as `root`
![OSCP Scrutiny Linux Image26](/images/OSCP%20-%20Scrutiny%20-%20Linux%20-%20image26.png)
- Ran `cat /root/proof.txt` to print `96a5b0fce4ac011046cd0406ec495da5`
---
# Trophy & Loot
`local.txt` = `ecfbfa664ee495c58f9b9b35c0d08f7d`
`root.txt` = `96a5b0fce4ac011046cd0406ec495da5`
