---
title: Script - Python - search-replace
created: 2026-03-25
updated: 2026-07-17
status: seed
draft: false
tags:
  - script
related: 
  - "[[Scripts]]"
  - "[[Cyber Security]]"
language: Python
---
``` python
#!/usr/bin/env python3

from pathlib import Path

import argparse

import re

  

def slugify(text: str) -> str:

    """Replace spaces with dashes and strip leading/trailing spaces."""

    return text.strip().replace(" ", "-")

  

def process_file(path: Path, pattern: re.Pattern, repl_func, dry_run: bool) -> int:

    """

    Returns number of replacements made in this file.

    """

    text = path.read_text(encoding="utf-8")

    updated, n = pattern.subn(repl_func, text)

    if n > 0 and not dry_run:

        path.write_text(updated, encoding="utf-8", newline="\n")

    return n

  

def main():

    ap = argparse.ArgumentParser(

        description="Replace [[text]] in markdown files."

    )

    ap.add_argument("text", help="Search term inside [[...]] to replace (e.g., 'Bucket List').")

    ap.add_argument("--root", default=".", help="Root folder to scan (default: current directory).")

    ap.add_argument("--recursive", action="store_true", help="Recurse into subfolders.")

    ap.add_argument("--dry-run", action="store_true", help="Show what would change, but don't write files.")

    ap.add_argument("--ignore-case", action="store_true", help="Match [[text]] case-insensitively.")

    args = ap.parse_args()

  

    root = Path(args.root).resolve()

    pattern_glob = "**/*.md" if args.recursive else "*.md"

  

    # Build regex that matches [[<text>]], allowing for internal spaces

    flags = re.IGNORECASE if args.ignore_case else 0

    escaped = re.escape(args.text)

    needle = r"\[\[\s*" + escaped.replace(r"\ ", r"\s+") + r"\s*\]\]"

    pattern = re.compile(needle, flags=flags)

  

    # Replacement function (keeps proper slug formatting)

    def repl_func(match):

        return "#" + slugify(args.text)

  

    files = sorted(root.glob(pattern_glob))

    total_files = 0

    changed_files = 0

    total_replacements = 0

  

    for f in files:

        if not f.is_file():

            continue

        total_files += 1

        n = process_file(f, pattern=pattern, repl_func=repl_func, dry_run=args.dry_run)

        total_replacements += n

        if n > 0:

            changed_files += 1

            print(f"[UPDATED{'' if not args.dry_run else ' (dry)'}] {f.name} (+{n})")

        else:

            print(f"[SKIPPED] {f.name}")

  

    print(f"\nDone. Files scanned: {total_files}. Files changed: {changed_files}. Replacements: {total_replacements}.")

    if args.dry_run:

        print("No files were written (dry run). Use without --dry-run to apply changes.")

  

if __name__ == "__main__":

    main()
```
