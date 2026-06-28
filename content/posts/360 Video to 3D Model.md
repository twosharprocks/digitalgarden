---
title: 360 Video to 3D Model
created: 2025-10-28
updated: 2026-06-28
status: seed
draft: false
tags:
  - photogrammetry
  - diving
Related:
  - "[[Photogrammetry]]"
---
Reference: https://axel-busch.medium.com/how-to-quickly-create-a-3d-model-from-360-underwater-video-in-1h-or-less-b45b1cf29655

# Quick Notes
- Import & split Video
	- **File -> Import -> Video
- Alignment 
	- **Tools -> Camera Calibration: Spherical**
	- **Workflow -> Align Photos** (Preselection OFF)
- 

# Full Details

[What is the best lighting for underwater 360 video?](https://www.mantis-sub.com/academy/best-lighting-for-underwater-360-video)
Recommended 360 degree camera settings for photogrammetry:
-   Resolution: Highest resolution.
-   Image Quality: Highest quality.
-   White balance: Manual/fixed, not automatic.
-   Exposure: Automatic (generally).
-   max ISO: 200–400 for small sensors, up to 1600 for 1" or larger.
-   RAW Images: Not needed (generally).
-   Sharpening: Off or ‘soft’.
-   Stabilisation: On.
-   Direction lock: On.

Rules of thumb for buying a photogrammetry computer:
- RAM>CPU>GPU
- Desktop PC over a Laptop PC
## How do I create a 3D model from 360 degree video with Metashape?

There are five general steps involved in creating a 3D model through photogrammetry:

1.  **Import your video/photos** — videos will be converted to photos.
2.  **Align photos** — estimate the camera position and orientation at time of capture and match key points across images.
3.  **Build the point cloud** — points in 3D space that represent points on the surface of the model.
4.  **Build the 3D Model** — a triangle mesh model that represents the external surface of the model.
5.  **Create textures** — a texture contains the colour information for every surface area of the model.

## Step 1: Import video or photos
- For Video: **File -> Import -> Video …**
	- Set frame step = 1 photo per second (eg. 24fps = frame step of 24)
- For Photos: **Workflow -> Add Photos…**
After importing save the project by clicking on the menu item **File -> Save.**
## Step 2: Align photos

Tell Metashape our images are spherical panoramas.
1.  Click on the menu item **Tools -> Camera Calibration**
2.  Then then the parameter “Camera type” to “**Spherical**” and press \[OK\].
3.  Now click on the menu item **Workflow -> Align Photos…**

Set the following parameters in the Align Photos dialog:
**General:**
- Accuracy: High
- Generic preselection: On **(OR TURN THIS *OFF* FOR LONG-SLOW-HIGH ACCURACY ALIGNMENT)**
- Reference preselection: On **(OR TURN THIS *OFF* FOR LONG-SLOW-HIGH ACCURACY ALIGNMENT)**
- Type: Sequential
**Advanced:**
-   Exclude stationary tie points: On
-   **Press \[OK\]**

Positions of the cameras are displayed as spheres. 
This can be toggled with: **Model -> Show/Hide Items -> Show Cameras**
## Step 3: Build the point cloud
-   **Workflow -> Build Point Cloud…**

Then set the following parameters in the Build Point Cloud dialog:
**General:**
-   Source data: Depth maps
-   Quality: High
**Advanced:**
-   Depth filtering: mild
-   Calculate point colors: On
-   Calculate point confidence: On
-   **Press \[OK\]**

The point cloud can now be edited within the Metashape environment, for example unwanted points can be selected and deleted. The point cloud can also be exported to an external tool for further analysis.
## Step 4: Build the 3D model

Metashape supports three reconstruction methods:
1. Tie-points: Very fast, low-detail model based on tie points. Takes seconds.
2. **Depth-maps**: Slow reconstruction of a high-quality model using the GPU.
3. Point-cloud: Very slow reconstruction of a high-quality model based on the previously reconstructed or imported point cloud.

“Depth-maps” is recommended unless the point cloud was edited prior to model reconstruction.
To start the reconstruction: **Workflow -> Build Model…**

Set the following parameters in the Build Model dialog:
**General:**
-   Source data: Depth maps
-   Surface type: Arbitrary (3D)
-   Quality: High
-   Face count: High (or a desired number e.g. 1,000,000)
**Advanced:**
-   Interpolation: Enabled (default)
-   Depth filtering: Mild
-   Calculate vertex colors: On
-   Reuse depth maps: On
-   **Press \[OK\]**

To save a new model, leave the parameter “Replace default model” unchecked.

When **interpolation** is used, Metashape will try to fill holes. This is usually desired and the default setting. These extra surfaces can later always be deleted easily if they are unwanted.

Recommend creating at least two models:
1.  One model with **Face count: High**, and then
2.  Second model with **face count below 1,000,000**

The second model is more suitable to use for online sharing or in a game engine - Model now shows the shape of our cave very well, but the walls only show very little colour. 

Models with a lower face count have less details, but you can use the high-resolution model to create a [normal map texture](https://en.wikipedia.org/wiki/Normal_mapping) which can recover that detail very well when viewing. 
## Step 5: Build textures

To build textures: **Workflow -> Build Texture…**
Set the following parameters in the Build Texture dialog to build the **Diffuse map**:
**General:**
-   Texture type: Diffuse map
-   Source data: Images
-   Mapping mode: Generic
-   Blending mode: Mosaic
-   Texture size/count: 8192 x 1
**Advanced**:
-   Enable hole filling: On
-   Enable ghosting filter: On
-   **Press \[OK\]**

**Texture type**
- **"diffuse map"** is standard colour texture. 
- **"normal map"** used to add details without using more polygons (faces). 
	- Normal maps requires a higher polygon model (>1 million) overlaid on a model with <1 million.

**Texture size/count**
Modern devices can easily handle a 8192 texture size. 
For larger models, one 8192 texture is not enough for adequate detail - generate 4196 x 8, which is the same as 8192 x 2.

**Creating the normal map**
The normal map adds detail to the low-polygon model by extracting “bumpiness” information from a higher-detail model.

Set the following parameters in the Build Texture dialog to build the **Normal map**:
-   Texture type: Normal map
-   Source data: 3D model (highest face count)
-   Mapping mode: Keep uv
-   Blending mode: Mosaic
-   Texture size/count: (same as Diffuse map)
-   **Press \[OK\]**
## Export the model
The most popular format for 3D files is Wavefront .obj files (OBJ). These files include the textures as external jpg files and a material description file (.mtl) that ties the model and textures together.
## What can I do with a 3D model?
The most popular use case after exporting a model from the photogrammetry software is probably to share it online. Popular platforms are [Sketchfab](https://sketchfab.com/) or [Construkted](https://construkted.com/), and I recommend a model size of less than 1M polygons.

Sometimes you might want to edit the model more than what Metashape allows, or just view it on your computer. Popular free 3D viewing/editing softare are [Blender](https://www.blender.org/) and [Meshlab](https://www.meshlab.net/). The most popular commercial packages are [3ds Max](https://www.autodesk.com/products/3ds-max/overview) and [Maya](https://www.autodesk.com/products/maya/overview).

You can also import the model into a game engine like [Unity](https://unity.com/), [Godot](https://godotengine.org/), or [Unreal](https://www.unrealengine.com/en-US) and create a walk-through experience or game.
