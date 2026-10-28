"""Fail closed before exporting vault attachments. Private policy stays outside Git.

This checks file identities and references, not the meaning of prose or old Git history.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import subprocess
import sys
import shutil
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote, parse_qsl

PRIVATE_FOLDER = "Files - PRIVATE"
PRIVATE_SUFFIX = " - PRIVATE"
POLICY_PATH = Path.home() / "Documents/Codex/Attachment Privacy/asset-policy.json"
REPORT_PATH = POLICY_PATH.parent / "latest-publish-check.json"
TEXT_EXTENSIONS = {".md", ".html", ".xml", ".json", ".txt", ".css", ".js"}
ATTACHMENT_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".tif", ".tiff", ".pdf",
    ".kml", ".kmz", ".gpx", ".geojson", ".tml", ".csv", ".xlsx", ".xls", ".doc",
    ".docx", ".zip", ".7z", ".rar", ".mp4", ".mov", ".mp3", ".wav", ".obj", ".ply",
    ".stl", ".las", ".laz", ".heic", ".dxf", ".dwg",
}


class PrivacyError(RuntimeError):
    pass


def decoded(value):
    value = html.unescape(str(value)).replace("\\", "/")
    for _ in range(3):
        new = unquote(value)
        if new == value:
            break
        value = new
    return value


def private_marker(value, depth=0):
    value = decoded(value)
    if "?" in value and depth < 3:
        if any(private_marker(v, depth + 1) for _, v in parse_qsl(value.split("?", 1)[1])):
            return True
    value = value.split("|", 1)[0].split("#", 1)[0].split("?", 1)[0]
    value = value.strip().strip('<>"\'')
    for component in value.split("/"):
        if component.casefold() == PRIVATE_FOLDER.casefold():
            return True
        if Path(component).stem.casefold().endswith(PRIVATE_SUFFIX.casefold()):
            return True
    return False


def external_target(value):
    value = str(value).strip()
    if value.startswith(("#", "//")):
        return True
    # Browser-extension and other remote URL schemes are not local attachments.
    return bool(re.match(r"^[a-z][a-z0-9+.-]*:", value, re.I)) and not bool(re.match(r"^(?:file:|obsidian:|[a-z]:[/\\])", value, re.I))


def private_filename(name):
    path = Path(name)
    if path.stem.casefold().endswith(PRIVATE_SUFFIX.casefold()):
        return name
    return f"{path.stem}{PRIVATE_SUFFIX}{path.suffix}"


def fingerprints(path):
    size = path.stat().st_size
    sha256 = hashlib.sha256()
    git_sha1 = hashlib.sha1(f"blob {size}\0".encode())
    with path.open("rb") as file:
        for block in iter(lambda: file.read(1024 * 1024), b""):
            sha256.update(block)
            git_sha1.update(block)
    return {"sha256": sha256.hexdigest(), "git_blob_sha1": git_sha1.hexdigest(), "bytes": size}


def save_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + f".{os.getpid()}.tmp")
    temporary.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    os.replace(temporary, path)


def link_targets(text):
    # Wiki links (including embeds), inline Markdown, reference definitions, and HTML.
    for match in re.finditer(r"!?\[\[([^\]]+)\]\]", text):
        yield match[1].split("|", 1)[0].strip(), match.group(0).startswith("!")
    for match in re.finditer(r"!?\[(?:\\.|[^\]\\\n])*\]\(\s*(<[^>]+>|(?:\\.|[^\n)])+)\)", text):
        raw = match[1].strip()
        if raw.startswith("<"):
            raw = raw[1:raw.find(">")]
        else:
            raw = re.split(r'\s+["\']', raw, maxsplit=1)[0]
        yield raw.replace("\\ ", " "), match.group(0).startswith("!")
    for match in re.finditer(r"(?m)^\s*\[[^\]]+\]:\s*(<[^>]+>|\S+)", text):
        yield match[1].strip("<>"), False
    for match in re.finditer(r'''(?:src|href|poster)\s*=\s*["']([^"']+)["']''', text, re.I):
        yield match[1], False
    for match in re.finditer(r'''srcset\s*=\s*["']([^"']+)["']''', text, re.I):
        for item in match[1].split(","):
            yield item.strip().split(" ")[0], True


class PrivacyGuard:
    def __init__(self, vault, site, policy=POLICY_PATH):
        self.vault = Path(vault).resolve()
        self.assets = self.vault / "3 - Files"
        self.site = Path(site).resolve()
        self.policy_path = Path(policy).resolve()
        if self.policy_path.is_relative_to(self.site):
            raise PrivacyError("The private attachment register must be outside the public repository.")
        try:
            self.policy = json.loads(self.policy_path.read_text(encoding="utf-8-sig"))
        except (OSError, ValueError) as exc:
            raise PrivacyError("Attachment register is missing or unreadable; publishing is blocked.") from exc
        if self.policy.get("version") != 1:
            raise PrivacyError("Unsupported attachment register version.")
        for key in ("private_sha256", "private_git_blobs", "approved_source_sha256", "approved_output_sha256"):
            values = self.policy.get(key)
            length = 40 if key == "private_git_blobs" else 64
            if not isinstance(values, list) or any(not isinstance(v, str) or not re.fullmatch(f"[0-9a-f]{{{length}}}", v) for v in values):
                raise PrivacyError(f"Invalid attachment register field: {key}")
        self.private_sha = set(self.policy["private_sha256"])
        self.private_git = set(self.policy["private_git_blobs"])
        self.approved_source = set(self.policy["approved_source_sha256"])
        self.approved_output = set(self.policy["approved_output_sha256"])
        self.issues = []
        self._seen = set()
        self._hashes = {}
        self.names = defaultdict(list)
        self.stems = defaultdict(list)
        self.notes = set()
        self.asset_paths = []
        self._index()
        self._derivatives()

    def problem(self, code, path, target=""):
        key = (code, str(path), str(target))
        if key not in self._seen:
            self._seen.add(key)
            self.issues.append({"code": code, "path": str(path), "target": str(target)})

    def hash(self, path):
        path = Path(path).resolve()
        # Per-run cache only; every new publishing invocation reads file contents again.
        if path not in self._hashes:
            self._hashes[path] = fingerprints(path)
        return self._hashes[path]

    def is_private(self, path):
        if private_marker(path):
            return True
        identity = self.hash(path)
        return identity["sha256"] in self.private_sha or identity["git_blob_sha1"] in self.private_git

    def _index(self):
        if not self.assets.is_dir():
            raise PrivacyError("Vault attachment folder is missing.")
        for path in self.assets.rglob("*"):
            if path.is_symlink():
                self.problem("attachment_symlink_requires_review", path)
                continue
            if not path.is_file():
                continue
            if not path.resolve().is_relative_to(self.assets.resolve()):
                self.problem("attachment_outside_root", path)
                continue
            self.asset_paths.append(path)
            self.names[path.name.casefold()].append(path)
            self.stems[path.stem.casefold()].append(path)
            if private_marker(path):
                identity = self.hash(path)
                self.private_sha.add(identity["sha256"])
                self.private_git.add(identity["git_blob_sha1"])
                if PRIVATE_FOLDER.casefold() in [part.casefold() for part in path.parts] and not path.stem.casefold().endswith(PRIVATE_SUFFIX.casefold()):
                    self.problem("private_filename_needs_suffix", path)
        for folder in ("1 - Published", "2 - Unpublished"):
            self.notes.update(p.stem.casefold() for p in (self.vault / folder).rglob("*.md"))

    def _derivatives(self):
        manifest = self.site / ".cache/web-images.json"
        if not manifest.exists():
            return
        try:
            entries = json.loads(manifest.read_text(encoding="utf-8"))["files"]
        except (OSError, ValueError, KeyError) as exc:
            raise PrivacyError("Website image provenance is unreadable; publishing is blocked.") from exc
        for entry in entries.values():
            source_sha = entry.get("source_sha256")
            output_sha = entry.get("output_sha256")
            source = Path(entry.get("source", [""])[0])
            private = source_sha in self.private_sha or private_marker(source)
            if source.is_file() and source.resolve().is_relative_to(self.assets.resolve()):
                identity = self.hash(source)
                private = private or identity["git_blob_sha1"] in self.private_git or identity["sha256"] in self.private_sha
            if private:
                if source_sha:
                    self.private_sha.add(source_sha)
                if output_sha:
                    self.private_sha.add(output_sha)
            elif source_sha in self.approved_source and output_sha:
                self.approved_output.add(output_sha)

    def remember_private_identities(self):
        # Private markings survive later renames and moves out of the protected folder.
        if self.private_sha != set(self.policy["private_sha256"]) or self.private_git != set(self.policy["private_git_blobs"]):
            self.policy["private_sha256"] = sorted(self.private_sha)
            self.policy["private_git_blobs"] = sorted(self.private_git)
            save_json(self.policy_path, self.policy)

    def resolve_attachment(self, raw, embedded=False):
        target = decoded(raw).split("|", 1)[0].split("#", 1)[0].split("?", 1)[0].strip().strip("<>")
        if external_target(target):
            return []
        target_path = Path(target)
        if not embedded and not target_path.suffix and target_path.name.casefold() in self.notes:
            return []
        candidates = []
        for base in (self.vault, self.assets):
            path = base / target.lstrip("/")
            if path.is_file() and path.resolve().is_relative_to(self.assets.resolve()):
                candidates.append(path.resolve())
        if not candidates:
            candidates = self.names.get(target_path.name.casefold(), [])
        if not candidates and not target_path.suffix:
            candidates = self.stems.get(target_path.name.casefold(), [])
        return list(dict.fromkeys(Path(p).resolve() for p in candidates))

    def check_source(self, path):
        path = Path(path)
        if private_marker(path):
            self.problem("private_file_in_published", path)
        if self.is_private(path):
            self.problem("private_content_in_published", path)
        if path.suffix.casefold() != ".md":
            if self.hash(path)["sha256"] not in self.approved_source:
                self.problem("unapproved_non_note_in_published", path)
            return
        text = path.read_text(encoding="utf-8-sig")
        for target, embedded in link_targets(text):
            if private_marker(target):
                self.problem("private_reference", path, target)
                continue
            candidates = self.resolve_attachment(target, embedded)
            if len(candidates) > 1:
                self.problem("ambiguous_attachment_reference", path, target)
            for candidate in candidates:
                if self.is_private(candidate):
                    self.problem("private_attachment_reference", path, str(candidate))
                elif self.hash(candidate)["sha256"] not in self.approved_source:
                    self.problem("unapproved_attachment_reference", path, str(candidate))
            if not candidates and not external_target(target):
                leaf = Path(decoded(target).split("#")[0].split("?")[0])
                if leaf.suffix.casefold() in ATTACHMENT_EXTENSIONS:
                    self.problem("missing_attachment_reference", path, target)

    def require_exportable(self, path):
        path = Path(path).resolve()
        if not path.is_relative_to(self.assets.resolve()):
            raise PrivacyError("Attachment export source is outside 3 - Files.")
        if self.is_private(path):
            raise PrivacyError("Private attachment export blocked. See the local privacy report.")
        if self.hash(path)["sha256"] not in self.approved_source:
            raise PrivacyError("Unapproved attachment export blocked. Review it before publishing.")

    def scan_output_file(self, path):
        path = Path(path)
        if path.is_symlink() or not path.resolve().is_relative_to(self.site):
            self.problem("public_output_symlink_or_escape", path)
            return
        if private_marker(path.relative_to(self.site)):
            self.problem("private_filename_in_public_output", path)
        identity = self.hash(path)
        is_private = identity["sha256"] in self.private_sha or identity["git_blob_sha1"] in self.private_git
        if is_private:
            self.problem("private_bytes_in_public_output", path)
        relative = path.relative_to(self.site).as_posix()
        if not is_private and relative.startswith(("static/", "public/")) and path.suffix.casefold() in ATTACHMENT_EXTENSIONS:
            if identity["sha256"] not in self.approved_source | self.approved_output:
                self.problem("unapproved_public_attachment", path)
        if relative.startswith(("content/", "public/", "static/")) and path.suffix.casefold() in TEXT_EXTENSIONS:
            try:
                text = path.read_text(encoding="utf-8-sig")
            except UnicodeError:
                return
            for target, _ in link_targets(text):
                if private_marker(target):
                    self.problem("private_reference_in_public_output", path, target)

    def check_outgoing(self, base):
        result = subprocess.run(["git", "-C", str(self.site), "rev-list", f"{base}..HEAD"], capture_output=True, text=True)
        if result.returncode:
            raise PrivacyError("Cannot check outgoing Git history against the remote tracking branch.")
        blobs = {}
        for commit in result.stdout.splitlines():
            result = subprocess.run(["git", "-C", str(self.site), "diff-tree", "--root", "-m", "--no-commit-id", "--no-renames", "-r", "--raw", "-z", "--diff-filter=AM", commit], check=True, capture_output=True)
            entries = result.stdout.decode("utf-8").split("\0")
            for i in range(0, len(entries) - 1, 2):
                meta, name = entries[i], entries[i + 1]
                if not meta:
                    continue
                parts = meta.split()
                blob = parts[3]
                if parts[1] == "120000" or private_marker(name) or blob in self.private_git:
                    self.problem("private_or_unsafe_outgoing_commit", name, commit)
                blobs[blob] = name
        if not blobs:
            return
        process = subprocess.Popen(["git", "-C", str(self.site), "cat-file", "--batch"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        try:
            for blob, name in blobs.items():
                process.stdin.write((blob + "\n").encode())
                process.stdin.flush()
                header = process.stdout.readline().decode().strip().split()
                if len(header) != 3 or header[1] != "blob":
                    raise PrivacyError("Cannot inspect an outgoing Git object.")
                remaining = int(header[2])
                digest = hashlib.sha256()
                chunks = []
                inspect_links = Path(name).suffix.casefold() in TEXT_EXTENSIONS and remaining < 10_000_000
                while remaining:
                    block = process.stdout.read(min(remaining, 1024 * 1024))
                    if not block:
                        raise PrivacyError("Incomplete outgoing Git object.")
                    digest.update(block)
                    if inspect_links:
                        chunks.append(block)
                    remaining -= len(block)
                if process.stdout.read(1) != b"\n":
                    raise PrivacyError("Invalid Git object stream.")
                if digest.hexdigest() in self.private_sha:
                    self.problem("private_bytes_in_outgoing_history", name)
                if inspect_links:
                    for target, _ in link_targets(b"".join(chunks).decode("utf-8", errors="replace")):
                        if private_marker(target):
                            self.problem("private_reference_in_outgoing_history", name, target)
        finally:
            process.stdin.close()
            process.stdout.close()
            process.wait()

    def check(self, sources=True, outputs=True, index=False, outgoing=None):
        if sources:
            root = self.vault / "1 - Published"
            if not root.is_dir():
                raise PrivacyError("Published folder is missing.")
            for path in root.rglob("*"):
                if path.is_symlink():
                    self.problem("published_symlink_requires_review", path)
                elif path.is_file():
                    self.check_source(path)
        if outputs:
            command = subprocess.run(["git", "-C", str(self.site), "ls-files", "-z", "--cached", "--others", "--exclude-standard"], capture_output=True)
            if command.returncode:
                raise PrivacyError("Unable to enumerate public repository files.")
            for name in set(command.stdout.decode("utf-8").split("\0")) - {""}:
                path = self.site / name
                if path.is_file() or path.is_symlink():
                    self.scan_output_file(path)
        if index:
            # The index can differ from the files on disk; test what Git would commit too.
            result = subprocess.run(["git", "-C", str(self.site), "ls-files", "--stage", "-z"], capture_output=True, check=True)
            for entry in result.stdout.decode("utf-8").split("\0"):
                if not entry:
                    continue
                meta, name = entry.split("\t", 1)
                mode, blob, stage = meta.split()
                if stage != "0" or mode == "120000":
                    self.problem("unsafe_git_index_entry", name)
                if private_marker(name) or blob in self.private_git:
                    self.problem("private_git_index_entry", name)
                path = self.site / name
                if path.is_file() and self.hash(path)["sha256"] in self.private_sha:
                    self.problem("private_git_index_content", name)
            # Our workflow stages everything; a later concurrent edit must not bypass the check.
            if subprocess.run(["git", "-C", str(self.site), "diff", "--quiet"], capture_output=True).returncode:
                self.problem("checkout_changed_after_staging", self.site)
        if outgoing:
            self.check_outgoing(outgoing)
        self.remember_private_identities()
        return self.issues

    def report(self, path=REPORT_PATH):
        path = Path(path).resolve()
        if path.is_relative_to(self.site):
            raise PrivacyError("The private report must be outside the public repository.")
        data = {"version": 1, "passed": not self.issues, "issues": self.issues}
        save_json(path, data)
        return data


def retire_unreferenced_images(site, used_names, policy=POLICY_PATH):
    """Quarantine only known generated image copies that no source still references."""
    site = Path(site).resolve()
    manifest_path = site / ".cache/web-images.json"
    if not manifest_path.exists():
        return 0
    managed = json.loads(manifest_path.read_text(encoding="utf-8"))["files"]
    source_text = []
    for folder in ("content", "layouts", "themes", "assets", "static"):
        for path in (site / folder).rglob("*"):
            if path.is_file() and path.suffix.casefold() in TEXT_EXTENSIONS | {".toml", ".yaml", ".yml"}:
                source_text.append(decoded(path.read_text(encoding="utf-8-sig", errors="replace")).casefold())
    references = "\n".join(source_text)
    used = {name.casefold() for name in used_names}
    candidates = []
    for name, record in managed.items():
        if Path(name).name != name or "/" in name or "\\" in name:
            raise PrivacyError("Unsafe image cache filename.")
        if name.casefold() in used or name.casefold() in references:
            continue
        for folder in ("static/images", "public/images"):
            path = site / folder / name
            if not path.exists():
                continue
            if path.is_symlink() or path.resolve().parent != (site / folder).resolve():
                raise PrivacyError("Unsafe retired image path.")
            identity = fingerprints(path)
            if identity["sha256"] != record.get("output_sha256"):
                raise PrivacyError("An unused generated image was edited; review before retiring it.")
            candidates.append((path, identity))
    quarantine = Path(policy).resolve().parent / "retired-exports"
    if quarantine.is_relative_to(site):
        raise PrivacyError("Retired exports must be stored outside the public repository.")
    # Verify all candidates before moving any of them.
    for path, identity in candidates:
        destination = quarantine / identity["sha256"] / path.relative_to(site)
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists() and fingerprints(destination)["sha256"] != identity["sha256"]:
            raise PrivacyError("Retired-image backup collision.")
        if not destination.exists():
            shutil.copy2(path, destination)
        if fingerprints(destination)["sha256"] != identity["sha256"]:
            raise PrivacyError("Retired-image backup verification failed.")
        path.unlink()
    return len(candidates)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", type=Path, required=True)
    parser.add_argument("--site", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--policy", type=Path, default=POLICY_PATH)
    parser.add_argument("--report", type=Path, default=REPORT_PATH)
    parser.add_argument("--sources-only", action="store_true")
    parser.add_argument("--index", action="store_true")
    parser.add_argument("--outgoing", help="Remote tracking ref against which to inspect new commits")
    args = parser.parse_args()
    try:
        guard = PrivacyGuard(args.vault, args.site, args.policy)
        issues = guard.check(outputs=not args.sources_only, index=args.index, outgoing=args.outgoing)
        guard.report(args.report)
        print(f"Attachment privacy check: {'BLOCKED' if issues else 'passed'} ({len(issues)} findings).")
        print(f"Private report: {args.report}")
        return 2 if issues else 0
    except (PrivacyError, OSError, ValueError, subprocess.SubprocessError) as exc:
        print(f"Attachment privacy check BLOCKED: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
