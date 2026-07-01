import re
import sys
from pathlib import Path


DATAVIEW_RE = re.compile(r"```dataview(?:js)?\s*\n(.*?)```", re.IGNORECASE | re.DOTALL)
FRONT_MATTER_RE = re.compile(r"^\ufeff?---\s*\r?\n(.*?)\r?\n---\s*\r?\n", re.DOTALL)


def clean_scalar(value):
    return value.strip().strip('"').strip("'")


def parse_front_matter(path):
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return None

    metadata = {}
    current_list = None
    for line in match.group(1).splitlines():
        list_item = re.match(r"^\s*-\s+(.+?)\s*$", line)
        if list_item and current_list:
            metadata[current_list].append(clean_scalar(list_item.group(1)))
            continue

        field = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*?)\s*$", line)
        if not field:
            continue

        key, raw_value = field.groups()
        key = key.lower()
        if raw_value:
            metadata[key] = clean_scalar(raw_value)
            current_list = None
        else:
            metadata[key] = []
            current_list = key

    metadata["_path"] = path
    metadata["_relative"] = path.relative_to(path.parents[1])
    metadata["_filename"] = path.stem
    metadata.setdefault("title", path.stem)
    metadata.setdefault("tags", [])
    if not isinstance(metadata["tags"], list):
        metadata["tags"] = [metadata["tags"]]
    return metadata


def load_notes(content_dir):
    notes = []
    for path in content_dir.rglob("*.md"):
        try:
            metadata = parse_front_matter(path)
        except (OSError, UnicodeError) as exc:
            print(f"[WARN] Dataview skipped unreadable file {path.name}: {exc}")
            continue
        if metadata:
            notes.append(metadata)
    return notes


def relref_link(note):
    relative = note["_relative"].as_posix()
    return f'[{note["title"]}]({{{{< relref "{relative}" >}}}})'


def required_tags(query):
    tags = {
        value.lower()
        for value in re.findall(
            r'contains\s*\(\s*tags\s*,\s*["\']([^"\']+)["\']\s*\)',
            query,
            flags=re.IGNORECASE,
        )
    }
    tags.update(
        value.lower()
        for value in re.findall(
            r'\b(?:tags|page\.tags)\b.*?\.includes\s*\(\s*["\']([^"\']+)["\']\s*\)',
            query,
            flags=re.IGNORECASE,
        )
    )
    return tags


def filtered_notes(query, notes, current_path=None):
    tags = required_tags(query)
    selected = [
        note
        for note in notes
        if tags.issubset({tag.lower() for tag in note.get("tags", [])})
        and not (
            current_path
            and note["_path"] == current_path
            and re.search(
                r"page\.file\.path\s*!==?\s*dv\.current\(\)\.file\.path",
                query,
                flags=re.IGNORECASE,
            )
        )
    ]

    sort_match = re.search(
        r"(?mi)^\s*SORT\s+([\w.]+)\s+(ASC|DESC)\s*$",
        query,
    )
    if not sort_match:
        sort_match = re.search(
            r'\.sort\s*\(\s*[^,]*?page\.([\w.]+)\s*,\s*["\'](asc|desc)["\']',
            query,
            flags=re.IGNORECASE,
        )
    if not sort_match:
        return selected

    field, direction = sort_match.groups()
    reverse = direction.upper() == "DESC"
    key_name = "_filename" if field.lower() == "file.name" else field.lower()

    def sort_key(note):
        value = note.get(key_name, "")
        try:
            return float(value)
        except (TypeError, ValueError):
            return str(value).lower()

    return sorted(selected, key=sort_key, reverse=reverse)


def escape_cell(value):
    if isinstance(value, list):
        value = ", ".join(value)
    return str(value or "—").replace("|", r"\|").replace("\n", " ")


def render_list(query, notes, current_path=None):
    selected = filtered_notes(query, notes, current_path)
    if not selected:
        return "_No matching notes._"
    return "\n".join(f"- {relref_link(note)}" for note in selected)


def table_columns(query):
    table_match = re.search(
        r"(?is)^\s*TABLE\s+(.*?)\s+FROM\s+",
        query,
    )
    if not table_match:
        return []

    columns = []
    for raw_column in table_match.group(1).split(","):
        raw_column = raw_column.strip()
        alias_match = re.match(r"^([\w-]+)\s+AS\s+(.+)$", raw_column, re.IGNORECASE)
        if alias_match:
            field, label = alias_match.groups()
        else:
            field = raw_column
            label = raw_column.replace("_", " ").title()
        columns.append((field.lower(), label.strip()))
    return columns


def render_table(query, notes, current_path=None):
    selected = filtered_notes(query, notes, current_path)
    columns = table_columns(query)
    headers = ["Meal", *[label for _, label in columns]]
    separator = ["---"] * len(headers)
    rows = [
        [
            relref_link(meal),
            *[escape_cell(meal.get(field)) for field, _ in columns],
        ]
        for meal in selected
    ]

    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(separator) + " |",
    ]
    lines.extend("| " + " | ".join(row) + " |" for row in rows)
    if not rows:
        lines.append("| _No matching notes._ | " + " | ".join("—" for _ in columns) + " |")
    return "\n".join(lines)


def render_dataview(query, notes, current_path=None):
    normalized = query.lstrip().upper()
    if normalized.startswith("LIST"):
        return render_list(query, notes, current_path)
    if normalized.startswith("TABLE"):
        return render_table(query, notes, current_path)
    if "DV.PAGES" in normalized and "FOR (CONST PAGE OF PAGES)" in normalized:
        return render_list(query, notes, current_path)
    return f"```dataview\n{query}```"


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: dataview.py <content_dir>")

    content_dir = Path(sys.argv[1]).resolve()
    notes = load_notes(content_dir)
    changed = 0

    for path in content_dir.rglob("*.md"):
        try:
            original = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            print(f"[WARN] Dataview skipped unreadable file {path.name}: {exc}")
            continue
        rendered = DATAVIEW_RE.sub(
            lambda match: render_dataview(match.group(1), notes, path),
            original,
        )
        if rendered != original:
            path.write_text(rendered, encoding="utf-8")
            changed += 1

    print(f"[INFO] Expanded Dataview blocks in {changed} files using {len(notes)} notes.")


if __name__ == "__main__":
    main()
