---
title: "CISA - 2A - Governance"
created: 2026-04-22
updated: 2026-06-28
status: seed
draft: false
tags:
  - cyber-security
  - study
  - cisa
related:
  - "[[CISA]]"
video: https://www.youtube.com/watch?v=OUij4a2MGOQ&list=PL7XJSuT7Dq_UvA2knww9Rlzz2JHUpeOAb&index=3
---
# 1 - Laws, Regulations, and Industry Standards
## External Environment
- **Key Focus Areas**
	- Data Privacy and Protection (GDPR, HIPAA)
	- Intellectual Property (IP) 
	- Reliability of financial information (SOX) 
	- Compliance requirements can have global reach
*Exam Tip: Don't need to know law specifics, but must understand that these external requirements shape the control environment*

## Auditor's Role in Compliance
Verify the process of compliance is effective. 
Audit Checklist
- Does the enterprise identify all applicable laws? 
- Is the responsibility for compliance assigned to senior personnel? 
- Is there a process for monitoring, auditing, and enforcing compliance? 

*Exam Tip: Focus on the auditor's role in verifying the existence and effectiveness of a compliance framework*

# GRC
Goal: An integrated holistic view of assurance that enables an organisation to reliably achieve objectives, address uncertainty, and act with integrity

- **Governance**: Managing policies, processes and decisions (Steering the ship) )
- **Risk**: Identifying, assessing, and treating potential risk (Looking for icebergs) 
- **Compliance**: Adhering to laws, regulations, and standards (Following the rules of the sea)

**Assurance** is the level of confidence and trust that an organisation's systems, processes, and controls are effective at protecting information assets, managing risks, and ensuring compliance with relevant standards and policies
- Who, how and what of an audit affects confidence

# 2 - Organisational Structure, IT Governance, and IT Strategy
## Enterprise Governance of IT (EGIT) 
- Integral part of corporate governance that is led by the **Board of directors** and **executive management**
- **Primary Driver**: Strategic alignment of IT with business objectives
- Core Concerns
	- **Value Delivery**: Does It support and enhance business goals? 
	- **Risk Management**: Are IT-related risks identified and managed effectively

Governance sets the direction, management executes it

**IT Strategy Committee**: Board level, advises board on IT strategy, alignment, big picture issues (Strategic direction) 
**IT Steering Committee**: Management/Executive Level, executes the strategy by approving plans/budgets/priorities, (Tactical implementation - Primary role is ensuring IT *projects* support business requirements and deliver value, body that approves and overseas major IT projects) 

## Three Lines Model
- **First line**: Operational Management, owns and manages risks and controls as part of their day-to-day job
- **Second Line**: Risk and Compliance Functions, provide expertise, support, and monitoring over the first line
- **Thrid Line**: Internal Audit, provides independent and objective assurance over first two lines
	- IS Auditors operate in the **third line**

## Separation for Duties
- **Purpose**: Key control to prevent one person from having *conflicting critical responsibilities* to reduce risk of fraud or error
- **Auditor's Role**: Review organisational cart to assess if SoD is properly implemented. 
- **If SoD is not possible**, look for compensating controls
	- Supervisory Reviews
	- Detailed Audit Trails
	- Reconciliation
	- Exception Reporting
# 3 - IT Policies, Standards, Procedures and Practices
## Hierarchy of Governance Documents
- **Policies**: The "Why"? High-level statements of management's intent
- **Standards**: The "What"? Mandatory requirements to ensure compliance with policies
- **Procedures**: The "How"? Step-by-step instructions to achieve policy objectives
- **Guidelines**: The "How-To tips" Recommended, non-mandatory best practices

*Exam Tip: Understand the hierarchy of Policies -> Standards -> Procedures -> Guidelines*

# 4 - Enterprise Architechture and Considerations
## Understanding Enterprise Architechture
- **Purpose**: Blueprint that defines an organisation' structure, operations, and technology to achieve its current and future objectives
- **Primary Advantage**: Guide technology election and ensures new initiatives align with the overall IT framework and business strategy
	- Frameworks like *Zachman* and *TOGAF* provide a structured way to view enterprises
- An IS auditor should identify an EA as incomplete if it *lacks a future-state description*. 
# 5 - Enterprise Risk Management
A structured process to manage threats, reducing risk to an acceptable risk (Residual Risk)
- **Risk Appetite**: Amount of risk the enterprise is willing to take to achieve its goals (Strategic decision by senior leadership) - Willingness to take risk
- **Risk Tolerance**: Acceptable deviation from the risk appetite (Tactical measure) - Acceptable variation
- *Risk Capacity is the maximum bearable risk for the organisation*

*Exam Tip: Asset Identification is the first step in the risk management life cycle* (Can't protect what you don't know you have)

## Four Responses to Risk
- **Mitigate**: Implement controls to reduce the risk (Audit: Controls are implemented and tested)
- **Avoid**: Stop the activity causing the risk (Audit: Activity has been eliminated) 
- **Share/Transfer**: Shift the risk to a third party (Audit: Insurance policy, outsourcing contract)
- **Accept**: Formally acknowledge the risk (Audit: Documented management decision)

*Exam Tip: Red flag for an auditor if management simply ignores a risk without a formal acceptance with a timeline (max annually)*

## Risk Analysis Methods
- **Qualitative**: Descriptive rankings like "High", "Medium", and "Low" (Simple but subjective)
- **Semiqualitative**: Assigns a numerical scale to the qualitative rankings to add structure (eg. High=5, Medium=3, Low=1)
- **Quantitative**: Uses numeric (often monetary) values to describe risk (More objective but can be complex)

## Core Risk Management Process
- IT Risk Identification -> IT Is Assessment -> Ris Response & Mitigation -> Risk & Control Monitoring & Reporting (Loop back to Risk ID)

*Exam Tip: Risk management should be viewed as a continuous, adaptive loop*

# 6 - Privacy Program and Principles
- **Privacy Notice**: For the public/customers
- **Privacy Policy**: For employees (Internal)
- **Privacy Impact Assessment (PIA)**: Process to identify and reduce privacy risks (typically before a project starts)
- **Legal Basis for Processing**: Organisations require a lawful reason to process personal data, such as a *Legitimate Interest* and *Consent*

## Privacy Program Fundamentals
- **Data Subject Rights**: Individuals have rights over their data
- **Trans border Data Flow**: Legal complexities of moving data between countries
	- Can be challenging in the cloud with data replication
*Exam Tip: Be aware of data subject rights and major compliance challenge of Trans border data flow*

# 7 - Data Governance and Classification
## Data Governance
Overall strategy or managing data accuracy, integrity, and security - treat as a strategic asset

## Data Classification
Catagorisaing data based on it's severity to apply appropriate protection
- **Benefit**: Allows enhanced control with optimum budget by focusing security on most critical data
- **Typical Levels**: Restricted Confidential, Internal, Public
- Key Roles
	- **Data Owner**: Business manager or director. Accountable for the data and responsible for classifying the data (defines the access rules) 
	- **Data Custodian**: Typically the IT department. Responsible for the safe custody and storage of the data, implements the security controls defined by the Data Owner

*Exam Tip: Data Owner is responsible for classification. The business owns the data, NOT the IT department*

# Exam Tips
- *Board of Directors* holds ultimate accountability for governance
- Distinguish *governance* (setting direction) from *management* (execution)
- *IT steering committee* approves & overseas projects
- **Hierarchy**: Policy -> Standard -> Procedure -> Guideline 
- **Enterprise Architecture (EA)** is incomplete without a **future state**
- **Risk Management** begins with *asset identification*
- Master the **Three Lines Model** and the purpose of GRC
- The **Data Owner (Business)** classifies data, the **Data Custodian (IT)** protects it. 


---
**This also reminds me of**... 

---
# References
