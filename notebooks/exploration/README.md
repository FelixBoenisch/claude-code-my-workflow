# Exploration notebooks

Free-form Jupyter notebooks for exploratory analysis: alternative cuts of the
data, robustness checks, descriptive deep-dives, sanity-check plots, payoff
calculations, anything that doesn't (yet) need to land in the paper.

## Inventory

| Notebook | Code cells | What's in it | Status |
|---|---|---|---|
| [delegator_analysis_full.ipynb](delegator_analysis_full.ipynb) | 83 | Canonical delegator analysis. The figure-producing cells are now in [`scripts/python/03_h1_delegation.py`](../../scripts/python/03_h1_delegation.py), [`04_logit_delegation.py`](../../scripts/python/04_logit_delegation.py), and [`07_performance.py`](../../scripts/python/07_performance.py). The other ~75 cells are exploratory: alternative robustness specs, sub-cuts by attention check, performance-by-delegation visualisations, etc. | exploratory + canonical (canonical cells already ported) |
| [evaluator_analysis_full.ipynb](evaluator_analysis_full.ipynb) | 41 | Canonical evaluator analysis. Figure-producing cells now in [`05_h2_punishment.py`](../../scripts/python/05_h2_punishment.py) and [`06_logit_punishment.py`](../../scripts/python/06_logit_punishment.py). The other ~35 cells are exploratory cuts of the punishment data. | exploratory + canonical (canonical cells already ported) |
| [extended_analysis_delegator.ipynb](extended_analysis_delegator.ipynb) | 49 | Extended exploratory work on Player A behaviour beyond the canonical analysis. | exploratory |
| [extended_analysis_evaluator.ipynb](extended_analysis_evaluator.ipynb) | 54 | Extended exploratory work on Player B punishment behaviour. | exploratory |
| [link_delegator_evaluator.ipynb](link_delegator_evaluator.ipynb) | 11 | Cross-side analysis joining the two players (e.g., comparing beliefs to actual punishment by individual). | exploratory |
| [old_pilot_delegator_analysis.ipynb](old_pilot_delegator_analysis.ipynb) | 51 | Pilot-wave delegator analysis. Pre-dates the main wave. Useful as historical reference. | legacy / pilot-only |
| [old_pilot_evaluator_analysis.ipynb](old_pilot_evaluator_analysis.ipynb) | 25 | Pilot-wave evaluator analysis. | legacy / pilot-only |
| [payoff_calc.ipynb](payoff_calc.ipynb) | 31 | Payoff computation across waves. **Useful for resolving the [earnings pending] placeholder in the manuscript.** | tool — promote to script when needed |
| [payoff_calc_main.ipynb](payoff_calc_main.ipynb) | 24 | Payoff computation, main-punishment wave only. | tool |
| [payoff_calc_main_no_punish.ipynb](payoff_calc_main_no_punish.ipynb) | 27 | Payoff computation, no-punishment wave. | tool |
| [power.ipynb](power.ipynb) | 2 | Power analysis sketch. | exploratory (minimal — likely needs expansion to support the manuscript's [Appendix PAP] block) |
| [within_session_delegator.ipynb](within_session_delegator.ipynb) | 17 | Within-session calculations done while running each Prolific batch (e.g., computing on-the-fly payoffs to send to Prolific bonuses). | operational, not analytical |

Total: 12 notebooks, 415 code cells.

## Paths

All read paths have been rewritten to the current folder layout
(`data/raw/`, `data/interim/`, `data/clean/`). `savefig` calls that previously
wrote to `../../output/` now write to `_outputs/` (a local subfolder of
`notebooks/exploration/`) so that exploration figures don't pollute the
canonical `manuscript/figures/` location.

## Conventions

- **Read from `data/clean/*.parquet` (or `*.xlsx`).** The cleaned files are the
  canonical inputs; the cleaning pipeline that produces them is in
  [`data/code_legacy/`](../../data/code_legacy/) (not yet ported).
- **Don't write to `manuscript/figures/` or `tables/`** from notebooks. Anything
  that ends up in the paper goes through [`scripts/python/`](../../scripts/python/)
  so it's reproducible and tracked by the manifest.
- **Save your own outputs locally** (`notebooks/exploration/_outputs/` is fine).
- **Promote to a script when an analysis stabilises.** If a notebook cell
  becomes load-bearing for a paper claim, port it to `scripts/python/NN_*.py`,
  update the manifest, and reference the script from the manuscript.
- **Don't commit `.ipynb_checkpoints/`.** Already gitignored.

## Getting started

```python
import sys
sys.path.insert(0, "../../scripts/python")
from lib.io import load_delegator, load_evaluator
d = load_delegator()
e = load_evaluator()
```

## Cross-references

- [`scripts/python/`](../../scripts/python/) — canonical analysis pipeline (paper-producing)
- [`data/code_legacy/`](../../data/code_legacy/) — frozen archive of the canonical cleaning notebooks (raw → clean), not yet ported to Python
- [`master_supporting_docs/payments/pilot_bonuses.txt`](../../master_supporting_docs/payments/pilot_bonuses.txt) — pilot bonus payment list (paper trail)
