# P01 — Sample / data-collection paragraph

**Source:** `manuscript/results.tex` line 3 (the paragraph before `\subsection*{Player~A -- Delegation behavior}`).
**Status:** Draft, awaiting feedback.
**Last updated:** 2026-05-06.

---

## 1. Why the appendix / table references don't display

**Diagnosis: not the references — the `.aux` file is empty.**

`manuscript/main.aux` after the last compile contains only:

```
\relax
\gdef \@abspage@last{1}
```

No `\newlabel{...}` lines at all → every `\ref{...}` and `\pageref{...}` in the document resolves to `??`. The two flagged refs (`appendix:sum_stats`, `tab:treatment_balance`) are not the problem; they are *symptoms*. Both labels are correctly defined:

- `appendix:sum_stats` → `manuscript/appendix.tex:7`
- `tab:treatment_balance` → `tables/balance_player_a.tex:4`, and `appendix.tex:9` does `\input{../tables/balance_player_a.tex}` properly.

**Root cause:** the broken `\textcolor{red}{\textbf{[…]}}` blocks elsewhere in `results.tex` (currently lines 7, 50, 79, 97, 138) abort compilation with `Paragraph ended before \@textcolor was complete` + `Too many }'s`. pdflatex's error recovery destabilises the `.aux` write, so labels never get recorded. With no labels in `.aux`, *no* `\ref` resolves anywhere in the document.

**Fix:** when we get to the paragraphs that contain those blocks, close the open `\textcolor{...}{...}` braces (one of them in this very paragraph block, line 7). After three clean passes (`pdflatex` → `bibtex` → `pdflatex` → `pdflatex`) the refs will resolve. No change to the references in P01 themselves is needed.

---

## 2. Numeric checks against `scripts/python/_outputs/numbers.json`

| Claim in paragraph | Manuscript value | Manifest value | Verdict |
|---|---|---|---|
| Player A average bonus | £2.49 | `player_a_mean_bonus_excl_risk = 2.49` | Matches — but see caveat below |
| Player B average bonus | £2.30 | `player_b_mean_bonus_excl_risk = 2.3` | Matches — see caveat |
| Player A average time | 12 min | `time_a_min = 12.4` | Rounded down; close enough |
| Player B average time | ≈ 8 min | `time_b_min = 7.9` | Rounded up; close enough |
| N = 322 (161 + 161) | 322 | consort: 80 + 81 + 80 + 81 = 322 | Matches |

Both `[Comment: Check]` markers can be removed once you accept the values.

### Caveat on the bonus numbers

`scripts/python/10_payoffs.py` header explicitly states the figure is the **mean bonus excluding both the Prolific show-up fee and the risk-MPL outcome**. The script's own docstring closes with:

> "Felix should add the Prolific base fee + a small risk-MPL adjustment when reporting total earnings in the manuscript."

The current paragraph says the bonus is "on top of the Prolific show-up fee" — that's correct (the show-up fee is added separately) — but it doesn't note that the figure also excludes the risk-MPL piece. Two clean options:

- **(a) Clarify exclusion in text:** "an average bonus of £2.49 (excluding the risk-elicitation lottery, paid separately) on top of the Prolific show-up fee."
- **(b) Add the risk-MPL piece to the figure** and report a single all-in bonus. Requires going back to the raw oTree exports (per the script header, the cleaned files don't carry the MPL inputs).

Option (a) is the lighter-touch fix.

---

## 3. Likely error in the attrition footnote

The paragraph's second footnote currently reads:

> "Due to attrition and subsequent re-matching we recruited an extra pair in the *Punishment* condition."

`numbers.json` consort breakdown:

| Cell | Completed |
|---|---|
| Player A, Punishment | **80** |
| Player A, No-Punishment | **81** |
| Player B, Punishment | (not exposed in the JSON I checked, but symmetric: ~80) |
| Player B, No-Punishment | 81 |

So Punishment has **80** pairs and No-Punishment has **81** pairs — i.e., the extra pair is in **No-Punishment**, not Punishment. Worth confirming against `09_consort.py`'s output before changing, but the current footnote looks like it has the condition flipped.

---

## 4. Other small items

1. **Placeholder footnote on exclusion criteria.** Currently:

   > "\footnote{Comment: insert exclusion criteria - So that all subjects would visually perceive the experiment in the same way, phone and tablet users were not able to participate in the experiment.}"

   The intended sentence is already inside the placeholder; if you're happy with it, the simplest move is to drop the "Comment: insert exclusion criteria - " preamble and keep the rest verbatim. If you want to add other preregistered exclusions (consent? completed all stages?), this is the place.

2. **Slight redundancy:** "British online platform Prolific, with all participants recruited from the United Kingdom." Prolific is UK-based but globally used; the substantive constraint is UK residency. Suggest:

   > "the online platform Prolific, with participation restricted to UK residents."

3. **Attention-check exclusion deferred to analysis section.** You've decided to introduce the exclusion when discussing the analysis sample. That's defensible, but a reader reaching the next subsection will wonder which N drives the 42.5% / 59.3% delegation shares (the analysis N is 131 = 70 + 61, not 161). Consider whether to add a single bridging clause here, e.g.:

   > "All N's reported in the analyses below correspond to the preregistered analysis sample, which excludes participants who failed the attention checks; the recruitment vs. analysis breakdown appears in Appendix Figure~\ref{fig:consort}."

   This avoids reader confusion when 322 → 131 without re-introducing the full exclusion discussion.

4. **Date range:** "between February and June 2023" is a 5-month window — unusual for an online experiment of this size. If data collection was actually a few sessions within that window, that's worth noting (or tightening the dates).

---

## 5. Suggested revision — track-changes view

I am **not** rewriting the paragraph wholesale; per your "keep content at draft stage" preference, this is a minimal-edit suggestion that resolves the verified issues only. Treat as a strawman.

> Data collection took place between February and June 2023 through the online platform Prolific, with participation restricted to UK residents.\footnote{To ensure all subjects perceived the experimental interface identically, phone and tablet users were not allowed to participate.} A total of $322$ subjects were recruited ($161$ assigned to Player~A, $161$ to Player~B).\footnote{We preregistered the collection of data from $320$ participants ($80$ per role per treatment). Due to attrition and subsequent re-matching, we recruited an extra pair in the \textit{No-Punishment} condition.} On average, Player~A spent $12$ minutes completing the experiment and earned an average bonus of $\pounds 2.49$ (excluding the risk-elicitation lottery, paid separately) on top of the Prolific show-up fee, while Player~B spent approximately $8$ minutes and earned an average bonus of $\pounds 2.30$. Treatment randomization was effective, as demonstrated by the balance across observable characteristics (Appendix~\ref{appendix:sum_stats}, Table~\ref{tab:treatment_balance}).

Changes vs. current:
- "British online platform Prolific … recruited from the United Kingdom" → "online platform Prolific, with participation restricted to UK residents".
- Footnote 1 reworded; "Comment: insert exclusion criteria" preamble dropped.
- Footnote 2: "Punishment" → "No-Punishment" (pending your confirmation against `09_consort.py`).
- Bonus exclusion clause added.
- `[Comment: Check]` markers removed.

---

## 6. Open questions for you

1. Which way do you want to handle the bonus caveat — (a) text clarification, or (b) recompute including risk-MPL?
2. Confirm the No-Punishment vs Punishment direction of the extra pair before I change it.
3. Want a short bridging sentence about the analysis sample (point 4.3), or hold for the analysis subsection?
4. Are the date-range bounds correct as-is, or do you want to tighten them?
