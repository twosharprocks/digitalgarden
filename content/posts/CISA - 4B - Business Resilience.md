---
title: "CISA - 4B - Business Resilience"
created: 2026-04-29
updated: 2026-06-28
status: reference
draft: false
tags:
  - cyber-security
  - cisa
  - study
related:
  - "[[CISA]]"
  - "[[CISA - 4A - IS Operations]]"
---
# 1 - Business Impact Analysis (BIA) 
**Resilience** is an organisation's ability to adapt to disruptions and maintain continuous assets while protecting assets

Three Core Questions the BIA must answer;
- What are the organisation's critical business processes? 
- What critical IT resources are related to these processes? 
- What is the critical recovery period before unacceptable losses are suffered? (Maximum tolerable downtime (MTD)

*Exam Tip: Auditor's role is to verify the BIA process is comprehensive, outputs are accurate, and it's sponsored and approved by senior management*

# 2 - System Resiliency
BIA is required to gather accurate information from the right people

Data Gathering Methods
- Questionnaires: Key users in IT and end-user areas
- Interviews: Group of key users
- Group Meetings: Bring IT and end-users together to reach consensus on business impacts

Analysis - *Identify system Criticality, determine MTD, RPO, RTO*
- Data is tabulated and analysed to develop BCP and DRP
- Impact Bands developed to evaluate impact of downtime (hours, ays, weeks)
- Financial Impact may be assigned to these bands
## Determining Criticality
- **Business process owner** is the most authoritive source
- Indication
	- Supports health and safety? 
	- Disruption will cause significant income loss? 
	- Process is required for legal or statutory compliance
- Classification
	- Critical: Cannot be performed manually, interruption tolerance is low
	- Vital: Can be performed manually for a brief period (<5days)
	- Sensitive: Can be performed manually for an extended period with difficulty
	- Nonsensitive: Can be interrupted for an extended period with little to no cost

*Exam Tip: Understand the inverse relationship between cost of downtime and cost of recovery*
- Short recovery time = higher cost

## System and Operational Resilience
Ability of a system to withstand, adapt to, and recover from unexpected disruption while maintaining core functions

Built with redundant components, fail over mechanisms, and robust data backup strategies to ensure continuous operation

*Exam Tip: Understand the capabilities of various technologies in each area to more effectively assess a customer's resiliency*

## Application Resiliency
- **Clustering**: Installed on multiple servers (nodes) to provide higher availability
	- **Active-Passive**: App runs on ONE active node, with others on standby to take over if active fails
	- **Active-Active**: App runs on EVERY node with high availability and load balancing (requires app to be "cluster-aware")
- **Geo-Clustering**: Clusters spanning cities/countries/continents to protect against site failure

## Network Resiliency
- **Alternative Routing**: Routing info through alt medium like cellular/microwave as a backup to fiber
- **Diverse Routing**: Routing traffic through different physical paths (with split or duplicate cable facilities) to avoid single point of failure (cable cut)
- **Last Mile Circuit Protection**: Redundant connections from telco provider to organisation building
- **Long-Haul Network Diversity**: Multiple long-distance carriers to prevent single carrier failure

*Exam Tip: Organisation's responsibility (not the providers) to ensure adequate network backup*

# 3 - Data Backup, Storage, and Restoration
Key Goal: Backup and restoration stretgy must align with the RPO and RTO from the BIA
- **Immutable Backups**: Critical control against ransomware, backup data is fixed and cannot be altered or deleted even by an admin
	- 3-2-1 Strategy: 3 copies of data, 2 different media types, 1 copy off-site
- **Backup Schemes**
	- **Full Backup**: Copies all files (slowest but simplest)
	- **Incremental backup**: Changes since last backup of any type, fastest backup, least storage, most complex restoration
	- **Differential Backup**: Changes since last full backup, faster restore than incremental, slower than incremental
- **Data Storage Resilence (RAID)**
	- Combines physical disks into logical units for redundancy/performance
- **Replication**
	- **Syncronous**: Local write is not confirmed until data is successfully written to the remote site
	- **Asynchronous**: Data is replicated on a scheduled basis, allows some data loss but less demanding on the network
- **Backup Media**: Tapes, removable hard drives, snapshots, virtual tape libraries
	- **Rotation Method (GFS)**: Grandfather(monthly)-Father(weekly)-Son(daily)
	- **Offsite Controls**: Must have physically secure access, environmental controls and inventory. 
	- **Backup media should always be encrypted**

# 4 - Business Continuity Plan (BCP) 
Comprehensive organisation-wide plan to sustain essential business operations during/after disruption
- **Owned by Senior Management**: BCP addresses all functions and assets required for the organisation to survive (people, processes, and technology)
- **Protection of human life** is the ultimate priority

*Auditor's Tip: Single best way to determine the effectiveness of a BCP is reviewing the results of previous tests*

**Plan Development**
- Based on BIA and documented in simple language, includes procedures, responsibilities, contact information
**Plan Testing**
- An untested plan is an unreliable plan. Goal is to evaluate effectiveness and performance of personnel
- Types
	- **Desk-based/Paper Test**: Paper walk through of plan with key personnel
	- **Simulation/Preparedness Test**: Localised test or role-playing exercise where actual resources are used to simulate crash but without full interruption
	- **Full Operational Test**: Primary site is actually shutdown and operations are moved to the recovery site

**Auditor's Role**
- **Review the BCP** to ensure it aligns with business objectives and BIA
- **Evaluate the Plan** for adequacy, currency, and completeness
- **Review results** from previous tests
- **Evaluate Offsite storage facilities** for proper security and environmental controls
- **Interview key personnel** to confirm they understand their roles and responsibilities
- **Review contracts** for alternate sites and insurance coverage for adequacy

# 5 - Disaster Recovery Plans (DRP) 
- **RTO - Recovery Time Objective**: Maximum acceptable downtime for a system after disaster is declared. *How quickly must we be back online?*
- **RPO - Recovery Point Objective**: Maximum acceptable amount of data loss measured in time. *How much data can we afford to lose? 4 hrs? 1 day?*
	- RTO and RPO are outputs of the BIA and dictate the cost and type of recovery solution needed
*Exam Tip: Lower RTO/RPO values mean HIGHER costs*

**Recovery Site Alternatives**
- **Mirrored Site**: Fully redundant with real-time data, fully staffed and equipped, near-zero RTO
- **Hot Site**: Fully equipped, needs current data to be loaded, mins-hours RTO
- **Warm Site**: Partially equipped, needs hardward/software/data, hours to days RTO
- **Cold Site**: Empty facility with space, power, cooling but no IT equipment, weeks to months RTO
- **Reciprocal Agreement**: Share facilities with another company, unreliable RTP

*Exam Tip: Reciprocal agreements are generally not considered a viable option to due security, resources and compatibility*

Testing is mandatory to ensure the plan will work. 
Testing progression (least to most disruptive)
1. **Checklist Review**: Distrubut checklists to team members to ensure currency
2. **Structure Walkthrough**: Team reviews plan on paper step-by-step to find gaps
3. **Simulation Test**: Scenario-based role-playing exercise without activating recovery site
4. **Parallel Test**: Recovery site is activated and runs in parallel with primary site
5. **Full Interruption Test**: Primary site is shutdown and all operations are failed over to recovery site

*Exam Tip: Review test plans, observe execution where possible, evaluate documented results to ensure objectives were met/improvements made*

Auditor's Focus
- **Formal Documentation**: Verify all phases of the test (pretest, test, and post test) were fully documented
- **Quantitative Metrics**: Test results must measure the following quantitatively;
	- **Time**: Did the recovery effort meet the Recovery Time Objective (RTO)? 
	- **Data**: Was all the data recovered and did it meet the Recovery Point Objective (RPO)? 
	- **Amount/Throughput**: Was the recovery site able to process the required amount of work and handle the necessary transaction volume? 
	- **Accuracy**: Was the data entry and processing at the recovery site as accurate as it would be under normal circumstances? 
- **Post-Test Followup**: Evaluation is not complete until the auditor verifies a follow-up process is in place. Auditor will look for evidence that any problems or deficiencies found during the test led to formal recommendations, and recommendations were used to update and improve Disaster recovery plan (DRP)

*Exam Tip: Auditor analysis provides assurance of DRP effectiveness in practice*





---
**This also reminds me of**... 

---
# References
