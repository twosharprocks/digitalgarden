---
title: Mini Essays
created: 2025-10-31
updated: 2026-06-29
status: reference
draft: false
tags:
  - writing
  - interests
  - mini-essay
Related: 
  - "[[Writing]]"
  - "[[Mini Essays - Ideas]]"
  - "[[Template - Mini Essay]]"
---
---
- To Write - [Mini Essay - Letter to Yourself in 2031]({{< relref "posts/Mini Essay - Letter to Yourself in 2031.md" >}}) - Where do I want to be in 2031?

```dataview
const pages = dv.pages("")
  .where(page =>
    dv.array(page.tags).includes("mini-essay") &&
    page.file.path !== dv.current().file.path
  )
  .sort(page => page.updated, "desc");

dv.paragraph(dv.markdownList(pages.map(page => page.file.link)));
```



