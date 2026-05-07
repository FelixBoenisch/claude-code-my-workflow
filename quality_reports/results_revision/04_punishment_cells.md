# P04 — Average punishment in the four cells

**Source paragraph:** `manuscript/results.tex` lines ~30–32 (the red-textcolor draft blocks for "Sub result 6" / "Main result 2") and the cleaner `\paragraph{Headline.}` block on line ~38.
**Status:** Analysis only — descriptive cell means + within-subject delegation tests, full vs attention-pass samples. **No edits to `results.tex` yet.**
**Last updated:** 2026-05-07.

---

## 1. Sample definitions

- **Full sample** (Punishment condition, $N=80$): every Player B in the *Punishment* condition. Punishment elicited via the strategy method on the punishment-elicitation screen.
- **Attention-check passers** ($N=67$): the same restricted to `pass_att2 == 1` — i.e., Player Bs who passed the attention check on the punishment-elicitation screen. This is the canonical analysis sample, as preregistered.

The attention check on the evaluator side is `pass_att2`; the data does not carry a `pass_att1` for evaluators. The exclusion drops $13$ subjects ($16.3\%$).

I'm only reporting the *Punishment* condition because punishment in the *No-Punishment* condition is hypothetical (asked but never paid). The four-cell vector is collected for both, but only one is a real choice. If you want the hypothetical numbers as a side panel, easy to add.

---

## 2. Cell means

Logged in `explorations/results-revision/explore.py`, P04 block. Punishment elicited in £0.10 increments on $[\pounds 0, \pounds 2]$.

### Full sample ($N=80$)

| Cell | Mean (£) | SD | Median | $\%$ zero | $t$-test vs 0 ($p$) |
|---|---:|---:|---:|---:|---:|
| Delegated, good outcome | $0.329$ | $0.613$ | $0.000$ | $67.5\%$ | $7\!\times\!10^{-6}$ |
| Delegated, bad outcome | $0.482$ | $0.683$ | $0.000$ | $51.2\%$ | $1.5\!\times\!10^{-8}$ |
| Self-decided, good outcome | $0.297$ | $0.585$ | $0.000$ | $67.5\%$ | $2\!\times\!10^{-5}$ |
| Self-decided, bad outcome | $0.553$ | $0.728$ | $0.125$ | $47.5\%$ | $1.8\!\times\!10^{-9}$ |

### Attention-check passers ($N=67$)

| Cell | Mean (£) | SD | Median | $\%$ zero | $t$-test vs 0 ($p$) |
|---|---:|---:|---:|---:|---:|
| Delegated, good outcome | $0.311$ | $0.579$ | $0.000$ | $67.2\%$ | $4\!\times\!10^{-5}$ |
| Delegated, bad outcome | $0.494$ | $0.681$ | $0.100$ | $49.3\%$ | $1.2\!\times\!10^{-7}$ |
| Self-decided, good outcome | $0.310$ | $0.591$ | $0.000$ | $65.7\%$ | $6\!\times\!10^{-5}$ |
| Self-decided, bad outcome | $0.571$ | $0.717$ | $0.200$ | $44.8\%$ | $1.2\!\times\!10^{-8}$ |

The current Headline paragraph in `results.tex` (£0.311 / £0.310 good, £0.494 / £0.571 bad) uses the **passer** numbers — confirmed.

---

## 3. Within-subject delegation effect, conditional on outcome (paired tests)

Each pair compares `punish_nodel_*` to `punish_del_*` for the same Player B. Positive mean difference = self-decided punished more than delegated (the H2 prediction).

| Sample | Outcome | Mean $\text{self} - \text{del}$ | Paired $t$-test $p$ | Wilcoxon signed-rank $p$ | $N$ |
|---|---|---:|---:|---:|---:|
| Full | good | $-0.032$ | $0.535$ | $0.271$ | $80$ |
| Full | bad | $+0.071$ | $0.131$ | $0.544$ | $80$ |
| Passers | good | $-0.001$ | $0.989$ | $0.594$ | $67$ |
| Passers | bad | $+0.077$ | $0.153$ | $0.533$ | $67$ |

**Reading:**

- The delegation effect is essentially zero in the good-outcome cell (point estimate $\le \pounds 0.03$, $p \in [0.27, 0.99]$).
- The bad-outcome cell shows the predicted H2 direction (self punished about $\pounds 0.07$ more than delegated) but is not significant on either test.
- Wilcoxon $p$-values are systematically higher than paired $t$-test $p$-values — this is because the punishment distribution is heavily zero-inflated ($\sim 50$–$67\%$ of Player Bs do not punish in any given cell), which is exactly the situation where Wilcoxon trades off rank information for the magnitude information. Worth picking one for the body and reporting the other in a robustness footnote.
- The full-sample and passer-sample numbers tell the same story.

---

## 4. Two side observations from the cell means

- **Outcome-based punishment is real:** in both samples, the bad-outcome cells exceed the good-outcome cells by about $\pounds 0.18$–$0.26$ on average. (We can attach a paired test on this if you want it in the body.)
- **The "$41.8\%$ of Player Bs do not punish in any cell"** number from the existing body matches a different cut: it's *across* the four cells (i.e., share who chose $0$ in all four), not the per-cell zero share above. Both numbers are useful; flagging so we don't conflate them.

---

## 5. Open questions for you

1. **Sample for the body table:** lead with passers (preregistered exclusion, what the current body uses) and footnote the full-sample numbers, or lead with full and footnote passers?
2. **Do you want the No-Punishment hypothetical cell means** as a side panel, or keep them out of the headline analysis?
3. **Test statistic for the H2 paired comparison** — paired $t$-test ($p=0.153$) or Wilcoxon ($p=0.533$)? The current body reports both. The $t$-test is the higher-powered choice given zero-inflation; Wilcoxon is more conservative.
4. **Outcome-based punishment** — worth a sentence flagging that bad-outcome cells exceed good-outcome cells significantly? It's the design's "punishment is informative, not noise" check.
5. Once a sample / framing is fixed, I'll draft the body paragraph rewriting the red-textcolor blocks against this evidence.
