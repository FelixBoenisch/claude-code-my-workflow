"""Data loaders. Convert xlsx → parquet on first call for speed."""
from __future__ import annotations
import os
import pandas as pd
from .paths import DELEGATOR, EVALUATOR, CLEAN

# Subjects who never produced a credible weight guess over the ten rounds.
# A guess is credible if it is non-zero; all non-zero guesses in the data fall
# in 114-253 lbs, which is a plausible adult body weight throughout.
# Credible-guess counts are 10 for 158 subjects, then 7, then 2, then 0, so any
# cutoff between 3 and 7 selects exactly these two.
INCREDIBLE_GUESSERS = ("d8goj7g9", "pd4bg6c3")


def _load(xlsx_path):
    parquet = xlsx_path.with_suffix(".parquet")
    if not parquet.exists() or parquet.stat().st_mtime < xlsx_path.stat().st_mtime:
        df = pd.read_excel(xlsx_path)
        df.to_parquet(parquet, index=False)
    return pd.read_parquet(parquet)


def load_delegator() -> pd.DataFrame:
    df = _load(DELEGATOR)
    if os.environ.get("EXCLUDE_INCREDIBLE_GUESSERS") == "1":
        df = df[~df["code"].isin(INCREDIBLE_GUESSERS)].reset_index(drop=True)
    return df


def load_evaluator() -> pd.DataFrame:
    return _load(EVALUATOR)
