---
title: Photogrammetry - Will's Notes
created: 2025-09-11
updated: 2025-11-01
status: reference
draft: false
tags:
  - photogrammetry
  - diving
Related: 
  - "[[360 Video to 3D Model]]"
---
---
Hey, couple of things to make your life easier if you want to process up to the model…

1) when running the create model DON’T colourise vertices… just create the mesh when you do the model. This will give you a model quicker!!

2) Use gradual selection in the tie-points phase (before running the model)… it ‘cleans’ the points that are too far off… play a little bit with the settings, but the combination: 0.5 / 20 / 10 should work. Skip the number of photos as with the 360, it might be too harsh!!!

3) Use gradual selection on the model (mesh) as well… it will clean the shit that is floating inside the cave… also use the size of ‘whatever’ to clean the edges… fill holes and smooth the holes 😜 (all this in tools).

And after you are happy with the model, texturise it!!! I select 40 textures (on average). This way your model is ‘light’ and the textures are not ‘physically’ glued to them 😜

---
*Can you give me a quick written breakdown on how to break the alignment and reset it again?*

- First, duplicate the chunk ![😉](https://static.xx.fbcdn.net/images/emoji.php/v9/t57/1/16/1f609.png) 
- On the new chunk, use the selection tool (manual) to grab all the points of the component you want to reset. 
- Once all tie point are pink (selected) right click and you go for **filter photos by tie points**. 
- You will need to have the photos window open (view menu). On the photos window, select only the aligned photos. 
- Once all marked right click, and select reset alignment. This will reset the alignment of the chunk you want to re-align. 

- Go to the chunk you want the photos to be aligned on (double click). 
- Use the photo window to select the same photos you just reset on the previous chunk, and this time when you right click, you will look for align photos… 

Repeat ![😉](https://static.xx.fbcdn.net/images/emoji.php/v9/t57/1/16/1f609.png)
