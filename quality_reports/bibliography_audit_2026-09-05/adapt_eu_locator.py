"""Avoid a duplicated publication year in aer.bst's misc format."""
import hashlib
import json
from apply_approved_changes import BIB, HERE, entries, field_spans

key = 'european_union_ai_act_2024'
old = 'Official Journal of the European Union, L, 2024/1689, 12 July 2024'
new = 'Official Journal of the European Union, L, 2024/1689, 12 July'
text = BIB.read_bytes().decode('utf-8')
start, end, entry = entries(text)[key]
_, a, b, _, current, _ = field_spans(entry)['howpublished']
assert current == old
entry = entry[:a] + '{' + new + '}' + entry[b:]
text = text[:start] + entry + text[end:]
BIB.write_bytes(text.encode('utf-8'))
path = HERE / 'implemented_changes.json'
report = json.loads(path.read_text(encoding='utf-8'))
for change in report['changes']:
    if change['key'] == key and change['field'] == 'howpublished':
        change['new'] = new
        change['reason'] = 'Complete official locator. Omit the year from howpublished because aer.bst appends year=2024, yielding 12 July 2024 once.'
        change['rendering_adaptation'] = True
report['after_sha256'] = hashlib.sha256(BIB.read_bytes()).hexdigest()
path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(report['after_sha256'])
