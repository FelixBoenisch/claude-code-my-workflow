"""Data loaders. Convert xlsx → parquet on first call for speed."""
from __future__ import annotations
import pandas as pd
from .paths import DELEGATOR, EVALUATOR, CLEAN

# Player As who entered zero -- not a credible body-weight prediction -- in at
# least eight of the ten initial rounds. The non-zero submission counts are 10
# for 158 subjects, 7 for one subject, 2 for one subject, and 0 for one subject.
UNREALISTIC_GUESSERS = ("d8goj7g9", "pd4bg6c3")


def _load(xlsx_path):
    parquet = xlsx_path.with_suffix(".parquet")
    if not parquet.exists() or parquet.stat().st_mtime < xlsx_path.stat().st_mtime:
        df = pd.read_excel(xlsx_path)
        df.to_parquet(parquet, index=False)
    return pd.read_parquet(parquet)


def load_delegator(*, include_unrealistic: bool = False) -> pd.DataFrame:
    """Load Player-A data, excluding unrealistic guessers by default.

    Set ``include_unrealistic=True`` only for full-raw-sample sensitivity checks.
    """
    df = _load(DELEGATOR)
    if not include_unrealistic:
        df = df[~df["code"].isin(UNREALISTIC_GUESSERS)].reset_index(drop=True)
    return df


def load_evaluator() -> pd.DataFrame:
    return _load(EVALUATOR)
