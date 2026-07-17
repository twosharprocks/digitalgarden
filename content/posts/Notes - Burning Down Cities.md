---
title: "Notes - Burning Down Cities"
created: 2025-04-26
updated: 2025-10-30
status: seed
draft: false
tags:
  - cyber-security
related: 
  - "[[Cyber Security]]"
  - "[[Threat Actors]]"
  - "[[Threat Modelling]]"
  - "[[OT Cyber Security]]"
  - "[[SecOT+]]"
---
---
*Target System*: IoT/IIoT device C2 via next-gen smart meteres with customer-facing wifi
- Other pathways: Smart inverters & utility scale battery storage

*The Attack* 
Utilise known vulnerability to cause catastrophic failure & fire
- Requires <5% success rate
![Pasted Image 20250426144202](/images/Pasted%20image%2020250426144202.png)
Foreign actors buying up 3rd party generation with direct connection to FEPS
Legacy systems and lack of patching are the issue here

Centralised control is the heart of the attack
- Near future: control system which can communicate to all IoT systems in a house
- Near future: Edge computing on the side of people's houses with direct & unrestricted connection to the internet

Devices
- Smart Ovens: Removed a lot of mechanical safeties to allow overheating
- UPS batteries: Changing firmware to cause thermal runaways
- Water Heaters: 
- Smart Meters: Large capacitors (modify firmware to overload)
- Can also use inverter to cause overloads

Solutions
- Do not need to wifi on the meters (do not need customer wifi or internet connection)
- Issue commands through manufacturer's cloud (Use APIs)
- Platform-agnostic app

Attack Chain
1. Target enrolls IIoT device into meter-based control
2. Compromise meter
3. ID vulnerable IoT devices
4. Issue malicious commands

![Pasted Image 20250426150419](/images/Pasted%20image%2020250426150419.png)


---
**This reminds me of**...

---
# References

