"""Single source of truth for all project paths."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
RAW = DATA / "raw"
INTERIM = DATA / "interim"
CLEAN = DATA / "clean"

MANUSCRIPT = ROOT / "manuscript"
FIGURES = MANUSCRIPT / "figures"
TABLES = ROOT / "tables"

OUTPUTS = ROOT / "scripts" / "python" / "_outputs"

DELEGATOR = CLEAN / "delegator_cleaned.xlsx"
EVALUATOR = CLEAN / "evaluator_cleaned.xlsx"
DELEGATOR_PAGETIMES = INTERIM / "03_pagetimes" / "delegator_full_merged.xlsx"

for d in (FIGURES, TABLES, OUTPUTS):
    d.mkdir(parents=True, exist_ok=True)
