---
title: Script - Python - search-replace
created: 2026-03-25
updated: 2026-03-24
status: seed
draft: false
tags:
  - Script
---
Related: [Scripts](/posts/scripts/) [Cyber Security](/posts/cyber-security/)

``` python
#!/usr/bin/env python3

from pathlib import Path

import argparse

import re

  

def slugify(text: str) -> str:

Â  Â  """Replace spaces with dashes and strip leading/trailing spaces."""

Â  Â  return text.strip().replace(" ", "-")

  

def process_file(path: Path, pattern: re.Pattern, repl_func, dry_run: bool) -> int:

Â  Â  """

Â  Â  Returns number of replacements made in this file.

Â  Â  """

Â  Â  text = path.read_text(encoding="utf-8")

Â  Â  updated, n = pattern.subn(repl_func, text)

Â  Â  if n > 0 and not dry_run:

Â  Â  Â  Â  path.write_text(updated, encoding="utf-8", newline="\n")

Â  Â  return n

  

def main():

Â  Â  ap = argparse.ArgumentParser(

Â  Â  Â  Â  description="Replace [[text]] with #text (spaces become dashes) in markdown files."

Â  Â  )

Â  Â  ap.add_argument("text", help="Search term inside [[...]] to replace (e.g., 'Bucket List').")

Â  Â  ap.add_argument("--root", default=".", help="Root folder to scan (default: current directory).")

Â  Â  ap.add_argument("--recursive", action="store_true", help="Recurse into subfolders.")

Â  Â  ap.add_argument("--dry-run", action="store_true", help="Show what would change, but don't write files.")

Â  Â  ap.add_argument("--ignore-case", action="store_true", help="Match [[text]] case-insensitively.")

Â  Â  args = ap.parse_args()

  

Â  Â  root = Path(args.root).resolve()

Â  Â  pattern_glob = "**/*.md" if args.recursive else "*.md"

  

Â  Â  # Build regex that matches [[<text>]], allowing for internal spaces

Â  Â  flags = re.IGNORECASE if args.ignore_case else 0

Â  Â  escaped = re.escape(args.text)

Â  Â  needle = r"\[\[\s*" + escaped.replace(r"\ ", r"\s+") + r"\s*\]\]"

Â  Â  pattern = re.compile(needle, flags=flags)

  

Â  Â  # Replacement function (keeps proper slug formatting)

Â  Â  def repl_func(match):

Â  Â  Â  Â  return "#" + slugify(args.text)

  

Â  Â  files = sorted(root.glob(pattern_glob))

Â  Â  total_files = 0

Â  Â  changed_files = 0

Â  Â  total_replacements = 0

  

Â  Â  for f in files:

Â  Â  Â  Â  if not f.is_file():

Â  Â  Â  Â  Â  Â  continue

Â  Â  Â  Â  total_files += 1

Â  Â  Â  Â  n = process_file(f, pattern=pattern, repl_func=repl_func, dry_run=args.dry_run)

Â  Â  Â  Â  total_replacements += n

Â  Â  Â  Â  if n > 0:

Â  Â  Â  Â  Â  Â  changed_files += 1

Â  Â  Â  Â  Â  Â  print(f"[UPDATED{'' if not args.dry_run else ' (dry)'}] {f.name} (+{n})")

Â  Â  Â  Â  else:

Â  Â  Â  Â  Â  Â  print(f"[SKIPPED] {f.name}")

  

Â  Â  print(f"\nDone. Files scanned: {total_files}. Files changed: {changed_files}. Replacements: {total_replacements}.")

Â  Â  if args.dry_run:

Â  Â  Â  Â  print("No files were written (dry run). Use without --dry-run to apply changes.")

  

if __name__ == "__main__":

Â  Â  main()
```
