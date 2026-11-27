"""Build a search allowlist from fixed prepared public copies and rendered HTML."""
import argparse
import csv
import hashlib
import html
import io
import json
import pathlib
import re
import subprocess
import urllib.parse
import yaml

ROOT = pathlib.Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--rendered", type=pathlib.Path, required=True, help="Fresh Hugo HTML prebuild directory")
parser.add_argument("--prepared", type=pathlib.Path, default=pathlib.Path.home() / "Documents" / "Codex" / "Website Publication" / "effective-sources")
parser.add_argument("--manifest", type=pathlib.Path, default=pathlib.Path.home() / "Documents" / "Codex" / "Website Publication" / "source-manifest.json")
parser.add_argument("--report", type=pathlib.Path, default=pathlib.Path.home() / "Documents" / "Codex" / "Website Publication" / "search-eligibility-latest.json")
args = parser.parse_args()
SITE = ROOT
PREPARED = args.prepared.resolve()
MANIFEST = args.manifest.resolve()
RENDERED = args.rendered.resolve()
REPORT = args.report.resolve()
HOST = "https://digitalgarden.joshrichards.com.au"
HELD = {
    "trip - murra el elevyn - 2025 oct.md",
    "trip - sulawesi - 2025 aug.md",
    "oscp - cheat sheet - linux.md",
    "antarctica.md",
}
HOLD_TERMS = ("murra el elevyn", "murra-el-elevyn", "sulawesi", "oscp - cheat sheet - linux", "antarctica")

def frontmatter(path):
    raw = path.read_text(encoding="utf-8-sig")
    if not raw.startswith("---"):
        raise ValueError("missing YAML front matter")
    value = yaml.safe_load(raw.split("---", 2)[1]) or {}
    if not isinstance(value, dict):
        raise ValueError("invalid YAML front matter")
    return value

def clean_text(value):
    return " ".join(html.unescape(re.sub(r"<[^>]+>", "", value)).split())

def displayed_metadata(path):
    raw = path.read_text(encoding="utf-8")
    heading = re.search(r'<h1 class="post-title">(.*?)</h1>', raw, re.S)
    if not heading:
        raise ValueError("public post heading missing")
    anchors = re.findall(r'<a href="([^"]+)">(.*?)</a>', heading[1], re.S)
    if len(anchors) != 1:
        raise ValueError("public post heading link ambiguous")
    link, title_markup = anchors[0]
    title = clean_text(title_markup)
    tag_block = re.search(r'<span class="post-frontmatter__label">Tags:</span>\s*<span class="post-frontmatter__value post-frontmatter__links">(.*?)</span>', raw, re.S)
    tags = [clean_text(markup).removeprefix("#") for _, markup in re.findall(r'<a href="([^"]+)">(.*?)</a>', tag_block[1], re.S)] if tag_block else []
    return link, title, tags

manifest = json.loads(MANIFEST.read_text(encoding="utf-8-sig"))
prepared_files = sorted(PREPARED.glob("*.md"))
if set(manifest) != {path.name for path in prepared_files}:
    raise ValueError("Prepared public copy set differs from source manifest")
for path in prepared_files:
    if manifest[path.name] != hashlib.sha256(path.read_bytes()).hexdigest():
        raise ValueError("Prepared public copy differs from source manifest: " + path.name)
listing = subprocess.check_output(["hugo", "list", "all", "--source", str(SITE), "--noBuildLock"], text=True, encoding="utf-8")
rows = list(csv.DictReader(io.StringIO(listing)))
post_rows = {pathlib.PurePosixPath(row["path"].replace("\\", "/")).name.casefold(): row for row in rows if row["kind"] == "page" and row["section"] == "posts"}
approvals = {}
decisions = []
for prepared in prepared_files:
    name = prepared.name
    reason = None
    record = None
    try:
        digest = hashlib.sha256(prepared.read_bytes()).hexdigest()
        if manifest.get(name) != digest:
            raise ValueError("prepared copy differs from approved source manifest")
        source_meta = frontmatter(prepared)
        staged = SITE / "content" / "posts" / name
        if not staged.is_file():
            raise ValueError("staged Hugo post missing")
        staged_meta = frontmatter(staged)
        if source_meta.get("title") != staged_meta.get("title") or (source_meta.get("tags") or []) != (staged_meta.get("tags") or []):
            raise ValueError("prepared and staged public metadata differ")
        row = post_rows.get(name.casefold())
        if source_meta.get("draft") or source_meta.get("private") or str(source_meta.get("status", "")).casefold() in ("draft", "private"):
            reason = "draft_or_private"
        elif name.casefold() in HELD:
            reason = "held_entry"
        else:
            if not row:
                raise ValueError("Hugo post listing missing")
            if row["draft"].casefold() == "true":
                raise ValueError("Hugo marks page as draft")
            relative_url = urllib.parse.urlparse(row["permalink"]).path
            rendered = RENDERED / urllib.parse.unquote(relative_url).strip("/") / "index.html"
            if not rendered.is_file():
                raise ValueError("rendered public page missing")
            displayed_link, displayed_title, displayed_tags = displayed_metadata(rendered)
            if displayed_link != relative_url or not displayed_title:
                raise ValueError("rendered public title or URL ambiguous")
            metadata_text = json.dumps({"name": name, "title": displayed_title, "url": relative_url, "tags": displayed_tags}, ensure_ascii=False).casefold()
            if "christmas island" in metadata_text or "christmas-island" in metadata_text:
                reason = "christmas_island_hold"
            elif "byaduk" in metadata_text:
                reason = "byaduk_hold"
            elif any(term in metadata_text for term in HOLD_TERMS):
                reason = "related_hold_metadata"
            else:
                source_tags = source_meta.get("tags") or []
                if not isinstance(source_tags, list) or not all(isinstance(t, str) for t in source_tags):
                    verified_tags = []
                    tag_note = "tags_unverified"
                elif displayed_tags == source_tags:
                    verified_tags = displayed_tags
                    tag_note = None
                else:
                    verified_tags = []
                    tag_note = "tags_unverified"
                record = {"approved": True, "source_title": source_meta["title"], "hugo_title": row["title"], "title": displayed_title,
                          "path": relative_url, "url": HOST + relative_url, "tags": verified_tags}
                key = ("posts/" + name).lower()
                if key in approvals:
                    raise ValueError("case-insensitive source path collision")
                approvals[key] = record
                reason = "eligible" if not tag_note else "eligible_tags_omitted"
    except Exception as exc:
        reason = "ambiguous_" + str(exc)
    decisions.append({"source": name, "reason": reason, "title": record["title"] if record else None,
                      "url": record["url"] if record else None, "tags": record["tags"] if record else None})

output = SITE / "data" / "search_approvals.json"
output.write_text(json.dumps(approvals, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
REPORT.parent.mkdir(parents=True, exist_ok=True)
REPORT.write_text(json.dumps(decisions, indent=2, ensure_ascii=False), encoding="utf-8")
from collections import Counter
counts = Counter(row["reason"] for row in decisions)
print(json.dumps({"prepared_count": len(decisions), "allowlist_count": len(approvals), "reasons": dict(counts)}, indent=2))
