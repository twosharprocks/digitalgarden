import os
import re
import sys
import shutil
from pathlib import Path
from urllib.parse import unquote, quote
from collections import Counter

# --- CONFIG ---
script_dir = Path(__file__).resolve().parent
posts_dir = script_dir / "content" / "posts"
attachments_dir = Path(r"G:\My Drive\Vaults\Digital-Garden\3 - Files")
static_images_dir = script_dir / "static" / "images"

# For relref generation of page links, this is the mount name under /content
CONTENT_MOUNT = "posts"

DRY_RUN = False
OVERWRITE_EXISTING = False  # set True to always copy/overwrite
# ---------------

mode = sys.argv[1].strip().lower() if len(sys.argv) >= 2 else None
if mode == "--images-only":
    if len(sys.argv) >= 3:
        posts_dir = Path(sys.argv[2])
    if len(sys.argv) >= 4:
        attachments_dir = Path(sys.argv[3])
    if len(sys.argv) >= 5:
        static_images_dir = Path(sys.argv[4])

print(f"[INFO] Posts: {posts_dir}")
print(f"[INFO] Attachments: {attachments_dir}")
print(f"[INFO] Static images: {static_images_dir}")

if not posts_dir.exists():
    raise SystemExit(f"[FATAL] Missing posts_dir: {posts_dir}")
if not attachments_dir.exists():
    print(f"[WARN] Missing attachments_dir: {attachments_dir} (image copy may fail)")
static_images_dir.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------------------------
# Helpers for IMAGES
# --------------------------------------------------------------------
# Build a case-insensitive filename index for attachments (recursive)
name_index = {}
if attachments_dir.exists():
    print("[INFO] Indexing attachments...")
    for p in attachments_dir.rglob("*"):
        if p.is_file():
            name_index.setdefault(p.name.lower(), p)

def pretty_alt_from_filename(filename: str) -> str:
    """
    Turn 'pasted image 2024-10-04 12-00-00.png' into 'Pasted image 2024 10 04 12 00 00'
    and 'my_photo-of-thing.jpg' into 'My photo of thing'
    """
    stem = Path(filename).stem
    s = stem.replace("_", " ").replace("-", " ")
    s = re.sub(r"\s+", " ", s).strip()
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
    if attachments_dir.exists() and cand.exists():
        return cand
    base = Path(decoded).name.lower()
    return name_index.get(base)

def copy_image(src: Path, dest_dir: Path):
    dest = dest_dir / src.name
    if DRY_RUN:
        return dest
    if dest.exists() and not OVERWRITE_EXISTING:
        try:
            if dest.stat().st_size == src.stat().st_size:
                return dest
        except Exception:
            pass
        return dest
    dest_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    return dest

# Patterns for images
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

# --------------------------------------------------------------------
# Helpers for WIKILINKS → relref
# --------------------------------------------------------------------
def slugify_anchor(s: str) -> str:
    x = s.strip().lower()
    x = re.sub(r"[^\w\s\-]", "", x)
    x = re.sub(r"\s+", "-", x)
    return x

def norm_key(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip().lower())

def build_page_index(content_dir: Path):
    """Return dict of normalized keys → relative md path under posts_dir."""
    index = {}
    md_files = list(content_dir.rglob("*.md"))
    readable_files = []
    for f in md_files:
        rel = f.relative_to(content_dir)
        stem = f.stem
        keys = {norm_key(stem), norm_key(stem.replace("-", " "))}

        # Very light front matter parse
        try:
            txt = f.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            txt = f.read_text(encoding="utf-8-sig")
        except OSError as exc:
            print(f"[WARN] Skipping unreadable Markdown file {f.name}: {exc}")
            continue
        readable_files.append(f)

        m = re.match(r"^---\s*\n(.*?)\n---\s*\n", txt, flags=re.S)
        if m:
            fm = m.group(1)
            mt = re.search(r"(?mi)^\s*title\s*:\s*(.+?)\s*$", fm)
            if mt:
                t = mt.group(1).strip().strip('"').strip("'")
                if t:
                    keys.add(norm_key(t))
            # aliases can be inline list or block list; grab simple cases
            inline_aliases = re.search(r"(?mi)^\s*aliases\s*:\s*(\[.*\])\s*$", fm)
            if inline_aliases:
                raw = inline_aliases.group(1)
                for a in re.findall(r"'([^']+)'|\"([^\"]+)\"|([^\s,\[\]]+)", raw):
                    ali = next((x for x in a if x), None)
                    if ali: keys.add(norm_key(ali))
            block_aliases = re.search(
                r"(?ms)^\s*aliases\s*:\s*\n((?:\s*-\s*.+\n?)*)",
                fm,
            )
            if block_aliases:
                for a in re.findall(r"(?m)^\s*-\s*(.+?)\s*$", block_aliases.group(1)):
                    val = a.strip().strip('"').strip("'")
                    if val:
                        keys.add(norm_key(val))

        for k in keys:
            index.setdefault(k, rel)
    return index, readable_files

# Match page wikilinks: [[Target]], [[Target|Alias]], [[Target#Section]], [[Target|Alias#Section]]
WIKILINK_RE = re.compile(r"\[\[([^\]\|\#]+)(?:#([^\]\|]+))?(?:\|([^\]]+))?\]\]")

def replace_wikilinks_outside_code(text: str, index: dict, md_files: list, content_mount: str, content_dir: Path):
    fence_pat = re.compile(r"^\s*```")
    out_lines = []
    fenced = False
    front_matter = False
    first_line = True

    def resolve_target(target: str):
        key = norm_key(target.replace("-", " "))
        rel = index.get(key)
        if rel:
            return rel
        # best-effort filename guess
        guess = Path(target.strip().replace(" ", "-") + ".md")
        candidates = [p for p in md_files if p.name.lower() == guess.name.lower()]
        return candidates[0].relative_to(content_dir) if candidates else None

    def repl(m: re.Match) -> str:
        target = m.group(1).strip()
        heading = m.group(2).strip() if m.group(2) else None
        alias = m.group(3).strip() if m.group(3) else None

        rel = resolve_target(target)
        text_label = alias or target
        if rel:
            if heading:
                href = f'{{{{< relref "{content_mount}/{rel.as_posix()}#{slugify_anchor(heading)}" >}}}}'
            else:
                href = f'{{{{< relref "{content_mount}/{rel.as_posix()}" >}}}}'
            return f'[{text_label}]({href})'
        else:
            # leave plain text if unresolved
            return text_label

    for line in text.splitlines(keepends=False):
        if first_line:
            first_line = False
            if line.strip().lstrip("\ufeff") == "---":
                front_matter = True
                out_lines.append(line)
                continue
        elif front_matter:
            out_lines.append(line)
            if line.strip() == "---":
                front_matter = False
            continue

        if fence_pat.match(line):
            fenced = not fenced
            out_lines.append(line)
            continue
        if fenced:
            out_lines.append(line)
        else:
            # Avoid touching image-style wikilinks here; those are handled separately
            if "![" in line or line.lstrip().startswith("!"):
                out_lines.append(WIKILINK_RE.sub(lambda m: m.group(0), line))
            else:
                out_lines.append(WIKILINK_RE.sub(repl, line))

    # Preserve trailing newline if it existed
    return "\n".join(out_lines) + ("\n" if text.endswith("\n") else "")

# --------------------------------------------------------------------
# Execution modes
# --------------------------------------------------------------------
# Modes:
#   (no args)          -> run images + wikilinks
#   --images-only      -> run only image processing
#   --wikilinks-only   -> run only wikilinks; allow optional args:
#                         images.py --wikilinks-only <content_dir> <mount>
if mode == "--wikilinks-only":
    # Allow overriding posts_dir & mount via args for PS step 3B
    content_dir = posts_dir
    content_mount = CONTENT_MOUNT
    if len(sys.argv) >= 3:
        content_dir = Path(sys.argv[2])
    if len(sys.argv) >= 4:
        content_mount = sys.argv[3]

    print(f"[INFO] Converting WikiLinks in: {content_dir} (mount='{content_mount}')")
    index, md_files = build_page_index(content_dir)
    changed = 0
    for md in Path(content_dir).rglob("*.md"):
        try:
            raw = md.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            raw = md.read_text(encoding="utf-8-sig")
        new = replace_wikilinks_outside_code(raw, index, md_files, content_mount, content_dir)
        if new != raw:
            if not DRY_RUN:
                md.write_text(new, encoding="utf-8")
            changed += 1
    print(f"[INFO] WikiLinks converted in {changed} files.")
    sys.exit(0)

# Default or --images-only continue below
stats = Counter()
posts_scanned = 0
files_rewritten = 0
missing = []

# Process images for every .md
for md in posts_dir.rglob("*.md"):
    posts_scanned += 1
    try:
        text = md.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        text = md.read_text(encoding="utf-8-sig")
    except OSError as exc:
        print(f"[WARN] Skipping unreadable Markdown file {md.name}: {exc}")
        continue
    original = text

    # Replace wikilink images like ![[pic.jpg]]
    def repl_wiki(m: re.Match) -> str:
        target = m.group(1)
        stats["matched"] += 1
        src = find_source(target) if attachments_dir.exists() else None
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

    # Replace Markdown images like ![alt](pic.jpg)
    def repl_md(m: re.Match) -> str:
        alt_existing = (m.group(1) or "").strip()
        target = m.group(2)
        stats["matched"] += 1
        src = find_source(target) if attachments_dir.exists() else None
        if not src:
            missing.append((md, f"({target})"))
            print(f"[WARN] Missing (markdown) in {md.name}: ({target})")
            return m.group(0)
        dest = copy_image(src, static_images_dir)
        stats["copied"] += 1
        url_name = quote(dest.name)
        alt = alt_existing or pretty_alt_from_filename(dest.name)
        return f"![{alt}](/images/{url_name})"

    text = MD_IMG_RE.sub(repl_md, text)

    # Cleanup: normalize any number of '!' and spaces before '[' to a single '!' (fix stray '!')
    text = re.sub(r"!+\s*(?=\[)", "!", text)

    # Normalize nested links emitted by Obsidian, which Hugo rejects.
    text = re.sub(
        r"\[([^\]]+)\]\(\[(https?://[^\]]+)\]\(\2\)\)",
        r"[\1](\2)",
        text,
    )
    text = re.sub(r"\]\(\*(https?://)", r"](\1", text)
    text = text.replace("http://%20http//", "http://")

    if text != original:
        if not DRY_RUN:
            md.write_text(text, encoding="utf-8")
        files_rewritten += 1

print("\n=== IMAGE SUMMARY ===")
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

# If user asked for images-only, stop here
if mode == "--images-only":
    sys.exit(0)

# Run wikilink conversion as part of a full pass (no args case)
print("\n[INFO] Also converting WikiLinks to Hugo relref...")
index, md_files = build_page_index(posts_dir)
changed = 0
for md in posts_dir.rglob("*.md"):
    try:
        raw = md.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        raw = md.read_text(encoding="utf-8-sig")
    except OSError as exc:
        print(f"[WARN] Skipping unreadable Markdown file {md.name}: {exc}")
        continue
    new = replace_wikilinks_outside_code(raw, index, md_files, CONTENT_MOUNT, posts_dir)
    if new != raw:
        if not DRY_RUN:
            md.write_text(new, encoding="utf-8")
        changed += 1
print(f"[INFO] WikiLinks converted in {changed} files (full pass).")
