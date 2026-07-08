---
title: OSCP
created: 2025-07-05
updated: 2026-07-08
status: seed
draft: false
tags:
  - study
  - oscp
  - cyber-security
Related:
  - "[[Cyber Security]]"
  - "[[OSCP]]"
---
```dataview
const groupOrder = ["General", "Windows", "Linux", "Active Directory", "Other"];

function hasTag(page, tag) {
  return dv.array(page.tags).map(t => String(t).replace(/^#/, "").toLowerCase()).includes(tag);
}

function oscpSystem(page) {
  const name = page.file.name;
  const parts = name
    .replace(/^OSCP\s*-\s*/i, "")
    .split(" - ")
    .map(part => part.replace(/\s*\(DNF\)\s*$/i, "").trim());

  if (/cheat sheet/i.test(name)) return "General";
  if (parts.some(part => /^(ad|active directory)$/i.test(part))) return "Active Directory";
  if (parts.some(part => /^windows$/i.test(part))) return "Windows";
  if (parts.some(part => /^linux$/i.test(part))) return "Linux";
  if (parts.some(part => /^(core|exam prep)$/i.test(part))) return "General";
  return "Other";
}

const pages = dv.pages("")
  .where(page =>
    page.file.path !== dv.current().file.path &&
    (page.file.name.startsWith("OSCP - ") || hasTag(page, "oscp"))
  )
  .sort(page => page.file.name, "asc");

for (const groupName of groupOrder) {
  const groupPages = pages.where(page => oscpSystem(page) === groupName);
  if (!groupPages.length) continue;

  dv.header(2, groupName);

  const list = dv.container.createDiv();
  list.setAttribute(
    "style",
    "padding-inline-start: 1.4em !important; margin-block: var(--p-spacing) !important;"
  );

  for (const page of groupPages) {
    const item = list.createDiv();
    item.setAttribute(
      "style",
      "display: flex !important; align-items: baseline !important; margin: 0 !important; padding: 0 !important; font-size: var(--font-text-size) !important; line-height: var(--line-height-normal) !important;"
    );
    const marker = item.createSpan({ text: "›" });
    marker.setAttribute(
      "style",
      "flex: 0 0 1.2em !important; color: var(--text-accent) !important; font-weight: 800 !important;"
    );
    const link = item.createEl("a", {
      text: page.file.name,
      cls: "internal-link",
      attr: {
        "data-href": page.file.path,
        href: page.file.path
      }
    });
    link.setAttribute(
      "style",
      "font-size: inherit !important; line-height: inherit !important;"
    );
  }
}
```
