"""Extract references from supporting_papers/_extracted_text/*.txt.

Outputs:
- references_extracted.csv      : (rank, key, canonical, n_papers, papers, sample)
- references_extracted.md       : human-readable table, sorted by n_papers desc
- references_raw_per_paper.csv  : raw extracted references for spot-checking

Strategy
--------
Per paper:
1. Detect single- vs two-column layout (heuristic: count lines with >=2 fragments
   when split on runs of 4+ spaces).
2. If two-column, separate the document into independent left/right column streams.
3. For each stream:
   - Find a "References" / "Bibliography" / "REFERENCES" header.
   - If found, group lines into reference entries by an author-comma-initial start.
   - If no header was found in any stream, fall back to numbered-reference detection
     (matches papers using Nature/Science-style numbered refs).
4. Normalize each entry to `<firstauthor_lastname_lower>_<year>` as the dedup key
   (loose match: drops trailing 2015a -> 2015).
5. Aggregate counts across papers, write CSV/Markdown.

PDF-extracted text is noisy — this is a best-effort parser, not perfect. Expect ~80%
recall on references and occasional cross-paper merges of same-author-same-year items.
"""

from __future__ import annotations

import csv
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEXT_DIR = HERE / "supporting_papers" / "_extracted_text"
OUT_CSV = HERE / "references_extracted.csv"
OUT_MD = HERE / "references_extracted.md"
OUT_RAW = HERE / "references_raw_per_paper.csv"

REFERENCES_HEADER = re.compile(
    r"^\s*(?:[IVX]+\.?\s+|\d+\.?\s+|)"
    r"(references|references\s+cited|bibliography|literatur(?:ur)?|literature\s+cited|"
    r"works\s+cited|r\s*e\s*f\s*e\s*r\s*e\s*n\s*c\s*e\s*s)\s*\.?\s*$",
    re.IGNORECASE,
)
APPENDIX_HEADER = re.compile(
    r"^\s*(appendix|appendices|supplementary|supporting\s+information|"
    r"online\s+appendix)\b",
    re.IGNORECASE,
)
# Author-style reference start: "Surname, X." or "Surname, Y., ..." or "DeMarzo, P."
REF_START = re.compile(
    r"^([A-ZÄÖÜÉÈÀÂÊÎÔÛÇŁŚŻŹĆŃ][A-Za-zÄÖÜäöüßéèàâêîôûçłśżźćńÁÉÍÓÚáéíóúñ'’\-]+"
    r"(?:\s+[A-Z][a-z]+)?)\s*,\s*[A-Z]"
)
# Alternative style: "Surname X[Y][Z][, more]" (no comma between surname and initials).
# Used by Annual Reviews, INFORMS journals (Mgmt Sci), some IS journals, and many
# Nature-style author lists. Only accepted when the line also contains a year.
REF_START_NOCOMMA = re.compile(
    r"^([A-ZÄÖÜÉÈÀÂÊÎÔÛÇŁŚŻŹĆŃ][A-Za-zÄÖÜäöüßéèàâêîôûçłśżźćńÁÉÍÓÚáéíóúñ'’\-]+)"
    r"\s+[A-Z][A-Z]?[A-Z]?[,.\s\(]"
)
# Numbered reference: "1. Surname...", "[1] Surname...", or "1 Surname..." (no period).
NUM_REF_START = re.compile(
    r"^\s*(\d+\.?|\[\d+\])\s+([A-ZÄÖÜÉÈÀÂÊÎÔÛÇŁŚŻŹĆŃ][A-Za-zÄÖÜäöüßéèàâêîôûçłśżźćńÁÉÍÓÚáéíóúñ'’\-\.]+)"
)
# Initials-first author style (PNAS, Nature, Science): "E. Napolitano, ..." or "B. F. Malle, ..."
INITIALS_FIRST_RE = re.compile(
    r"^(?:[A-Z]\.?\s*-?\s*[A-Z]?\.?\s*){1,4}"
    r"([A-ZÄÖÜÉÈÀÂÊÎÔÛÇŁŚŻŹĆŃ][a-zA-ZÄÖÜäöüßéèàâêîôûçłśżźćńÁÉÍÓÚáéíóúñ'’\-]+)"
    r"[,.\s]"
)
YEAR_RE = re.compile(r"\b(19|20)\d{2}[a-z]?\b")


def strip_accents(s: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn"
    )


def split_columns(line: str) -> list[str]:
    """Split a line into fragments on runs of 4+ spaces (column-gap heuristic)."""
    parts = re.split(r"\s{4,}", line.rstrip())
    return [p.strip() for p in parts if p.strip()]


def detect_layout(lines: list[str]) -> bool:
    """True if document looks two-column."""
    two_col = sum(1 for ln in lines if len(split_columns(ln)) >= 2)
    return two_col >= max(10, len(lines) // 5)


def build_streams(lines: list[str], two_col: bool) -> list[list[str]]:
    """Return one or two column streams aligned to original line numbers."""
    if not two_col:
        return [[ln.rstrip() for ln in lines]]
    left: list[str] = []
    right: list[str] = []
    for ln in lines:
        frags = split_columns(ln)
        if not frags:
            left.append("")
            right.append("")
        elif len(frags) == 1:
            left.append(frags[0])
            right.append("")
        else:
            left.append(frags[0])
            right.append(" ".join(frags[1:]))
    return [left, right]


def find_references_start(stream: list[str]) -> int:
    """Return the line index AFTER the last References-style header, or -1."""
    last = -1
    for i, ln in enumerate(stream):
        if REFERENCES_HEADER.match(ln.strip()):
            last = i
    return last


def is_section_break(line: str) -> bool:
    """Stop scanning references when we hit an Appendix-style heading on its own line."""
    s = line.strip()
    if not s:
        return False
    if APPENDIX_HEADER.match(s) and len(s) < 60:
        return True
    return False


def looks_like_ref_start(line: str) -> bool:
    """True if line plausibly starts a reference entry (either citation style)."""
    if REF_START.match(line) and YEAR_RE.search(line[:300]):
        return True
    if REF_START_NOCOMMA.match(line) and YEAR_RE.search(line[:300]):
        # Extra filter: avoid matching common false positives like
        # "Journal Title", "American Economic Review", section titles, etc.
        # Require at least one comma-or-period followed by another capital letter
        # OR a parenthesised year in the line (typical of an author list).
        first200 = line[:200]
        if re.search(r"\(\s*(19|20)\d{2}", first200) or re.search(
            r"[A-Z][a-z]+\s+[A-Z][A-Z]?,\s+[A-Z][a-z]+\s+[A-Z]", first200
        ):
            return True
    return False


def group_author_references(lines: list[str]) -> list[str]:
    """Group lines into reference entries using author-style detection."""
    refs: list[str] = []
    current: list[str] = []
    for ln in lines:
        if is_section_break(ln):
            break
        stripped = ln.strip()
        if not stripped:
            if current:
                joined = " ".join(current).strip()
                if joined:
                    refs.append(joined)
                current = []
            continue
        if looks_like_ref_start(stripped):
            if current:
                joined = " ".join(current).strip()
                if joined:
                    refs.append(joined)
                current = []
            current.append(stripped)
        else:
            if current:
                current.append(stripped)
    if current:
        joined = " ".join(current).strip()
        if joined:
            refs.append(joined)
    return refs


def group_numbered_references(lines: list[str]) -> list[str]:
    """Group lines into numbered references (Nature/Science/legal style).

    Year is NOT required on the starting line — many Nature-style refs put
    the year on a continuation line. Instead we require the full reference
    string to contain a year (checked downstream in `is_plausible_reference`).
    """
    refs: list[str] = []
    current: list[str] = []
    expected_n = 1
    for ln in lines:
        stripped = ln.strip()
        if not stripped:
            if current:
                joined = " ".join(current).strip()
                if joined:
                    refs.append(joined)
                current = []
            continue
        m = NUM_REF_START.match(stripped)
        if m:
            num_str = m.group(1).strip("[]. ")
            try:
                num = int(num_str)
            except ValueError:
                num = -1
            # Accept if number is plausible and roughly increasing.
            if 1 <= num <= 999 and num >= expected_n - 3:
                if current:
                    joined = " ".join(current).strip()
                    if joined:
                        refs.append(joined)
                    current = []
                current.append(stripped)
                expected_n = num + 1
                continue
        if current:
            current.append(stripped)
    if current:
        joined = " ".join(current).strip()
        if joined:
            refs.append(joined)
    return refs


def is_plausible_reference(ref: str) -> bool:
    if len(ref) < 30 or len(ref) > 2000:
        return False
    if not YEAR_RE.search(ref):
        return False
    if APPENDIX_HEADER.match(ref):
        return False
    alpha = sum(1 for c in ref if c.isalpha())
    if alpha < 20:
        return False
    return True


def normalize_key(ref: str) -> tuple[str, str] | None:
    """Return (lastname_year_key, 'Lastname (year)') or None."""
    # Strip leading numbering like "1. ", "[12] ", "1 " (no period).
    cleaned = re.sub(r"^\s*(\d+\.?|\[\d+\])\s+", "", ref)
    m = REF_START.match(cleaned)
    if m:
        surname = m.group(1)
    else:
        m2 = REF_START_NOCOMMA.match(cleaned)
        if m2:
            surname = m2.group(1)
        else:
            # Initials-first style (PNAS-style "E. Napolitano, ...").
            mi = INITIALS_FIRST_RE.match(cleaned)
            if mi:
                surname = mi.group(1)
            else:
                m3 = re.match(
                    r"^([A-ZÄÖÜÉÈÀÂÊÎÔÛÇŁŚŻŹĆŃ][A-Za-zÄÖÜäöüßéèàâêîôûçłśżźćńÁÉÍÓÚáéíóúñ'’\-]+)",
                    cleaned,
                )
                if not m3:
                    return None
                surname = m3.group(1)
    surname_key = strip_accents(surname).lower().replace("'", "").replace("’", "")
    surname_key = re.split(r"\s+", surname_key)[0]
    if len(surname_key) < 2:
        return None
    year_match = YEAR_RE.search(cleaned[:400])
    if not year_match:
        return None
    year = year_match.group(0)
    year_key = re.sub(r"[a-z]$", "", year)
    return (f"{surname_key}_{year_key}", f"{surname.strip()} ({year})")


def extract_references_from_paper(path: Path) -> tuple[list[tuple[str, str, str]], str]:
    """Returns (list of (key, canonical, raw), method_used)."""
    try:
        raw = path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        print(f"  ! could not read {path.name}: {e}")
        return [], "read_error"
    lines = raw.splitlines()
    two_col = detect_layout(lines)
    streams = build_streams(lines, two_col)

    all_refs: list[str] = []
    # Find header location in any stream; propagate that position to streams
    # without their own header (handles the case where "References" appears
    # only in one PDF column).
    header_positions: list[int] = []
    for stream in streams:
        start = find_references_start(stream)
        if start >= 0:
            header_positions.append(start)
    method = "author_header"
    if header_positions:
        shared_start = min(header_positions)
        for stream in streams:
            own_start = find_references_start(stream)
            tail_start = own_start + 1 if own_start >= 0 else shared_start + 1
            tail = stream[tail_start:]
            # Try both author-style and numbered-style; keep whichever yields more.
            author_refs = group_author_references(tail)
            numbered_refs = group_numbered_references(tail)
            if len(numbered_refs) > len(author_refs):
                all_refs.extend(numbered_refs)
            else:
                all_refs.extend(author_refs)
    else:
        # No header found anywhere. Try BOTH numbered and author detection on the
        # last 40% of each stream; keep whichever method yields more references.
        numbered_total: list[str] = []
        author_total: list[str] = []
        for stream in streams:
            tail = stream[max(0, int(len(stream) * 0.4)) :]
            numbered_total.extend(group_numbered_references(tail))
            author_total.extend(group_author_references(tail))
        if len(author_total) >= 10 and len(author_total) >= len(numbered_total):
            all_refs = author_total
            method = "author_tail_fallback"
        elif len(numbered_total) >= 10:
            all_refs = numbered_total
            method = "numbered_fallback"
        else:
            method = "no_refs"

    results: list[tuple[str, str, str]] = []
    seen_local: set[str] = set()
    for ref in all_refs:
        if not is_plausible_reference(ref):
            continue
        key_pair = normalize_key(ref)
        if key_pair is None:
            continue
        key, canonical = key_pair
        if key in seen_local:
            continue
        seen_local.add(key)
        results.append((key, canonical, ref))
    return results, method


def main() -> None:
    if not TEXT_DIR.exists():
        raise SystemExit(f"Text directory not found: {TEXT_DIR}")
    files = sorted(TEXT_DIR.glob("*.txt"))
    print(f"Processing {len(files)} papers...")

    aggregate: dict[str, dict] = defaultdict(
        lambda: {"canonical": "", "papers": set(), "samples": []}
    )
    raw_rows: list[tuple[str, str, str, str]] = []
    papers_with_no_refs: list[str] = []
    method_counts: dict[str, int] = defaultdict(int)

    for f in files:
        results, method = extract_references_from_paper(f)
        method_counts[method] += 1
        if not results:
            papers_with_no_refs.append(f.name)
            print(f"  [{f.name}] 0 references parsed  (method={method})")
            continue
        print(f"  [{f.name}] {len(results)} references parsed  (method={method})")
        for key, canonical, raw in results:
            entry = aggregate[key]
            if not entry["canonical"]:
                entry["canonical"] = canonical
            entry["papers"].add(f.stem)
            if len(entry["samples"]) < 3:
                entry["samples"].append(raw[:300])
            raw_rows.append((f.stem, key, canonical, raw))

    sorted_keys = sorted(
        aggregate.keys(), key=lambda k: (-len(aggregate[k]["papers"]), k)
    )

    with OUT_CSV.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["rank", "key", "canonical", "n_papers", "papers", "sample_reference"])
        for rank, key in enumerate(sorted_keys, 1):
            entry = aggregate[key]
            papers = sorted(entry["papers"])
            sample = entry["samples"][0] if entry["samples"] else ""
            w.writerow(
                [rank, key, entry["canonical"], len(papers), "; ".join(papers), sample]
            )

    with OUT_RAW.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["paper", "key", "canonical", "raw_reference"])
        for row in raw_rows:
            w.writerow(row)

    total_unique = len(sorted_keys)
    total_papers_processed = len(files) - len(papers_with_no_refs)
    multi_cited = sum(1 for k in sorted_keys if len(aggregate[k]["papers"]) >= 2)

    md = []
    md.append("# Reference extraction across supporting papers\n")
    md.append(f"- **Papers scanned:** {len(files)}")
    md.append(
        f"- **Papers with parseable References:** {total_papers_processed}"
    )
    md.append(f"- **Papers with NO references parsed:** {len(papers_with_no_refs)}")
    md.append(f"- **Unique references (firstauthor + year):** {total_unique}")
    md.append(f"- **References cited in 2+ papers:** {multi_cited}")
    md.append("- **Methods used:**")
    for m, n in sorted(method_counts.items(), key=lambda x: -x[1]):
        md.append(f"  - {m}: {n}")
    md.append("")

    if papers_with_no_refs:
        md.append("## Papers where no references could be parsed\n")
        for p in papers_with_no_refs:
            md.append(f"- `{p}`")
        md.append("")

    md.append("## All references (sorted by citation count, desc)\n")
    md.append("| Rank | Citations | Reference | Sample text |")
    md.append("|---:|---:|---|---|")
    for rank, key in enumerate(sorted_keys, 1):
        entry = aggregate[key]
        n = len(entry["papers"])
        canonical = entry["canonical"].replace("|", "\\|")
        sample = (entry["samples"][0] if entry["samples"] else "").replace("|", "\\|")
        sample = sample[:200] + ("…" if len(sample) > 200 else "")
        md.append(f"| {rank} | {n} | {canonical} | {sample} |")

    OUT_MD.write_text("\n".join(md) + "\n", encoding="utf-8")

    print("\nDone.")
    print(f"  Unique references: {total_unique}")
    print(f"  References cited in 2+ papers: {multi_cited}")
    print(f"  Papers without parseable refs: {len(papers_with_no_refs)}")
    for m, n in sorted(method_counts.items(), key=lambda x: -x[1]):
        print(f"    method {m}: {n}")
    print(f"  CSV:  {OUT_CSV}")
    print(f"  MD:   {OUT_MD}")
    print(f"  Raw:  {OUT_RAW}")


if __name__ == "__main__":
    main()
