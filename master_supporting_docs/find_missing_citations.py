"""Compare top extracted references against the manuscript's existing citations."""

from __future__ import annotations

import csv
import glob
import os
import re
import unicodedata

MANUSCRIPT_DIR = r"c:/Users/USER/Documents/Test environment/paper/manuscript"
BIB_PATH = r"c:/Users/USER/Documents/Test environment/paper/manuscript/ProjectAlgorithm.bib"
CSV_PATH = r"c:/Users/USER/Documents/Test environment/paper/master_supporting_docs/references_extracted.csv"

CITE_RE = re.compile(r"\\cite[a-zA-Z]*\*?\{([^}]+)\}")
BIB_AUTHOR_RE = re.compile(r"author\s*=\s*\{([^}]+)\}", re.IGNORECASE)
BIB_YEAR_RE = re.compile(r"year\s*=\s*\{?\s*(\d{4})", re.IGNORECASE)
BIB_ENTRY_RE = re.compile(r"@\w+\s*\{\s*([^,\s]+)\s*,", re.IGNORECASE)


def strip_accents(s: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn"
    )


def keys_in_manuscript() -> set[str]:
    cited: set[str] = set()
    for path in glob.glob(os.path.join(MANUSCRIPT_DIR, "*.tex")):
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            text = f.read()
        for m in CITE_RE.finditer(text):
            for k in m.group(1).split(","):
                k = k.strip()
                if k:
                    cited.add(k)
    return cited


def parse_bib(path: str) -> dict[str, str]:
    """Return {bibkey: 'firstauthor_year' normalized key}."""
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        text = f.read()
    # Split into entries by '@type{key,'
    out: dict[str, str] = {}
    # Iterate using positions of '@' entries
    for m in re.finditer(r"@\w+\s*\{\s*([^,\s]+)\s*,", text):
        key = m.group(1)
        # find end of entry by counting braces from the opening brace
        start = m.end()
        depth = 1
        i = start
        while i < len(text) and depth > 0:
            ch = text[i]
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
            i += 1
        body = text[start:i]
        ma = BIB_AUTHOR_RE.search(body)
        my = BIB_YEAR_RE.search(body)
        if ma and my:
            authors = ma.group(1)
            # First author surname: before first comma OR before " and " or first word if no comma
            first = authors.split(" and ")[0].strip()
            if "," in first:
                surname = first.split(",")[0].strip()
            else:
                # "Firstname Surname" style
                parts = first.split()
                surname = parts[-1] if parts else ""
            surname_key = (
                strip_accents(surname).lower().replace("'", "").replace("’", "")
            )
            surname_key = re.split(r"\s+", surname_key)[0]
            year = my.group(1)
            out[key] = f"{surname_key}_{year}"
    return out


def main() -> None:
    cited_keys = keys_in_manuscript()
    bib_map = parse_bib(BIB_PATH)

    # Build the set of normalized keys already cited
    cited_normalized: set[str] = set()
    for key in cited_keys:
        if key in bib_map:
            cited_normalized.add(bib_map[key])
        else:
            # Try parsing the citation key itself if it follows the
            # repo's "author_keyword_year" convention.
            m = re.match(r"^([a-z]+).*?(\d{4})", key)
            if m:
                cited_normalized.add(f"{m.group(1).lower()}_{m.group(2)}")

    print(f"Citation keys in manuscript: {len(cited_keys)}")
    print(f"Bib entries with parseable author+year: {len(bib_map)}")
    print(f"Normalized 'firstauthor_year' set: {len(cited_normalized)}")

    # Read the extracted references CSV
    rows: list[dict] = []
    with open(CSV_PATH, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["n_papers"] = int(row["n_papers"])
            rows.append(row)
    rows.sort(key=lambda r: -r["n_papers"])

    # Filter: not already cited
    missing = [r for r in rows if r["key"] not in cited_normalized]

    print(f"\nTotal unique extracted refs: {len(rows)}")
    print(f"Already cited (normalized match): {len(rows) - len(missing)}")
    print(f"NOT yet cited: {len(missing)}\n")

    print("Top 10 most-cited references NOT in manuscript:\n")
    print(f"{'Rank':<5} {'N':<4} {'Key':<30} {'Sample'}")
    print("-" * 110)
    for i, r in enumerate(missing[:25], 1):
        sample = r["sample_reference"][:80].replace("\n", " ")
        print(f"{i:<5} {r['n_papers']:<4} {r['key']:<30} {sample}")


if __name__ == "__main__":
    main()
