---
title: "CISA - 3B - IS Implementation"
created: 2026-04-27
updated: 2026-06-30
status: seed
draft: false
tags:
  - cyber-security
  - cisa
  - study
Related:
  - "[[CISA]]"
Video: https://www.youtube.com/watch?v=2MMZ-hqSY50&list=PL7XJSuT7Dq_UvA2knww9Rlzz2JHUpeOAb&index=6
---
# 1 - Testing Methodologies
- **1. Unit Testing**: Individual program module (by developers)
- **2. Integration Testing**: Testing connection and data flow between modules
- **3. System Testing**: Testing entire integrated system to verify it meets technical and functional requirements (by test team in non-prod environment)
	- **Recovery Testing**: Check systems ability to recover after failure
	- **Security Testing**: Verify access controls and no new security holes introduced
	- **Load, Volume and Stress Testing**
		- Load: Performance with large data quantity (peak hours)
		- Volume: Maximum volume of records the system can handle
		- Stress: Maximum number of concurrent users the system can handle
	- **Performance Testing**: Testing system against benchmarks
- **4. Acceptance Testing**: Final gate before implementation, users validate system meets business needs
	- **Quality Assurance Testing (QAT)**: "Did we build the system right?". Focused on technical aspects, performed by IT department, Verify it works as documented and to all tech specs
	- **User Acceptance testing (UAT)**: "Did we build the right system". Focused on functional aspects and business readiness, performed by business users, ensure system is production-ready and meets business requirements from user perspective (This is the ***final sign-off***)

*Exam Tip: UAT is the most critical milestone before implementation, and **business users** give final approval not the IT department*

## Other Testing
- **Alpha Testing**: Early form of testing by developers (eg. System testing)
- **Beta Testing**: Form of UAT with system released to a limited number of external users for real-world exposure
- **White Box testing**: Testing internal logic and code structure (tester can see code operation)
	- Used in *unit* and *integration* testing
- **Black Box testing**: Testing system function without knowledge of internal code (inputs & outputs only)
	- Used in *integration* and *acceptance* testing
- **Pilot testing**: Preliminary test focused on specific, predetermined aspects of a system in a limited evaluation
- **Regression Testing**: Rerunning test cases after a change to ensure new errors have not been introduced
- **Parallel Testing**: Feeding data into old and new systems to compare results and verify new system performance
- **Bottom-Up Tetsing**: Tests individual atomic units working upward until complete system is tested
	- Advantage: Errors in low-level modules are found early
- **Top-Down Testing**: Starts testing major functions and interfaces at a high-level then works down to details of individual modules
	- Avantage: Tests major functions early, interface errors found sooner, build user confidence by seeing a working version early

## Data Integrity Testing and the Acid principle
- **Data Integrity Testing**: Examine accuracy, completeness, consistency, and authorisation of data. Ensures data elements confirm to validation rules
- **Acid Principle for Transactions** - IMPORTANT
	- **Atomicity**: All parts of a transaction complete, or none do (no partial updates)
	- **Consistency**: Transaction brings the database from one valid state to another
	- **Isolation**: Concurrent transactions do not interfere with each other
	- **Durability**: Once a transaction is complete it survives system failure

## Application Systems Testing Techniques
- **Generalised Audit Software (Gas)**: Class of Computer Assisted Audit Techniques (CAATs)
	- **Test Data/Deck**: Simulates transactions through real programs to verify controls & edits
	- **Parallel Operation**: Process production data through old and new systems at the same time to compare results
	- **Integrated Test Facility (ITF)**: Uses a fictitious file/entry in live production database to process test transactions alongside live data
	- **Parallel Simulation**: Processes production data using programs that simulate the application's logic to verify the live system results
*Exam Tip: Integrated Test Facility (ITF) is the most likely to be an exam topic*

## IS Auditor's Role in Testing
Provide independent assurance over the entire testing process
- **Review the Test Plan**: Ensure the plan is complete, tests controls, shows evidence of user participation & sign-off
- **Reconcile Data**: Ensure accuracy and completeness in control totals and converted data
- **Interview users**: Speak to users to gauge their understanding of the new system, methods and operating instructions
- **Verify Security**: Develop & execute access tests to verify system security is functioning as designed


# 2 - Configuration and Release Management
**Configuration Management**: identifying, defining, and baselining ALL components of a system and controlling changes throughout their lifecycle

**Configuration Management Database (CMDB)**: Central repository storing information on hardware and software assets and their relationships

**Release Management**: Process of managing, planning, scheduling and controlling a software build through different stages and environments
- Includes testing and deploying releases into production

**Key Control**: A new version of a system should only be built from trusted, baselined items stored in a controlled library

# 3 - System Migration, Infrastructure Deployment, and Data Conversion
## System Implementation and Planning
- **Implementation**: Initiated after successful testing phase and sign-off. Key part is panning ongoing operational life (detailed support structure and training plan)
- **Knowledge Transfer methods**: Plan should define how knowledge is transferred to support staff including *shadowing* (observing project team in action) and *Relay-Baton Approach* (Knowledge/responsibility transfer in small manageable portions) 
- **Training Plan**: Formal plan to address skill gaps with defined content, scheduling, duration and delivery mechanism

## Go-Live Process
- **Data Conversion/Migration**: Process of converting and moving data from old to new
	- Key concerns & Checklist: Data cleansing, verification, audit trails, exception reports, conversion dress rehearsal, rollback plan
		- IS auditor's primary concern in data migration is integrity, accuracy, and completeness of the data
	- *Exam Tip: IS auditor must VERIFY a fallback/rollback plan exists AND HAS BEEN TESTED. Migration should not proceed without a proven way to revert to previous stable state.*
- **Changeover (Go-live/Cutover)**: Switch from old to new
	- **Parallel Changeover**: Pro: lowest risk, fallback. Con: Highest cost, resource intensive
		- Safest and most expensive
	- **Phased Changeover**: System implemented one module/department at a time. Pro: moderate risk/cost. Con: Resource challenges
	- **Abrupt Changeover**: AKA "Direct Cutover". Specific Data cutover between systems. Lowest cost, highest risk, no fallback
- **End-User Training**: Preparing users to operate new system effectively
- **Certification and Accreditation**: Evaluating and accepting system for production use after implementation
	- **Certification**: Technical process where assessor performs assessment of systems management, operational/technical controls against a standard
	- **Accreditation**: Formal management decision by senior official to authorise operation of an information system and explicitly accept the residual risk to the enterprise
	- *Exam Tip: Accreditation is the final step, and an acceptance of residual risk by business management (not IT or auditors)*
- **After Implementation**: Ongoing maintenance
	- **Change Requests** are formally authorised, prioritised and tracked
	- **Emergency Changes** have documented processes
	- **Security Adequate** to protect production source and executable code
	- **Change Control Log** shows all changes were resolved
	- **Adequate testing** of changes before being moved to production
# 4 - Post-Implementation Review
Determine if the new system have met objectives and identify lessons learned for future projects

Key Areas of Review
- **Adequacy of the system**: Does the system meet user requirements (Are controls working effectively?)
- **Projected costs vs Benefits (Benefits Realisation**): Is the system delivering the promised value from the business vase (ROI)
- **Assessment of the Project process**: Were project management methodologies and standards followed? (Lessons learned)

Auditor's Role
- **Independence is Paramount**: Auditor who consulted heavily on the project should NOT perform the post-implementation review (PIR) 
- **Concentrate on the Control Aspects** of the system and project management process
- Key Steps
	- We're the system objectives and requirements actually met? 
	- Verify cost benefits from the business case are measured and reported
	- Review the Controls from the business case are operating as designed in the live production environment
	- Identify systematic problems by reviewing operator error logs, help desk tickets, and change requests. 

# Key Takeaways
- **Master the Testing Levels**: Know the sequence and purpose of Unit, Integration, System, and Acceptance(QAT vs UAT) testing
- **Differentiate** between White vs Black box testing, Alpha vs Beta testing, Load vs Volume vs Stress Testing
- **Know the Go-Live Strategies**: Risk/Cost trade-offs between Parallel, Phased, and Abrupt changeovers
- **Focus on Risk and Controls**: Data conversion risks (need for a tested rollback plan) and importance of configuration/release management controls
- **Accreditation = Risk Acceptance**: Accreditation is the formal acceptance of residual risk by business management


---
**This also reminds me of**... 

---
# References
