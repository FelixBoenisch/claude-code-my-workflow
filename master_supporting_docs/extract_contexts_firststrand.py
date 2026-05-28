"""Extract in-text citation contexts for the four core 'responsibility avoidance
through delegation' references, across every supporting paper that cites them.

Targets: Bartling & Fischbacher (2012), Hamman et al. (2010), Coffman (2011),
Oexl & Grossman (2013). Self-citations (a target paper citing itself) are excluded.

Same machinery as extract_citation_contexts.py: reflow two-column PDFs into clean
per-column streams, match author-year citation patterns, pull ~280 chars of context
around each match, de-duplicate near-identical snippets, write a markdown report.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEXT_DIR = HERE / "supporting_papers" / "_extracted_text"
CSV_PATH = HERE / "references_extracted.csv"
OUT_MD = HERE / "references_firststrand_contexts.md"

CONTEXT_BEFORE = 280
CONTEXT_AFTER = 280

# (csv_key, surname, year, display_label, self_paper_stem_to_exclude)
TARGETS = [
    ("bartling_2012", "Bartling", "2012",
     "Bartling & Fischbacher (2012) — Shifting the blame: on delegation and responsibility",
     "bartling_shifting_2012"),
    ("hamman_2010", "Hamman", "2010",
     "Hamman, Loewenstein & Weber (2010) — Self-interest through delegation",
     "hamman_self-interest_2010"),
    ("coffman_2011", "Coffman", "2011",
     "Coffman (2011) — Intermediation reduces punishment (and reward)",
     "coffman_intermediation_2011"),
    ("oexl_2013", "Oexl", "2013",
     "Oexl & Grossman (2013) — Shifting the blame to a powerless intermediary",
     "oexl_shifting_2013"),
]


def split_columns(line: str) -> list[str]:
    parts = re.split(r"\s{4,}", line.rstrip())
    return [p.strip() for p in parts if p.strip()]


def reflow_to_streams(lines: list[str]) -> list[str]:
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


def build_citation_patterns(surname: str, year: str) -> list[re.Pattern]:
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


def find_citation_contexts(text: str, surname: str, year: str) -> list[str]:
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
    results: list[str] = []
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
        results.append(snippet)
    return results


def citing_papers_from_csv(key: str) -> list[str]:
    with CSV_PATH.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["key"] == key:
                return [p.strip() for p in row["papers"].split(";") if p.strip()]
    return []


def slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s


def main() -> None:
    out: list[str] = []
    out.append(
        "# Citation contexts — core 'responsibility avoidance through delegation' references\n"
    )
    out.append(
        "_In-text contexts for the four canonical human-to-human delegation papers, across "
        "every supporting paper that cites them. ~280 chars of context before/after each "
        "match; citation marker in **bold**; line breaks and PDF-extraction artefacts "
        "cleaned up. A target paper citing itself is excluded._\n"
    )
    out.append("## Table of contents\n")
    for i, (_, surname, year, label, _self) in enumerate(TARGETS, 1):
        out.append(f"{i}. [**{label}**](#{slugify(f'{i}-{surname}-{year}')})")
    out.append("")

    total = 0
    for i, (key, surname, year, label, self_stem) in enumerate(TARGETS, 1):
        out.append("\n---\n")
        out.append(f"## {i}. {label}\n")
        papers = [p for p in citing_papers_from_csv(key) if p != self_stem]
        out.append(f"**Cited in {len(papers)} papers** (excluding self): {', '.join(papers)}\n")
        no_ctx: list[str] = []
        for paper in papers:
            txt_path = TEXT_DIR / f"{paper}.txt"
            if not txt_path.exists():
                continue
            lines = txt_path.read_text(encoding="utf-8", errors="replace").splitlines()
            streams = reflow_to_streams(lines)
            contexts: list[str] = []
            seen: set[str] = set()
            for stream in streams:
                for snippet in find_citation_contexts(stream, surname, year):
                    norm = re.sub(r"\W+", "", snippet.lower())[:200]
                    if norm in seen:
                        continue
                    seen.add(norm)
                    contexts.append(snippet)
            if not contexts:
                no_ctx.append(paper)
                continue
            out.append(f"\n### {paper}\n")
            for j, snippet in enumerate(contexts, 1):
                out.append(f"{j}. …{snippet}…\n")
                total += 1
        if no_ctx:
            out.append(
                f"\n_No in-text narrative found (likely numbered-citation style) in: "
                f"{', '.join(no_ctx)}_\n"
            )

    OUT_MD.write_text("\n".join(out), encoding="utf-8")
    print(f"Wrote {OUT_MD}")
    print(f"Total snippets: {total}")


if __name__ == "__main__":
    main()
