"""Repair missing field separators from the first application pass."""
import hashlib
import json
from apply_approved_changes import BIB, HERE, entries, field_spans

targets = {
    'fiorina_legislator_1986': 'year',
    'bogert_humans_2021': 'doi',
    'jolly_not_2025': 'note',
    'tontrup_strategic_2025': 'url',
    'normann_delegate_2025': 'url',
    'weitzner_reputational_2024': 'url',
    'tsumura_effects_2026': 'doi',
    'salatino_influence_2025': 'doi',
    'freer_friedman_weidenholzer_2024': 'url',
    'freisinger_decoding_2024': 'url',
    'gawn_lying_2019': 'year',
    'kandul_do_2018': 'year',
    'maximiano_gift_2013': 'year',
    'jung_towards_2021': 'doi',
    'dawes_robust_1979': 'year',
    'tacconelli_how_2026': 'annote',
    'beckers_drivers_2022': 'annote',
    'santoni_de_sio_four_2021': 'doi',
    'european_commission_liability_2019': 'url',
}
text = BIB.read_bytes().decode('utf-8')
records = entries(text)
positions = []
for key, field in targets.items():
    start, _, entry = records[key]
    pos = field_spans(entry)[field][2]
    assert entry[pos] != ',', (key, 'already fixed')
    positions.append(start + pos)
for pos in sorted(positions, reverse=True):
    text = text[:pos] + ',' + text[pos:]
BIB.write_bytes(text.encode('utf-8'))
report_path = HERE / 'implemented_changes.json'
report = json.loads(report_path.read_text(encoding='utf-8'))
report['after_sha256'] = hashlib.sha256(BIB.read_bytes()).hexdigest()
report['field_separator_repairs'] = list(targets)
report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'Repaired {len(positions)} separators. SHA256: {report["after_sha256"]}')
