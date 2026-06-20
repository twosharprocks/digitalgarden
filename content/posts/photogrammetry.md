---
title: Photogrammetry
created: 2025-08-20
updated: 2025-11-01
status: tree
draft: false
tags:
  - caving
  - diving
  - photogrammetry
Related: 
  - "[[360 Video to 3D Model]]"
  - "[[Photogrammetry - Will's Notes]]"
---
# Ideas
Dedicated PC Photogrammetry Rig to Will 
- Photogrammetry - Rig Setup 
*For a dedicated Windows photogrammetry box:*
- Install NVIDIA Studio Drivers (not Game Ready)
- Disable Windows sleep/hibernation
- Set Power Plan to High Performance
- Exclude project folders from Windows Defender scanning
- Disable automatic reboots for updates
- Put your project cache/scratch on a separate NVMe drive

Other
- Share models on Soggy Wombats Website
# Software
- [Metashape](https://www.agisoft.com/)
	- Buy [Metashape Pro](https://www.agisoft.com/features/professional-edition/)? & run [Metashape Cloud](https://www.agisoft.com/features/cloud/)? 
- [Reality Capture](https://www.capturingreality.com/realitycapture-1-5) 
	- Free it but can't do spherical/360 images
- [Postshot](https://www.jawset.com/)
- [Polycam phone app](https://poly.cam/tools/photogrammetry#get-app-section)
# Data Storage & Processing
- On-Prem: SSD storage in a NAS (see Gear)
	- Citrix to remotely access home server?
- Portable: [Rugged 2Tb HDD - $130](https://www.amazon.com.au/Silicon-Power-SP020TBPHDA80S3K-Shockproof-Waterproof/dp/B075J4YJHS/ref=pd_sbs_d_sccl_2_2/355-9176792-2952911)
- Cloud: AWS with S3 bucket
	- ChatGPT - Remote Photogrammetry with StarLink
	- Use S3 to store final models that display on a website - [Stack Overflow](https://stackoverflow.com/questions/59720658/storing-stl-files-in-s3-bucket-for-rendering-by-stl-viewer-javascript-plugin-in)
	- [Amazon Console - Login](https://ap-southeast-2.console.aws.amazon.com/)
	- ChatGPT - Cloud-Based Photogrammetry]]
	* [Run Photogrammetry in the Cloud - AWS How-To](https://www.instructables.com/Run-Photogrammetry-in-the-Cloud/) <-- ***READ THIS IT'S IMPORTANT***
* Other Cloud: [MaxCloudOn](https://photogrammetry.maxcloudon.com/) is dedicated photogrammetry service with $20 credit
* [belowJS](https://belowjs.com/) - Sharing cave models

# Gear 
- X5 - [Wired - X5 Review](https://www.wired.com/review/insta360-x5-360-camera/) - [X5 replacement lenses ($30)](https://store.insta360.com/product/x5-replacement-lens-kit)
	- Benefit of X5 having user replaceable lens - scratches from dry caving
	- Dive Case Polish? [Autosol 75ml Acrylic Polish](https://www.bunnings.com.au/autosol-75ml-acrylic-polish_p4461011) ***TESTED - POOR RESULTS***
- Lighting
	- Third [BigBlue VL18000PBRC](https://adreno.com.au/products/big-blue-vl18000pbrc-led-video-light-w-optional-remote-control)? $1500AUD (Adreno)
	- BigBlue [Remote Control](https://bigbluedivelights.com/products/complete-remote-control-kit-for-rc-ready-lights/) - $150US (From BigBlue)
- Geolocation
	- [Insta360 GPS Remote](https://www.aliexpress.com/p/tesla-landing/index.html?scenario=c_ppc_item_bridge&productId=1005008772082697&_immersiveMode=true&withMainCard=true&src=google&aff_platform=true&isdl=y) for $80 from AliExpress
	- Drone - use metadata from photos
- LiDAR
	- [Raven Spatial Scanner](https://store.3dmakerpro.com/pages/raven) - $999USD
		- Don't get RTK - no GPS inside caves, and GPS fix provided by drone)
		- Don't need Max version - use X4/5 for high res textures
# Other Ideas
- Improved photogrammetry rig?
	- 4x GoPros on helmet? Concerns about weight/neck strain
	- Clamp [two Carbon Fibre Floats](https://www.amazon.com.au/LetonPower-Underwater-Ultralight-Buoyancy-Floating/dp/B0CSJRL442/ref=sr_1_18) 
		- 4x triple ball clamps 
		- 4x GoPros at the front
		- 3-4x lights at the back
	- Hose Clamps with foam/rubber between?) 
 - Is there an exploration/business plan here?
	- How do you visit amazing places share the experience?
- Drones are essential for geolocation
	- Pre-program flight/photography path to centre on a cave, then fly around it in a manner that captures the data required for a 3D model?
	- Insta360 Drone with 360 cameras
- [Marcin Stempniewicz](https://www.facebook.com/marcin.stempniewicz) - Maria Concordia Project, [running a course on presenting 3D models](https://www.facebook.com/marcin.cela/videos/1416202782903181/?idorvanity=2263629560406211)
	- [Youtube - Marcin's U3DA Course (Demo)](https://www.youtube.com/watch?v=HelaJQWoQOE&list=PL9C8D_aYLcg_JnztwAs5yPff-WH8YKnmJ)
	- [Underwater photogrammetry Academy](https://www.u3da.pl/)
	- [Do a Domestika course on using Blender](https://www.domestika.org/en/courses/92-introduction-to-3d-design-and-modeling-with-blender)
- Collect Photogrammetry data for a [caving game](https://www.youtube.com/watch?v=r8ZhJy4Uqz8)?
- Upload 360 footage to Google [Street View Studio](https://streetviewstudio.maps.google.com/) 
	- Requires GPS data (upload GPX file)
- Work with ASF to 3D model important caves - become the specialist for photogrammetry here.
	- Important to include radio location - Aren Leishman
		- Place pingers in cave, do photogrammetry scan, then use pinger GPS data to scale the size of the photogrammetry data
		- Place pingers on 1st dive (one at entrance, one at far end), get gps fixes on surface, then do photogrammetry while recovering pingers

---
# References
* [Reddit - Cave Photogrammetry Discussion](https://www.reddit.com/r/photogrammetry/comments/vkq95n/software_advice_for_insideout_cave_mapping/)
* [GitHub - OrbSLAM3](https://github.com/UZ-SLAMLab/ORB_SLAM3)
* [GitHub - RTAB-Map](https://github.com/introlab/rtabmap/wiki) & [Explainer](https://introlab.github.io/rtabmap/)
* [Reddit - Limitations of 360 cameras in photogrammetry](https://www.reddit.com/r/photogrammetry/comments/az68pn/photogrammetry_from_360_photos_proof_of_concept/)
* [Photogrammetry for 3D Mapping of Caves](https://ruuth.xyz/Photogrammetryfor3DMappingofCaves.html) **Comprehensive resource**
	- *Recommend Meshroom* - [Meshroom for Beginners](https://meshroom-manual.readthedocs.io/en/latest/tutorials/sketchfab/sketchfab.html) & [GitHub - Meshroom](https://github.com/alicevision/Meshroom)
* [List of free photogrammetry software](https://3dknowledge.com/free-photogrammetry-software/)
* Liz Rogers - [Standard photography for 3D mapping](https://lizrogersphotography.com/2012/10/3d-mapping-the-pillar-in-tank-cave/) 

Will using 4x GoPros on rig taking a still every 1 second
- [Image Processing From Will ](https://www.agisoft.com/forum/index.php?topic=16091.0&fbclid=IwY2xjawG4w0BleHRuA2FlbQIxMAABHYBoBK5P85QtPilsGUPS4cTEJfS61UlCiViwQFE5qSAQ9qUB9XA9upAyJg_aem_jkZpLIpgOoWSnbrrZ69tVA)
- [Youtube - Extracting 3D Models with Blender & 3x X5 cameras](https://www.youtube.com/watch?v=N15E_0kZ1UM)
	- [360 Extrator for Blender](https://toppinappi.gumroad.com/l/360extractor)
- Processing & Lighting
	* [Photogrammetry with 360deg Camera](https://axel-busch.medium.com/how-to-quickly-create-a-3d-model-from-360-underwater-video-in-1h-or-less-b45b1cf29655)
	* [Best Lighting for 360 camera](https://www.mantis-sub.com/academy/best-lighting-for-underwater-360-video)

