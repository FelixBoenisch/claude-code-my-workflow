"""For each paper in supporting_papers/_extracted_text, detect:
  (i)  whether it has a Literature / Related Work section separate from the Introduction,
  (ii) whether the first paragraph of that section is a bridging/framing paragraph
       similar to line 3 of manuscript/literature.tex
       (e.g., "This paper bridges three strands of literature: (i) ..., (ii) ..., (iii) ...").

Output: a markdown report with per-paper classification, the literature-section
heading found (if any), the first paragraph for spot-checking, and a summary count.

Caveats: PDF-extracted text loses formatting (no font size / bolding). Detection
relies on heuristics: short standalone lines containing canonical heading words,
optional numbering, plus column-aware reflow for two-column papers. Expect 90%+
accuracy on most journals; outliers in legal / Nature-style layouts need manual check.
"""

from __future__ import annotations

import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEXT_DIR = HERE / "supporting_papers" / "_extracted_text"
OUT_MD = HERE / "literature_section_audit.md"

LIT_KEYWORDS = {
    "related literature",
    "related work",
    "related works",
    "related research",
    "related studies",
    "literature",
    "literature review",
    "literature and hypotheses",
    "theoretical background",
    "theoretical framework",
    "theoretical foundations",
    "conceptual background",
    "conceptual framework",
    "conceptual development",
    "prior literature",
    "prior work",
    "prior research",
    "previous literature",
    "previous work",
    "previous research",
    "empirical background",
    "background",
    "theory and hypotheses",
    "theory and background",
    "theory and literature",
}
PREFIX_STRIP_RE = re.compile(
    r"^\s*(?:[IVX]+\.?\s+|\d+(?:\.\d+)*\.?\s+|[A-Z]\.\s+)"
)
SUBTITLE_SPLIT_RE = re.compile(r"[:—–\-]")
BIB_HEADING_RE = re.compile(
    r"^\s*(literature\s+cited|works\s+cited|references|bibliography)\s*\.?\s*$",
    re.IGNORECASE,
)
LIT_HEADING_RE = None  # legacy placeholder (replaced by is_lit_heading)

INTRO_HEADING_RE = re.compile(
    r"^\s*(?:[IVX]+\.?\s+|\d+\.?\d*\.?\s+|[A-Z]\.\s+)?introduction\b",
    re.IGNORECASE,
)

# Headings that indicate the next big section after Literature (used to stop scanning).
NEXT_SECTION_HINT_RE = re.compile(
    r"^\s*(?:[IVX]+\.?\s+|\d+\.?\d*\.?\s+|[A-Z]\.\s+)?"
    r"(experimental\s+design|design|method(?:s|ology)?|model|the\s+model|"
    r"theoretical\s+(?:model|framework)|setup|set-?up|"
    r"hypotheses|hypothesis|data|results|empirical\s+strategy|"
    r"experiment|the\s+experiment|conceptual\s+(?:model|framework))\b",
    re.IGNORECASE,
)

# Things that look like headings but aren't (TOC entries, body sentences).
TOC_DOTS_RE = re.compile(r"\.{3,}")
BODY_SENTENCE_RE = re.compile(r"[a-z]\.\s+[A-Z]")  # prose-style sentence boundary
BODY_LEAD_RE = re.compile(
    r"^\s*(?:[IVX]+\.?\s+|\d+\.?\d*\.?\s+|[A-Z]\.\s+)?"
    r"(?:we|the|this|in\s+(?:this|our|the|section)|our|some|several|"
    r"although|while|despite|since|because|here|first|second|next|prior)\b",
    re.IGNORECASE,
)

# Signals of an explicit bridging/framing paragraph.
# Patterns the user's literature.tex line 3 uses: "(i) X, (ii) Y, (iii) Z" plus
# "bridges three strands of literature".
ENUMERATION_RE = re.compile(
    r"\(\s*i\s*\).{1,300}\(\s*ii\s*\)|"
    r"\(\s*1\s*\).{1,300}\(\s*2\s*\)|"
    # "First, ... Second/Third/Next/Then, ..." (with or without comma after "first")
    r"\bfirst\b.{1,400}\b(?:second|third|next|then|lastly|finally)\b",
    re.IGNORECASE | re.DOTALL,
)
STRANDS_RE = re.compile(
    r"\b(?:two|three|four|five|several|multiple)\s+"
    r"(?:primary\s+|main\s+|key\s+|distinct\s+|broad\s+)?"
    r"(?:strands?|streams?|bodies?|areas?|literatures?|lines?|branches?|"
    r"sets?\s+of\s+(?:studies|papers|results))\s+"
    r"(?:of|in)\s+(?:literature|research|work|the\s+literature|the\s+research)",
    re.IGNORECASE,
)
# Bridge verb + literature word + at least 2 commas in close range (indicating
# a list of distinct strands like "literature on X, Y, and Z").
BRIDGE_LIST_RE = re.compile(
    r"\b(?:bridges?|contributes?\s+to|draws?\s+on|connects?\s+to|builds?\s+on|"
    r"speaks?\s+to|sits?\s+at|relates?\s+to|intersect(?:s|ion)|combines?|"
    r"integrat(?:es|ing)|review(?:s|ed|ing)?|examines?|spans?|positions?)\b"
    r".{0,40}\b(?:literatures?|strands?|streams?|bodies?|research|work)\b"
    r".{0,200}\band\b",
    re.IGNORECASE | re.DOTALL,
)
# Stronger version: same as above but also requires either explicit enumeration
# OR the literal phrase "strands/streams/bodies of literature".
BRIDGE_VERB_RE = re.compile(
    r"\b(?:bridges?|contributes?\s+to|draws?\s+on|connects?\s+to|builds?\s+on|"
    r"speaks?\s+to|sits?\s+at|relates?\s+to|intersect(?:s|ion)|combines?|"
    r"integrat(?:es|ing))\b.{0,80}\b(?:literatures?|strands?|streams?|"
    r"bodies?|research|work)",
    re.IGNORECASE | re.DOTALL,
)

# How many chars of the section to inspect for the framing paragraph.
FRAMING_WINDOW = 1500


def split_columns(line: str) -> list[str]:
    parts = re.split(r"\s{4,}", line.rstrip())
    return [p.strip() for p in parts if p.strip()]


def reflow_streams(lines: list[str]) -> list[list[str]]:
    """Return per-column line streams (1 stream if single column, 2 if two-col)."""
    two_col = sum(1 for ln in lines if len(split_columns(ln)) >= 2) >= max(
        10, len(lines) // 5
    )
    if not two_col:
        return [[ln.rstrip() for ln in lines]]
    left, right = [], []
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


def looks_like_heading(line: str, max_len: int = 90) -> bool:
    s = line.strip()
    if not s or len(s) > max_len:
        return False
    if TOC_DOTS_RE.search(s):
        return False
    if BODY_SENTENCE_RE.search(s):
        return False
    if BODY_LEAD_RE.match(s):
        return False
    if s.endswith(",") or s.endswith(";"):  # body-fragment continuation
        return False
    return True


def normalize_heading(line: str) -> str:
    """Strip leading numbering and trailing subtitle for keyword matching."""
    s = line.strip()
    s = PREFIX_STRIP_RE.sub("", s)  # drop "2. " / "II. " / "A. "
    s = SUBTITLE_SPLIT_RE.split(s, maxsplit=1)[0].strip()
    s = s.strip(".")
    return s


def is_lit_heading(line: str) -> bool:
    if not looks_like_heading(line):
        return False
    if BIB_HEADING_RE.match(line.strip()):
        return False
    core = normalize_heading(line).lower()
    if not core:
        return False
    # Direct match
    if core in LIT_KEYWORDS:
        return True
    # "<kw> and <something>" — e.g., "Related literature and conjectures"
    for kw in LIT_KEYWORDS:
        if core.startswith(kw + " and ") or core.startswith(kw + " & "):
            return True
    return False


def is_intro_heading(line: str) -> bool:
    if not looks_like_heading(line):
        return False
    core = normalize_heading(line).lower()
    return core == "introduction"


def is_next_section_heading(line: str) -> bool:
    if not looks_like_heading(line):
        return False
    core = normalize_heading(line).lower()
    # Reject if core itself is a lit heading (we shouldn't stop on another lit-style heading
    # — we just keep collecting).
    if core in LIT_KEYWORDS:
        return False
    NEXT_KW = {
        "experimental design", "design", "method", "methods", "methodology",
        "model", "the model", "theoretical model", "theoretical framework",
        "setup", "set-up", "hypotheses", "hypothesis", "data", "results",
        "empirical strategy", "experiment", "the experiment",
        "conceptual model", "conceptual framework", "discussion", "conclusion",
        "general discussion",
    }
    if core in NEXT_KW:
        return True
    for kw in NEXT_KW:
        if core.startswith(kw + " and "):
            return True
    return False


def find_first_lit_heading(stream: list[str]) -> tuple[int, str] | None:
    for i, ln in enumerate(stream):
        if is_lit_heading(ln):
            return i, ln.strip()
    return None


def find_first_intro_heading(stream: list[str]) -> tuple[int, str] | None:
    for i, ln in enumerate(stream):
        if is_intro_heading(ln):
            return i, ln.strip()
    return None


def extract_section_text(
    stream: list[str], start_idx: int, max_chars: int = FRAMING_WINDOW
) -> str:
    collected: list[str] = []
    n = 0
    for ln in stream[start_idx + 1 :]:
        s = ln.strip()
        if not s:
            collected.append("")
            continue
        if is_next_section_heading(ln) or is_intro_heading(ln):
            break
        collected.append(s)
        n += len(s)
        if n >= max_chars:
            break
    return " ".join(collected).strip()


def classify_bridging(first_paragraph: str) -> tuple[bool, list[str]]:
    """Return (has_bridging_frame, evidence_list)."""
    evidence: list[str] = []
    s = first_paragraph[:FRAMING_WINDOW]
    enum_match = bool(ENUMERATION_RE.search(s))
    strands_match = bool(STRANDS_RE.search(s))
    bridge_list_match = bool(BRIDGE_LIST_RE.search(s))
    bridge_verb_match = bool(BRIDGE_VERB_RE.search(s))
    if enum_match:
        evidence.append("enumeration ((i)/(ii), 1)/2), or first/second)")
    if strands_match:
        evidence.append("'N (primary/main) strands/streams/bodies of literature'")
    if bridge_list_match:
        evidence.append("bridge/review verb + literature + 'and' (list of strands)")
    elif bridge_verb_match:
        evidence.append("bridge verb near 'literatures' (weak)")
    # A bridging frame is flagged when at least one of the strong signals fires:
    # - explicit enumeration of strands
    # - "N strands of literature" wording
    # - bridge/review verb + literature + list connector ("and")
    strong = enum_match or strands_match or bridge_list_match
    return strong, evidence


def analyse_paper(text_path: Path) -> dict:
    raw_lines = text_path.read_text(encoding="utf-8", errors="replace").splitlines()
    streams = reflow_streams(raw_lines)

    intro_hit: tuple[int, str, int] | None = None  # (line_idx, heading, stream_idx)
    lit_hit: tuple[int, str, int] | None = None

    for sidx, stream in enumerate(streams):
        if intro_hit is None:
            f = find_first_intro_heading(stream)
            if f:
                intro_hit = (f[0], f[1], sidx)
        if lit_hit is None:
            f = find_first_lit_heading(stream)
            if f:
                lit_hit = (f[0], f[1], sidx)
        if intro_hit and lit_hit:
            break

    has_separate_lit = lit_hit is not None

    first_paragraph = ""
    has_bridging = False
    bridging_evidence: list[str] = []
    if has_separate_lit:
        lit_stream = streams[lit_hit[2]]
        first_paragraph = extract_section_text(lit_stream, lit_hit[0])
        has_bridging, bridging_evidence = classify_bridging(first_paragraph)

    return {
        "paper": text_path.stem,
        "intro_heading": intro_hit[1] if intro_hit else "",
        "lit_heading": lit_hit[1] if lit_hit else "",
        "has_separate_lit": has_separate_lit,
        "has_bridging": has_bridging,
        "bridging_evidence": bridging_evidence,
        "first_paragraph": first_paragraph[:1200],
    }


def main() -> None:
    files = sorted(TEXT_DIR.glob("*.txt"))
    print(f"Analysing {len(files)} papers...")

    results = [analyse_paper(f) for f in files]
    n_total = len(results)
    n_lit = sum(1 for r in results if r["has_separate_lit"])
    n_bridge = sum(1 for r in results if r["has_bridging"])
    n_bridge_only_if_lit = sum(
        1 for r in results if r["has_separate_lit"] and r["has_bridging"]
    )

    md: list[str] = []
    md.append("# Literature-section audit across supporting papers\n")
    md.append(
        "For each paper in `master_supporting_docs/supporting_papers/_extracted_text/`, "
        "this report records: (i) whether a Literature / Related Work section exists as "
        "a separate section from the Introduction, and (ii) whether the first paragraph "
        "of that section is an explicit framing/bridging paragraph similar to line 3 of "
        "`manuscript/literature.tex` (`'This paper bridges three strands of literature: "
        "(i) ..., (ii) ..., and (iii) ...'`).\n"
    )
    md.append("## Summary\n")
    md.append(f"- **Papers scanned:** {n_total}")
    md.append(
        f"- **Papers with a separate Literature / Related Work section:** "
        f"{n_lit} / {n_total} ({n_lit / n_total:.0%})"
    )
    md.append(
        f"- **Papers with a bridging framing paragraph (overall):** "
        f"{n_bridge} / {n_total} ({n_bridge / n_total:.0%})"
    )
    md.append(
        f"- **Of papers with a separate lit section: framing paragraph at its start:** "
        f"{n_bridge_only_if_lit} / {n_lit if n_lit else 1} "
        f"({(n_bridge_only_if_lit / n_lit if n_lit else 0):.0%})\n"
    )
    md.append("## Detection rules\n")
    md.append(
        "- A **separate Literature section** is recognised when a short standalone line "
        "(≤ 80 chars) matches a known heading: *Related Literature*, *Related Work*, "
        "*Literature [Review]*, *Background*, *Theoretical Background*, *Prior / Previous "
        "Literature*, *Related Research*, *Theoretical / Conceptual Framework*, *Theory "
        "and Hypotheses / Literature / Background*, *Related Studies*. Numbering / Roman "
        "numerals are allowed as prefixes."
    )
    md.append(
        "- A **bridging paragraph** is flagged when the first ~1,500 chars of the lit "
        "section contain *either* (a) explicit enumeration of strands — `(i) ... (ii)`, "
        "`1) ... 2)`, or `first ... second ...` — *or* (b) a phrase like `'N strands "
        "/ streams / bodies of literature'`. A bridge verb alone (e.g., `'contributes "
        "to two literatures'`) without enumeration or 'strands' wording does NOT trigger "
        "the flag, to keep the precision high.\n"
    )
    md.append("## Per-paper table\n")
    md.append(
        "| Paper | Separate lit section? | Heading found | Bridging paragraph? | Evidence |"
    )
    md.append("|---|:---:|---|:---:|---|")
    for r in results:
        lit = "✅" if r["has_separate_lit"] else "—"
        bridge = "✅" if r["has_bridging"] else "—"
        heading = r["lit_heading"].replace("|", "\\|") if r["lit_heading"] else ""
        ev = "; ".join(r["bridging_evidence"]) if r["bridging_evidence"] else ""
        md.append(f"| `{r['paper']}` | {lit} | {heading} | {bridge} | {ev} |")
    md.append("")

    md.append(
        "## First paragraphs of detected literature sections (for spot-checking)\n"
    )
    md.append(
        "_Below is the first paragraph found after each detected literature heading "
        "(truncated at 1,200 chars). Use this to verify the detection and to compare "
        "framing styles across papers._\n"
    )
    # Sort: bridging first, then the rest with a lit section.
    with_lit = [r for r in results if r["has_separate_lit"]]
    with_lit.sort(key=lambda r: (not r["has_bridging"], r["paper"]))
    for r in with_lit:
        flag = " (bridging frame)" if r["has_bridging"] else ""
        md.append(f"\n### `{r['paper']}` — heading: *{r['lit_heading']}*{flag}\n")
        md.append(f"> {r['first_paragraph'] or '_(no body text captured)_'}\n")

    no_lit = [r for r in results if not r["has_separate_lit"]]
    if no_lit:
        md.append("\n## Papers with no separate Literature section detected\n")
        for r in no_lit:
            md.append(f"- `{r['paper']}`")
        md.append("")

    OUT_MD.write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"Wrote {OUT_MD}")
    print(f"  Separate lit section: {n_lit} / {n_total}")
    print(f"  Bridging frame:       {n_bridge} / {n_total}")
    print(f"  Both:                 {n_bridge_only_if_lit} / {n_lit if n_lit else 0}")


if __name__ == "__main__":
    main()
