"""For the top-N most-cited references NOT yet cited in the manuscript, find every
in-text mention across the papers that cite them and extract the surrounding context.

Approach
--------
1. Read references_extracted.csv (produced by extract_references.py).
2. Read all manuscript .tex files; parse \\cite{...} commands to get cited keys.
3. Parse ProjectAlgorithm.bib for normalized (firstauthor_lastname + year) keys
   so we can match cited bib keys to extracted refs.
4. Filter the CSV down to the top N references with the highest citation count
   that are NOT already cited in the manuscript.
5. For each target reference, search each citing paper's reflowed text for
   citation patterns matching (surname, year):
      - Narrative:    "Surname (YYYY)", "Surname et al. (YYYY)"
      - Parenthetical:"(Surname, YYYY)", "(Surname et al., YYYY)"
      - Two-author:   "Surname and Other (YYYY)", "Surname & Other YYYY"
6. Extract ~280 chars of context before/after each match, clean whitespace,
   de-duplicate near-identical snippets within a paper.
7. Write a markdown report with table of contents at top.

Papers using numbered references (Nature/Science/PNAS [24] style) often have no
narrative attached to the marker — these are listed at the end of each section
as "no narrative found".
"""

from __future__ import annotations

import csv
import glob
import os
import re
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEXT_DIR = HERE / "supporting_papers" / "_extracted_text"
CSV_PATH = HERE / "references_extracted.csv"
MANUSCRIPT_DIR = HERE.parent / "manuscript"
BIB_PATH = MANUSCRIPT_DIR / "ProjectAlgorithm.bib"
OUT_MD = HERE / "references_top30_missing_contexts.md"

TOP_N = 30
CONTEXT_BEFORE = 280
CONTEXT_AFTER = 280

CITE_RE = re.compile(r"\\cite[a-zA-Z]*\*?\{([^}]+)\}")
BIB_AUTHOR_RE = re.compile(r"author\s*=\s*\{([^}]+)\}", re.IGNORECASE)
BIB_YEAR_RE = re.compile(r"year\s*=\s*\{?\s*(\d{4})", re.IGNORECASE)


def strip_accents(s: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn"
    )


def split_columns(line: str) -> list[str]:
    parts = re.split(r"\s{4,}", line.rstrip())
    return [p.strip() for p in parts if p.strip()]


def reflow_to_streams(lines: list[str]) -> list[str]:
    """Return one continuous text per column (left, then right)."""
    two_col = sum(1 for ln in lines if len(split_columns(ln)) >= 2) >= max(
        10, len(lines) // 5
    )
    if not two_col:
        return [" ".join(ln.strip() for ln in lines if ln.strip())]
    left_lines: list[str] = []
    right_lines: list[str] = []
    for ln in lines:
        frags = split_columns(ln)
        if not frags:
            left_lines.append("")
            right_lines.append("")
        elif len(frags) == 1:
            left_lines.append(frags[0])
            right_lines.append("")
        else:
            left_lines.append(frags[0])
            right_lines.append(" ".join(frags[1:]))
    left = " ".join(ln for ln in left_lines if ln.strip())
    right = " ".join(ln for ln in right_lines if ln.strip())
    return [left, right]


def keys_in_manuscript() -> set[str]:
    cited: set[str] = set()
    if not MANUSCRIPT_DIR.exists():
        return cited
    for path in glob.glob(str(MANUSCRIPT_DIR / "*.tex")):
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            text = f.read()
        for m in CITE_RE.finditer(text):
            for k in m.group(1).split(","):
                k = k.strip()
                if k:
                    cited.add(k)
    return cited


def parse_bib(path: Path) -> dict[str, str]:
    """Return {bibkey: 'firstauthor_year'}."""
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8", errors="replace")
    out: dict[str, str] = {}
    for m in re.finditer(r"@\w+\s*\{\s*([^,\s]+)\s*,", text):
        key = m.group(1)
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
            first = authors.split(" and ")[0].strip()
            if "," in first:
                surname = first.split(",")[0].strip()
            else:
                parts = first.split()
                surname = parts[-1] if parts else ""
            surname_key = (
                strip_accents(surname).lower().replace("'", "").replace("’", "")
            )
            surname_key = re.split(r"\s+", surname_key)[0]
            year = my.group(1)
            out[key] = f"{surname_key}_{year}"
    return out


def get_top_missing(top_n: int) -> list[dict]:
    """Return the top N rows from the CSV that are NOT cited in the manuscript."""
    cited_keys = keys_in_manuscript()
    bib_map = parse_bib(BIB_PATH)
    cited_normalized: set[str] = set()
    for key in cited_keys:
        if key in bib_map:
            cited_normalized.add(bib_map[key])
        else:
            m = re.match(r"^([a-z]+).*?(\d{4})", key)
            if m:
                cited_normalized.add(f"{m.group(1).lower()}_{m.group(2)}")

    rows: list[dict] = []
    with CSV_PATH.open("r", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            row["n_papers"] = int(row["n_papers"])
            rows.append(row)
    rows.sort(key=lambda r: -r["n_papers"])
    missing = [r for r in rows if r["key"] not in cited_normalized]
    return missing[:top_n]


def build_citation_patterns(surname: str, year: str) -> list[re.Pattern]:
    # Case-insensitive so ALL-CAPS or title-case author entries match either way.
    s = re.escape(surname)
    y = re.escape(year)
    yr = rf"{y}[a-z]?"
    flags = re.IGNORECASE
    return [
        re.compile(
            rf"\b{s}(?:\s+(?:et\s+al\.?|and\s+[A-Z][a-zA-Z\-]+|&\s+[A-Z][a-zA-Z\-]+))?\s*\(\s*{yr}\s*\)",
            flags,
        ),
        re.compile(
            rf"\(\s*(?:[^()]*?[;,]\s*)?{s}(?:\s+(?:et\s+al\.?|and\s+[A-Z][a-zA-Z\-]+|&\s+[A-Z][a-zA-Z\-]+))?\s*,?\s*{yr}",
            flags,
        ),
        re.compile(
            rf"\b{s}(?:\s+(?:et\s+al\.?|and\s+[A-Z][a-zA-Z\-]+|&\s+[A-Z][a-zA-Z\-]+))?,\s*{yr}\b",
            flags,
        ),
    ]


def find_citation_contexts(
    text: str, surname: str, year: str
) -> list[tuple[int, str]]:
    patterns = build_citation_patterns(surname, year)
    matches: list[tuple[int, int]] = []
    for pat in patterns:
        for m in pat.finditer(text):
            matches.append((m.start(), m.end()))
    if not matches:
        return []
    matches.sort()
    merged: list[tuple[int, int]] = []
    for start, end in matches:
        if merged and start <= merged[-1][1] + 5:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))

    results: list[tuple[int, str]] = []
    for start, end in merged:
        a = max(0, start - CONTEXT_BEFORE)
        b = min(len(text), end + CONTEXT_AFTER)
        local_text = text[a:b]
        snippet = re.sub(r"-\s+", "", local_text)
        snippet = re.sub(r"\s+", " ", snippet).strip()
        for pat in patterns:
            for m in pat.finditer(local_text):
                raw = local_text[m.start() : m.end()]
                raw_clean = re.sub(r"-\s+", "", raw)
                raw_clean = re.sub(r"\s+", " ", raw_clean).strip()
                snippet = snippet.replace(raw_clean, f"**{raw_clean}**", 1)
                break
            else:
                continue
            break
        results.append((start, snippet))
    return results


def label_for(row: dict) -> tuple[str, str, str]:
    """Return (surname_for_regex, year, display_label) from a CSV row.

    `surname_for_regex` is title-cased (matches typical in-text citation form,
    even if some bibliographies stored the name in ALL CAPS).
    """
    key = row["key"]
    m = re.match(r"^([a-z]+)_(\d{4})$", key)
    surname_lower, year = (m.group(1), m.group(2)) if m else (key, "")
    # Title-case for both the regex and display, so "DANA" → "Dana".
    surname = surname_lower.capitalize() if surname_lower else "Unknown"
    display_label = f"{surname} ({year})" if year else surname
    return surname, year, display_label


def slugify(text: str) -> str:
    s = strip_accents(text).lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


def main() -> None:
    if not CSV_PATH.exists():
        raise SystemExit(f"Missing {CSV_PATH} — run extract_references.py first.")

    missing = get_top_missing(TOP_N)
    print(f"Top {TOP_N} most-cited refs not in manuscript: {len(missing)}")

    # Build TOC entries first (we need to know section anchors).
    toc: list[str] = []
    for i, row in enumerate(missing, 1):
        surname, year, canonical = label_for(row)
        n = row["n_papers"]
        anchor = slugify(f"{i}-{surname}-{year}")
        toc.append(
            f"{i}. [**{canonical}** — cited in {n} papers](#{anchor})"
        )

    out: list[str] = []
    out.append(
        "# Citation contexts for the top 30 most-cited references not in the manuscript\n"
    )
    out.append(
        "_For each reference, every paper in `master_supporting_docs/supporting_papers/` "
        "that cites it is listed, followed by the in-text snippets where the citation "
        "appears (~280 chars of context before and after, with line breaks and "
        "PDF-extraction artefacts cleaned up). The citation marker is shown in **bold**._\n"
    )
    out.append(
        "_Papers using numbered citation style (Nature/Science/PNAS [N] format) often "
        "have no narrative attached to the citation marker — these are listed at the end "
        "of each section as **no in-text narrative found**._\n"
    )
    out.append("## Table of contents\n")
    out.extend(toc)
    out.append("")

    total_snippets = 0
    for i, row in enumerate(missing, 1):
        surname, year, canonical = label_for(row)
        anchor = slugify(f"{i}-{surname}-{year}")
        n = row["n_papers"]
        papers = [p.strip() for p in row["papers"].split(";") if p.strip()]

        # Section header uses a manual anchor by repeating the slug in the heading
        # so GitHub-flavored markdown auto-generates the same anchor.
        out.append(f"\n---\n")
        out.append(f"## {i}. {canonical} — cited in {n} papers\n")
        out.append(f"**Citing papers:** {', '.join(papers)}\n")

        no_context_papers: list[str] = []
        for paper in papers:
            txt_path = TEXT_DIR / f"{paper}.txt"
            if not txt_path.exists():
                continue
            raw_lines = txt_path.read_text(
                encoding="utf-8", errors="replace"
            ).splitlines()
            streams = reflow_to_streams(raw_lines)
            all_contexts: list[str] = []
            seen: set[str] = set()
            for stream in streams:
                for _, snippet in find_citation_contexts(stream, surname, year):
                    norm = re.sub(r"\W+", "", snippet.lower())[:200]
                    if norm in seen:
                        continue
                    seen.add(norm)
                    all_contexts.append(snippet)
            if not all_contexts:
                no_context_papers.append(paper)
                continue
            out.append(f"\n### {paper}\n")
            for j, snippet in enumerate(all_contexts, 1):
                out.append(f"{j}. …{snippet}…\n")
                total_snippets += 1

        if no_context_papers:
            out.append(
                f"\n_No in-text narrative found (likely numbered-citation style) "
                f"in: {', '.join(no_context_papers)}_\n"
            )

    OUT_MD.write_text("\n".join(out), encoding="utf-8")
    print(f"Wrote {OUT_MD}")
    print(f"Total snippets extracted: {total_snippets}")


if __name__ == "__main__":
    main()
