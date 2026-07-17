---
title: "CISA - 3A - IS Acquisition and Development"
created: 2026-04-26
updated: 2026-06-28
status: seed
draft: false
tags:
  - study
  - cisa
  - cyber-security
related:
  - "[[CISA]]"
video: https://www.youtube.com/watch?v=tvXiHA4Ft00&list=PL7XJSuT7Dq_UvA2knww9Rlzz2JHUpeOAb&index=5
---
# 1 - Project Governance and Management
- **Initiating**: High level objectives and securing approvals, documented in project charter
- **Planning**: Develop detailed roadmap, defining scope setting a budget, establishing a timeline and identifying potential risks
- **Executing**: The "Doing" phase. The team performs the work defined in the plan to create the project deliverables
- **Controlling and Monitoring**: Tracking the projects progress and changes in scope/schedule, running alongside execution phase
- **Closing**: Project formally finalised and completed. Final deliverables approved by the client, closing out contracts, documenting lessons learned. 

## Project Governance vs Managment
- **Project Governance**: Sets the *direction* and provides oversight. Oversight framework typically performed by a Steering Committee for how project decisions are made so they align with the business strategy an risk appetite. 
- **Project Management**: Executes the *plan* efficiently. Executing the plan to achieve project goals, performed by a Project Manager. 
- **Project Portfolio Management**: Centralised management of all projects to ensure prioritisation and strategic business objective alignment

*Exam Tip: The IT Steering Committee is the group responsible for prioritising project requests and providing overall governance*

## Key Project Roles and Responsibilities
- **Senior Management**: Demonstrates commitment and approves resources
- **Project Steering Committee**: Provides overall direction, ensures stakeholder representation, ultimately responsible for deliverables, costs, and schedule
- **Project Sponsor**: Business owner providing the funding, champions project, assumes ownership of the outcome
- **User Management**: Assumes ownership of the resulting system, provides user representatives, approves system deliverables
- **Project Manager**: Day-to-day management, monitors costs and schedule, responsible for mitigating project risk (delivery risk)
- **Quality Assurance (QA)**: Independently reviews deliverables to confirm compliance with requirements. 

*Exam Tips: Distinguish between the following roles*
- *The Sponsor funds the project and is responsible for risks to business benefits*
- *The Steering Committee governs the project*
- *The Project Manager manages the project and is responsible for risks to project delivery*

## The Triple Constraint 
AKA "The Iron Triangle" 
- **Scope**: Deliverables, what the project will deliver
- **Cost**: Budget for the project
- **Time**: Duration, Schedule for completion

*Exam Tip: QUALITY is the central theme impacted by these three constraints*

## Project Success Factors and Tools
- **Work Breakdown Schedule (WBS)**: Decomposes project into smaller, manageable work packages. Foundation of cost and schedule planning
- **Gantt Chart**: Bar chart illustrating the project schedule
- **PERT/CPM**: Network diagram that identifies the ***Critical Path*** (longest sequence of dependent tasks to determine projects minimum duration)

## Cost Estimation Techniques
- **Analgous**: Uses costs from a similar past project (Quick but least accurate)
- **Parametric**: Uses statistical relationships (eg. Cost per server), more accurate
- **Bottom-Up**: Estimates every single work package and rolls them up, most accurate & time consuming

## Function Point Analysis (FPA)
- Technique to measure software size based on user functionality (inputs, outputs, files, ect) not lines of code

## Planning, Estimation, and Benefits
- **Project Benefits Realisation**: Continuous process to ensure project outcomes achieve the promised business value (described in the business case)
	- Measured by things like ***Return on Investment (ROI)***
	- *Exam Tip: Do not need to calculate FPA on the exam, just need to know it's a technique for estimating software size based on user functionality*
	- *Exam Tip: Project success is ultimately measured by benefits realisation, not just finishing on time and within budget*

## Auditors Role in Project Measurement
- **Provide independent assurance**: Project is being managed effectively, risks are controlled, system will meet business requirements
- **Key Activities**: 
	- Review project charter/business case/risk management process
	- Observe steering committee meetings
	- Review deliverables at key milestones to ensure controls are built-in
	- Advise on control deficiencies
- **Independence is Crucial**: Provide assurance about the project, not manage or make decisions for the project
	- IS auditor is an ***advisor*** not a do-er

# 2 - Business Case and Feasibility Analysis
## Business Case
- **Justifying the investment**: Business Case is the single most important document for project justification. Rationale for the project based on expected business benefits
- **Purpose**: Links the project to strategic business objectives, provides basis for investment decision, sets baseline for measuring success via benefit realisation

*Exam Tip: Remember the function and importance of the business case!*

- **Stage Gates/Kill Points**: Pre-defined points to re-evaluate project's business case (If no longer valid, project should be terminated). 
- **Feasibility Study**: Determine if the project is viable before significant investment
	- **Technical**: Do we have the skills to use it? 
	- **Economic** Benefits outweigh costs (Cost-Benefit Analysis, ROI, Total Cost of Ownership)
	- **Operational**: Will the new system work within the organisation's culture and existing processes
	- **Schedule**: Can it be completed in an acceptable time? 
	- *Exam Tip: Is auditor's role is to review the business case and feasibility study to ensure cost justifications are verifiable, chosen solution was reasonable and the process was unbiased*
	- ***The auditor is an ADVISOR not a do-er*** 

# 3 - System Development Methodologies
## System Development Life Cycle (SDLC)
Structured framework for development and maintain systems, with two main approaches
- **Predictive (Waterfall)**: Assumes requirements are well-understood and stable, progress flows sequentially through distinct phases, very formal and documentation heavy
	- Each phase must be fully completed before the next begins
	- Used when requirements are non-negotiable, determined by safety regulations medical standards, errors impact life-and-death
	- Inflexible, very costly to make changes once a phase is complete
	- *V-shaped model* is an extension of Waterfall that focuses on the relationship between each development phase and it's testing level. Eg. User Acceptance Testing validates requirements while Unit Testing validates detailed design
- **Adaptive (Agile)**: Assumes requirements will change, progress is iterative and incremental with short cycles and rapid feedback loops
	- **Agile**: Collaborative, iterative approach to software development - small adaptable increments called "sprints"
	- **Scrum**: Popular Agile framework that helps agile teams work together to deliver complex projects
	- **DevOps**: Culture of combining Development and IT Operations to shorten development life cycle with automation
		- Enables Continuous Integration/Continuous Delivery (CI/CD)
	- **DevSecOps**: Evolution of evOps that integrates security (shift left)
*Exam Tip: Key audit concern is ensuring Separation of Duties (SoD) is maintained through automated controls*

## Other Key Development Methods
- **Prototyping**: Quickly building a working model to get early user feedback (risk that security, audit trails, backup are overlooked) 
- **Rapid Application Development (RAD)** Prototyping, small teams and powerful teams to develop systems quickly
- **Component-Based Development**: Assembling applications from pre-existing reusable software components
- **Business Process Re-engineering (BPR)**: Radical redesign of business processes to achieve dramatic improvements (risk that critical controls may be re-engineered out)

*Exam Tip: Is auditor must identify key existing controls and evaluate the impact of their removal*

## Traditional SDLC Phases
- **Feasibility Study**: Strategic benefits, costs, viability, to create business case
- **Requirements Definition**: What the system must do with active user involvement
- **Design (Build)**: Detailed technical specifications, architecture, databases, program specs based on defined requirements
- **Development (Build)**: Actual programming (coding) and testing based on design specifications 
- **Final Testing & Implementation**: Final User Acceptance Testing (UAT), data migration, user training, operation of the new system
- **Post-Implmentation Review**: Formal process after system is live, used to determine if the system met objectives and if projected ROI was accurate

## Build vs Buy Decision
When an organisation purchases **commercial-off-the-shelf (COTS)** software, SDLC changes to:
- **Phase 3 - Design** becomes **Software Selection & Acquisition**
- **Phase 4 - Development** becomes **Configuration**

**Request for Proposal (RFP)** is sent to vendors detailing requirements with criteria including;
- Vendor viability
- Support
- Source code escrow (source code held by trusted 3rd party in case vendor goes out of business)

*Exam Tip: IS auditor's role in acquisition is to **review the RFP** to ensure security and control requirements are included, and to **ensure the final contract is reviewed by legal council** and protects the organisation.*

# 4 - Control Identification and Design
- **Core Principle**: Controls must be identified and designed at the earliest stages of SDLC
- **Cost of Defects**: The cost to fix a control weakness increases exponentially the later it is found
- **Application Controls** Controls specific to a business application to ensure data integrity
	- **Input controls**: Preventative, ensures input data is authorised, accurate and complete
		- **Check Digit**: Number added to ID common entry errors
		- **Completeness Check**: Field not left blank 
		- **Limit Check**: Number cannot exceed a max value
		- **Range Check**: Upper and lower bounds for data
		- **Reasonableness Check**: Compare data to expected value (eg. Flagging order for 500 units when 20 is normal)
		- **Validity Check**: Compare data to predefined acceptable values (eg. Gender being M, F, or N)
		- **Duplicate Check**: Chec for transaction entered twice (eg. Invoice number being paid twice)
		- **Sequence Check**: Control numbers to ensure a sequence (eg. Invoice 101, 102, 104 triggers flag for 103)
		- **Existence Check**: Compare data with criteria in a file/table (eg. Transaction code entered in transaction code field)
		- **Key verification**: Compare keying process between two individuals to ensure repeated input (worker number keyed twice by different people to ensure acuracy)
		- **Table Lookups**: Compare data to ensure it complies with criteria in a table (System looks up an entered city code to find corresponding city name)
		- **Logical Relationship Check**: if a condition is true, additional conditions or data relationships may be required to be true (employees hire date must be later than their date of birth)
	- Processing controls: Ensure data remains complete and accurate during processing
		- Key Risk: Direct back-end database updates (eg. SQL injection), access must be strictly controlled, logged and reviewed by management. 
	- Output controls: Ensuring results are accurate, complete and to the correct recipients. 
*Exam Tip: Control identification and design are the most crucial task for an auditor*

## Key Exam Takeaways
- **Understand the roles** of sponsor vs Steering Committee vs Project Manager
- **Business Case** is the ultimate measure of success
- **Auditor's Role** is Independent, not a project participant, and best time to add value is **early** in the SDLC
- Key differences between **Waterfall** vs **Agile**
- **COTS** changes the SDLC
- **Master Application Controls** (especially **Check Digits**)
---
**This also reminds me of**... 

---
# References
