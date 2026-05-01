"""Data loaders. Convert xlsx → parquet on first call for speed."""
from __future__ import annotations
import pandas as pd
from .paths import DELEGATOR, EVALUATOR, CLEAN


def _load(xlsx_path):
    parquet = xlsx_path.with_suffix(".parquet")
    if not parquet.exists() or parquet.stat().st_mtime < xlsx_path.stat().st_mtime:
        df = pd.read_excel(xlsx_path)
        df.to_parquet(parquet, index=False)
    return pd.read_parquet(parquet)


def load_delegator() -> pd.DataFrame:
    return _load(DELEGATOR)


def load_evaluator() -> pd.DataFrame:
    return _load(EVALUATOR)
