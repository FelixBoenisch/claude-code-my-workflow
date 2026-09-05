import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
inventory = json.loads((HERE / 'inventory.json').read_text(encoding='utf-8-sig'))
records = []
for name in ['core', 'algorithms', 'additional', 'root']:
    records.extend(json.loads((HERE / f'{name}.json').read_text(encoding='utf-8-sig')))
for record in records:
    record['verified_citation'] = record['verified_citation'].replace('?.', '?')
    if isinstance(record.get('limitations'), list):
        record['limitations'] = ' '.join(record['limitations'])
bykey = {r['key']: r for r in records}
original = {r['key']: r for r in inventory['entries']}
assert len(records) == len(bykey) == 106
assert set(bykey) == set(original)
assert sum(r['cited'] for r in records) == 54
bib = HERE.parents[1] / 'manuscript' / 'ProjectAlgorithm.bib'
assert hashlib.sha256(bib.read_bytes()).hexdigest() == inventory['bib_sha256']

def cell(value):
    if value is None:
        return 'Remove field'
    return str(value).replace('|', r'\|').replace('\r', '').replace('\n', ' ')

def code(value, missing=False):
    if value is None:
        return 'Absent' if missing else 'Remove field'
    return '`' + cell(value).replace('`', "'") + '`'

def links(record):
    return '; '.join(f"[{cell(s['title'])}]({s['url']})" for s in record['sources']) or 'No matching scholarly source located.'

def optional(change):
    return 'optional' in change.get('category', '').lower() or 'optional' in change['reason'].lower()

def row_changes(record, kind):
    return [c for c in record['changes'] if optional(c) == (kind == 'optional')]

updated = [r for r in records if r['changes']]
stats = {
    'all_entries': len(records), 'cited': 54, 'uncited': 52,
    'entries_with_proposals_including_optional': len(updated),
    'cited_entries_with_proposals_including_optional': sum(r['cited'] for r in updated),
    'bibliography_sha256': inventory['bib_sha256'],
}
(HERE / 'audit.json').write_text(json.dumps({'scope': stats, 'entries': sorted(records, key=lambda r: r['key'])}, ensure_ascii=False, indent=2), encoding='utf-8')

intro = '''# Bibliography audit: proposed changes for review

Audit date: **5 September 2026**. **No bibliography or manuscript changes have been made.**

The active manuscript is `paper/manuscript/main.tex`, which uses `paper/manuscript/ProjectAlgorithm.bib`. Its 13 active source files cite **54 distinct records**; the bibliography contains **106 records**, including **52 not currently cited**. Citation extraction excluded commented text and followed the active input files. The source citation set agrees exactly with the existing `main.aux`. There are no missing citation keys, duplicate keys, or duplicated DOI strings.

Every bibliography entry was reviewed individually for authors and order, title, venue, year, volume, issue, pages or article number, DOI, and publication status, as applicable. Evidence comes from publisher records and PDFs, author institutional deposits, official working-paper repositories, and publisher-supplied bibliographic metadata. Where direct access failed, the ledger specifies the substitute evidence and remaining limits. A working-paper status means that no journal version was located, not a guarantee that no unindexed publication exists.

## Principal proposed changes

### Currently cited records

1. **Freer, Friedman, and Weidenholzer:** replace the 2024 working-paper citation with the published **2026** article in *Games and Economic Behavior*, **159: 56–70**, DOI **10.1016/j.geb.2026.05.012**. Change entry type to `article`, add final publication fields, and remove the obsolete preprint note. Keep the citation key, so LaTeX references continue to resolve. [Publisher](https://www.sciencedirect.com/science/article/pii/S0899825626000898); [Essex record](https://repository.essex.ac.uk/43353/).
2. **Sunstein and Gaffe:** correct **290–319 → 290–317**, add issue **1** and DOI **10.52214/stlr.v26i1.13339**, add the publisher URL, and clear the verification flag. **Year requires a choice:** the journal PDF is labelled **Fall 2024**, while its website labels the issue **2025** and supplies a 2025 citation. Retain 2024 pending review; using 2025 to follow the website is also defensible. [Publisher citation](https://journals.library.columbia.edu/index.php/stlr/article/view/13339); [PDF](https://journals.library.columbia.edu/index.php/stlr/article/download/13339/6543/36781).
3. **Beckers et al.:** correct the second author's BibTeX name from `Cavalcante Siebert, Luciano` to **`Siebert, Luciano Cavalcante`**. The surname is Siebert. Issue **1** can also be added. [Publisher](https://www.nature.com/articles/s41598-022-19876-0); [TU Delft](https://research.tudelft.nl/en/publications/drivers-of-partially-automated-vehicles-are-blamed-for-crashes-th/).
4. **Tontrup and Sprigman:** retain working-paper status and the 2025 citation year; correct the note to distinguish **written 6 October 2025**, **posted 13 November 2025**, and **revised 27 June 2026**. The existing posting date is wrong. The SSRN DOI can be added. [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5696827).
5. **Lemley and Casey; Buiten, de Streel, and Peitz:** their current volume and pagination are correct. Remove the resolved **CONFIRM** notes, which currently print in the bibliography. Link Lemley to the published journal page; add Buiten's DOI **10.1016/j.clsr.2023.105794**. [Lemley journal record](https://lawreview.uchicago.edu/print-archive/remedies-robots); [Buiten institutional publication record](https://researchportal.unamur.be/en/publications/the-law-and-economics-of-ai-liability/).
6. **EU AI Act:** add its official publication locator **OJ L, 2024/1689, 12 July 2024**, the official ELI URL, and clear the verification flag. The original 2024 act remains a valid citation. [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng).
7. **Tacconelli et al.:** retain the published online/ahead-of-print citation; no final volume or pagination was located. Correct the internal annotation's analyzed sample size **3,808 → 2,808** (248 + 1,202 + 1,358). This annotation is not printed by the current style. [Publisher-supplied PubMed record](https://pubmed.ncbi.nlm.nih.gov/42242875/).
8. **Completions and consistency:** add the verified missing DOIs for **Fiorina, Gawn and Innes, Kandul and Kirchkamp, and Dawes**, plus issue **4** for **Santoni de Sio and Mecacci**. Optional changes include full first names for **Bartling and Fischbacher**, a more precise corporate author for the **2019 European Commission report**, and consistent name/journal typography. Clear **Bigman et al.**'s author-verification flag; **Desman Wilson** is correct. Exact values and sources appear below.

### Records not currently cited

The clearest corrections are **Roman → Rouven Litterscheidt**, **Huck et al.'s DOI → 10.1016/j.ijindorg.2003.10.005**, and **Freisinger and Schneider's DOI → 10.1016/j.emj.2024.10.004**, with its final **2025, 43(6): 958–969** publication fields replacing the erroneous article number. Final volume/article or issue fields should be completed for **Tsumura and Yamada, Salatino et al., Blunden and Steffel, Arnestad et al., and Jolly et al.** Bockstedt and Buckman and Kormylo et al. can be harmonized to the **2026** *Management Science* issue year; INFORMS also exposes their 2025 online-year citations, so this is a convention choice. Exact changes, including optional DOIs and resolved flags, are listed below.

## Working-paper and recent-publication status

| Record | Status found | Planned treatment |
|---|---|---|
| Freer, Friedman, and Weidenholzer | Published in *Games and Economic Behavior* 159 (2026), 56–70 | Replace working-paper metadata with journal metadata. |
| Chevrier and Teixeira | GREDEG 2024-04; revised September 2024 | Keep working-paper citation. |
| Tontrup and Sprigman | SSRN 5696827; revised June 2026 | Keep working-paper status; correct posting/revision note. |
| Irlenbusch | ECONtribute Discussion Paper 417, June 2026 | Keep current citation. |
| Ivanova-Stenzel and Tolksdorf | Rationality and Competition Discussion Paper 558, December 2025 | Keep current series version; earlier SSRN version is also available. |
| Normann et al. | arXiv:2510.27636, October 2025 | Keep current identified preprint version; optional repository DOI. |
| Weitzner | Author still lists it under Working Papers; arXiv v3 July 2024 | Keep status and year; correct subject class `econ.GN` to `econ.TH`; optional repository DOI. |
| Tacconelli et al. | Journal article online 4 June 2026; still indexed ahead of print | Keep current authors/title/year/DOI; do not invent volume or pages. |

The individual ledger below supplies direct sources for each status.

## Matters requiring an author decision

- **Sunstein's year:** 2024 in the journal PDF versus 2025 on the journal website. The default proposal retains 2024 pending review. The page correction and DOI are certain.
- **`stein_dont_2020`:** no matching scholarly source was located. The uncited record already flags possible fabrication. Proposed action is to quarantine it outside the active bibliography while preserving the original record; no invented replacement.
- **`goldbach_geht_2019`, `kurtzberg_attribution_2004`, and `liu_when_2021`:** the papers currently described can be verified, but existing annotations say earlier sessions substituted them for differently titled or authored works. Correct metadata does not resolve which source was originally intended. Retain those identity questions until you identify the intended works.
- **Issue-year conventions:** preserve final issue years throughout; this supports 2026 for the two INFORMS records and retaining the already correct 2026 dates for Dargnies, Jolly, Hüholt, and Tsumura. Sunstein's conflicting publisher issue labels require separate judgment. The 2005 imprint year for Bolton and Dewatripont remains appropriate despite a December 2004 release date.
- **Correction notices:** Salatino's publisher corrected author indexing in 2025; the current `Lo Bue, Salvatore` is already right. Ismagilova's publisher links a 2026 ethics-statement erratum; no bibliographic change is indicated, and the full erratum text was not independently retrieved. These notices do not justify changing the original article's DOI or year.

## Exact field changes for review

Changes below are proposals only. “Absent” means the field is not currently present. “Remove field” removes only the stated field. All citation keys would stay unchanged. Article numbers are retained in `pages`, matching the existing bibliography and its `aer` style. No unused verified record is proposed for deletion merely because it is unused.
'''

parts = [intro]
for cited, group in [(True, 'Currently cited'), (False, 'Not currently cited')]:
    for kind in ['standard', 'optional']:
        title = 'Corrections, completions, and resolved flags' if kind == 'standard' else 'Optional enrichments and formatting'
        parts += [f'### {group}: {title}\n', '| Citation key | Field | Current | Proposed | Reason | Evidence |', '|---|---|---|---|---|---|']
        for record in sorted(records, key=lambda r: r['key']):
            if record['cited'] != cited:
                continue
            changes = row_changes(record, kind)
            for index, change in enumerate(changes):
                source = links(record) if index == 0 else 'Same sources above.'
                parts.append(f"| `{record['key']}` | `{change['field']}` | {code(change['old'], True)} | {code(change['new'])} | {cell(change['reason'])} | {source} |")
        parts.append('')

parts += ['## Individual verification ledger\n', 'This ledger covers all 106 records, including those with no proposed changes. The exact-field tables above control the proposed edits; dates and alternative versions discussed below are not automatic replacements.\n']
for cited, title in [(True, 'All 54 currently cited records'), (False, 'All 52 records not currently cited')]:
    parts += [f'### {title}\n', '| Citation key | Citation and verification result | Sources | Qualifications |', '|---|---|---|---|']
    for record in sorted(records, key=lambda r: r['key']):
        if record['cited'] != cited:
            continue
        result = record['status'].replace('_', ' ')
        qual = record.get('limitations') or 'No material bibliographic discrepancy identified beyond listed proposals.'
        parts.append(f"| `{record['key']}` | {cell(record['verified_citation'])}<br>**Result:** {cell(result)}. | {links(record)} | {cell(qual)} |")
    parts.append('')

parts += [
    '## Integrity and review boundary\n',
    f"The bibliography is unchanged: its SHA-256 digest is `{inventory['bib_sha256']}` before and after this audit. Manuscript files were read only. The audit produced only review materials in this directory. No compilation was required because no manuscript or bibliography edits were made. Existing `main.bbl` was inspected to confirm that the unresolved `note` fields print in the references.\n",
    'Bibliographic verification does not establish whether each paper supports every substantive claim in the manuscript. Source-identity doubts and inaccessible details are stated explicitly above. Existing Zotero attachment paths, abstracts, and past access dates are not independently verifiable publication metadata and are not proposed for bulk cleanup.\n',
    'After your review, only the agreed changes should be applied, followed by a BibTeX/LaTeX rebuild to check the printed author names, dates, and references.\n',
    'Supporting files: [machine-readable complete audit](audit.json), [citation inventory](inventory.json), [core evidence](core.md), [algorithm papers evidence](algorithms.md), [additional papers evidence](additional.md).\n',
]
(HERE / 'REPORT.md').write_text('\n'.join(parts), encoding='utf-8')
print(json.dumps(stats, indent=2))
print('Wrote REPORT.md and audit.json. Bibliography digest unchanged.')
