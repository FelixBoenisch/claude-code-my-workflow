"""Run the existing MiKTeX toolchain and save audit-scoped build evidence."""
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
MANUSCRIPT = HERE.parents[1] / 'manuscript'
BIN = Path('C:/Users/USER/AppData/Local/Programs/MiKTeX/miktex/bin/x64')
BUILD = HERE / 'build'
BUILD.mkdir(exist_ok=True)
source_hashes = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in MANUSCRIPT.glob('*.tex')}
backup_pdf = BUILD / 'main.before-bibliography-update.pdf'
if not backup_pdf.exists():
    shutil.copyfile(MANUSCRIPT / 'main.pdf', backup_pdf)
commands = [
    ('latex1', [str(BIN / 'pdflatex.exe'), '-interaction=nonstopmode', '-halt-on-error', '-file-line-error', 'main.tex']),
    ('bibtex', [str(BIN / 'bibtex.exe'), 'main']),
    ('latex2', [str(BIN / 'pdflatex.exe'), '-interaction=nonstopmode', '-halt-on-error', '-file-line-error', 'main.tex']),
    ('latex3', [str(BIN / 'pdflatex.exe'), '-interaction=nonstopmode', '-halt-on-error', '-file-line-error', 'main.tex']),
]
results = []
for label, command in commands:
    result = subprocess.run(command, cwd=MANUSCRIPT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=180)
    (BUILD / f'{label}.stdout').write_bytes(result.stdout)
    print(label, 'exit', result.returncode, flush=True)
    results.append({'step': label, 'exit_code': result.returncode})
    if result.returncode:
        print(result.stdout.decode('utf-8', errors='replace')[-7000:].encode('ascii', errors='backslashreplace').decode(), flush=True)
        raise SystemExit(result.returncode)
log = (MANUSCRIPT / 'main.log').read_text(encoding='utf-8', errors='replace')
blg = (MANUSCRIPT / 'main.blg').read_text(encoding='utf-8', errors='replace')
assert not re.search(r'undefined citations|Citation .* undefined|There were undefined|^!', log, re.M)
assert not re.search(r'Warning--|error message', blg, re.I)
assert {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in MANUSCRIPT.glob('*.tex')} == source_hashes
text_result = subprocess.run([str(BIN / 'pdftotext.exe'), '-layout', str(MANUSCRIPT / 'main.pdf'), str(BUILD / 'main.txt')], capture_output=True, timeout=60)
assert text_result.returncode == 0, text_result.stderr
summary = {
    'steps': results, 'source_tex_files_unchanged': True,
    'bibtex_warnings': False, 'undefined_citations': False,
    'pdf_sha256': hashlib.sha256((MANUSCRIPT / 'main.pdf').read_bytes()).hexdigest(),
    'pdf_bytes': (MANUSCRIPT / 'main.pdf').stat().st_size,
    'remaining_latex_warnings': [line for line in log.splitlines() if 'Warning:' in line],
}
(HERE / 'build_verification.json').write_text(json.dumps(summary, indent=2), encoding='utf-8')
print(json.dumps(summary, indent=2), flush=True)
