---
title: "CISA - 5B - Security Event Management"
created: 2026-05-02
updated: 2026-06-30
status: seed
draft: false
tags:
  - cyber-security
  - cisa
  - study
Related: 
  - "[[CISA]]"
  - "[[Cyber Security]]"
Video: https://www.youtube.com/watch?v=gQGoUwcwr8A&list=PL7XJSuT7Dq_UvA2knww9Rlzz2JHUpeOAb&index=10
---
# 1 - Security Awareness Training and Programs
Effective security is dependent on people. 
- Change their behaviour and foster a culture of good security practices so they change from the weakest link to the first line of defence. 

Awareness
- Change behaviour (answer the "what"). All employees from day one. Passive - videos, newsletters, posters
Training
- Teach how to do a job securely (answer the "how"). Specific to function areas, hands-on learning with instructors and labs
Education
- InDepth knowledge for security professionals (answer the "how"). For security professionals seeking career expertise, intensive learning through univerity/courses/seminars/research

*Auditor's Role is to assess if the organisation is applying the right level of learning to the right audience to achieve its security goals*
- Verify the program is based on a formal needs assessment that considers different groups
- *Exam Tip: Operational staff and system users are often the riskiest groups and require a high degree of awareness training*

Program should be continuous cycle
- Define scope
- Select Staff
- Identify Audience
- Motivate Trainees
- Administer Program
- Maintain Program
- Evaluate Program

Measure effectiveness with: Reduced number of security incidents, Increased reporting of suspicious events by employees, and improved results from phishing simulation tests

# 2 - Information System Attack Methods and Techniques
Fraud Triangle
- Motivation
- Opportunity
- Rationalisation

Types of Attacker
- Hackers: Explore systems, not always with malicious intent
- Crackers: Break into systems with malicious intent
- Script Kiddies: Use scripts/programs written by others
- Insider: Empolyyes or former employees who pose significant threat due to knowledge or access

Social Engieneering
- Phishing
	- Spear Phishing: Targets specific organisation
	- Whaling: Targets senior executives

## Common Attacks
- Denial of sevice (DoS): Attack designed to make machine/network unavailable
- Distributed DoS (DDoS): DoS attack launched from multiple compromised systems (botnet)
- Man-In-The-Middle (MitM): Attacker secretly relays and possibly alters comms between two parties
- Malware
	- Trojan (disguised, Logic Bomb (specific conditions), Worm (self replicating), ransomware (encrypt and demand)

# 3 - Security Testing Tools and Techniques
- Testing: Proactive effort to reveal flaws
- Vulnerability Scan: Identifies a list of known vulnerabilities
- Penetration test: Attempts to actively exploit vulnerabilities
- Testing Teams: Red, Blue, Purple

Pentesting: External (outside the network), Internal (inside perimeter), blind testing (blackbox), double-blind (tester/tested not aware of the test - most effective way incident handling/response), targeted ("lights-on" whitebox)

*Exam Tip: Auditor must verify that any pentest had documented prior approval from senior management - otherwise it's illegal*

App Security Testing Techniques
- SAST (Static): Analyse without running code, whitebox (read blueprints of building to ID flaws)
- DAST (Dynamic): Test app while running, blackbox (rattles doors and windows of finished building)
- IAST (Interactive): Hybrid using agent inside running app, grey box (inside building with the floor plan) 
- SCA (Software Composition Analysis): ID/analyse open-source components to find known vulnerabilities (checking supplier list for parts in building with known defects)

# 4 - Security Monitoring Tools and Techniques
SOC: Constantly monitors to detect, analyse, respond to security incidents.

IDS/IPS Audit Checklist
- Asset Inventory: Complete to determine what needs to be monitored? 
- Policy: Formal and documented that defines rules and compliance requirements
- Baselining: Has a baseline of normal network behaviour been established
- Placement: Sensors placed for adequate visibility? At the perimeter, in the DMZ? 
- Tuning: System regularly tuned to update rules and reduce false positives
- Incident Response: Documented IRP linked to IDS/IPS alerts? 

Honeypots
- *Auditor's Perspective: Evaluate the use of a honeypot as a detective and intelligence-gathering tool. Consider the risk the honeypot could be used to launch an attack on other systems, and consider the reputation Al risk if external services identify/publicise the "vulnerable" system*

# 5 - Security Incident Response Management
Events: Any observable item
Incident: Unplanned and have an adverse impact on the organisation
- Not all incidents require the security team
- Dedicated team responsible for executing the Incident Response Plan (IRP) is the Computer Security Incident Response Team (CSIRT)

**Incident Response Plan**
- **Preparation**: Establish tools, CSIRT, procedures
- **Detection and Analysis**: Identifying an incident has occurred and assessing its scope
- **Containment, Eradication and Recovery**: Isolating affected systems, remove threat, restore operations
- **Post-Incident Activity**: Lessons learned
	- MOST Important STEP


# 6 - Evidence Collection and Forensics
Types of Investigations
- Administrative: Policy violations
- Criminal: Evidence to convict
- Civil: One entity sues another
- Regulatory: Conducted by government agency against organisation

Computer Forensics
- Auditor's Role: Ensure the organisation has a formal documented process for forensic investigations
- Phases
	- First Response: Initial actions
	- Evidence Collection and Seizure: Volatile sources first
	- Data Acquisition: Forensic images of data
	- Data ANalysis: Examining acquired data
	- Documentation & Reporting: All findings for potential legal proceedings
- Chain of Custody
	- Detailed chronological document that tracks handling of evidence
	- Proves the integrity of the evidence and show it has not been tampered with
	- Tracks: Who has access, where it was stored, what procedures were performed on it, How it was transferred
	- *Exam Tip: Broken or incomplete chain of custody is one of the most common reasons digital evidence is rule inadmissable*
- Evidence Integrity Principles
	- **Data Acquistion**: Never work on original evidence, bit-for-bit copying, use write-blockers to prevent original disk altering
	- **Volatile Data**: Do not change the power state of the device - if on, leave on
	- **Verification**: Use cryptographic hashes (eg. SHA-256) to verify forensic image is an exact, unaltered copy of the original

# Key Exam Takeaways
- **Differentiate between**
	- Awareness vs Training vs Education
	- Vulnerability Scan vs Penetration Test
	- SAST vs DAST
	- IDS vs IPS
	- SIEM vs SOAR
	- Honeypot vs IPS
- **Incident Response**: Plan is useless unless it is documented and tested
- **Forensics is about process**: Auditor's primary concern is chain of custody and preservation of original evidence
- **Auditor's Role is to EVALUATE the process, NOT perform the task**

---
**This also reminds me of**... 

---
# References
