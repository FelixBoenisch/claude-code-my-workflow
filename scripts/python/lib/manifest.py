"""Numbers manifest: every numeric claim the manuscript makes is recorded here.

Each script appends to a dict that gets written to _outputs/numbers.json. This
file is the source of truth for /audit-reproducibility.
"""
from __future__ import annotations
import json
from .paths import OUTPUTS

MANIFEST_PATH = OUTPUTS / "numbers.json"


def load() -> dict:
    if MANIFEST_PATH.exists():
        return json.loads(MANIFEST_PATH.read_text())
    return {}


def reset() -> None:
    """Start a pipeline run with an empty numbers manifest."""
    MANIFEST_PATH.write_text("{}\n")


def update(values: dict) -> None:
    cur = load()
    cur.update(values)
    MANIFEST_PATH.write_text(json.dumps(cur, indent=2, sort_keys=True))


def get(key: str, default=None):
    return load().get(key, default)
