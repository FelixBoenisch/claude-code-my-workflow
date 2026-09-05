"""Preserve a verified compound surname in BibTeX's rendered output."""
import hashlib
import json
from apply_approved_changes import BIB, HERE, entries, field_spans

key = 'santoni_de_sio_four_2021'
old = 'Santoni de Sio, Filippo and Mecacci, Giulio'
new = '{Santoni de Sio}, Filippo and Mecacci, Giulio'
text = BIB.read_bytes().decode('utf-8')
start, end, entry = entries(text)[key]
_, a, b, _, current, _ = field_spans(entry)['author']
assert current == old
entry = entry[:a] + '{' + new + '}' + entry[b:]
text = text[:start] + entry + text[end:]
BIB.write_bytes(text.encode('utf-8'))
path = HERE / 'implemented_changes.json'
report = json.loads(path.read_text(encoding='utf-8'))
report['changes'].append({
    'key': key, 'field': 'author', 'old': old, 'new': new,
    'reason': 'Visual QA found aer.bst rendered de Sio, Filippo Santoni. Protect the compound surname to render and sort Santoni de Sio correctly.',
    'source': 'https://link.springer.com/article/10.1007/s13347-021-00450-x',
    'category': 'implementation formatting',
})
report['after_sha256'] = hashlib.sha256(BIB.read_bytes()).hexdigest()
path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(report['after_sha256'])
