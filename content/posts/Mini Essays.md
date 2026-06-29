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
```dataviewjs
const pages = dv.pages("")
  .where(page =>
    dv.array(page.tags).includes("mini-essay") &&
    page.file.path !== dv.current().file.path
  )
  .sort(page => page.updated, "desc");

const list = dv.container.createEl("ul");
list.style.listStyle = "none";

for (const page of pages) {
  const item = list.createEl("li");
  item.createSpan({ cls: "list-bullet" });
  item.createEl("a", {
    text: page.file.name,
    cls: "internal-link",
    attr: {
      "data-href": page.file.path,
      href: page.file.path
    }
  });
}
```

