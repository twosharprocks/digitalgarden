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


def parse_tag_array(raw_value):
    return [
        value.lower()
        for value in re.findall(r'["\']([^"\']+)["\']', raw_value or "")
    ]


def dataview_categories(query):
    categories_match = re.search(
        r"(?is)\bconst\s+categories\s*=\s*\[(.*?)\]\s*;",
        query,
    )
    if not categories_match:
        return []

    categories = []
    for object_match in re.finditer(r"\{(.*?)\}", categories_match.group(1), re.DOTALL):
        definition = object_match.group(1)
        heading_match = re.search(
            r'\bheading\s*:\s*["\']([^"\']+)["\']',
            definition,
            flags=re.IGNORECASE,
        )
        if not heading_match:
            continue

        all_match = re.search(r"\ball\s*:\s*\[(.*?)\]", definition, re.I | re.S)
        any_match = re.search(r"\bany\s*:\s*\[(.*?)\]", definition, re.I | re.S)
        categories.append(
            {
                "heading": heading_match.group(1),
                "all": parse_tag_array(all_match.group(1) if all_match else ""),
                "any": parse_tag_array(any_match.group(1) if any_match else ""),
            }
        )
    return categories


def render_categorized_list(query, notes, current_path=None):
    categories = dataview_categories(query)
    if not categories:
        return None

    base_tags = required_tags(query)
    candidates = [
        note
        for note in notes
        if base_tags.issubset({tag.lower() for tag in note.get("tags", [])})
        and note["_path"] != current_path
    ]

    sections = []
    for category in categories:
        selected = []
        for note in candidates:
            tags = {tag.lower() for tag in note.get("tags", [])}
            if not set(category["all"]).issubset(tags):
                continue
            if category["any"] and not tags.intersection(category["any"]):
                continue
            selected.append(note)

        selected.sort(key=lambda note: note["_filename"].lower())
        lines = [f"# {category['heading']}"]
        if selected:
            lines.extend(f"- {relref_link(note)}" for note in selected)
        else:
            lines.append("_No matching notes._")
        sections.append("\n".join(lines))

    return "\n\n".join(sections)


def oscp_system(note):
    name = note.get("_filename", "")
    parts = [
        re.sub(r"\s*\(DNF\)\s*$", "", part, flags=re.IGNORECASE).strip()
        for part in re.sub(r"^OSCP\s*-\s*", "", name, flags=re.IGNORECASE).split(" - ")
    ]

    if re.search(r"cheat sheet", name, flags=re.IGNORECASE):
        return "General"
    if any(re.fullmatch(r"(ad|active directory)", part, flags=re.IGNORECASE) for part in parts):
        return "Active Directory"
    if any(re.fullmatch(r"windows", part, flags=re.IGNORECASE) for part in parts):
        return "Windows"
    if any(re.fullmatch(r"linux", part, flags=re.IGNORECASE) for part in parts):
        return "Linux"
    if any(re.fullmatch(r"(core|exam prep)", part, flags=re.IGNORECASE) for part in parts):
        return "General"
    return "Other"


def render_oscp_index(query, notes, current_path=None):
    normalized = query.upper()
    if not (
        "OSCP" in normalized
        and "GROUPORDER" in normalized
        and "OSCPSYSTEM" in normalized
        and "FILE.NAME.STARTSWITH" in normalized
    ):
        return None

    group_order = ["General", "Windows", "Linux", "Active Directory", "Other"]
    selected = []
    for note in notes:
        if current_path and note["_path"] == current_path:
            continue
        tags = {str(tag).replace("#", "", 1).lower() for tag in note.get("tags", [])}
        filename = note.get("_filename", "")
        if filename.startswith("OSCP - ") or "oscp" in tags:
            selected.append(note)

    selected.sort(key=lambda note: note.get("_filename", "").lower())

    sections = []
    for group_name in group_order:
        group_notes = [note for note in selected if oscp_system(note) == group_name]
        if not group_notes:
            continue
        lines = [f"## {group_name}"]
        lines.extend(f"- {relref_link(note)}" for note in group_notes)
        sections.append("\n".join(lines))

    return "\n\n".join(sections) if sections else "_No matching OSCP notes._"


def trip_sort_key(note):
    month_numbers = {
        "jan": 1,
        "feb": 2,
        "mar": 3,
        "apr": 4,
        "may": 5,
        "jun": 6,
        "jul": 7,
        "aug": 8,
        "sep": 9,
        "oct": 10,
        "nov": 11,
        "dec": 12,
    }
    match = re.search(
        r"\b(20\d{2})\s+"
        r"(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|"
        r"Jul(?:y)?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|"
        r"Nov(?:ember)?|Dec(?:ember)?)\b",
        note.get("_filename", ""),
        flags=re.IGNORECASE,
    )
    if not match:
        return 0
    year = int(match.group(1))
    month = month_numbers.get(match.group(2)[:3].lower(), 0)
    return year * 100 + month


def uses_trip_template(note):
    templates = note.get("template", [])
    if not isinstance(templates, list):
        templates = [templates]
    for template in templates:
        target = str(template or "").strip().strip('"').strip("'")
        if re.sub(r"\.md$", "", target, flags=re.IGNORECASE).endswith("Template - Trip"):
            return True
    return False


def render_trips_index(query, notes, current_path=None):
    normalized = query.upper()
    if not (
        "USESTRIPTEMPLATE" in normalized
        and re.search(r"\bTRIPS\s*=\s*DV\.PAGES", normalized)
        and "TRIPS" in normalized
        and "TRIP - " in normalized
    ):
        return None

    categories = [
        ("Upcoming", "planning"),
        ("Past", "complete"),
        ("Cancelled", "cancelled"),
    ]

    trips = []
    for note in notes:
        filename = note.get("_filename", "")
        if filename.startswith("Template - "):
            continue
        if filename.startswith("Trip - ") or uses_trip_template(note):
            trips.append(note)

    sections = []
    for heading, status in categories:
        selected = [
            note
            for note in trips
            if str(note.get("status", "")).lower() == status
        ]
        selected.sort(key=trip_sort_key, reverse=True)
        lines = [f"# {heading}"]
        if selected:
            lines.extend(f"- {relref_link(note)}" for note in selected)
        else:
            lines.append("_No matching notes._")
        sections.append("\n".join(lines))

    return "\n\n".join(sections)


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
    oscp_index = render_oscp_index(query, notes, current_path)
    if oscp_index is not None:
        return oscp_index
    trips_index = render_trips_index(query, notes, current_path)
    if trips_index is not None:
        return trips_index
    if normalized.startswith("LIST"):
        return render_list(query, notes, current_path)
    if normalized.startswith("TABLE"):
        return render_table(query, notes, current_path)
    if "CONST CATEGORIES" in normalized and "DV.HEADER" in normalized:
        categorized = render_categorized_list(query, notes, current_path)
        if categorized is not None:
            return categorized
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
