---
title: CISSP - Misc Notes
created: 2025-07-07
updated: 2025-10-30
status: reference
draft: false
tags:
  - cyber-security
  - cissp
related: 
  - "[[CISSP]]"
---
---
The **Payment Card Industry Data Security Standard (PCI-DSS) has 12 main requirements**. Each requirement has additional sub-controls. 
1. Install and maintain a firewall configuration to protect cardholder data
2. Do not use vendor-supplied defaults for system passwords and other security parameters
3. Protect stored cardholder data
4. Encrypt transmission of cardholder data across open, public networks
5. Use and regularly update anti-virus software or programs
6. Develop and maintain secure systems and applications
7. Restrict access to cardholder data by business need-to-know
8. Assign a unique ID to each person with computer access
9. Restrict physical access to cardholder data
10. Track and monitor all access to network resources and cardholder data
11. Regularly test security systems and processes
12. Maintain a policy that addresses information security for employees and contractors

---
**Internet Protocol Security (IPsec)** is a *suite of protocols that provides protection at the network layer* of the Open System Interconnection (OSI) model. IPsec is *frequently used to establish a Virtual Private Network (VPN) between two routers*. IPsec protects the original IP packet by encrypting or hashing the IP packet and adding a new Authentication Header (AH) or Encapsulating Security Payload (ESP) header with a new IP header.

IPsec can be used in either AH or ESP mode:
- **Authentication Header (AH)** provides integrity of the packet through the addition of an AH header. This includes **authentication for each packet but no encryption**.
- **Encapsulating Security Payload (ESP)** provides the confidentiality of the packet and adds an ESP header. This provides **limited authentication for each packet and encryption of the original packet**.

IKE has two modes:
- **Main Mode uses a six-way handshake** where parameters are exchanged in multiple rounds with encrypted key exchange. This is more secure than Aggressive Mode. A key exchange using a Diffie-Hellman (DH) or DH-like algorithm is always preferred over using a pre-shared key.
- **Aggressive Mode uses a three-way handshake** where the hashed Pre-Shared Key (PSK) is sent unencrypted.

---
Frame relay resides in the Open System Interconnect (OSI) model's data link layer and uses packet-switching technology to connect different Wide Area Networking (WAN) connections together. Frame relay uses virtual circuits and Data Link Connection Identifier (DLCI) addresses to connect routers.

Asynchronous Transfer Mode (ATM) is a cell-switching technology. Border Gateway Protocol (BGP) is an IP routing protocol. Fibre Channel (FC) was designed to create a local area network for the purpose of storage networks, not a WAN.

---
**Content Distribution Network (CDN)**: Collection of different content that a website may display, distributed across geographical regions. A CDN allows website creators to improve performance by providing a website’s content in a geographical region closest to the client. This reduces latency and download times.

Spyware is software that watches a user's behavior and sends that information to the creator/owner/user of the spyware. It would not open dozens of connections, just the one. Man-In-The-Middle (MITM) attacks are difficult to detect in the manner that Nadia is monitoring. The Man is in the middle of the connection, between the user and the website. There are no extra connections. Connection failures can be simple connection failures. They can occur for many different reasons, many of which have no security implications.

---
Internet Protocol Security (IPSec) is known as a "suite" of protocols that is commonly used in many VPN configurations and regarded as a standard for security in IP networks. Also known as IP Security, IPSec comes in many forms and is used depending on what type of encryption is needed. IPSec allows for:

- Authentication headers to provide non-repudiation and integrity checks by encrypting the header
- Encapsulating Security Payload (ESP) to encrypt the data payload
- Hash-based Message Authentication Code (HMAC)
- IP Payload Compression (IPComp) to compress data
- Internet Key Exchange (IKE) to allow for secure methods of exchanging public and private data

Transport Layer Security (TLS) is a cryptographic protocol that provides secure communication over a network. It is commonly used to establish secure connections between clients (such as web browsers) and servers (such as web servers) to ensure the confidentiality, integrity, and authenticity of data transmitted between them.

Secure Shell (SSH) is a network protocol that provides a secure way to access and manage remote systems over an unsecured network. It offers encrypted communication between the client and server, ensuring confidentiality, integrity, and authentication of data transmitted over the network. SSH provides a secure and encrypted method for remote administration, file transfer, and secure tunneling, making it widely used for managing and accessing remote systems and servers.

OpenVPN is an open-source Virtual Private Network (VPN) protocol and software solution that enables secure and private communication over the Internet. It provides a flexible and customizable VPN solution for establishing encrypted connections between clients and servers. It can be used to remotely access corporate networks, but it is normally used by users, not data centers for IaaS.

---
The Biba model has two main rules:

- **Simple integrity** property states that a subject cannot read an object at a lower integrity level, but can read an object at a higher integrity level. Known as "no read down" or "read up".
- **Star (`*`) integrity property** states that a subject cannot write to an object at a higher integrity level, but can write to an object at a lower integrity level. Known as "no write up" or "write down".

The Biba model does not include a property for view or check.

---
A common auditing standard is the Statement on Standards for Attestation Engagements (SSAE-18) which provides Service Organization Control (SOC) reports. 
SOC Reports
- SOC 1: Financial for a point in time, 
- SOC 2: Five trust principles (security, confidentiality, processing integrity, availability, and privacy) evaluated over a period of time.
- SOC-3: Results of SOC-2 audit written for distribution. SOC-3 report is generally much smaller & just considered a seal of approval.

---
A Redundant Array of Independent Disks (RAID) is used to group disks and provide fault tolerance or increase performance. In this scenario, Alex should choose **RAID-0 to increase the write speed of each node** since he's using several servers to provide redundancy rather than implementing it at the disk level with RAID.

- **RAID-0 stripes data across multiple disks**. This increases the chance of failure, but increases the write and read speed.
- **RAID-1 mirrors** data across multiple disks. This decreases the usable drive space by 50% and provides some write speed benefits if multiple disks can be written at once.
- **RAID-3** provides fault tolerance and high data throughput by **striping data across multiple drives and dedicating one drive to store parity information**. This does stripe, but it is not commonly used.
- **RAID-4** provides fault tolerance and improved performance by striping data across multiple drives, **similar to RAID-3**. However, it performs **block-level striping**, not bit-level.
- **RAID-5 stripes data across multiple disks and adds parity information**. This provides fault tolerance, but decreases write speeds.

---
Organizations can have three types of security plans:

- **Strategic plans**: 5 years, describe overall security goals.
- **Tactical plans**: 1 year, describe how particular goals can be accomplished.
- **Operational plans**:  Extremely short duration, in-depth detail on how to accomplish strategic/tactical plans.

Contingency plans are not one of the three types of security management plans.

---
Transmission Control Protocol/Internet Protocol (TCP/IP) model

The TCP/IP model is a simplified four-layer framework used to standardize and facilitate communication over the internet, consisting of the Network Access, Internet, Transport, and Application layers.

OSI Layers: Physical, Data Link, Network, Transport, Session, Presentation, and Application
- Please Do Not Throw Sausage Pizza Away 

---
- **Confidential or Proprietary:** Highest level of classified data that could cause exceptional damage to the organization if exposed. An organization’s trade secrets or “secret sauce” could be considered proprietary data.
- **Private:** Next-highest level of classified data and shouldn’t be shared outside the organization and could cause significant damage if exposed. PII and PHI may be classified as private data.
- **Sensitive:** Data that could cause damage to the organization if made public. The organization’s network layout and the devices it uses may be sensitive data.
- **Public:** Data that is intended to be openly disclosed. This includes the contents of websites, social media, brochures, etc.

---
Access Control List (ACL): Table that includes subjects and assigned privileges. 
- Access control lists are bound to a specific object. When a subject attempts an action on the object, the system checks the access control list to determine if the subject has the appropriate privileges to perform the action.

Compatibility matrix: Table that shows which systems or applications are compatible with each other. 
- Maps systems/applications to other systems/applications. An access control matrix is a table that shows which subjects are granted access to which objects. Both subjects and objects are visible in the access control matrix. 

Role-based access: Assigns permissions based on a user's role in the organization. 
- The roles are mapped to the objects and the permissions that the role is granted.

---
Clipping level: Threshold for the number of error occurrences before it's considered suspicious or sets off an alarm. Now commonly called thresholds.

---
*Software audit trails* keep track of user activities and *provide accountability* to the user base. Audit trails are especially important for software that contains sensitive data. For instance, they are required by the Health Insurance Portability and Accountability Act (HIPAA) to audit who has access to patient data and when the data was accessed.

---
- **HMAC-Based One-Time Password (HOTP):** HOTPs are generated using an incrementing counter. Each authentication attempt using an HOTP causes the authenticator and server to both regenerate it.
- **Time-Based One-Time Password (TOTP):** TOTPs are regenerated by the authenticator and the server at regular intervals. With synchronized clocks, this ensures that both devices have the same code at the same time without needing to communicate after initial setup.

---
Biometrics 
- Retinal: Blood vessels in the retina can be affected by health conditions, may also conflict with privacy laws.
- Iris scans are >> detailed than fingerprint or facial scan

---
**Software Capability Maturity Model (SCMM)** is based on the principle that a *mature software development process will produce quality software*

---
**This also reminds me of**... 

---
# References

