---
title: "CISA - 4A - IS Operations"
created: 2026-04-28
updated: 2026-06-28
status: seed
draft: false
tags:
  - cyber-security
  - cisa
  - study
Related:
  - "[[CISA]]"
---
# 1 - Common Technology Comonents
## Open Systems Interconnection (OSI) Model
- Application: User facing (HTTP, FTP, SMTP)
- Presentation: Data formatting, encryption, compression
- Session: Establishes, manages, terminates connections
- Transport: Reliable end-to-end data transfer (TCP, UDP)
- Network: Addressing and routing (IP addresses routers)
- Data Link: Physical addressing and error detection (MAC addresses, switches)
- Physical: Hardware that transmits the bits (cables/hubs) 
*Exam Tip: Must understand the function and devices in each layer*
- Focus on 3,4 and 7 (maybe 6)

## LAN/WAN Devices
- **Repeater/Hub**: Layer 1, regenerates signal to extend network range. Hubs are multi-port repeaters
- **Bridge/Layer 2 Switch**: Layer 2, connects network segments, reduces collision domains, uses MAC addresses to filter and forward *frames*,  hardware-based and more efficient than bridges
- **Router**: Layer 3, logically links networks, makes intelligent routing decisions based on IP addresses

## Common Physical Topologies
- **Star**: Most common, all connected to central hub
- **Bus**: All devices share a single communication line
- **Ring**: Outdated, connected in circular fashion

## TCP/IT Suite
- **Defacto standard protocol suite for the internet**
- Internet Protocol
	- IPv4: 32-bit address (most used today)
	- IPv6: 128-bit address (gradually replacing IPv4) 
- **Network Address Translation**
	- Converts private internal IP addresses into public external IP addresses
	- Hides internal network structure and IP addresses from external attacks

## Converged Protocols
- Merging specialised/proprietary protocols with stabdard TCP/IP
	- **VoIP**: Voice over IP, transports voice calls
	- **FCoE**: Fiber Channel over Ethernet, encapsulates high-speed storage over ethernet
	- **iSCSI**: Lower-cost alternative to Fiber Channel, allows storage device access over TCP/IP network
	- **MPLS**: High-performance network tech that directs data using short path labels instead of long network addresses, independent of routing tables

## Hardware 
* **Maintenance**: Auditor's role is to **verify a formal maintenance plan exists** and is being followed, and **reviewing hardware monitoring reports** to detect problems and predict future needs. 
* **USB Mass Storage**: Malware vector, data theft risk, risk of data and media loss. 
	* **Key controls**: Encryption, Granular Control Software (allow keyboards, block storage), Policy & Awareness (screen lock)

# 2 - IT Asset Management
Ensuring organisations assets are accounted for, deployed, maintained and disposed of when no longer needed

## Process
- **Identify all IT assets**
- **Create/Maintain Inventory**
- **Track asset through its life cycle**

## Key Inventory Fields
- **Owner & Custodian**
- **Location**
- **Security/Risk Classification**
- **Compliance Requirements**

*Exam Tip: Auditors Role is to verify a complete and accurate inventory of all IT assets exists and is actively maintained*

# 3 - Job Scheduling and Production Process Automation
**Job schedule**: List of batch jobs that must be run, execution order, any dependencies

**Job Scheduling Software**: Automates the scheduling process to ensure resources are used optimally & processes are executed consistently

**Key Controls**
- High priority jobs are given optimal resource availability
- Maintenance functions are performed during non-peak times
- Logs are maintained of all job successes and failures

**Exam Tip**: Auditor's Role is to review the job schedule to ensure it aligns with business priorities and review console logs for evidence of job failures and timely resolution

# 4 - System Interfaces
## The Process
- **Data Integrity**:
- **Data Confidentiality**: 
- **Data Availability**: 

## Key Inventory Fields
- **Reconciliation**: Using control totals or cryptographic checksums to verify data ent equals data received
- **Encryption**: Protecting data during transfer
- **Audit Trails**: Logging all interface activity (who sent what, to who, and when it was received)

# 5 - End-User Computing 
- **End-User Computing (EUC)**: Ability of non-It professionals design and implement their own applications
- **Shadow IT**: Use of systems, services or software without explicit approval from the IT department
- **Key Risks**
	- Lack of security controls
	- Data Loss (not properly backed up)
	- Compliance Violations (sensitive data in unapproved locations)
- **Auditor's Role**: Evaluate organisations policies and compensating controls for managing these risks


# 6 - Data Governance
Overall management of the availability, usability, integrity and security of data used in an enterprise

Key Principles of IS Operations
- **Ownership**: Data owners must be assigned for critical information assets
- **Classification**: Assets must be classified based on sensitivity to apply appropriate controls
- **Integrity**: Controls must ensure data accuracy and completeness
- **Security**: Access controls, encryption, and logging must be implemented based on data classification

*Exam Tip: Auditor's role is to verify that a data governance framework is in place and that operational processes adhere to it*

# 7 - Systems Performance Management
**Goal**: Ensure that IS architecture, software, and resources can efficiently meet current and future business demand

**Key Areas**
- **Operating Systems Management**: Ensure core software running the computer is secure and properly configured
- **Software and Source Code Management**: Controlling software licences and underlying code of applications
- **Capacity Management**: Planning and monitoring computing resources to ensure they are sufficient. 

*Exam Tip: Auditor's role is to review system configuration files and parameters to ensure that control options protecting the OS's supervisory state are properly configured and secured from unauthorised changes*

**Software Licencing**: Auditor's role is to compare software licence agreements with software inventory scans to identify and report any violations (unlicensed use). 

**Source Code Management**: Process of managing and protecting the human-readable code that makes up an application
- **Version Control System**: Software like Git that tracks all changes to source code, control access, and allows rollback to previous versions
- **Source Code Escrow**: Agreement to store source code with a trusted third party that is released if the vendor goes out of business

## Capacity Management
- **Monitor** key metrics
- **Analyse** trends to establish a baseline &  forecast future needs
- **Tune** system for optimisation
- **Implement**: new capacity before performance is impacted

*Exam Tip: Auditor's role is to review the capacity plan and verify it is based on business input, considers future growth, and updated at least annually*
# 8 - Problem and Incident Management
**Incident Management**
- Goal: Restore normal service operations as quickly as possible
- Focus: Minimise immediate business impact of a disruption
	- "Fire department" fighting an active fire
**Problem Management**
- Goal: Identify root cause of one or more incidents to prevent reoccurance
- Focus: Root cause analysis (eg. 5 whys, fishbone diagram) and create a Known Error Database
	- "Fire inspector" for identifying cause of fire post-incident

# 9 - Change, Configuration, Release and Patch Management
**Change Management**: Overarching process to ensure changes are made efficiently and with minimum disruption
- **Patch Management**: Subset of change management, focused on acquiring, testing, and installing code changes to address security vulnerabilities
**Configuration Management**: Process of identifying, controlling and tracking all versions of hardware, software, and documentation (Configuration Items - CIs) 
**Release Management**: Process of planning, scheduling, and controlling software build through different stages into production
- **Types of Releases**
	- **Major**: Significant new function
	- **Minor**: Small enhancements and fixes
	- **Emergency**: Urgent fixes to prevent significant business impact (often bypass testing, increased risk)
- **Key Controls**
	- Formal (documented) request, authorisation, testing, and implementation procedures
	- Segregation of duties between development, testing, and production environments
	- **Critical Control**: Documented and tested rollback plan MUST exist to restore the system to it's previous state if a release fails

*Exam Tip: Auditor's role is to verify that formal change control procedures exist, are documented, and are followed for all types of changes*

# 10 - IT Service Level Management
**ITSM**: Process-based approach to managing IT as a service to the business, often guided by frameworks like ITIL

**Service Level Agreement (SLA)**: Formal agreement between an IT service provider and a customer detailing services to be provided. 
- Key components of an SLA
	- Describes serve in non-technical business-focused terms
	- Defines specific, measurable service levels (eg. 99% uptime)
	- Includes penalties for non-performance

*Exam Tip: Organisation can outsource responsibility for service delivery, but it cannot outsource the accountability for protecting its data and providing service to its customers*

# 11 - Database Management
**Database Management System (DBMS)**: software that organises, controls, and provides access to data (eg. Oracle, MSFT SQL Server)

**Database Structures**
- **Relational (RDBMS)**: Most common, organises data in tables with rows and columns
	- **Primary Keys**: Unique identity, only one per table
	- **Foriegn Keys**: Used to enforce relationships between two tables. if a table has a Foriegn key, it corresponds to a still-existing primary key in the other table
- **Hierarchical/Network**: Older, tree-like or web-like structures
- **Object-Oriented (OODBMS)**: Stores data as objects, useful for complex data types
- **NoSQL**: "Not only SQL", designed for large volumes of unstructured data ("big data")

**Key Database Controls**
- **Access Controls**: Strictly limit access to data based on principle of least privilege. Special attention to privileged users like Database Administrator with God-like database powers
- **Integrity Controls**: Refenetial integrity to ensure relationships between tables are maintained (can't create an order for a customer that doesn't exist in the customer table)
- **Concurrency Controls**: Manages simultaneous updates using techniques like *record locking* to prevent two users changing the same piece of data at the same time
- **Audit and Logging**: Database activity monitoring (DAM) should be enabled, logs should be regularly reviewed

# Key Exam Takeaways
- **Master the fundamentals**: Know the OSI model, key hardware, and network devices
- **Differentiate Key Concepts**: Be absolutely clear on the difference between Incident vs Problem Management
- **Focus on Risk and Control**: For every operational process, understand the primary risks and key controls an auditor would look for
- **Think Like an Auditor**: Your role is to evaluate and provide assurance, which includes reviewing plans, testing controls and assessing processes
	- You do NOT perform the operational tasks
- **Accountability is Paramount**: Accountability for risk and service delivery always remains with the enterprise and when a service is outsourced. 


---
**This also reminds me of**... 

---
# References
