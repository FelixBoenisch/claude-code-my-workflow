# `appendix.tex` — old vs new

## Overview

The old `appendix.tex` (97 lines) had:
- Summary statistics / treatment balance for Player A (full numerical table)
- Full regression results — delegation decision (Table A2 with all controls)
- Two empty placeholder figure environments for Player A and Player B design figures (no actual figures)
- Punishment frequencies figure (`figures/punishment_shares.png`)

The new `appendix.tex` (151 lines) has:
- Condition balance — Player A (now via `\input{../tables/balance_player_a.tex}`)
- **NEW**: Condition balance — Player B (`\input{../tables/balance_player_b.tex}`)
- Full regression results — delegation decision (now `\input{../tables/reg_delegation_full.tex}`)
- **NEW**: Determinants of Player B's chosen punishment (`\input{../tables/reg_punishment.tex}`)
- **NEW**: Preregistration and deviations subsection with a full PAP-deviations table
- **NEW**: CONSORT-style flow diagram (TikZ, populated with derivable counts)
- Experimental timeline figures for Player A and Player B (now drawn in TikZ, replacing the empty placeholders in the old draft)
- Punishment frequencies figure (preserved, unchanged target file)

## What changed in the prose

- **Tables now `\input{}`-ed from generated artefacts** under `tables/` rather than hand-coded inline.
- **Significance stars stripped** from all tables (AEA editorial policy); exact $p$-values reported in table notes.
- **Player A balance table notes** unchanged in substance.
- **Regression note** rewritten to spell out exact two-sided $p$-values for headline coefficients.
- **Player B balance table is new** — was "results available on request" in the old text.
- **Player B punishment regression is new** — was a placeholder in the old text.
- **PAP deviations table is new** — formalises which tests are preregistered, what was reported, and why deviations exist.
- **CONSORT diagram is new** — was not in the old draft at all.
- **Player A and Player B experimental timelines** — previously empty figure environments with `\includegraphics[]{}` (no file); now drawn in TikZ showing the full screen sequence with attention-check screens shaded.

## Dropped items

The old appendix was sparse, so there's relatively little to drop. The
items that didn't survive:

- **The empty `\includegraphics[]{}` placeholder figure environments** for `fig:design_playerA` and `fig:design_playerB`. Replaced by drawn TikZ timelines in the new appendix.
- **The "Summary statistics - Treatment balance" caption** has been retitled "Condition balance — Player A" matching the new naming convention.

(That's essentially it — the old appendix was minimal; almost everything in the new appendix is either a faithful re-rendering of what was already there or a new addition.)

## Items added in the new appendix that did NOT come from the old

These came from the peer-review pipeline, not from any pre-existing material in the old draft:

- **Player B balance table** — added in response to the methods referee flagging "Player B's identification is within-subject, but balance for completeness". Currently has [pending] cell values waiting on `02_balance.py` to populate (which it now does via `tables/balance_player_b.tex`).
- **Player B punishment regression table** — added in response to the methods referee. Now populated via `06_logit_punishment.py` → `tables/reg_punishment.tex`.
- **PAP deviations subsection + table** — added in response to the methods referee's critical peeve (preregistration adherence FAIL). The table maps every preregistered test to what's reported and the deviation rationale. Registry link + ID still placeholder.
- **CONSORT diagram** — added in response to both the methods referee (attrition asymmetry concern) and the editor's data-quality bar. Currently shows derivable counts (completed, attention-excluded, analysis sample) with the recruitment-funnel rows (invited / consented / pre-attrition randomised) flagged as needing the Prolific audit log.

## Why the changes (where I can infer)

- The shift to `\input{}`-ed generated tables came from the project's single-source-of-truth rule: scripts produce; manuscript references. This was a structural improvement.
- The new appendix tables and CONSORT diagram all came from the peer-review pipeline's gaps audit.
- The TikZ timelines were drawn from the existing prose description of each player's screen sequence (no new content; just typesetting the existing description).
