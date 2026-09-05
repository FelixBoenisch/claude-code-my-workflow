"""Replace the review report with an implementation record; archive the review."""
import hashlib
import json
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
audit = json.loads((HERE / 'audit.json').read_text(encoding='utf-8'))
applied = json.loads((HERE / 'implemented_changes.json').read_text(encoding='utf-8'))
build = json.loads((HERE / 'build_verification.json').read_text(encoding='utf-8'))
records = {r['key']: r for r in audit['entries']}
changes = defaultdict(list)
for change in applied['changes']:
    changes[change['key']].append(change)
cited_changed = sum(records[key]['cited'] for key in changes if key != 'stein_dont_2020')
assert applied['after_sha256'] == hashlib.sha256((HERE.parents[1] / 'manuscript/ProjectAlgorithm.bib').read_bytes()).hexdigest()
assert not build['bibtex_warnings'] and not build['undefined_citations']

def cell(value):
    if value is None:
        return '(absent / removed)'
    return str(value).replace('|', '\\|').replace('\r', '').replace('\n', '<br>')

lines = [
    '# Bibliography audit: implemented changes', '',
    'Completed **5 September 2026**, following the author\'s review and instructions. ', '',
    f'Updated **38 existing records** ({cited_changed} currently cited), deleted **`stein_dont_2020`**, and rebuilt the manuscript. '
    'The bibliography now contains **105 entries**; all **54 cited keys** resolve. '
    'The manuscript\'s `.tex` source files were preserved.', '',
    '## Author decisions implemented', '',
    '- **Sunstein and Gaffe:** use **2025**, January, *Science and Technology Law Review*, **26(1): 290-317**, '
    'DOI **10.52214/stlr.v26i1.13339**, following the [journal website](https://journals.library.columbia.edu/index.php/stlr/article/view/13339). '
    'The existing citation key `sunstein_anatomy_2024` is retained so source citations continue to work.',
    '- **Stein:** deleted `stein_dont_2020`. The original entry remains available in the audit and the bibliography backup.',
    '- **Goldbach, Kurtzberg, and Liu:** confirmed uncited and preserved byte-for-byte; no action is needed on their identity annotations for the current manuscript.',
    '- **Issue years:** applied the agreed final-issue convention, including **2026** for Bockstedt/Buckman and Kormylo et al., '
    '**2025** for Freisinger/Schneider, and the published **2026** Freer/Friedman/Weidenholzer article.',
    '- Applied the reviewed corrections, metadata completions, optional enrichments, and removal of resolved verification notes.', '',
    '## Ismagilova erratum retrieved', '',
    'The complete notice was found appended to the existing supporting article PDF and extracted as '
    '[ismagilova_ethics_erratum_2026.pdf](ismagilova_ethics_erratum_2026.pdf). All three pages were rendered and visually inspected. '
    'The source PDF was preserved.', '',
    '**Item 7**, across erratum pages **1-2**, adds the omitted ethics and informed-consent statement for Ismagilova and Ploner. '
    'It says formal ethics approval was not required under the University of Trento guidelines for anonymous adult participants facing no identifiable risk; '
    'Prolific participation was voluntary, study information was provided before participants opted in, and withdrawal was permitted. '
    'It lists no revisions to their results, data, or analyses. The current supporting article already includes this statement on printed page 9.', '',
    'The notice is *Computers in Human Behavior: Artificial Humans*, **8 (2026), 100317**, '
    'DOI [10.1016/j.chbah.2026.100317](https://doi.org/10.1016/j.chbah.2026.100317). '
    'The original article remains **2025, volume 4, article 100147**, with its original DOI. '
    'No erratum entry was added to the manuscript bibliography because it is not cited.', '',
    '[Full statement, source links, and retrieval evidence](ISMAGILOVA_ERRATUM_RETRIEVAL.md).', '',
    '## Rendering adjustments', '',
    'Three small BibTeX adaptations preserve the verified metadata in the existing `aer` bibliography style:', '',
    '- Heaton\'s article locator is stored as `note = {Article No. 11.}` because the style does not support an `articleno` field.',
    '- The compound surname is protected as `{{Santoni de Sio}, Filippo and Mecacci, Giulio}`. '
    'Without the inner braces, BibTeX printed "de Sio, Filippo Santoni" and sorted the reference under D. '
    'The protected form follows the [publisher citation](https://link.springer.com/article/10.1007/s13347-021-00450-x).',
    '- The EU Act\'s `howpublished` ends in `12 July`; the retained `year = {2024}` supplies the year once in the rendered locator. '
    'This avoids printing "12 July 2024 2024" while preserving the complete date.', '',
    'The existing style does not print DOI, URL, or ISBN fields; those enrichments are retained in the bibliography file.', '',
    '## Verification', '',
    '- Independent comparison against the reviewed audit, the user\'s decisions, and the original bibliography: **passed**.',
    '- BibTeX syntax, unique entry keys, revised field values, and all 54 cited keys: **passed**.',
    '- `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`: **all successful**, with no BibTeX warnings or undefined citations.',
    '- Final reference pages 27-31 were visually checked; names, ordering, dates, and page layout are correct.',
    '- Two pre-existing non-bibliographic LaTeX warnings remain: marginal-note geometry and the layouts package scale setting.', '',
    '[Independent QA](implementation_qa.md) | [Build evidence](build_verification.json) | '
    '[Machine-readable change ledger](implemented_changes.json).', '',
    '## Implemented field changes', '',
    'The table gives the final stored values. Citation keys were preserved except for the approved Stein deletion. '
    'The [original review report](REPORT.before-implementation.md) retains the verification evidence for every one of the original 106 entries.', '',
    '| Citation key | Cited | Field | Before | Implemented |',
    '|---|---|---|---|---|',
]
for key in sorted(changes):
    cited = 'Yes' if records[key]['cited'] else 'No'
    for change in changes[key]:
        field = change['field']
        old = 'Complete original record' if field == 'entry' else cell(change['old'])
        new = 'Deleted' if field == 'entry' else cell(change['new'])
        lines.append(f'| `{key}` | {cited} | `{field}` | {old} | {new} |')
lines += [
    '', '## Preserved originals', '',
    '- [Original bibliography snapshot](ProjectAlgorithm.bib.before-approved-changes).',
    '- [Review report before implementation](REPORT.before-implementation.md).',
    '- The pre-build manuscript PDF is preserved at `build/main.before-bibliography-update.pdf`.',
    '', f'Original bibliography SHA-256: `{applied["before_sha256"]}`.  ',
    f'Final bibliography SHA-256: `{applied["after_sha256"]}`.', '',
]
report = HERE / 'REPORT.md'
archive = HERE / 'REPORT.before-implementation.md'
if not archive.exists():
    assert report.read_text(encoding='utf-8').startswith('# Bibliography audit: proposed changes for review')
    archive.write_bytes(report.read_bytes())
report.write_text('\n'.join(lines), encoding='utf-8')
print(f'Wrote implementation report: {len(applied["changes"])} field/deletion changes; {cited_changed} cited records updated.')
