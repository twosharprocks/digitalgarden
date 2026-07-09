---
title: "2025 Volume 6 Future Proofing Cybersecurity -  A Practical Roadmap to Quantum Resilience"
source: "https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/future-proofing-cybersecurity?utm_source=sfmc&utm_medium=email&utm_campaign=general-comms&utm_term=mem_journal_oc_awar_promo_mem-only_november-2025&utm_source=sfmc&utm_content=468420&utm_id=60cd59b0-c7ba-475e-b83b-e946a2db5dcd&sfmc_activityid=ec421849-bc90-4ea6-9205-44fd195fbe86&utm_medium=email"
author:
  - "Pranjal Sharma"
published: 2025-11-01
created: 2025-11-08
related: "[[Reading]]"
tags:
  - unread
  - source
  - physics
  - interests
description: Source
updated: 2026-07-09
status: seed
---
![A digital lock symbolizing security and privacy in the modern online landscape, emphasizing the importance of data protection.](https://www.isaca.org/-/media/images/isacadp/project/isaca/journal/2025/volume-6/j25v6_future-proofing.png?mw=550&hash=ED9BC6D2BE2C174AE0A485208007358D)

**Author:** Pranjal Sharma  
**Date Published:** 1 November 2025  
**Read Time:** 15 minutes  

Quantum computing and its associated risk have been among the most discussed topics within cybersecurity circles for years. However, unlike the risk posed by generative or agentic artificial intelligence (AI), quantum is often perceived as a distant threat, and one that does not require immediate action. This is a grave mistake, however, as while the arrival of mainstream quantum computing may still be years away, its impact is clear: The ability of quantum computers to break cryptography and render modern algorithms obsolete cannot be underestimated. The security of the public internet is based on these algorithms, and the impact of such an event will be widespread.

A critical gap remains between acknowledging the quantum threat and taking concrete steps to mitigate it. This gap is not due to a lack of knowledge, but rather a lack of clearly defined roadmaps to guide organizations to quantum resiliency. Thus, a practical blueprint is presented to help organizations achieve quantum resilience through governance, technical architecture, and implementation techniques.

## Defining Quantum-Resilient Architecture

Quantum computing represents a foundational shift in how information is processed. In contrast to classical computers that use bits representing 0 or 1, quantum computing uses qubits to convey information.[<sup>1</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/?utm_source=sfmc&utm_medium=email&utm_campaign=general-comms&utm_term=mem_journal_oc_awar_promo_mem-only_november-2025&utm_source=sfmc&utm_content=468420&utm_id=60cd59b0-c7ba-475e-b83b-e946a2db5dcd&sfmc_activityid=ec421849-bc90-4ea6-9205-44fd195fbe86&utm_medium=email#1) These qubits can exist in multiple states simultaneously due to quantum principles such as superposition and entanglement, which enable quantum computers to process information exponentially faster than today's computers.

Preparing for a post-quantum world is not a matter of applying a patch or upgrade; instead, it requires a comprehensive approach that encompasses both architectural and procedural changes.

This also opens the door to threats that did not previously exist, specifically the ability of quantum computers to break popular public key encryption algorithms such as Rivest–Shamir–Adleman (RSA) and elliptic curve cryptography (ECC). Modern cryptography relies on these algorithms, and the impact on areas such as banking, finance, and digital signatures could be catastrophic. Preparing for a post-quantum world is not a matter of applying a patch or upgrade; instead, it requires a comprehensive approach that encompasses both architectural and procedural changes. This is where the concept of quantum-resilient architecture comes in.

Quantum-resilient architecture requires more than exchanging today’s vulnerable encryption for tomorrow’s post-quantum cryptographic (PQC) algorithms. A broader blueprint must be followed to design systems that are agile, modular, and adaptable to evolving quantum threats. This means building infrastructures that can adapt to cryptographic schemes without requiring the overhaul of entire systems.

This shift toward resilience must be embedded at the enterprise architecture level and not simply bolted on after the fact. Just as the rise of cloud computing required rethinking of traditional cybersecurity controls, the quantum era demands a new design paradigm. A quantum-resilient architecture will anticipate the cryptographic disruptions that quantum computing poses and proactively secure critical assets..

## Foundations of a Quantum-Resilient Architecture

Many organizations overemphasize the need to upgrade their cryptographic algorithms when preparing for a post-quantum world. While essential, this is only one action of many that must be taken. A truly quantum-resilient architecture goes beyond the replacement of cryptographic algorithms and creates resilience across multiple domains:

1. Cryptographic agility
2. Layered and modular design
3. Long-term data protection awareness
4. Identity and authentication modernization
5. Governance and life cycle management
The quantum threat not only has the potential to compromise sensitive information but also targets identity systems that form the foundation of digital trust.

**Cryptographic Agility**  
Cryptographic agility [<sup>2</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/?utm_source=sfmc&utm_medium=email&utm_campaign=general-comms&utm_term=mem_journal_oc_awar_promo_mem-only_november-2025&utm_source=sfmc&utm_content=468420&utm_id=60cd59b0-c7ba-475e-b83b-e946a2db5dcd&sfmc_activityid=ec421849-bc90-4ea6-9205-44fd195fbe86&utm_medium=email#2) (crypto-agility) is the foundation of quantum resilience. It refers to an organization’s ability to rapidly switch between cryptographic algorithms without significant system redesign and overhead. Many modern systems have had cryptographic choices hardcoded deep within their application logic, with organizations assuming they will not require change or replacement for the foreseeable future. This creates massive risk. When that cryptographic algorithm is broken, the entire system may need to be reengineered.

Quantum-resilient architectures address this risk through crypto-agility that mandates:

- Taking inventory of existing cryptographic usage to understand risk exposure
- Abstracting cryptographic logic through standardized libraries or application programming interfaces (APIs)
- Using hybrid cryptographic methods (combining classical and post-quantum algorithms during migration)

This agility ensures that post-quantum algorithms, such as those recently standardized by the US National Institute of Standards and Technology (NIST),[<sup>3</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/?utm_source=sfmc&utm_medium=email&utm_campaign=general-comms&utm_term=mem_journal_oc_awar_promo_mem-only_november-2025&utm_source=sfmc&utm_content=468420&utm_id=60cd59b0-c7ba-475e-b83b-e946a2db5dcd&sfmc_activityid=ec421849-bc90-4ea6-9205-44fd195fbe86&utm_medium=email#3) can be adopted quickly without significant disruption.

![Figure 1 - Tenets of Quantum-Resilient Architecture](https://www.isaca.org/-/media/images/isacadp/project/isaca/articles/journal/2025/volume-6/future-proofing-1.png?h=305&w=450&hash=3CD5531542C02B8A2C6E91006BDB8471)

Organizations that build in visibility, accountability, and adaptability today will be far better positioned to respond when quantum capabilities become mainstream.

**Layered and Modular Design**  
A quantum-resilient system is layered: Multiple controls protect each component and each layer is loosely coupled so that changes in one layer do not break any of the others.

In a quantum-resilient architecture, this involves:

- Separating identity, data, and cryptography layers to isolate and manage each threat independently
- Applying quantum-safe encryption at the data layer while preparing for quantum-safe authentication at the identity layer
- Segmenting high-value assets and applying tailored controls, especially for data with long-term secrecy requirements (e.g., legal contracts, medical records, intellectual property)

This layered approach enables organizations to incrementally upgrade components and apply targeted investments where risk is highest, rather than waiting for a full-system replacement.

**Long-Term Data Protection Awareness**  
One of the most immediate quantum risk factors is the concept of harvest now, decrypt later (HNDL),[<sup>4</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/?utm_source=sfmc&utm_medium=email&utm_campaign=general-comms&utm_term=mem_journal_oc_awar_promo_mem-only_november-2025&utm_source=sfmc&utm_content=468420&utm_id=60cd59b0-c7ba-475e-b83b-e946a2db5dcd&sfmc_activityid=ec421849-bc90-4ea6-9205-44fd195fbe86&utm_medium=email#4) in which malicious parties intercept encrypted traffic and store it to decrypt it in the future (when quantum capabilities mature). This is especially hazardous for data that requires confidentiality over a long period.

Quantum-resilient architectures incorporate:

- Data classification frameworks to identify long-lived sensitive data
- Post-quantum encryption or hybrid cryptography for high-value assets
- Data life cycle policies that account for evolving cryptographic standards

Consider a hypothetical example. In 2025, a major hospital transmits sensitive genomic and patient data over Transport Layer Security (TLS) 1.2 to an external research partner for long-term storage and analysis. Unbeknownst to the hospital, a nation-state adversary intercepts and archives this encrypted traffic, anticipating advances in quantum decryption.

In 2030, with access to a cryptographically relevant quantum computer, the adversary successfully decrypts the archived session. As a result, protected health information (PHI) is exposed, triggering US Health Insurance Portability and Accountability Act (HIPAA) violations,[<sup>5</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/?utm_source=sfmc&utm_medium=email&utm_campaign=general-comms&utm_term=mem_journal_oc_awar_promo_mem-only_november-2025&utm_source=sfmc&utm_content=468420&utm_id=60cd59b0-c7ba-475e-b83b-e946a2db5dcd&sfmc_activityid=ec421849-bc90-4ea6-9205-44fd195fbe86&utm_medium=email#5) regulatory fines, patient lawsuits, and erosion of public trust.

**Identity and Authentication Modernization**  
The quantum threat not only has the potential to compromise sensitive information but also targets identity systems that form the foundation of digital trust. Public key cryptography underpins most modern authentication systems, including public key infrastructure (PKI), digital certificates, federated single sign-on (SSO), and OAuth-based access control. A sufficiently advanced quantum computer could compromise these systems by breaking the mathematical problems (e.g., RSA, ECC) that guarantee their security.

A quantum-resilient architecture prepares for this by:

- Decoupling identity logic, enabling flexible updates
- Planning for post-quantum certificate support and revocation mechanisms
- Engaging with identity providers and federated partners to ensure alignment with PQC standards

This ensures that authentication, one of the most exploited attack surfaces, remains reliable even in a post-quantum future.

Consider Google’s Quantum-Safe Digital Signatures in its Cloud Key Management Service (KMS) as an example.[<sup>6</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/?utm_source=sfmc&utm_medium=email&utm_campaign=general-comms&utm_term=mem_journal_oc_awar_promo_mem-only_november-2025&utm_source=sfmc&utm_content=468420&utm_id=60cd59b0-c7ba-475e-b83b-e946a2db5dcd&sfmc_activityid=ec421849-bc90-4ea6-9205-44fd195fbe86&utm_medium=email#6) Google Cloud recently introduced quantum-safe digital signature support in its Cloud KMS, aligning with NIST’s post-quantum cryptography standards, FIPS 204 and FIPS 205.[<sup>7</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/?utm_source=sfmc&utm_medium=email&utm_campaign=general-comms&utm_term=mem_journal_oc_awar_promo_mem-only_november-2025&utm_source=sfmc&utm_content=468420&utm_id=60cd59b0-c7ba-475e-b83b-e946a2db5dcd&sfmc_activityid=ec421849-bc90-4ea6-9205-44fd195fbe86&utm_medium=email#7) Enterprises can now cryptographically sign and verify data using post-quantum algorithms, enabling early integration into security workflows without waiting for full ecosystem adoption. For organizations looking to pilot quantum-safe authentication, Google's rollout provides a clear model, demonstrating that digital signatures are just as critical as encryption in the quantum migration journey.

**Governance and Life Cycle Management**  
Quantum-resilient architecture recognizes that the paradigm shift towards quantum risk awareness will not occur in a vacuum. It embeds continuous governance and risk ownership via:

- Assigning responsibility for quantum readiness (e.g., a quantum task force)
- Updating enterprise risk management (ERM) and architecture reviews to include quantum threats
- Participating in working groups and industry think tanks to stay current

Resilience is not static and evolves in response to new attacks and controls. Organizations that build in visibility, accountability, and adaptability today will be far better positioned to respond when quantum capabilities become mainstream.

## How to Build a Layered Quantum-Resilient Architecture

Quantum resilience is not achieved by implementing isolated components or simply upgrading encryption standards. Instead, it requires a strategic approach that promotes agility, isolates risk domains, and allows for incremental upgrades. This approach is essential not only for managing quantum risk but also for enabling long-term adaptability and compliance as new cryptographic standards and attack vectors emerge.

A layered, modular architecture is illustrated in **figure 2**. Each layer is architected for flexibility and designed to operate independently, enabling an organization to adapt more quickly and with lower operational risk.

![Figure 2 - Three-Layered Approach to Quantum Resilience](https://www.isaca.org/-/media/images/isacadp/project/isaca/articles/journal/2025/volume-6/future-proofing-2.png?h=422&w=450&hash=2D66311919E7A4A2C218A02AD17DE2AB)

**Cryptographic Layer: Abstraction and Agility**  
This foundational layer handles all core encryption and key exchange operations. A common practice is to hardcode cryptographic algorithms directly into applications, making upgrades complex and risky. To become quantum-resilient, organizations must decouple encryption logic from application code by introducing cryptographic abstraction layers, typically via centralized libraries or key management APIs.  
  
This enables cryptographic agility, allowing for the seamless integration of post-quantum algorithms without requiring a redesign of the entire architecture.

Key practices include:

- Using standardized libraries to abstract cryptographic calls
- Supporting hybrid modes (e.g., TLS with both classical and post-quantum keys)
- Enabling algorithm negotiation and graceful fallback mechanisms

This layer also includes cryptographic life cycle management tools that continuously take inventory of, and monitor usage across, environments.

**Identity and Access Layer: Quantum-Safe Authentication**  
In a layered architecture, the identity and access layer is abstracted from the application layer and can be secured independently. Organizations can begin preparing by:

- Deploying identity providers (IdPs) that support PQC or hybrid authentication
- Upgrading PKI to accommodate new certificate formats and longer key lengths
- Testing post-quantum digital signatures in internal applications and APIs
Quantum resilience is not a one-off activity or technical upgrade. It is a governance requirement that must be embedded into risk architecture and audit programs to be successful.

**Data Protection Layer: Longevity and Localization**  
Data is often the oldest asset in an organization. While passwords can be reset and tokens can be revoked, leaked or decrypted data may have irreversible consequences, especially when targeted with HNDL attacks. The data protection layer focuses on:

- Classifying data by secrecy lifespan (e.g., legal contracts or health records that require protection for 10 years or more)
- Applying PQC or hybrid encryption schemes to long-term archives
- Isolating storage regions based on jurisdictional requirements, addressing both sovereignty and residency concerns
- Using secure enclaves or trusted execution environments (TEEs) to limit access to decrypted data

This layer also integrates with data loss prevention (DLP) systems, backups, and retention policies to ensure that encryption at rest and in transit evolves in line with cryptographic standards.

## Integrating Quantum Risk Into Enterprise Architecture Reviews and Audits

Quantum resilience is not a one-off activity or technical upgrade. It is a governance requirement that must be embedded into risk architecture and audit programs to be successful. This ensures that quantum issues are not treated as isolated cryptographic problems, but rather as sources of risk with operational, regulatory, and reputational implications.

There are several actions organizations can take to incorporate quantum readiness into their architecture review processes and audit practices.

**Enhancing Existing Review Criteria**  
Traditional architecture reviews typically focus on areas such as system performance, scalability, cost optimization, and security, and are based on frameworks such as COBIT <sup>®</sup>, TOGAF, or the Sherwood Applied Business Security Architecture (SABSA).[<sup>8</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/?utm_source=sfmc&utm_medium=email&utm_campaign=general-comms&utm_term=mem_journal_oc_awar_promo_mem-only_november-2025&utm_source=sfmc&utm_content=468420&utm_id=60cd59b0-c7ba-475e-b83b-e946a2db5dcd&sfmc_activityid=ec421849-bc90-4ea6-9205-44fd195fbe86&utm_medium=email#8) To prepare for a post-quantum world, organizations must evolve these reviews by adding quantum risk as a key item.  
  
Enhancements include:

- **Cryptographic inventory mapping** —All review submissions should include a record of cryptographic dependencies, identifying which protocols are in use (e.g., RSA, ECC, the Advanced Encryption Standard \[AES\]) and their potential quantum vulnerabilities.
- **Data sensitivity assessment** —Architecture reviews must classify data by secrecy duration. Data requiring protection for five, 10, or 20 years or more (e.g., medical records, trade secrets) should be flagged for prioritization during PQC transition.
- **Cryptographic agility check** —It is the responsibility of the architects to document how the cryptographic primitives are implemented, even if they are hardcoded, configurable, or abstracted through APIs, and whether hybrid or modular upgrades are feasible.

Including these elements at the architectural review stage avoids costly rework later and ensures that quantum security is built into systems from day one.

**Embed Quantum Risk Into the Internal Audit and GRC Functions**  
Internal audits are crucial to identify whether systems comply with policy, fulfill compliance obligations, and manage risk effectively. As part of their evolving role in cybersecurity and digital trust, audit teams must now assess quantum readiness in alignment with the enterprise's risk appetite.

Key recommended actions include:

- **Update audit checklists** to include cryptographic posture reviews, with a focus on identifying deprecated or quantum-vulnerable algorithms.
- **Test hybrid implementations** where PQC has been piloted, evaluating performance, fallback behavior, and interoperability
- **Review vendor contracts and cloud dependencies** to ensure that quantum-safe options are available, particularly for encryption, key management, and identity services.
- **Evaluate governance readiness**, including whether a quantum task force or steering committee exists and whether risk registers include PQC.
- **Incorporate PQC into third-party risk management** by requiring vendors to disclose cryptographic dependencies and transition plans.

This integration also enables more transparent communication with external auditors, regulators, and partners, demonstrating a mature, forward-looking approach to cybersecurity and resilience.

**Drive Awareness at the Executive Level**  
Enterprise architecture and audit teams must partner with the chief information security officer (CISO), chief information officer (CIO), and risk officers to elevate quantum risk to the boardroom. Presenting PQC migration as a business continuity, regulatory, and digital trust issue rather than a narrow IT problem ensures that the organization can allocate funding, assign ownership, and track progress effectively.

Boards should be briefed on:

- The projected timeline for cryptographically relevant quantum computers
- Potential impact on regulated data and services
- Competitive and reputational benefits of being quantum-ready

## Practical Steps to Begin the Quantum-Resilient Journey

For many organizations, the idea of preparing for quantum computing can feel overwhelming. However, the shift toward quantum-resilient architecture does not require a massive transformation overnight. Like any large-scale change, it begins with small, deliberate steps taken now to avoid disruption later.

There are four practical, phased actions enterprises can take to begin building quantum resilience into their systems, processes, and governance functions, without waiting for the quantum future to become the present reality.

## **Conduct a Cryptographic Inventory**  
The first step toward quantum resilience is identifying where cryptography is used across the organization.  	  
The scope of this exercise should cover encryption algorithms, digital signatures, key exchange protocols, and hash functions.  
  
Key actions to take are:
- **Scanning applications, systems, and third-party services** for cryptographic libraries and dependencies
- **Creating a centralized registry** that maps each cryptographic instance to its algorithm, purpose, and potential vulnerability to quantum attacks
- **Prioritizing business-critical applications and long-term data assets** that will need post-quantum protection sooner

## **Segment and Classify Data**  
Based on the previous step, organizations must assess which types of data are most susceptible to HNDL attacks and thus prioritize their protection.
	  
Recommended actions are to:
- **Classify data based on sensitivity and required confidentiality duration** (e.g., contracts, health records, research and development).
- **Encrypt or re-encrypt long-term data** using hybrid algorithms or crypto-agile approaches.
- **Review data sharing and storage practices,** especially for backups and archived information that may be overlooked in regular audits.

This process should involve both data owners and technical teams to ensure accuracy and accountability.

## Establish a Post-Quantum Steering Committee  
**Quantum resilience is not just a cybersecurity concern. It impacts the legal, compliance, risk, and procurement functions, along with business continuity. Forming a cross-functional committee enables the organization to align priorities, assign accountability, and monitor progress effectively.  
	  
This group should:
- **Set objectives and timelines** for PQC transition aligned with business goals
- **Track NIST and International Organization for Standardization (ISO) developments** to stay aligned with standards as they evolve
- **Engage with vendors and cloud providers** to ensure support for quantum-safe services and infrastructure
In regulated industries (e.g., banking, telecom, healthcare), this committee can also act as a liaison with regulators and auditors

## **Pilot Hybrid Cryptographic Implementations  
**One of the most effective short-term steps to quantum resiliency is testing hybrid cryptography, where classical algorithms, such as RSA or ECC, are paired with post-quantum candidates, such as Kyber or Dilithium,[<sup>9</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/?utm_source=sfmc&utm_medium=email&utm_campaign=general-comms&utm_term=mem_journal_oc_awar_promo_mem-only_november-2025&utm_source=sfmc&utm_content=468420&utm_id=60cd59b0-c7ba-475e-b83b-e946a2db5dcd&sfmc_activityid=ec421849-bc90-4ea6-9205-44fd195fbe86&utm_medium=email#9) released by NIST.  
	  
This step includes:
- **Running pilot projects** on internal applications, especially for TLS, email encryption, or virtual private networks (VPNs)
- **Testing performance and key exchange behavior** to validate efficiency and security
- **Ensuring backward compatibility** so that the systems using new post-quantum algorithms remain interoperable with existing applications and infrastructure
- **Gathering feedback** from developers and security teams to understand usability and integration challenges

To complement these phased actions, a number of readiness metrics can be used to track progress, assign responsibility, and evaluate quantum preparedness across diverse domains (**figure 3**).

**Figure 3 - Key Metrics to Evaluate Quantum Readiness**

| **Metric** | **Description** | **Goal** | **Why It Matters** |
| --- | --- | --- | --- |
| Cryptographic   assets inventoried | Proportion of systems/applications where cryptographic dependencies (algorithms, libraries, key lengths) have been mapped | ≥ 90% | Enables visibility to quantum-vulnerable exposure and prioritization of remediation |
| Cryptographic interfaces   abstracted | Share of systems using standardized cryptography libraries/APIs instead of hardcoded algorithms | ≥ 80% | Enables crypto-agility and simplifies post-quantum transitions |
| Long-lived data segmented and encrypted with PQC/hybrid | Percentage of data with > 5-year confidentiality needs that is protected using PQC or hybrid schemes | ≥ 70% | Prevents HNDL exposure of sensitive assets |
| Number of PQC pilot deployments completed | Number of PQC pilots tested in production or internal systems (e.g., TLS, VPN, email, code signing) | ≥ 3% | Demonstrates operational testing and readiness before mandatory compliance |
| Quantum risk coverage in ERM reviews and audits | Whether quantum threats are explicitly addressed in enterprise risk, audit checklists, and architecture reviews | Yes | Ensures risk ownership, funding, and long-term roadmap accountability |
## Conclusion

Quantum computing is no longer a distant abstraction confined to academic labs. While no one knows the exact date when a cryptographically relevant quantum computer (CRQC) will arrive, organizations must act as though it is inevitable. The cost of inaction could be catastrophic not only in terms of data compromise but also for regulatory noncompliance, reputational harm, and business continuity failure.

CISOs, enterprise architects, and risk officers have a unique opportunity. They can wait for regulatory mandates and cryptographic failures to force action, or they can lead with foresight, framing quantum resilience as a competitive advantage rather than a compliance burden. By conducting a cryptographic inventory, classifying data, establishing a steering committee, and piloting hybrid cryptography, organizations will position themselves to be well on their way to completing their quantum migration journey.
## Endnotes
[<sup>1</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/?utm_source=sfmc&utm_medium=email&utm_campaign=general-comms&utm_term=mem_journal_oc_awar_promo_mem-only_november-2025&utm_source=sfmc&utm_content=468420&utm_id=60cd59b0-c7ba-475e-b83b-e946a2db5dcd&sfmc_activityid=ec421849-bc90-4ea6-9205-44fd195fbe86&utm_medium=email#f1) Schneider, J.; Smalley, I.; “,” IBM, 10 June 2025  
[<sup>2</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/?utm_source=sfmc&utm_medium=email&utm_campaign=general-comms&utm_term=mem_journal_oc_awar_promo_mem-only_november-2025&utm_source=sfmc&utm_content=468420&utm_id=60cd59b0-c7ba-475e-b83b-e946a2db5dcd&sfmc_activityid=ec421849-bc90-4ea6-9205-44fd195fbe86&utm_medium=email#f2)  National Institute of Standards and Technology, “ [Crypto Agility,](https://csrc.nist.gov/projects/crypto-agility "Open in a new tab")” USA  
[<sup>3</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/?utm_source=sfmc&utm_medium=email&utm_campaign=general-comms&utm_term=mem_journal_oc_awar_promo_mem-only_november-2025&utm_source=sfmc&utm_content=468420&utm_id=60cd59b0-c7ba-475e-b83b-e946a2db5dcd&sfmc_activityid=ec421849-bc90-4ea6-9205-44fd195fbe86&utm_medium=email#f3)  National Institute of Standards and Technology (NIST), “ [NIST Releases First Three Finalized Post Quantum Encryption Standards](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards "Open in a new tab"),” USA, 13 August 2024  
[<sup>4</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/?utm_source=sfmc&utm_medium=email&utm_campaign=general-comms&utm_term=mem_journal_oc_awar_promo_mem-only_november-2025&utm_source=sfmc&utm_content=468420&utm_id=60cd59b0-c7ba-475e-b83b-e946a2db5dcd&sfmc_activityid=ec421849-bc90-4ea6-9205-44fd195fbe86&utm_medium=email#f4)  NIST, “ [What Is Post Quantum Cryptography?](https://www.nist.gov/cybersecurity/what-post-quantum-cryptography "Open in a new tab"),” USA  
[<sup>5</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/?utm_source=sfmc&utm_medium=email&utm_campaign=general-comms&utm_term=mem_journal_oc_awar_promo_mem-only_november-2025&utm_source=sfmc&utm_content=468420&utm_id=60cd59b0-c7ba-475e-b83b-e946a2db5dcd&sfmc_activityid=ec421849-bc90-4ea6-9205-44fd195fbe86&utm_medium=email#f5)  US Department of Health and Human Services, “ [The Security Rule](https://www.hhs.gov/hipaa/for-professionals/security/index.html "Open in a new tab"),” USA  
[<sup>6</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/?utm_source=sfmc&utm_medium=email&utm_campaign=general-comms&utm_term=mem_journal_oc_awar_promo_mem-only_november-2025&utm_source=sfmc&utm_content=468420&utm_id=60cd59b0-c7ba-475e-b83b-e946a2db5dcd&sfmc_activityid=ec421849-bc90-4ea6-9205-44fd195fbe86&utm_medium=email#f6)  Choucair, C.; “ [Google Expands Post-Quantum Cryptography Support With Quantum-Safe Digital Signatures](https://thequantuminsider.com/2025/02/24/google-expands-post-quantum-cryptography-support-with-quantum-safe-digital-signatures/ "Open in a new tab"),” Google, 24, February 2025  
[<sup>7</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/?utm_source=sfmc&utm_medium=email&utm_campaign=general-comms&utm_term=mem_journal_oc_awar_promo_mem-only_november-2025&utm_source=sfmc&utm_content=468420&utm_id=60cd59b0-c7ba-475e-b83b-e946a2db5dcd&sfmc_activityid=ec421849-bc90-4ea6-9205-44fd195fbe86&utm_medium=email#f7)  NIST, “ [Module-Lattice-Based Digital Signature Standard](https://csrc.nist.gov/pubs/fips/204/final "Open in a new tab"),” USA, 2024; NIST, “ [Stateless Hash-Based Digital Signature Standard](https://csrc.nist.gov/pubs/fips/205/final "Open in a new tab"),” USA, 2024  
[<sup>8</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/?utm_source=sfmc&utm_medium=email&utm_campaign=general-comms&utm_term=mem_journal_oc_awar_promo_mem-only_november-2025&utm_source=sfmc&utm_content=468420&utm_id=60cd59b0-c7ba-475e-b83b-e946a2db5dcd&sfmc_activityid=ec421849-bc90-4ea6-9205-44fd195fbe86&utm_medium=email#f8) ISACA <sup>®</sup>, [*COBIT <sup>®</sup>*](https://www.isaca.org/cobit "Open in the same tab"), USA, 2018,; The Open Group, [The TOGAF Standard](https://pubs.opengroup.org/architecture/togaf9-doc/arch/ "Open in a new tab"), Version 9.2; SABSA, “ [SABSA Executive Summary](https://sabsa.org/sabsa-executive-summary/ "Open in a new tab") ”  
[<sup>9</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/?utm_source=sfmc&utm_medium=email&utm_campaign=general-comms&utm_term=mem_journal_oc_awar_promo_mem-only_november-2025&utm_source=sfmc&utm_content=468420&utm_id=60cd59b0-c7ba-475e-b83b-e946a2db5dcd&sfmc_activityid=ec421849-bc90-4ea6-9205-44fd195fbe86&utm_medium=email#f9)  Cybersecurity & Information Systems Information Analysis Center (CSIAC), “ [A Quantum Good Authentication Protocol,](https://csiac.dtic.mil/articles/a-quantum-good-authentication-protocol/ "Open in a new tab")” *CSIAC 2025*, vol. 9, iss. 1, 2025

### Pranjal Sharma

Is a senior software engineer with more than 14 years of experience in cloud computing, distributed systems, AI, machine learning (ML), cybersecurity, and zero trust. He has a diverse background in technology development and sales. Sharma has contributed to the Institute of Electrical and Electronics Engineers (IEEE) as an author, publication reviewer, and chair. His expertise spans a wide range of technologies, including advanced network security protocols, scalable cloud solutions, and data privacy frameworks. He is currently focused on implementing zero trust architectures to enhance security in distributed environments and building resilient systems for organizations adapting to modern security challenges. Sharma is also the inventor of a pending patent related to cloud-based security architecture.