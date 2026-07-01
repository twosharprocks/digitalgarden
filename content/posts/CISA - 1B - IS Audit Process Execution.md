---
title: "CISA - 1B - IS Audit Process Execution"
created: 2026-04-20
updated: 2026-06-30
status: seed
draft: false
tags:
  - cyber-security
  - cisa
  - study
Related:
  - "[[CISA]]"
  - "[[CISA - 1A - IS Audit Process Planning]]"
Video: https://www.youtube.com/watch?v=iR5sRFWbpnA&list=PL7XJSuT7Dq_UvA2knww9Rlzz2JHUpeOAb&index=2
---
# 1 - Audit Project Management
## Structured Repeatable Process
- Process Flow
1. Define Scope & Objectives
2. Gather Evidence
3. Evaluate Strengths & Weaknesses
4. Form Conclusions
5. Prepare Report
6. Follow-Up

*Exam Tip: An effective audit is managed like a formal project*

## Three-phase Framework
1. Planning Phase: Determine subject, define objective, set scope pre-audit planning, determine procedures
2. Fieldwork & Documentation Phase: Acquire data, test controls, discover & validate issues, document resuts
3. Reporting phase: Gather requirements, draft report, issue report follow-up

## Fieldwork & Documentation Phase
- **Acquire Data**: File share, GRC tools, ect) 
- **Test Controls**: Apply techniques (interviews, observation, and inspection)
- **Discover & Validate Issues**: Identifying deviations from expected outcome (policy requirements
	- Form the basis of findings
- **Document Results**: Recording every test, observation, and piece of evidence in work papers per organisational standards

## Audit Programs & Work Papers
- **Audit Program**: Step-by-step instructions (the "recipe" for the audit). Formal documentation, repeatability, and meeting professional standards
- **Work Papers**: Bridge between audit objectives and the final report. Must provide clear traceability from a finding back to collected evidence. Must be secure and retained based on legal & organisational requirements

## Auditors Responsibility Regarding Fraud
- **Management's Responsibility**: Establish, implement and maintain internal controls to deter and detect fraud
- **Auditor's Responsiblity**: Exercise professional care, be alert to opportunities or indicators of fraud, and have knowledge of common fraud indicators
- **Auditor's Action**: Communicate the need for a detailed investigation to appropriate authorities if fraud is suspected

## Agile Auditing
- **Traditional (Waterfall) Audit**: Used for regulatory compliance, large-scale audits
	- Structure: Plan - > Fieldwork - > Report
- **Agile Audit**: Suited to continuous or IT operations. Iterative, collaborative, and responsive to change. Blurs line between planning & fieldwork. Focuses on:
	- Individuals & interactions over processes and tools
	- Customer (auditee) collaboration over contract negotiation
	- Responding to change over following a rigid plan

## Agile development Model
- **Sprint Planning**: 1-2 week planning development, testing, demonstration

## Key Benefits of Agile Auditing
- **Reduced Planning Time**: Sprints condense planning
- **Streamlined Engagements**: Planning, fieldwork and reporting combined into single cohesive engagement
- **Direct Customer Collaboration**: Auditee is part of the process (daily "scrum" meetings)
- **Flexible Scope**: Allows for real-time adjustments as new information is discovered
- **Real-time assurance**: Findings are communicated as they're discovered, not held for the final report

# 2 - Sampling Methodology
## Why Sample? 
- Time and cost often preclude 100% verification
	- Goal: Infer characteristics about whole population from representative sample
- Two Main Purposes
	- Compliance Testing: Are controls working as designed? 
	- Substansive Testing: Data and transactions accurate & valid

## Compliance v Substansive Testing
- **Compliance Testing**: Controls being applied consistently and effectively? 
	- Example: Select 30 change requests to verify each has managers approval signature
	- Focused on **the process*
- **Substantive Testing**: Any monetary errors or data integrity issues in the final data
	- Example: Recalculate interest on a sample of 50 loans to verify accuracy of total interest income reported
	- Focused on **the outcome and data**

If **Compliance Testing** shows controls are strong and reliable, the auditor can justify reducing *Substansive testing*

If **Compliance Testing** shows controls are weak/non-existent, the amount of *substantive testing* needs to increase to compensate

## Statistical vs. Nonstatistical Sampling
- **Statistical Sampling**: Uses laws of probability with calculation of sample size and evaluation. Allows the auditor to state conclusions with a specific confidence level
- **Nonstatistical Sampling**: Based on auditor's experience and judgement by selecting items deemed most risky or material. Drawback is results cannot be mathematically projected to the entire population

## Decoding Statistical Sampling
- **Confidence Coefficient**: Probability sample is a true representation. Larger sample = higher confidence
- **Level of Risk**: 1 - Confidence Coefficient (eg. CC=95% - > Risk = 5%)
- **Precision**: Acceptable range of error. Larger sample = tighter precision
	- **Tolerable error rate**: Maximum error rate acceptable before control is ineffective
	- **Expected error rate**: Estimate of errors you'll find

## Key Sampling Mthods
- **Attribute Sampling**: "How many?", determines the rate of occurance of a characteristic. (eg. % of change requests with proper approval)
- **Stop-or-Go Sampling**: Efficient form of attribute sampling when few errors are expected, stopping audit test when sufficient assurance is achieved (saves time)
- **Discovery Sampling**: Specialised technique for detecting a single instance of a critical event (eg. Fraud, major control circumvention)
- **Variable Sampling**: "How much?", substantive testing to estimate a numerical value (eg. Total dollar value of inventory errors)
- **Stratified Mean Per Unit**: Variable sampling that divides population into subgroups (strata) to reduce variability, allows smaller more efficient sample size
- **Judgmental Sampling**: No-statistical method using auditor experience to select items of risk or significance

![[CISA - Domain 1B - Sampling Methods]] 

# 3 - Audit Evidence Collection Techniques
- **What is audit evidence?**: Information used by the auditor to determine if the entity or data being audited follows the established criteria or objectives. 
- **Three Pillars of Quality Evidence**
	- *Sufficient* - Is there enough? (Quantity)
	- *Relevant* - Does it relate to the audit objective (Quality)
	- *Competent/Reliable* - Can it be trusted? (Quality)

## Determinants of Evidence Reliabilty
**Hierarchy of Reliability** (Highest to Lowest)
1. Direct Observation by auditor
2. Evidence from an independent, qualified third party (eg. Bank confirmation, SOC Report)
3. Evidence from a well-controlled internal process (eg. system-generated log from a secure system)
4. Documentary evidence from the auditee (eg. Manually created list, a screenshot)
5. Verbal statements from the auditee (least reliable, always corroborated)

## Evidence Gathering Techniques
- **Reviewing**: Review organisational structures, policies, standards, and system documentation
- **Interviewing**: Conducting *structured inquiries* with appropriate personnel
- **Observing**: Watching processes and employees performing their duties in real-time
- **Repreformance**: Independently executing a control procedure to verify (eg. Checking a locked door)
- **Walk-throughs**: Tracing a single transaction from initiation to completion in order to understand the entire process & its controls

# 4 - Data Analytics
## Leveraging Data Analytics
- Allows the auditor to test full data sets (100%) instead of just samples
- **Common Use Cases
	- Identify exceptions or potential fraud
	- Assess control effectiveness
	- Conduct enterprise-wide risk assessments
	- Identify business process improvements and inefficiencies

## Computer-Assisted Audit Techniques (CAAT)
- **Generalised Audit Software (Gas)**: Purpose-built software for auditors
	- Can directly read and analyse data from various database platforms, flat-file systems, and ERPs
	- Performs functions like file access, data selection, statistical analysis, duplicate checking, and gap detection
- **Other CAATs**: Utility software test data, vulnerability scanners, penetration testing tools. 

## Continuous Auditing vs Continuous Monitoring
- **Continuous Monitoring**: Internal control process performed by management to observe performance of systems and controls in real-time (eg. Security alerts)
- **Continuous Auditing**: Independent and objective process by auditor to perform tests and assessments on a continuous or nor near-continuous basis (eg. Auditor's system independently querying user access list each day to identify and report conflicting permissions)

## Five Techniques for Continuous Auditing
- **Scarf (System Control Audit Review File) / EAM (Embedded Audit Module)**: Audit software embedded into host application to select/log transactions that meet specific criteria (Highly complex, **embedded** where regular processes cannot be interrupted) 
- **Snapshots**: Take pictures of transactions as it follows through system to create an audit trail (Medium complexity, **audit trail** tracing transaction path)
- **Audit Hooks**: System alert that call auditor attention in real-time (Low complexity, **real-time notifications**) 
- **Integrated Test Facility (ITF)**: Dummy company/division in live production environment to test transactions (High complexity, **dummy entity** using test data in live environment)
- **Continuous and Intermittent Simulation**: System simulating processing of specific transactions and auditing them in parallel (Medium complexity, **simulates** transactions that require examination)

## Role of AI & ML in Auditing
- Automates tedious manual processes
- Identifies complex patterns and anomalies
- Allows **Continuous Auditing**
	- Inadequate testing of the Ai can produce questionable results
	- Training data must be correct, complete and unbiased
	- Balance trust in the machine with professional skepticism an human judgement

# 5 - Reporting and Communication Techniques
- **Effective communication** is what gives the audit it's value
- Key Auditor Skills
	- **Facilitation**
	- **Negotiation**
	- **Conflict Resolution**
- **Goal is not to "win" an argument, but to *persuade management* to take corrective action and improve controls

## The Exit Interview
- Formal meeting with auditee management at the end of fieldwork
- Key Objectives
	- Ensure the factual accuracy of all findings before they're written
	- Discuss recommendations and ensure they are realistic, practical and cost-effective
	- Negotiate and agree upon implementation dates
	- **"No Suprises" rule**: Avoid blindsiding management in final report

## Key Elements of an Audit Report
1. Introduction
2. Overall Conclusion & Opinion
3. Reservations/Qualifications: Limitations affecting the audit
4. Detailed findings/recommendations
- For each finding, include
	1. Condition: What is the weakness
	2. Criteria: What should it be (standard, policy, best practice)
	3. Cause: Why did it happen (root cause)
	4. Effect/Risk: What is the business impact? Why should management care? 
	5. Recommendation: How to fix it
	6. Materiality: Relative importance of a finding (not all findings are equal)
	7. Follow-up activities
		1. Must include followup activities


---
**This also reminds me of**... 

---
# References
