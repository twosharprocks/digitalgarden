---
title: Y2038 - Epochalypse
created: 2025-11-01
updated: 2026-07-30
status: seed
draft: false
tags:
  - cyber-security
  - interests
related:
  - "[[Cyber Security]]"
---
*On 19 January 2038 at 03:14:07 UTC implementations relying on 32-bit signed integer representations of Unix epoch time will overflow, resulting in a system time of 20:45:52 UTC on 13 December 1901*

[Time Security SIG](https://www.first.org/global/sigs/time/) - The Time Security SIG exists to help the global FIRST community prepare for the 2036–2038 epoch rollovers. By coordinating research, testing, and outreach on time integrity, the SIG connects CSIRTs, vendors, and standards bodies to strengthen resilience across critical infrastructure. Our goal: ensure the world’s clocks keep running — securely — long past 2038.

[Youtube - 2038 Is Not A Future Issue Get That Through Your Thick Skull](https://www.youtube.com/watch?v=zKk_pBQKTHg)

# MilCom Presentation
**Title**: After the Epochalypse - Assuring Defence and Critical Infrastructure in 2038 and beyond
**Summary**
At 03:14:08 UTC on 19 January 2038, the timestamp value used by systems that represent Unix time as a signed 32-bit integer will overflow - the so-called “Epochalypse”. Like the Y2K bug before it, most modern 64-bit platforms will avoid this issue. But "Y2038" vulnerabilities remain in numerous embedded devices, legacy software, operational technology, network appliances, communications equipment, sensors and supply-chain components. In some cases, this integer overflow could cause critical mission systems to suddenly believe it is 1901.

For Defence and critical infrastructure, Y2038 is not just a date-handling defect - it's a cyberworthiness, systems-assurance and operational-resilience issue. Affected systems could reject valid data, disrupt scheduled activities, invalidate authentication, corrupt audit trails or experience critical failures. Interdependencies could allow a minor timestamp glitch in one component to have wider mission or service consequences. Y2038 issues may also emerge well before 2038, as vulnerable systems process future-dated maintenance records, contracts, certificates, licences or planning data.

This presentation will explain the technical basis of the Y2038 problem, and examine how vulnerable time representations may persist in file systems, databases and query functions, legacy applications, and embedded systems which underpin communications devices, routers, wireless access points, IP cameras, mobile and field systems, as well as GPS receivers and inertial guidance systems used in vehicles and aircraft. Representative scenarios will illustrate potential effects on communications and network management, positioning, navigation and timing, maintenance, security monitoring, and logging.

The presentation will offer a practical approach to managing Y2038 risk by locating vulnerable time representations across software, data, interfaces and embedded components; assessing whether affected systems can be updated or replaced; obtaining evidence from suppliers; identifying vulnerable dependencies; and testing critical boundaries. These findings can then inform remediation priorities and system lifecycle planning.

**Alignment with Criteria:**
This presentation reinforces AE's reputation as an industry leader providing cyberworthiness, risk management, and technical expertise to support Defence through a threat-informed and risk-based approach. The presentation topic supports AE's mission to "Secure Australia" by raising awareness about a significant threat to the future capability of Defence and Critical Infrastructure, providing vulnerability information to clients and stakeholders, while also showcasing and building Alpha Echo's reputation as an innovative and forward-thinking contractor. If scanning for time representations that use signed 32-bit integers can be integrated into a developing AE product (one that detects vulnerabilities in systems it's connected to) then this presentation could also help showcase an emerging AE capability and offer a potential solution to the issue.


---
**This also reminds me of**... 

---
# References

