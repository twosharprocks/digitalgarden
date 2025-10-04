import os
import re
import shutil
from pathlib import Path
from urllib.parse import unquote, quote
from collections import Counter

# --- CONFIG ---
posts_dir = Path(r"C:\Users\Josh\Documents\garden\content\posts")
attachments_dir = Path(r"C:\Users\Josh\My Drive\Vaults\Digital-Garden\Files")
static_images_dir = Path(r"C:\Users\Josh\Documents\garden\static\images")
DRY_RUN = False
OVERWRITE_EXISTING = False  # set True to always copy/overwrite
# ---------------

print(f"[INFO] Posts: {posts_dir}")
print(f"[INFO] Attachments: {attachments_dir}")
print(f"[INFO] Static images: {static_images_dir}")

if not posts_dir.exists():
    raise SystemExit(f"[FATAL] Missing posts_dir: {posts_dir}")
if not attachments_dir.exists():
    raise SystemExit(f"[FATAL] Missing attachments_dir: {attachments_dir}")
static_images_dir.mkdir(parents=True, exist_ok=True)

# Build a case-insensitive filename index for attachments (recursive)
print("[INFO] Indexing attachments...")
name_index = {}
for p in attachments_dir.rglob("*"):
    if p.is_file():
        name_index.setdefault(p.name.lower(), p)

def pretty_alt_from_filename(filename: str) -> str:
    """
    Turn 'pasted image 2024-10-04 12-00-00.png' into 'Pasted image 2024 10 04 12 00 00'
    and 'my_photo-of-thing.jpg' into 'My photo of thing'
    """
    stem = Path(filename).stem
    # Normalize separators
    s = stem.replace("_", " ").replace("-", " ")
    # Squash extra spaces
    s = re.sub(r"\s+", " ", s).strip()
    # Title-case words with letters; leave all-caps abbreviations/numbers intact
    def smart_cap(w):
        if w.isupper() and len(w) <= 4:  # keep short acronyms (e.g., NASA, PNG)
            return w
        if re.fullmatch(r"\d+", w):      # keep pure numbers as-is
            return w
        return w.capitalize()
    words = [smart_cap(w) for w in s.split(" ")]
    return " ".join(words) or "Image"

def find_source(raw_target: str):
    """Return a Path for the image to copy, handling subpaths and URL-encoded names."""
    decoded = unquote(raw_target.strip())
    cand = attachments_dir / decoded
    if cand.exists():
        return cand
    base = Path(decoded).name.lower()
    return name_index.get(base)

def copy_image(src: Path, dest_dir: Path):
    dest = dest_dir / src.name
    if DRY_RUN:
        return dest
    if dest.exists() and not OVERWRITE_EXISTING:
        # Optional: skip if same size (cheap sanity check)
        try:
            if dest.stat().st_size == src.stat().st_size:
                # print(f"[SKIP] Exists (same size): {dest.name}")
                return dest
        except Exception:
            pass
        # If sizes differ but you still don't want to overwrite, just return
        # To force overwrite, set OVERWRITE_EXISTING=True
        return dest
    # Ensure dir exists then copy
    dest_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    return dest

# Patterns
# 1) Obsidian wikilink images: ![[path/name.ext|optional]] or ! [[path/name.ext]]
WIKI_IMG_RE = re.compile(
    r"(?:!\s*)?\[\[\s*([^|\]]+\.(?:jpe?g|png|gif))\s*(?:\|[^\]]*)?\]\]",
    re.IGNORECASE
)
# 2) Markdown inline images: ![alt](path/name.ext "opt title")
MD_IMG_RE  = re.compile(
    r"!\[([^\]]*)\]\(\s*([^)]+\.(?:jpe?g|png|gif))(?:\s+(?:\"[^\"]*\"|'[^']*'))?\s*\)",
    re.IGNORECASE
)

stats = Counter()
posts_scanned = 0
files_rewritten = 0
missing = []

for md in posts_dir.rglob("*.md"):
    posts_scanned += 1
    text = md.read_text(encoding="utf-8")
    original = text

    # Replace wikilinks
    def repl_wiki(m: re.Match) -> str:
        target = m.group(1)
        stats["matched"] += 1
        src = find_source(target)
        if not src:
            missing.append((md, f"[[{target}]]"))
            print(f"[WARN] Missing (wikilink) in {md.name}: [[{target}]]")
            return m.group(0)
        dest = copy_image(src, static_images_dir)
        stats["copied"] += 1
        url_name = quote(dest.name)
        alt = pretty_alt_from_filename(dest.name)
        return f"![{alt}](/images/{url_name})"

    text = WIKI_IMG_RE.sub(repl_wiki, text)

    # Replace Markdown images
    def repl_md(m: re.Match) -> str:
        alt_existing = (m.group(1) or "").strip()
        target = m.group(2)
        stats["matched"] += 1
        src = find_source(target)
        if not src:
            missing.append((md, f"({target})"))
            print(f"[WARN] Missing (markdown) in {md.name}: ({target})")
            return m.group(0)
        dest = copy_image(src, static_images_dir)
        stats["copied"] += 1
        url_name = quote(dest.name)
        # Keep existing alt if present; otherwise generate from filename
        alt = alt_existing or pretty_alt_from_filename(dest.name)
        return f"![{alt}](/images/{url_name})"

    text = MD_IMG_RE.sub(repl_md, text)

    # Cleanup: normalize any number of '!' and spaces before '[' to a single '!' (fix stray '!')
    text = re.sub(r"!+\s*(?=\[)", "!", text)

    if text != original:
        if not DRY_RUN:
            md.write_text(text, encoding="utf-8")
        files_rewritten += 1

print("\n=== SUMMARY ===")
print(f"Posts scanned:         {posts_scanned}")
print(f"Files rewritten:       {files_rewritten}")
print(f"Image references seen: {stats['matched']}")
print(f"Images copied:         {stats['copied']}")
print(f"Missing:               {len(missing)}")

if missing:
    print("\nExamples of missing (up to 10):")
    for f, t in missing[:10]:
        print(f"  - {f.name}: {t}")

print("\nNotes:")
print("• Set OVERWRITE_EXISTING=True if you want to refresh files in /static/images.")
print("• Alt text now auto-generates from filenames when none is provided.")