---
title: "CISA - 2B - IT Management"
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
  - "[[CISA - 2A - Governance]]"
video: https://www.youtube.com/watch?v=8__h8iThjF0&list=PL7XJSuT7Dq_UvA2knww9Rlzz2JHUpeOAb&index=4
---
# 1 - IT Resource Management
The effective and efficient management of all IT resources: people, technology, and finances to achieve enterprise goals
- **IT Portfolio Management**: Ensure the enterprise is pursuing the best mix of IT projects to achieve its goals, with a focus on being a strategic process to decide where to invest, continue investing, or divest, based on value and strategic alignment
- **Business Case**: A formal, documented justification is required for all significant projects, even those that are mandatory for regulatory compliance
	- Used to evaluate results against the original plan after completion

## HR Management - Hiring & Onboarding
- **Key Hiring Controls**
	- Background checks
	- Confidentiality & NDAs
	- Disclosure of Conflict of Interest
	- Codes of Professional Conduct/Ethics
- **Employee Handbook**: Explains security policies, acceptable conduct, and company expectations
	- Note: This is a source of information, not a control itself

## HR Management - During Employment
- **Objective**: Manage performance and mitigate insider risk
- **Performance Management**: SMART Goals 
- **Training & Development**
	- Ongoing training is critical due to the pace of technology changes
	- Cross-training reduces dependency and provides backup
		- Risk assessment is required to ensure it doesn't create a new risk by giving one person too much knowledge (avoid SoD concern)
- **Key Detective Controls**
	- Required Vacations & Job Rotation: Uncovers fraudulent acts original employee was concealing

## HR Management - Termination
- **Objective**: Protect enterprise assets and data when an employee separates
- **Termination policies**: must be clearly defined for voluntary and involuntary separation
	- Involuntary brings additional risks
*Exam Tip: Same access revocation and reissue process should apply to employees transferring to a different department (role change is a job change)* 
- **Critical Control Procedures** (Offboarding checklist)
	- Return of all assets
	- Immediate revocation of access (including network, cloud, app-specific, ect)
	- Notification: Alert relevant staff and security personnel (Failure to notify may delay revocation of access)

## Financial Management Practices
- **Cost Allocation (Charge back)**: Process where costs of IT services are allocated back to the business functions that use them (makes business units more aware of IT costs and encourages efficient use)
- **IT Budgets**: Must lnk spending to short-term projects and long-term strategic objectives

*Exam Tip: ISACA perceives that IT and Security functions exist to serve the business*

## Capital vs Operating Expenses
- **Capital Expense CapEx)**: One-time purchase of a long-term asset (eg. Buying software to install on-prem)
- **Operating Expense (OpEx)**: Recurring operational cost (eg. Monthly cloud software)

*Exam Tip: Is auditor MST understand that the misclassification of expenses can be used to fraudulently manipulate financial statements.  Auditor should verify It costs are classified correctly according to established accounting standards*

## Information Security Management Responsibilities
- **Objective**: Safeguard enterprise's information assets by maintaining Confidentiality, Integrity, and Availability (CIA) 
- **Key Responsibilities**
	- *Risk Management & Assessment*: Identify, assess and implement strategies to mitigate risk
	- *Security Policy Development*: Develop and enforce security policies, standards, and procedures
	- *Incident Response & Management*: Establish procedures to handle security incidents and coordinate response efforts
	- *Security Awareness and Training*: Educate employees to create a security-concious culture
	- *Vulnerability Management*: Scan for weakness, apply patches, and conduct penetration testing
	- *Identity & Access Management (IAM)*: Manage user accounts and enforce the principle of least privilege (No permanent 24/7 Admin access)
	- *Compliance Management*: Ensure compliance with relevant laws, regulations and industry standards
*Exam Tip: Be familiar with these core functions and understand how they work together to protect the organisation*

# 2 - IT Vendor Management
## Sourcing and Outsourcing Strategy
- **Sourcing**: How the enterprise obtains IT functions (Insured, outsourced, hybrid)
- **Outsourcing**: Strategic decision to transfer delivery of services to a third party

***Golden Rule of Outsouricing***: An enterprise can outsource a service, but can **NEVER** outsource accountability for risk
- Management remains fully responsible

- **Globalisation Risks**
	- Legal, regulatory and tax issues
	- Cross-border data flow restrictions
	- Geopolitical instability
	- Cultural and Language differences
*Exam Tip: Additional Complexities = Additional Risks*

## Vendor Contracts and SLAs
- **Key Contract Clauses for CISA Exam
	- ***Right to Audit***: Explicit right to audit the vendor's controls
	- ***Security Requirements***: Vendor must comply with clients security policies and all relevant regulations
	- ***Software Escrow***: Custom built software has source code held by a neutral third-party, released to the client if the vendor fails to meet obligations or goes out of business
	- ***Subcontractor Approval***: Vendor must identify all subcontractors and require client approval to change them. 
	- ***Service Level Agreement***: Contractual Agreement that defined level of service, which must Include;
		- Measurable metrics
		- Penalties for non-performance
		- Ideally rewards for exceeding expectations (incentive) 

## Audit Types
- **SSAE - Statement on Standards for Attestation Engagements**
	- SOC 1: Mainly financial controls and used by CPAs auditing financial statements
	- ***SOC 2***: Assesses the design of security processes *at a specific point in time*
		- Often requires an NDA due to sensitive contents
		- SOC2 has become the de facto global standard
	- SOC 3: Only contains auditor's general opinions and non-sensitive data, publicly shareable


# 3 - IT Performance Monitoring and Reporting
## Key Indicators
- **Key Performance Indicator (KPI)**: Measure of how well a process is performing, and a lead inidicator of future success (eg. Percentage of projects delivered on time and on budget)
- **Key Risk Indicator (KRI)**: Metric that provides early warning of increased risk exposure before an incident occurs (eg. Sharp increase in the number of phishing attempts detected)
	- Reports on the future
- **Key Control Indicator**: Measure of how well a specific control is performing in mitigating risk (eg. Percentage of servers that are compliant with the patching policy). 
	- Reports on the past
## Balanced Scorecard
Strategic management tool for assessing IT performance that goes beyond purely financial measure to provide a holistic & balanced view. 

Four key perspectives on IT Performance
- **Business Contribution**: How does senior management view IT? 
- **User Orientation**: Customer satisfaction and retention
- **Operational Excellence**: How effective and efficient are the internal IT processes? 
- **Future Orientation**: How well is IT positioned to meet future needs? 

***ISACA preferred tool for IT performance measurement*** because it directly links IT performance to the overall business strategy from multiple viewpoints

## Performance Optimisation Methodologies
- **Continuous Improvement**: Philosophy that performance optimisation in an ongoing process. Uses the "Deming Cycle" (aka PCDA) 
	- *Plan* to establish objectives
	- *Do* to implement the plan
	- *Check* to study the results against expectations
	- *Act* to correct action based on what was learned
- **Six Sigma**: Data-driven approach focused on process improvement and defect reduction
	- Auditors validate the integrity of process measurement systems, review the consistency of control implementation, and check that improvements are sustained
- **Business Process Reengineering (BPR)**: Radical redesign of business processes to achieve dramatic improvements in performance (cost, quality, speed)
	- Auditors look for evidence of business impact analysis (BIA), control re-establishment post-BFR, documentation of new processes and segregation of duties. 

# 4 - Quality Assurance and Quality Management of IT
## QA vs QC
- **Quality Assurance (QA)**: Process oriented and Proactive. Planned an systematic pattern of actions to provide confidence that *processes conform to standards*
	- To prevent defects from occuring
	- eg. Ensuring developers follow the secure coding standard through training & code review
- **Quality Control (QC)**: Product oriented and Reactive. Observation techniques and activities used to find defects in a finished product. 
	- To identify and correct defects before release
	- eg. Performing vulnerability scanning on the completed application

## Quality Management Function
- **Independence is Key**: QA function should be independent of development and operation
- **Segregation of duties**: Individual should never perform a quality review of their own work
- **Quality Management Systems (QMS)**: Overall framework of processes and standards to control, measure and improve quality across the IT department (eg. ISO9001) 

## Exam Tips
Accountability for risk **always remains with the client** even when a service is outsourced (core governance principle)

Know the critical clauses for vendor contracts (especially the right to audit and the purpose of the SLA) 

Be able to clearly explain the difference between a SOC1 (financial) and a SOC2 (security/operational) report. 
- ***Also know the difference between SOC2 Type I (Point in time) and Type II (Period of time, 6months of longer)***

Understand the purpose of the HR controls like mandatory vacations and job rotations

Recognise why the **IT Balanced Scorecard** is the preferred performance measurement tool because of it's multi-perspective approach

Be able to provide examples of **Quality Assurance** and **Quality Control** 

---
**This also reminds me of**... 

---
# References
