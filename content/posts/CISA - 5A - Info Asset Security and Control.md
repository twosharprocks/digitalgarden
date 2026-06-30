---
title: "CISA - 5A - Info Asset Security and Control"
created: 2026-04-30
updated: 2026-06-28
status: seed
draft: false
tags:
  - cyber-security
  - cisa
  - study
Related:
  - "[[CISA]]"
Video: https://www.youtube.com/watch?v=gQGoUwcwr8A&list=PL7XJSuT7Dq_UvA2knww9Rlzz2JHUpeOAb&index=9
---
# 1 - Information Asset Security Frameworks, Standards and Guidelines
**Policies** are the high-level statements of management's intent (what and why). They must be;
- **Business driven**: Aligned with business objectives
- **Accessible**: Everyone in the company must be able to access them
- **Enforceable**: Must contain penalties for noncompliance
*Auditor's Focus*: Review the policy's last update to ensure it is current and relevant to the organisation's needs

**Standards** are the mandatory requirements that support  policy

**Guidelines** are recommended, non-mandatory best practices that provide advice when specific standards don't apply

**Procedures** are detailed instructions for implementing policies and standards (How-to and considered the lowest level in the documentation chain)

**Frameworks**
- **ISO27001**: International standard for Information Security Management System
- **NIST CSF**: Risk-based framework organised around Identify, Protect, Detect, Respond, Recover
- **COBIT**: ISACA's framework for governance and management of enterprise IT
- **PCI DSS** Mandatory standard for any organisation that stores, processes or transmits cardholder data
- **CSA Clout Controls Matrix (CCM)**: Framework of security controls specific to cloud computing

*Auditor's Role*: Not enough to simply have a framework - you have to ask if it's relevant to the organisation and if they're using it effectively to manage risk. 

**Baselines**
Standardised, minimum level of security that a system, network or device must adhere to throughout its life cycle. Examples:
- **Hardening**: Disabling unnecessary services and parts to reduce the attack surface
- **Passwords**: Enforcing strong passwords and providing password guidance
- **Patching**: Configuring systems for automatic OS and app patching
- **Malware**: Requiring automatically updated antivirus
*Auditor's Role*: Obtain the organisation's baseline configurations and test a sample of systems to verify compliance

# 2 - Privacy Principles
- Auditors must verify the enterprise has a formal privacy policy. 
- Auditor's must evaluate whether staff are aware of the privacy consideration in their roles. 
- Audit should confirm the presence of specific policies like NDAs to address privileged information

Look at
- **Mobile Devices**: Best practices for Mobile Device Management, collecting minimum amount of data for business purposes
- **Biometrics**: Auditor must evaluate privacy concern as biometrics may be intrusive
- **Encrypted communications**: TLS and PGP are key controls for communication privacy
- **Wireless Networks**: Unsecured wireless creates significant privacy threats

# 3 - Physical Access and Environmental Controls
Mechanism to protect facilities and tangible assets from authorised access

**Multi-layered defense** of controls like guards, visitor logs, mantras, locked server racks, wide range of door locks

**Environmental Controls** ensure the continued availability. 
**Controls** include Ups for short-term, generators or long-term, HVAC for temperature and humidity, fire suppression (gas preferred to water)
- Data centre fire suppression need NOT be human compatible

**Auditor's Focus**
Physical
- Review visitor logs
- Check for piggybacking
- Verify man trap functionality
- Ensure security guards are bonded
Environmental
- Verify fire suppressions inspection is current (minimum annually)
- Review UPS and Generator test reports
- Look under raised floors and above ceilings for water and smoke detectors

# 4 - Identity and Access Management
Right people accessing the right resources and the right time
**IAM Lifecycle**
- Enrollment
- Role Determination
- Provisioning
- Review/Updating
- Deprovisioning

**IAM Architecture**
- **Centralised**: Handled by one group, consistent, but can be slow to respond to local needs
- **Decentralised**: Delegated to local departments, risk of inconsistent standards, quicker response

**Authetication** is a subject proving they are who they claim to be
- Something you know, you have, or are
- **MFA** requires more than one authentication factor
- **Single Sign-One (SSO)**: Multiple app access from one set of login credentials

**Authorisation** comes after authentication and determines resources user can access
- **Access Control Methods**
	- **Mandatory Access Control (MAC)**: Access determined by security labels (high security, no user modification of access)
	- **Discretionary Access Control (DAC)**: Data owner determines access (eg. File creator allows access through sharepoint). Most common but least secure
	- **Role-Based Access Control (RBAC)**: Access assigned based on job role Most common in business and considered best practice
	- **Rule-Based Access Control**: Like firewalls
		- Harder to audit as number of rules grows
	- **Attribute-Based Access Control (ABAC)**: All about context (user is in a department and accessing during business hours)
		- Most granular and flexible for auditors, ideal for zero-trust environments (common in cloud IaaS)
	- **Policy-Based Access Control (PBAC)**: Combines user business role with policies to determine privilege
		- High-level strategic approach that needs it's technical implementation (via ABAC or RBAC) verified for correct policies enforcement

# 5 - Network and End-Point Security

**Next Generation Firewall (NGFW)**: Application awareness, deep packet inspection, integrated IDS/IPS

**Web Application Firewall (WAF)**: Operates at level 7 to protect web applications from common attacks (SQLi & XSS) 

**Demilitarised Zone (DMZ)**: Perimeter network that isolates publicly accessible servers from the internal network

*Exam Tip: Differentiate between NGFW (network and users) and WAF (protects web apps)*

# 6 - Data Classification
**Data Loss Prevention** prevents loss, misuse or access to sensitive data. Classify regulated confidential and business-critical data, identifies violations of policy

*Exam Tip: DLP is a content-aware technology that works by inspecting the content to see if it matches a defined policy*

# 7 - Data Encryption and Encryption-Related Techniques
**Symmetric** uses a single key (eg. AES used for bulk data encryption)
**Asymmetric (Public Key)** solves the key distribution issue but is slower (ECC: Elliptic Curve Cryptography provides the same level of security as RSA but with smaller key sizes to be more efficient)
**Hashing** is irreversible and produces a fixed-length digest (protects integrity)
**Digital Signatures** provide integrity, authenticity and non-repudiation

*Exam Tip: Know the strongest algorithim, but knowing how to audit the key management lifecycle is better - the strongest encryption is useless if the keys are poorly managed*

# 8 - Public Key Infrastructure (PKI) 
**Create, manage, store, distribute and revoke public key certificates**
- **Certificate Authority (CA)** issues &  signs certificates
	- Root CA usually maintained offline
	- Also has subordinate CA (Policy CA or Intermediate CA), and Issuing CA at the bottom
- **Registration Authority** verifies identity of users requesting certificates from the CA
- **Digital Certificate** binds a public key to an identity
- **Certificate Policy (CP) / Certificate Pratice Statement (CPS)** define the rules and practices of PKI
- **Certificate Revocation List**: CA periodically publishes a blacklist of revised certificate serial numbers
	- Auditors concern I the time lag between when a cert is revoked and when the next CRL is published
- **Online Certificate Status Protocol (OCSP)**
	- Real-time protocol for querying CA server directly for specific certificate
	- Auditor's concern is dependency on CA's OCSP responder, could be single point of failure
- **Key PKI Risks for the Auditor**
	- **Compromise of the Root CA's Private Key**: Worst case scenario
	- **Poor Private Key Protection**: Failure to securely store private keys by users/systems
	- **Certificate Lifecycle Management Failure**: Not renewing certificates before they expire, and not revoking certificates leaves an organisation exposed
	- **Weak Keys/Algorithims**: Nothing less than 2048bit for RSA
- **Audit Procedures**
	- **Review governance**: Examine Certificate Policy (CP) and Certificate Practice Statement (CPS)
	- **Inspect the CA**: Verify physical and logical security of CA systems (root CA is offline and secure)
	- **Test Key Management**: Review procedures for key generation distribution, storage, rotation, destruction (lifecycle management)
	- **Verify Revokation**: Check CRL or OCSP mechanism is in place, being updated and used by clients

# 9 - Web-Based Communication Techniques
**Transport Layer Security (TLS)**: Standard for securing comms between web browsers and servers forming HTTPS (replaced SSL) 

**Web Application Firewall** protects Web applications by filtering and monitoring HTTPS traffic (layer 7, critical control because network firewalls often allow HTTPS traffic)

**Content Delivery Network**: Geographically dispersed servers to provide low latency and high availability of hosted Web content (vulnerable to session hijacking or credential theft)
- Best practice is to combine CDN with a WAF and be compatible with organisations SSL/TLS certificates
**Domain Name System Security Extensions (DNSSEC)** adds a layer to the DNS lookup by adding a digital signature to the DNS data
- Primary control to prevent DNS poisoning

**Secure Email Protocols**
- **Domain Keys Identified Mail (DKIM)** uses a digital signature to verify email was sent and authorised by the owner of the domain (detect forged sender addresses - phishing/spam)
- **Secure/Multipurpose Internet Mail Extensions (S/MIME)** is a standard that offers authentication and confidentiality through the use of public key encryptions and digital signatures
- **Sender Policy Framework (SPF)** is used by organisations to list all servers they send email from

*Exam Tip: TLS secure the pipe, WAF protects the application DNSSEC validates the address, DKIM/S/Mime authenticates the sender*

# 10 - Virtualised Environments
**Server Virtualisation** divides a physical server into unique isolated virtual servers with a hypervisor
- **VM Escape** is avoided by patching OSs and hypervisor, guest privileges are low, and server-level redundancy is in place
- **VM Sprawl** is when unmanaged VMs are deployed to the network - if It doesn't know it's there, it may not be patched/protected. Enforce security policies for adding VMs and use periodic scanning to ID new VMs

**Containerisation** enable apps to run on a shared OS kernel (don't have their own OS)

**Auditor Focus**
- Virtualisation;
	- Hypervisor is a critical single point of failure
	- Compromise of the Hypervisor can lead to compromise of all guest VMs
	- Must be hardened, patched, and access tightly controlled
- Containerisation
	- Weaker isolation than VMs as they share the same kernel
	- Vulnerability in the shared host kernel could affect all containers running on it

**Virtual Local Area Network (VLAN)** logically segments a physical network into broadcast domains (layer 2)
- **Auditor Focus**: Verify VLANs are configure correctly to enforce segmentation and routing between VLANs is restricted by a firewall
**Virtual Storage Area Network (VSAN)** logically partions within a physical storage area network (SAN)
- **Auitor Focus**: Confirm VSAN properly isolates storage traffic and prevents on VM from accessing another's storage
**Software Defined Networking** decouples the network control plane from the data plane for centralised management
- **Auditor's Focus**:SDN controller is highly privileged and must be highly secured

**Cloud Migration** requires auditor to focus on;
- **Formal plan and risk assessment** for migration
- **Data Classification and encryption**
- **Mapping on-premises controls to equivalent cloud controls**
- Top Risks
	- Insufficient Identity, Credential and Access Management
	- Insecure Interfaces and APIs
	- Misconfiguration and Insecure Change Control
	- Lack of Cloud Security Architecture and Strategy (redesign for the cloud)

**Share Responsibility Model** means the customer is always responsible for their data and the management of user access, regardless of the service model

# 11 - Mobile, Wireless, and Internet-of-Things (IoT) Devices
**Mobile Device Audit Procedures**
 - Govenance
 - Device Management
 - Patch Management

**Wireless Network Security (WLAN)**
- WPA3 is the current secure standard
- WPA2 with AES is the minimum acceptable
- WEP is completely insecure

**Internet of Things Security**
- Devices often have weak or no security, default passwords, and difficult to patch
- Isolate IoT devices on a separate segmented network as a control

# Key Exam Takeaways
- **Master Governance Hierarchy**: Policies, Standards, Baselines, Guidelines, and Procedures
- **IAM is Critical**: Familiar with IAM life cycle, Authentication factors, Access control methods (esp. RBAC)
- **Differentiate between techologies**: firewall vs IDS vs IPS, NGFW vs WAF, encryption vs hashing
- **Understand PKI**: CA, RA, CRL, OCSP
- **Embrace Modern Architecture**: Share Responsibility Model, virtualisation vs containers vs SDN
- **Secure The Edge**: Key controls for mobile (MDM, encryption), BYOD (selective wipe), Wireless (WPA3/WPA2), IoT (Network segmentation)

---
**This also reminds me of**... 

---
# References
