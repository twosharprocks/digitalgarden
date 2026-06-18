---
title: ChatGPT - Cloud-Based Photogrammetry
created: 2025-05-10
updated: 2025-11-01
status: reference
draft: false
tags:
  - Photogrammetry
  - Diving
---
Related: [Photogrammetry](/posts/photogrammetry/) [Diving - Ideas](/posts/diving-ideas/)
Original: https://chatgpt.com/share/681ea27e-93e4-8006-897c-903639b27d57

---
Processing **photogrammetry data in the cloud** is an increasingly practical approach, especially for users with intermittent workloads, tight deadlines, or limited access to high-performance local hardware. Hereâ€™s a breakdown of how it works, the benefits of different cloud providers, relevant **Agisoft Metashape licensing** requirements, and **cost considerations** assuming all processed models are downloaded and stored **locally** after completion.

---
## **Cloud-Based Photogrammetry: Overview**

Photogrammetry workflows (e.g., with **Agisoft Metashape Pro**) are computationally intensive, particularly during:
- **Depth map generation**
- **Dense cloud reconstruction**
- **Mesh generation**
- **Texture mapping**

These stages benefit significantly from **high-end GPUs** and substantial **RAM**, both of which are readily available in cloud environments.

A typical cloud workflow:
1. Upload source images (often large datasets) to cloud storage.
2. Spin up a virtual machine (VM) with powerful CPU/GPU and RAM.
3. Run Agisoft Metashape Pro (via GUI or script).
4. Download final models/results for local storage.
5. Destroy the VM to stop billing.

---
## **Cloud Provider Comparison**

|Provider|Strengths|VM Types for Metashape|Pricing Flexibility|Ideal Use|
|---|---|---|---|---|
|**AWS (Amazon Web Services)**|Most mature, wide global availability|`g5` (GPU), `c7i` (CPU), Spot instances|On-demand, spot, reserved|General users, automation via CLI|
|**Microsoft Azure**|Strong integration with Windows workflows|`NC`, `ND` GPU VMs, `F` and `D` CPU VMs|Pay-as-you-go, reserved|Windows-friendly, good enterprise support|
|**Google Cloud (GCP)**|Fastest startup times, excellent performance for batch jobs|`A2` GPU (NVIDIA A100), `C2` CPU|Per-second billing|Academic, AI-enhanced processing|
|**Paperspace / RunPod / Lambda**|GPU-specialized, lower pricing|A100/RTX 4090|Simple pricing, hourly|Hobbyists or short-term GPU jobs|

> For Agisoft Metashape, **AWS** is the most robust option due to support for CUDA-capable GPUs, large storage capacity, and options like **spot pricing**.

---

## **Agisoft Metashape Licensing in the Cloud**

### **License Options**

- **Standard License** (USD ~$179)
    - No CLI/Python scripting
    - No network processing
    - **Not suitable for cloud-based automation**
- **Professional Node-Locked License** (USD ~$629)
    - Bound to a single cloud VM (not portable between sessions)
    - Can be used on a **dedicated long-running instance**
- **Professional Floating License** (USD ~$1049 + license server)
    - Ideal for cloud: supports ephemeral VMs
    - Can serve multiple users or nodes (1 license per simultaneous use)
    - Can be hosted locally or on a separate cloud server
### **Cloud Licensing Models**

- **Use Case 1**: You host the **floating license server on-premises**, and cloud machines check in via VPN or public IP
- **Use Case 2**: You deploy a **floating license server in the cloud**, on a persistent, low-cost VM (e.g., AWS `t4g.small`)
- **Use Case 3**: Use a **node-locked license**, but this limits flexibilityâ€”ideal only if you reuse the same VM repeatedly
---

## **Workflow Architecture Example (AWS)**

1. **Upload images to AWS S3** (e.g., 50 GB = ~$1/month)
2. **Spin up EC2 GPU instance**, e.g., `g5.4xlarge` (1x NVIDIA A10G, 64 GB RAM)
3. **Attach EBS volume** (fast storage, ~$0.10/GB/month)
4. **Install Metashape Pro**, connect to floating license
5. **Run batch processing using CLI or GUI**
6. **Download results locally** via S3 or SCP
7. **Terminate EC2 instance** to stop billing

---
## **Cost Estimate (AUD) â€“ Example Job**

**Job**: 500 images, 24 MP each, generating dense point cloud, mesh, and texture  
**Instance**: AWS `g5.4xlarge` (~$3.90 AUD/hour on-demand)  
**Storage**: 200 GB EBS + 50 GB S3 = ~$30/month (if retained)  
**Processing Time**: ~8â€“12 hours  
**Total Cost**: ~$50 AUD per job (down to ~$20 with spot pricing)

If you process **weekly**, annual costs would be ~$2500â€“$5000 AUD.

---
## **Benefits of Cloud-Based Processing**

### **Scalability**
- Instantly deploy powerful VMs with GPUs (e.g., NVIDIA A100 or RTX-class)
- Parallel jobs possible across multiple VMs (if licensed appropriately)
### **Flexibility**
- Pay only for what you use (ideal for sporadic workloads)
- Upgrade or downgrade resources as needed per project
### **Avoids Upfront Costs**
- No need for $10,000+ hardware purchases
- Useful for short-term projects, field expeditions, or startups
### **Remote Collaboration**
- Teams can upload data from the field
- Processing can start immediately, even from remote locations

---
## **Considerations**
- **Data Upload Speed**: Uploading large datasets can be slow from rural or limited-bandwidth locations
- **License Management**: Floating licenses are best, but require setup
- **Security**: Sensitive data should be encrypted at rest and in transit
- **Cost Tracking**: Itâ€™s easy to forget to terminate cloud instancesâ€”use automation or billing alerts

---
## **Conclusion**
**Cloud-based photogrammetry** using Metashape Pro with GPU-accelerated instances offers powerful, scalable, and cost-effective processingâ€”especially when:

- You have sporadic or large workloads
- You donâ€™t want to invest heavily in hardware
- You plan to store outputs locally after processing

**AWS** offers the best balance of power, pricing, and flexibility, but Azure and GCP are viable depending on your workflow preferences. For most users, a **[Metashape Professional floating license](https://www.agisoft.com/features/professional-edition/)** is the best choice for cloud deployment.
