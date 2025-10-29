---
title: ASD Annual Cyber Threat Report 2023-2024 - Notes
created: 2025-04-16
Status: Seed
draft: false
tags:
  - Cybersecurity
---
Reference: https://www.cyber.gov.au/about-us/view-all-content/reports-and-statistics/annual-cyber-threat-report-2023-2024

---
# Executive Summary
State-sponsored cyber actors persistently targeting Australian government, critical infrastructure, and businesses using evolving tradecraft. (Espionage, malign influence, interference and coercion)
- Chinese state actors leveraging LOTL, behaviour consistent with pre-positioning for disruption
- Russia adapting techniques including cloud platform exploitation. 
- Critical infrastructure is an attractive target, making up 11% of ASD incident responses 
- Cybercrime is persistent and disruptive, and adapting to capitalise on AI. 

# Year In Review
Top 3 self-reported business crimes
- Email compromise (20%), online bank fraud (13%), Business email compromise fraud (13%$)
Australian Protective Domain Name System blocked access to 82million malicious domains (+21%)

Top 3 reported **critical infrastructure** incidents
- ==Compromised account/credentials (32%)== **Gov incidents = 30%**
	- *Mitigate with Phish-resistant MFA, log analysis, find/remove inactive user/service accounts, enforce least privilege
- ==Malware infection (17%)== **Gov incidents = 20%**
	- *Mitigate with Antivirus & EDR, update devices, implement application control, maintain backups of critical data applications/settings, regularly test backups`
- ==Compromised asset, network or infrastructure (12%)== **Gov incidents = 20%**
	- *Mitigate with: network segmentation/segregation, apply [ASD Industrial control systems remote access protocol](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/critical-infrastructure/industrial-control-systems-remote-access-protocol), define processes for implementing new software/patches into an ICS, sufficient logging & monitor key indicators, store logs securely*
- *All other incident types = 39%*

# State Actors
- Threat is likely to grow as strategic competition in Indo-Pacific region increases
- State-sponsored threat actors will continue to target Australian government, critical infrastructure, and businesses (as well as connected systems and supply chains)
	- Targeting for espionage and information-gathering
	- Focus on [LOTL techniques](https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/identifying-and-mitigating-living-off-the-land-techniques) & [Volt Typhoon targeting critical infrastructure](https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/prc-state-sponsored-cyber-activity_actions-for-critical-infrastructure-leaders)
	- [APT29 (SVR) adapting tactics for initial cloud access](https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/svr-cyber-actors-adapt-tactics-initial-cloud-access)

# Critical Infrastructure
- OT systems are increasingly interconnected and can have vulnerabilities that make them an easy target
- Critical infrastructure should adopt a "when" stance not "if".
	- Understand/map networks, implement logging, maintain asset registry
- 3 most common activity types for CI
	- Phishing (23%), Public-facing app exploitation (21%), brute force activity (15%)
- 3 most common incidents for CI
	- Compromised Credentials (32%)
	- Malware infection (17%)
	- Compromised asset/network/infrastructure (12%)
- Cyber activity against CI is persistent
	- Pre-positioning & espionage
	- Profit-driven opportunistic attacks
	- Defacement & DDoS by hackivists
- OT is vulnerable