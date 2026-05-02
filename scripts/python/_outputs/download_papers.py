"""Download open-access PDFs for cited papers, where possible.

Strategy: try Unpaywall API to find open-access versions, then download the PDF
directly. For papers without an OA version, write a placeholder with the DOI
and direct paywalled URL.
"""
from __future__ import annotations

import json
import re
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BIB = ROOT / "manuscript" / "ProjectAlgorithm.bib"
OUT_DIR = ROOT / "master_supporting_docs" / "supporting_papers"
EMAIL = "boenischfelix@wzb.eu"


def parse_bib(text: str) -> list[dict]:
    entries = []
    for raw in re.split(r"\n@", text)[1:]:
        m = re.match(r"^([a-z]+)\{([^,]+),\s*(.*?)\n\}\s*$", raw, re.DOTALL)
        if not m:
            continue
        kind, key, body = m.groups()
        fields = {"_key": key.strip(), "_kind": kind}
        for fm in re.finditer(r"(\w+)\s*=\s*\{(.*?)\}\s*,?\s*(?=\n\s*\w+\s*=|\Z)", body, re.DOTALL):
            fields[fm.group(1).strip().lower()] = re.sub(r"\s+", " ", fm.group(2).strip()).replace("{", "").replace("}", "")
        entries.append(fields)
    return entries


def fetch_unpaywall(doi: str) -> dict | None:
    url = f"https://api.unpaywall.org/v2/{doi}?email={EMAIL}"
    try:
        with urllib.request.urlopen(url, timeout=10) as r:
            return json.loads(r.read().decode())
    except Exception as e:
        return {"_error": str(e)}


def download_pdf(url: str, dest: Path) -> tuple[bool, str]:
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (academic-paper-collector)",
        })
        with urllib.request.urlopen(req, timeout=30) as r:
            data = r.read()
            if len(data) < 5000:
                return False, f"too small ({len(data)} bytes)"
            if data[:4] != b"%PDF":
                return False, "not a PDF (no %PDF header)"
            dest.write_bytes(data)
            return True, f"{len(data) // 1024} KB"
    except Exception as e:
        return False, str(e)


def main() -> None:
    bib_text = BIB.read_text(encoding="utf-8")
    entries = parse_bib(bib_text)

    log = []
    n_dl, n_oa_no_pdf, n_no_oa, n_no_doi = 0, 0, 0, 0

    for e in entries:
        key = e["_key"]
        doi = e.get("doi")
        title_short = (e.get("title", "") or "")[:60]
        if not doi:
            log.append(f"❌ {key:<40} no DOI in bib  | {title_short}")
            n_no_doi += 1
            continue

        unp = fetch_unpaywall(doi)
        if not unp or unp.get("_error"):
            log.append(f"⚠️  {key:<40} unpaywall error: {unp.get('_error', '?') if unp else 'no response'}  | DOI: {doi}")
            time.sleep(0.3)
            continue

        oa_loc = unp.get("best_oa_location")
        if not oa_loc:
            log.append(f"🔒 {key:<40} paywalled (no OA copy)  | DOI: {doi}")
            n_no_oa += 1
            time.sleep(0.3)
            continue

        pdf_url = oa_loc.get("url_for_pdf") or oa_loc.get("url")
        if not pdf_url:
            log.append(f"📄 {key:<40} OA but no PDF URL  | landing: {oa_loc.get('url', 'n/a')}")
            n_oa_no_pdf += 1
            time.sleep(0.3)
            continue

        dest = OUT_DIR / f"{key}.pdf"
        if dest.exists():
            log.append(f"✓ {key:<40} already downloaded ({dest.stat().st_size // 1024} KB)")
            n_dl += 1
            continue

        ok, info = download_pdf(pdf_url, dest)
        if ok:
            log.append(f"✅ {key:<40} downloaded {info}  | from: {pdf_url[:60]}")
            n_dl += 1
        else:
            log.append(f"⚠️  {key:<40} download failed: {info}  | tried: {pdf_url[:60]}")

        time.sleep(0.5)

    summary = [
        "# PDF download log",
        "",
        f"- Downloaded: **{n_dl}**",
        f"- Open-access without retrievable PDF: **{n_oa_no_pdf}**",
        f"- Paywalled (no OA copy found): **{n_no_oa}**",
        f"- No DOI in bib: **{n_no_doi}**",
        "",
        "Source: Unpaywall API (https://unpaywall.org/) for OA discovery.",
        "",
        "## Per-entry log",
        "",
        "```",
    ]
    summary.extend(log)
    summary.append("```")

    (OUT_DIR / "DOWNLOAD_LOG.md").write_text("\n".join(summary), encoding="utf-8")
    print(f"\nSummary: {n_dl} downloaded, {n_no_oa} paywalled, {n_oa_no_pdf} OA-no-PDF, {n_no_doi} no-DOI")
    print(f"Log written to {OUT_DIR / 'DOWNLOAD_LOG.md'}")


if __name__ == "__main__":
    main()
