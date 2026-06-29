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
- To Write - [Mini Essay - Letter to Yourself in 5 Years]({{< relref "posts/Mini Essay - Letter to Yourself in 5 Years.md" >}}) - Where do I want to be in 2031?

```dataviewjs
const pages = dv.pages("")
  .where(page =>
    dv.array(page.tags).includes("mini-essay") &&
    page.file.path !== dv.current().file.path
  )
  .sort(page => page.updated, "desc");

const list = dv.container.createEl("ul");
list.setAttribute(
  "style",
  "font-size: var(--font-text-size) !important; line-height: 1.6 !important; padding-inline-start: 2em !important; margin-block: 1em !important;"
);

for (const page of pages) {
  const item = list.createEl("li");
  item.setAttribute("style", "margin-block: 0.35em !important;");
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


