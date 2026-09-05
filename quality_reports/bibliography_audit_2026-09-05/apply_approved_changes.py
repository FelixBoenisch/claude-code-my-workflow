"""Apply the reviewed bibliography audit, preserving unrelated source text."""
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
MANUSCRIPT = HERE.parents[1] / 'manuscript'
BIB = MANUSCRIPT / 'ProjectAlgorithm.bib'
AUDIT = json.loads((HERE / 'audit.json').read_text(encoding='utf-8'))


def escaped(text, pos):
    count = 0
    while pos > 0 and text[pos - 1] == '\\':
        count += 1
        pos -= 1
    return count % 2 == 1


def closing_brace(text, start):
    depth = 1
    for pos in range(start + 1, len(text)):
        if not escaped(text, pos):
            if text[pos] == '{':
                depth += 1
            elif text[pos] == '}':
                depth -= 1
                if depth == 0:
                    return pos
    raise ValueError('Unbalanced braces')


def entries(text):
    found = {}
    for match in re.finditer(r'(?m)^@(\w+)\{([^,]+),', text):
        end = closing_brace(text, text.index('{', match.start())) + 1
        key = match.group(2)
        assert key not in found
        found[key] = (match.start(), end, text[match.start():end])
    return found


def field_spans(entry):
    fields = {}
    previous_end = 0
    for match in re.finditer(r'(?m)^([ \t]*)(\w+)\s*=\s*', entry):
        if match.start() < previous_end:
            continue
        start = match.end()
        if entry[start] == '{':
            end = closing_brace(entry, start) + 1
            value = entry[start + 1:end - 1]
        elif entry[start] == '"':
            end = start + 1
            while entry[end] != '"' or escaped(entry, end):
                end += 1
            end += 1
            value = entry[start + 1:end - 1]
        else:
            end = start
            while entry[end] not in ',\r\n':
                end += 1
            value = entry[start:end].strip()
        suffix = end
        if entry[suffix:suffix + 1] == ',':
            suffix += 1
        while entry[suffix:suffix + 1] in (' ', '\t'):
            suffix += 1
        if entry[suffix:suffix + 2] == '\r\n':
            suffix += 2
        elif entry[suffix:suffix + 1] == '\n':
            suffix += 1
        fields[match.group(2)] = (match.start(), start, end, suffix, value, match.group(1))
        previous_end = end
    return fields


def apply():
    before = BIB.read_bytes()
    expected_hash = AUDIT['scope']['bibliography_sha256']
    assert hashlib.sha256(before).hexdigest() == expected_hash, 'Bibliography changed since review; inspect before applying.'
    text = before.decode('utf-8')
    newline = '\r\n' if '\r\n' in text else '\n'
    original = entries(text)
    operations = []
    applied = []
    for record in AUDIT['entries']:
        key = record['key']
        start, end, entry = original[key]
        if key == 'stein_dont_2020':
            operations.append((start, end, ''))
            applied.append({'key': key, 'field': 'entry', 'old': entry, 'new': None,
                            'reason': 'User explicitly approved deletion.'})
            continue
        changes = [dict(change) for change in record['changes']]
        if key == 'european_union_ai_act_2024':
            for change in changes:
                if change['field'] == 'howpublished':
                    change['new'] = 'Official Journal of the European Union, L, 2024/1689, 12 July'
                    change['reason'] = 'Complete official locator; aer.bst appends the year field, avoiding a duplicated 2024.'
        if key == 'santoni_de_sio_four_2021':
            changes.append({
                'field': 'author',
                'old': 'Santoni de Sio, Filippo and Mecacci, Giulio',
                'new': '{Santoni de Sio}, Filippo and Mecacci, Giulio',
                'reason': 'Protect the compound surname so aer.bst renders and sorts Santoni de Sio correctly.',
                'source': 'https://link.springer.com/article/10.1007/s13347-021-00450-x',
            })
        if key == 'sunstein_anatomy_2024':
            for change in changes:
                if change['field'] == 'journal':
                    change['new'] = 'Science and Technology Law Review'
                    change['reason'] = 'User chose journal website metadata; use website journal title.'
            changes += [
                {'field': 'year', 'old': '2024', 'new': '2025', 'reason': 'User explicitly chose 2025 from journal website.'},
                {'field': 'month', 'old': None, 'new': 'jan', 'reason': 'Journal website gives publication date 31 January 2025.'},
            ]
        if key == 'heaton_social_2023':
            for change in changes:
                if change['field'] == 'articleno':
                    change['field'] = 'note'
                    change['new'] = 'Article No. 11.'
                    change['reason'] = 'Preserve verified ACM article locator in the aer-supported note field.'
        for change in changes:
            field = change['field']
            if field == 'entry_type':
                assert entry.startswith('@' + change['old'] + '{')
                entry = '@' + change['new'] + entry[entry.index('{'):]
            else:
                fields = field_spans(entry)
                current = fields.get(field)
                assert (current[4] if current else None) == change['old'], (key, field, current)
                new = change['new']
                if current:
                    a, b, c, d, _, indent = current
                    if new is None:
                        entry = entry[:a] + entry[d:]
                    else:
                        value = new if field == 'month' else '{' + new + '}'
                        entry = entry[:b] + value + entry[c:]
                elif new is not None:
                    indent = next(iter(fields.values()))[5] if fields else '    '
                    value = new if field == 'month' else '{' + new + '}'
                    if fields:
                        last_end = max(span[2] for span in fields.values())
                        if entry[last_end:last_end + 1] != ',':
                            entry = entry[:last_end] + ',' + entry[last_end:]
                    entry = entry[:-1] + indent + field + ' = ' + value + ',' + newline + '}'
            applied.append({'key': key, **change})
        if entry != original[key][2]:
            operations.append((start, end, entry))
    for start, end, replacement in sorted(operations, reverse=True):
        text = text[:start] + replacement + text[end:]
    updated = entries(text)
    assert len(updated) == 105
    assert set(updated) == set(original) - {'stein_dont_2020'}
    for key in ['goldbach_geht_2019', 'kurtzberg_attribution_2004', 'liu_when_2021']:
        assert updated[key][2] == original[key][2]
    changed_keys = {change['key'] for change in applied}
    for key in set(updated) - changed_keys:
        assert updated[key][2] == original[key][2], key
    for key in updated:
        field_spans(updated[key][2])
    cited = set(re.findall(r'\\citation\{([^}]+)\}', (MANUSCRIPT / 'main.aux').read_text(encoding='utf-8')))
    cited_keys = {key.strip() for group in cited for key in group.split(',')}
    assert cited_keys <= set(updated)
    backup = HERE / 'ProjectAlgorithm.bib.before-approved-changes'
    assert not backup.exists()
    backup.write_bytes(before)
    BIB.write_bytes(text.encode('utf-8'))
    report = {
        'date': '2026-09-05', 'before_sha256': expected_hash,
        'after_sha256': hashlib.sha256(BIB.read_bytes()).hexdigest(),
        'modified_existing_entries': len(changed_keys - {'stein_dont_2020'}),
        'deleted_entries': ['stein_dont_2020'], 'entry_count': len(updated),
        'cited_key_count': len(cited_keys), 'citation_keys_preserved': True,
        'untouched_uncited_identity_questions': ['goldbach_geht_2019', 'kurtzberg_attribution_2004', 'liu_when_2021'],
        'changes': applied,
    }
    (HERE / 'implemented_changes.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({key: value for key, value in report.items() if key != 'changes'}, indent=2))


if __name__ == '__main__':
    apply()
