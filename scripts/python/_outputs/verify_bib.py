"""Verify every bib entry against Crossref API.

Reads ProjectAlgorithm.bib, extracts (key, title, authors, journal, year, doi),
queries Crossref for each DOI, and reports mismatches.
"""
from __future__ import annotations

import json
import re
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BIB = ROOT / "manuscript" / "ProjectAlgorithm.bib"
OUT = ROOT / "master_supporting_docs" / "supporting_papers" / "VERIFICATION.md"


def parse_bib(text: str) -> list[dict]:
    entries = []
    for raw in re.split(r"\n@", text)[1:]:
        m = re.match(r"^([a-z]+)\{([^,]+),\s*(.*?)\n\}\s*$", raw, re.DOTALL)
        if not m:
            continue
        kind, key, body = m.groups()
        fields = {}
        for fm in re.finditer(r"(\w+)\s*=\s*\{(.*?)\}\s*,?\s*(?=\n\s*\w+\s*=|\Z)", body, re.DOTALL):
            fname = fm.group(1).strip().lower()
            fval = re.sub(r"\s+", " ", fm.group(2).strip())
            fval = fval.replace("{", "").replace("}", "")
            fields[fname] = fval
        fields["_key"] = key.strip()
        fields["_kind"] = kind
        entries.append(fields)
    return entries


def fetch_crossref(doi: str) -> dict | None:
    if not doi:
        return None
    url = f"https://api.crossref.org/works/{doi}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "academic-bib-verify/1.0 (mailto:boenischfelix@gmail.com)"})
        with urllib.request.urlopen(req, timeout=10) as r:
            return json.loads(r.read().decode())
    except Exception as e:
        return {"_error": str(e)}


def crossref_brief(cr: dict) -> dict:
    if not cr or cr.get("_error"):
        return {"error": cr.get("_error", "no response") if cr else "no response"}
    msg = cr.get("message", {})
    title = (msg.get("title") or [""])[0]
    authors = msg.get("author", [])
    author_str = "; ".join(f"{a.get('family', '?')}, {a.get('given', '?')}" for a in authors)
    container = (msg.get("container-title") or [""])[0]
    issued = msg.get("issued", {}).get("date-parts", [[None]])[0][0]
    volume = msg.get("volume")
    issue = msg.get("issue")
    page = msg.get("page")
    return {
        "title": title,
        "authors": author_str,
        "journal": container,
        "year": issued,
        "volume": volume,
        "issue": issue,
        "pages": page,
    }


def compare(local: dict, remote: dict) -> list[str]:
    if remote.get("error"):
        return [f"crossref-error: {remote['error']}"]
    diffs = []
    # Title
    lt = (local.get("title") or "").lower()
    rt = (remote.get("title") or "").lower()
    if lt and rt and not (lt in rt or rt in lt):
        # Allow loose match
        lt_words = set(re.findall(r"\w+", lt))
        rt_words = set(re.findall(r"\w+", rt))
        overlap = len(lt_words & rt_words) / max(len(lt_words | rt_words), 1)
        if overlap < 0.6:
            diffs.append(f"title: local='{local.get('title', '')[:80]}' vs cr='{remote.get('title', '')[:80]}'")
    # Year
    if local.get("year") and remote.get("year"):
        try:
            ly, ry = int(local["year"]), int(remote["year"])
            if abs(ly - ry) > 1:  # allow 1-year tolerance for online vs print
                diffs.append(f"year: local={ly} vs cr={ry}")
        except Exception:
            pass
    # Volume
    if local.get("volume") and remote.get("volume") and str(local["volume"]).strip() != str(remote["volume"]).strip():
        diffs.append(f"volume: local={local['volume']} vs cr={remote['volume']}")
    # First-author family name
    la = local.get("author", "")
    if la and remote.get("authors"):
        first_local = re.split(r"\s+and\s+|,", la)[0].strip().lower()
        first_remote = remote["authors"].split(";")[0].split(",")[0].strip().lower()
        # Strip LaTeX accents
        first_local = re.sub(r"\\[a-z]+|[\{\}'\"]", "", first_local).strip().lower()
        first_remote = re.sub(r"[\{\}'\"]", "", first_remote).strip().lower()
        if first_local and first_remote and first_local != first_remote:
            diffs.append(f"first-author family: local='{first_local}' vs cr='{first_remote}'")
    return diffs


def main() -> None:
    bib_text = BIB.read_text(encoding="utf-8")
    entries = parse_bib(bib_text)

    lines = ["# Bib verification report\n"]
    lines.append(f"**Date:** 2026-05-02 \n**Source:** Crossref API (`api.crossref.org/works/<doi>`)  \n**Total entries:** {len(entries)}\n")
    lines.append("Each entry below: local bib metadata vs Crossref metadata. Differences flagged.\n")
    lines.append("---\n")

    n_doi, n_no_doi, n_match, n_diff, n_err = 0, 0, 0, 0, 0
    sections = []

    for e in entries:
        key = e["_key"]
        doi = e.get("doi")
        section = [f"\n### `{key}`\n"]
        section.append(f"- **kind:** `{e['_kind']}`")
        section.append(f"- **local title:** {e.get('title', '—')[:200]}")
        section.append(f"- **local authors:** {e.get('author', '—')[:200]}")
        section.append(f"- **local journal:** {e.get('journal', '—')}")
        section.append(f"- **local year/vol/pages:** {e.get('year', '—')} / {e.get('volume', '—')} / {e.get('pages', '—')}")
        if doi:
            section.append(f"- **DOI:** `{doi}`")
            n_doi += 1
            cr = fetch_crossref(doi)
            brief = crossref_brief(cr)
            if "error" in brief:
                section.append(f"- ❌ **Crossref error:** {brief['error']}")
                n_err += 1
            else:
                diffs = compare(e, brief)
                section.append(f"- **CR title:** {brief['title'][:200]}")
                section.append(f"- **CR authors:** {brief['authors'][:200]}")
                section.append(f"- **CR journal:** {brief['journal']}")
                section.append(f"- **CR year/vol/pages:** {brief['year']} / {brief['volume']} / {brief['pages']}")
                if diffs:
                    section.append(f"- ⚠️ **DIFFS:** {'; '.join(diffs)}")
                    n_diff += 1
                else:
                    section.append("- ✅ MATCH")
                    n_match += 1
            time.sleep(0.2)  # be polite to Crossref
        elif e.get("url"):
            section.append(f"- **URL:** {e.get('url')}")
            section.append("- ⏭️ no DOI; cannot verify via Crossref")
            n_no_doi += 1
        else:
            section.append("- ⏭️ no DOI and no URL; cannot verify")
            n_no_doi += 1
        sections.append("\n".join(section))

    summary = (
        f"## Summary\n\n"
        f"- Entries with DOI: {n_doi} (matched {n_match}, diff {n_diff}, error {n_err})\n"
        f"- Entries without DOI: {n_no_doi}\n"
    )
    OUT.write_text("\n".join(lines) + summary + "\n".join(sections), encoding="utf-8")
    print(f"Wrote {OUT}")
    print(f"Matched: {n_match} / DOI'd: {n_doi}, Diffs: {n_diff}, Errors: {n_err}, No-DOI: {n_no_doi}")


if __name__ == "__main__":
    main()
