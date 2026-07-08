---
title: 2025 Volume 6 The Impact of Quantum Computing on Digital Trust
source: https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/the-impact-of-quantum-computing-on-digital-trust
author:
  - K. Brian Kelley
published: 2025-11-01
created: 2025-11-08
tags:
  - unread
  - source
Related:
  - "[[Reading]]"
  - "[[Physics]]"
  - "[[Quantum Computing]]"
  - "[[Book - Information Theory]]"
description: Source
---
![A networked ball, illustrating quantum computing](https://www.isaca.org/-/media/images/isacadp/project/isaca/journal/2025/volume-6/j25v6_the-impact.png?mw=550&hash=05DBE60B08DFB960380A2C59C4831404)

Quantum computing, when fully realized, will break the cryptographical algorithms that underpin many of the security and identity mechanisms in the digital trust ecosystem. For instance, the encryption around Transport Layer Security (TLS) will be broken by quantum computing. We will have to implement new mechanisms to secure e-commerce, document distribution, and other sensitive communications across networks both public and private.

With the regular reporting of advances in quantum computing, especially around hardware, it is predicted that the break could occur within the next 10 years. The US National Institute of Standards and Technology (NIST) has proposed that the first breaks could occur as early as 2030, while Dr. Michele Mosca, a quantum computing expert, predicts a 50% chance of breaks by 2031.[<sup>1</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/#1) Therefore, the call to action for organizations to prepare for a post-quantum cryptographical world is upon us.

## Public Key Cryptography

To understand how quantum computing will affect digital trust, we need to illustrate how public key cryptography, or the Rivest–Shamir–Adleman (RSA) algorithm, works. At its core there are two significantly large prime numbers multiplied together. There’s more to it, of course, but the algorithm is built around those two prime numbers.[<sup>2</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/#2) Anything that can make factoring a number that is the product of two prime numbers faster threatens the effectiveness of the algorithm. Elliptic curve cryptography (ECC) also relies on primes, though not directly.[<sup>3</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/#3) So anything that helps determine the primes in use threatens that type of cryptography as well.

As an example, consider two prime numbers, two and three. Their product is six; most 10-year-olds can factor that easily. But what if the product is 247? That’s a bit more challenging, being the product of 13 and 19. Factoring manually, especially if we know it’s the product of primes, isn’t that bad, as the worst-case scenario is solving six division problems (divide by two, three, five, seven, 11, and then 13). When we divide 247 by 13, we’ll see that 19 is the other factor. A computer would solve this immediately. However, as the prime numbers get larger, figuring out the prime number factors for a significantly large product becomes computationally impossible—in a reasonable time frame—for classical computing. Quantum computing, however, will shatter this issue, with the break of keys expected to take only minutes.

## Shor’s Algorithm

Why do we forecast that quantum computing will break public key cryptography when classical computing will not? The reason is a quantum algorithm for factoring large numbers, proposed by mathematician Peter Shor.[<sup>4</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/#4) This algorithm operates exponentially faster than any classical algorithms using quantum techniques. Because of this incredible increase in performance, algorithms such as RSA and those that make up ECC will be breakable given enough quantum computing power. The same cannot be said for classical computing. Because of the power and promise of the algorithm, it was named after the mathematician who proposed it, and is referenced regularly in quantum computing literature.

## Mosca’s Theorem

With the knowledge of how quantum computing will break public key cryptography, a question that typically follows is, “How long do we have?” It is important to note that the timeline for when quantum computing is expected to break traditional encryption algorithms isn’t the only factor. What is also important is how long data is valuable as well as how quickly an organization can convert to a post-quantum cryptography future. Enter Mosca, who proposed the following theorem:[<sup>5</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/#5)

X + Y > Z

Where:

- X = How long does your data need to be secured?
- Y = How long until your organization becomes quantum-secure?
- Z = How long until we develop a quantum computer powerful enough to break encryption?

If X + Y is greater than Z, that means an organization’s data is going to be at risk even if it is encrypted. Why add how long the data needs to be secured with how long until the organization becomes quantum-secure? That’s because of a concern called “harvest now, decrypt later.”

## Harvest Now and Decrypt Later

If current timelines predict that quantum computing will not be a threat to public key cryptography for a decade or more, is there reason for concern? In short, yes. Data has a lifespan of usefulness. Think about the reasons we have data retention standards:to protect ourselves during litigation and to reduce exposure during a data breach.[<sup>6</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/#6) Consider a financial institution that has a proper data retention policy. Once an individual no longer has a business relationship with the institution, a countdown begins until the individual’s data is purged or tokenized. Attributes such as social security numbers are encrypted and public key cryptography is involved somewhere in the encryption chain. So, at present, most of the risk has been mitigated. The data is encrypted at rest and purged or anonymized as soon as it’s no longer needed.

But what if a threat actor were able to steal the data, albeit in encrypted form? If quantum computing weren’t on the horizon, we wouldn’t be worried. Classical computing can’t keep up with our ability to simply make the keys longer. For instance, it’s normal for keys to be 2,048 bits or greater. In fact, Microsoft deprecated key lengths of 1,024 bits in 2024.[<sup>7</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/#7) A key with 2,048 bits corresponds to a number with 600 digits. The best that has been done as of the writing of a 2023 MIT article was a 250-digit number that took 3,000 hours of compute time.[<sup>8</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/#8)

So a threat actor can harvest now and store the encrypted data. But when cracking public key cryptography using quantum computing becomes a reality, there will be a question of whether such data is still valid. Consider that encrypted social security number attribute, along with the name of the person it belongs to and other pertinent information. Does that become unusable after 10 years? For the majority, the data would still be valid. Some of it might be stale, for instance, an address or a last name could have changed. But that encrypted attribute and who it ties to would still be legitimate. Or think about email exchanges where the email stores are encrypted. If public key cryptography is used, then those email stores would be vulnerable.

## Document Signing

Document signing relies on public key cryptography. While NIST has approved three standards for post-quantum cryptography, including two specifically for digital signatures,[<sup>9</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/#9) current digital signatures are based on public key cryptography. As of today, we don’t have an accepted mechanism for validating signed documents once quantum computing renders public key cryptography broken. Obviously, we can no longer trust the digital signature itself on a document, so something else will need to be used for validation. This goes beyond what we traditionally think of as documents, such as legal contracts and the like, because many current security measures around firmware, software, and other technical assets rely on the same type of digital signature mechanisms.[<sup>10</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/#10)

## Post-Quantum Cryptography Planning

There are a lot of unknowns with respect to post-quantum cryptography. We have forecasted dates with probabilities of when a strong enough quantum computer will be built to break public key encryption, but those are forecasts. We have gaps where we rely heavily on public key encryption, e.g., document signing and most encrypted communications over the network. We don’t know what mechanisms will be used to replace the security functions we rely on today. While there are particular post-quantum cryptography algorithms available, which ones will we standardize?

With that said, we can start to prepare for the post-quantum cryptography future. Many large cybersecurity organizations have published transition frameworks to help organizations get started with their migrations. One such example is the US Department of Homeland Security, which published a single-page, 7-step infographic to assist organizations.[<sup>11</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/#11)

Pick a framework, execute on it, and get ahead of Mosca’s theorem. After all, the post-quantum cryptography era will be upon us before we know it.

## Endnotes

[<sup>1</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/#f1) Susnjara, S.; Smalley, I.; “,” IBM, 4 September 2024  
[<sup>2</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/#f2) Pingley, A.; “ [The Math in Public-Key Cryptography Explained in Simple Words](https://medium.com/techanic/the-math-in-public-key-cryptography-in-simple-words-with-examples-e3a18cb4fa85 "Opens in a new tab"),” Medium, 20 May 2023  
[<sup>3</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/#f3) Sullivan, N.; “ [A (Relatively Easy to Understand) Primer on Elliptic Curve Cryptography](https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/ "Opens in a new tab"),” The Cloudflare Blog, 24 October 2013  
[<sup>4</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/#f4) QuEra, “ [Shor’s Algorithm](https://www.quera.com/glossary/shors-algorithm "Opens in a new tab") ”  
[<sup>5</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/#f5) Malinowski, R.; “ [Michele Mosca and the Power of Mosca’s Theorem: How It Helps Us to Grasp the Quantum Threat](https://www.theqrl.org/blog/grasping-the-quantum-threat-with-moscas-theorem/ "Opens in a new tab"),” The Quantum Resistant Ledger, 3 April 2023  
[<sup>6</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/#f6) Brook, C.; “ [What Is a Data Retention Policy? How it Works and Why You Need It](https://www.digitalguardian.com/blog/what-data-retention-policy-how-it-works-why-you-need-it "Opens in a new tab"),” Fortra, 15 July 2024  
[<sup>7</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/#f7) Patterson, N.; “ [TLS Server Authentication: Deprecation of Weak RSA Certificates](https://techcommunity.microsoft.com/blog/windows-itpro-blog/tls-server-authentication-deprecation-of-weak-rsa-certificates/4134028 "Opens in a new tab"),” Windows IT Pro Blog, 9 May 2024  
[<sup>8</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/#f8) Ornes, S.; “ [Inside the Quest for Unbreakable Encryption](https://www.technologyreview.com/2023/10/19/1081389/unbreakable-encryption-quantum-computers-cryptography-math-problems/ "Opens in a new tab"),” *MIT Technology Review*, 19 October 2023  
[<sup>9</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/#f9) National Institute for Standards and Technology, “ [Announcing Approval of Three Federal Information Processing Standards (FIPS) for Post-Quantum Cryptography](https://csrc.nist.gov/News/2024/postquantum-cryptography-fips-approved "Opens in a new tab"),” USA, 13 August 2024  
[<sup>10</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/#f10) Maurice, E.; “Preparing for Post Quantum Cryptography,” Oracle Security Blog, 4 March 2025  
[<sup>11</sup>](https://www.isaca.org/resources/isaca-journal/issues/2025/volume-6/#f11) US Department of Homeland Security, “ [Preparing for Post-Quantum Cryptography](https://www.dhs.gov/publication/preparing-post-quantum-cryptography-infographic "Opens in a new tab"),” USA, 10 April 2025

### K. BRIAN KELLEY | CISA, CDPSE, CSPO, MCSE, SECURITY+

Is an author and columnist focusing primarily on Microsoft SQL Server and Windows security. He currently serves as a data architect and an independent infrastructure/security architect concentrating on Active Directory, SQL Server, and Windows Server. He has served in a myriad of other positions, including senior database administrator, data warehouse architect, web developer, incident response team lead, and project manager. Kelley has spoken at 24 Hours of PASS, IT/Dev Connections, SQLConnections, the TechnoSecurity and Forensics Investigation Conference, the IT GRC Forum, SyntaxCon, and at various SQL Saturdays, Code Camps, and user groups.