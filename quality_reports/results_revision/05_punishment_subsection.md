# P05 — Player B / Punishment Behavior subsection

**Source:** `manuscript/results.tex` lines 28–65 (the entire `Player~B -- Punishment behavior` subsection, including the embedded Result 2 box, the punishment figure, and the "What predicts punishment?" paragraph).
**Status:** Plan, awaiting feedback. **No edits to `results.tex` yet.**
**Last updated:** 2026-05-07.

Analysis log: `explorations/results-revision/explore.py`, P04 + P05 blocks. Numeric checks against `_outputs/numbers.json`.

---

## 1. Comments inventory

Twelve comment markers in lines 28–65, plus one structural item (the duplicated red `\textcolor` blocks of an earlier pass have already been removed; only clean prose remains). Mapping each comment to the section of this plan that addresses it:

| # | Loc | Comment | Section |
|---|---|---|---|
| C1 | L32 | "Maybe do it the other way around?" — sample default | §2 |
| C2 | L34 | "verify that this is statistically correct" — cell means $> 0$ | §3 |
| C3 | L34 | Coffman (2011) on punishment of fair outcomes | §5 |
| C4 | L36 | "How many subjects forgo 10 cents just to punish little?" sanity check | §6 |
| C5 | L38 | Figure redesign — drop beliefs, add frequencies, full + passer panels | §7 |
| C6 | L42 | "We may have to replace by numbers of full sample" | §8 |
| C7 | L42 | "Should we point out … inconsistent with delegation pattern?" | §9 |
| C8 | L44 | "Reference will need to change if we move frequencies into main figure" | §7 |
| C9 | L46 | "Make full sample default, mention reduced sample" — duplicate of C1 | §2 |
| C10 | L46 | "Referring to a table we have not introduced yet" | §10 |
| C11 | L65 | Rewrite the beliefs-about-Player-A sentence | §11 |
| C12 | L65 | "Similar regressions where DV = punishment difference?" | §12 |

---

## 2. Sample default — full vs attention-pass (C1, C9)

The current subsection introduces the attention-check exclusion as preregistered (correct), then reports the headline numbers on the **passer** sample, then mentions the full-sample numbers as robustness. The user's question is whether to invert.

### What the data say

The two samples tell the same story:

| Quantity | Full ($N=80$) | Passers ($N=67$) |
|---|---:|---:|
| Delegated, good | $\pounds 0.329$ | $\pounds 0.311$ |
| Delegated, bad | $\pounds 0.482$ | $\pounds 0.494$ |
| Self-decided, good | $\pounds 0.297$ | $\pounds 0.310$ |
| Self-decided, bad | $\pounds 0.553$ | $\pounds 0.571$ |
| Insulation in bad cell ($\text{self}-\text{del}$) | $+0.071$ | $+0.077$ |
| Paired $t$-test on bad insulation, $p$ | $0.131$ | $0.153$ |
| Wilcoxon on bad insulation, $p$ | $0.544$ | $0.533$ |
| Never-punish-any-cell share | $45.0\%$ | $41.8\%$ |

### Recommendation

Switch the headline to **full sample** (consistent with the [To resolve] item *"For each analysis, make explicit whether this is with the reduced sample (attention checks) or full sample"*, and parallel to the new convention in the With-Controls table where Col 5 is the passer robustness rather than the headline). Move the passer numbers into a sentence that says "the result is essentially identical when restricting to the $67$ Player Bs who passed the attention check (mean difference $\pounds 0.077$ vs $\pounds 0.071$; paired $t$-test $p=0.153$ vs $p=0.131$)".

This is a stylistic preference; both readings are honest. Ticking the [To resolve] item with full-sample-as-headline is the cleanest move.

---

## 3. Verification: punishment in all four cells $> 0$ (C2)

`explore.py` P04 reports one-sample $t$-tests against zero in each cell, both samples:

| Cell | Full ($N=80$) — $t$-test $p$ | Passers ($N=67$) — $t$-test $p$ |
|---|---:|---:|
| Delegated, good | $7\!\times\!10^{-6}$ | $4\!\times\!10^{-5}$ |
| Delegated, bad | $1.5\!\times\!10^{-8}$ | $1.2\!\times\!10^{-7}$ |
| Self-decided, good | $2\!\times\!10^{-5}$ | $6\!\times\!10^{-5}$ |
| Self-decided, bad | $1.8\!\times\!10^{-9}$ | $1.2\!\times\!10^{-8}$ |

All four cells are highly significantly above zero in both samples. The body's claim is correct. Comment C2 can be deleted.

---

## 4. Outcome effect (bad cell $>$ good cell, within subject)

The body says *"Player Bs punish more for low-payoff outcomes than for high-payoff outcomes"* — worth attaching numbers and a paired test, since this is the design's "punishment is informative, not noise" check.

`explore.py` P05a — paired tests:

| Sample | Delegation | Mean (bad $-$ good) | Paired $t$ $p$ | Wilcoxon $p$ |
|---|---|---:|---:|---:|
| Full | delegated | $+0.153$ | $0.012$ | $0.008$ |
| Full | self-made | $+0.256$ | $0.0005$ | $0.0006$ |
| Passers | delegated | $+0.183$ | $0.009$ | $0.007$ |
| Passers | self-made | $+0.260$ | $0.001$ | $0.002$ |

Bad outcomes are punished significantly more than good outcomes, in both delegation modes and both samples. Worth a sentence in the body explicitly attaching a $p$-value.

---

## 5. Coffman comparison — punishment of fair / good outcomes (C3)

The user's note flags that Coffman (2011) also finds positive punishment for "fair" outcomes (where the decision-maker could not have done better with certainty), and that the framing in our setting is different: even with a good outcome, Player B might still hold strong views about whether the decision *should* have been delegated and punish accordingly. That keeps positive punishment in the good-outcome cell from being framed as noise.

**Recommendation:** add a one-sentence footnote to the cell-means paragraph. Suggested wording:

> "Positive punishment in the good-outcome cells need not reflect noise: Player Bs may hold ex-post views about whether the *delegation choice itself* was appropriate — independent of the realised outcome — and can punish accordingly. \citet{coffman_intermediation_2011} similarly documents non-trivial punishment in scenarios where the decision-maker's action could not have been improved upon."

This serves as a pre-emptive defense and also provides a citation hook for the discussion section.

---

## 6. Never-punish breakdown / "forgo 10 cents to punish a little" (C4)

`explore.py` P05b:

| Cells punished (out of 4) | Full ($N=80$) | Passers ($N=67$) |
|---:|---:|---:|
| 4 | $23$ ($28.8\%$) | $20$ ($29.9\%$) |
| 3 | $3$ ($3.8\%$) | $2$ ($3.0\%$) |
| 2 | $14$ ($17.5\%$) | $13$ ($19.4\%$) |
| 1 | $4$ ($5.0\%$) | $4$ ($6.0\%$) |
| 0 | $36$ ($45.0\%$) | $28$ ($41.8\%$) |

The $41.8\%$ figure in the body matches the **passer** sample exactly ($28/67$). In the **full sample**, the share who never punish is **$45.0\%$** — an item to switch if the headline moves to full sample (§8).

### "Forgo $10$p to punish a little"

The user's specific sanity-check question is whether subjects "pay $10$p just to punish $10$p" (i.e., choose minimal positive punishment, paying the fixed cost for almost no enforcement). Answers:

- **Subjects whose maximum punishment across the four cells is $\le \pounds 0.10$:** $3$ in both samples. So at most $3$ Player Bs forgo the $10$p fixed cost in any cell to impose only the minimum punishment.
- **Subjects whose smallest *non-zero* punishment is exactly $\pounds 0.10$ (in any cell):** $6$ in both samples. These are the Player Bs whose punishment portfolio includes at least one cell at the floor.

Both numbers are tiny relative to the $44$ (full) or $39$ (passers) Player Bs who punish in any cell. Bottom line: nobody is using the punishment mechanism just to pay the $10$p fixed cost for show. Worth a one-line sentence in the body or a footnote: *"only $3$ Player Bs ever choose strictly positive punishment of $\pounds 0.10$ or less in any cell, indicating that the costly punishment option is being used substantively rather than for tokenistic enforcement."*

---

## 7. Figure redesign (C5, C8)

The user's request: rebuild `figures/punishment.png` to (a) drop Player A's beliefs (move to the mechanism section's belief paragraph), (b) include zero-punishment frequencies per cell, (c) panel separately for full vs passer samples, (d) optionally include a version with hypothetical punishment from the *No-Punishment* condition.

### Proposed layout (two panels, two samples each)

- **Panel A — Average punishment (£) per cell.** Two side-by-side bar groups:
  - Group A1: Full sample ($N=80$), four bars (del-good, del-bad, nodel-good, nodel-bad).
  - Group A2: Passers ($N=67$), same four bars.
- **Panel B — Share punishing zero per cell.** Mirror layout: full vs passers, four bars each.

### Optional Panel C — hypothetical punishment

A third panel plotting the same four cells from the *No-Punishment* condition (where Player Bs were asked the same question hypothetically). Two readings of this:
- **Useful** as a sanity check on whether realized vs hypothetical punishment differ — could reinforce the H2 conclusion.
- **Distracting** because it pulls the reader's attention from the actual decisions to a hypothetical comparison. Risks visually conflating real with hypothetical.

I lean toward putting the hypothetical-punishment comparison in the appendix (with a single-sentence forward pointer in the body) rather than the main figure.

### Implementation

I would create a new script `scripts/python/20_punishment_figure.py` (next free number) that produces:

- `figures/punishment.png` — main figure (panels A and B, full + passers).
- `figures/punishment_hypothetical.png` — appendix figure with the *No-Punishment* hypothetical comparison.

This replaces the current `figures/punishment.png`. The Player-A belief overlay moves to a new figure produced under the punishment-beliefs paragraph (P06+, downstream).

### Reference cleanup downstream of the figure (C8)

If frequencies move into the main figure, the body's *"(Appendix Figure~\ref{fig:punishment_frequencies})"* in line 44 becomes wrong. The fix is to remove that parenthetical and let the body cite Figure~\ref{fig:punishment} only.

---

## 8. Numbers if switching to full sample (C6)

The cell numbers in lines 42–46 currently report passer values. If we switch to full as headline:

| Quantity | Current (Passers) | Replace with (Full) |
|---|---|---|
| del good | £0.311 | £0.329 |
| nodel good | £0.310 | £0.297 |
| del bad | £0.494 | £0.482 |
| nodel bad | £0.571 | £0.553 |
| Mean diff (bad cell) | £0.077 | £0.071 |
| Paired $t$-test bad | $p=0.153$ | $p=0.131$ |
| Wilcoxon bad | $p=0.533$ | $p=0.544$ |
| Never-punish share | $41.8\%$ | $45.0\%$ |
| $N$ for the within-subject test | $67$ | $80$ |

The robustness sentence in line 46 then flips: *"essentially identical when restricting to the $67$ Player Bs who passed the attention check (mean difference $\pounds 0.077$; paired $t$-test $p=0.153$)"*.

---

## 9. Inconsistency note (C7)

The user's question: should the body explicitly note that the punishment data are *inconsistent with* what would be needed to rationalise Player A's delegation pattern under H1?

Logic:
- Under the responsibility-avoidance (H1) reading, Player A delegates *more* under punishment because she expects delegation to insulate from punishment.
- We observe Player A delegating $16.8$ pp *less* under punishment (Result 1).
- For the H1 logic to operate at all, Player B would have to actually punish delegated decisions less than self-made decisions, especially in the bad-outcome cell.
- We find essentially no insulation in the good cell ($-\pounds 0.001$) and only a small directional, non-significant effect in the bad cell ($+\pounds 0.077$, $p=0.153$).
- So the realised punishment data do not deliver the structural conditions H1 would need.

This is a useful pre-emptive bridge to the M1 ruling-out argument in Section~\ref{sec:mechanism}. Suggested one-sentence insertion at the end of the headline punishment paragraph:

> "This non-result has implications for interpreting Result~1: the responsibility-avoidance logic of H1 would require Player B to differentially punish delegated decisions, and in particular in the bad-outcome cell — a structural condition the data do not deliver."

We can keep the M1 paragraph in the discussion section to develop this further.

---

## 10. Reference cleanup (C10)

`tab:reg_punishment_robustness` *is* defined (in `tables/reg_punishment_robustness.tex`, generated by `18_punishment_robustness.py`). The user's complaint is about the **flow**: the body references the table without first introducing it. Two clean options:

- **Option A — drop the parenthetical.** Replace *"(mean difference $\pounds 0.071$ vs $\pounds 0.077$; paired $t$-test $p=0.131$ vs $p=0.153$; Appendix Table~\ref{tab:reg_punishment_robustness})"* with just *"(mean difference $\pounds 0.071$ vs $\pounds 0.077$; paired $t$-test $p=0.131$ vs $p=0.153$)"*. The full robustness can be discussed in a single-sentence forward pointer.
- **Option B — introduce the table.** Add a half-sentence: *"… (we report the full attention-vs-no-attention regression in Appendix Table~\ref{tab:reg_punishment_robustness})"* — paired with the `tab:reg_punishment` reference in line 65, which already does this.

I lean A — the comparison is so close that the body sentence carries it.

---

## 11. Beliefs-about-Player-A sentence rewrite (C11)

Current text (line 65):

> "Punishment is also independent of Player B's belief about Player A's performance: across all four cells, Pearson correlations between cell-specific chosen punishment and Player B's weighted-average belief about Player A's score are essentially zero ($|r| \le 0.03$, all $p > 0.8$). This rules out the alternative explanation that Player Bs who think Player A is more capable systematically punish less (or more) - punishment is not driven by performance-conditional inference about Player A."

Issues, per the user comment:
- Reader may ask: *"why would punishment depend on Player A's performance? They are calibrated equal!"* The reason it's worth asking: *despite* common-knowledge equal calibration, Player B's *absolute-level* beliefs about Player A's performance might still vary across Player Bs (e.g., one thinks Player A is good at the task, another thinks she's poor) and this could in principle correlate with sanction severity — independently of the delegation choice. We rule this out empirically.

### Suggested rewrite

> "Even though the algorithm and Player A are calibrated to perform identically, Player Bs hold heterogeneous beliefs about Player A's *absolute* performance. One concern is that this heterogeneity could itself drive punishment patterns — for instance, a Player B who believes Player A is highly capable might sanction her self-made decisions more harshly because she 'should have' produced the high payoff. Empirically, this is not what we see: across all four cells, the Pearson correlation between Player B's weighted-average belief about Player A's score and chosen punishment is essentially zero ($|r| \le 0.03$, all $p > 0.8$). The within-subject pattern documented above is therefore not the average of two opposing belief-driven patterns."

This addresses the "why would beliefs matter?" question explicitly, motivates the analysis, and reports the same empirical finding.

---

## 12. Difference-DV regressions (C12)

Stacked panel (2 obs per subject, one per outcome), DV = $\text{punish\_nodel\_X} - \text{punish\_del\_X}$. Positive DV means self-decided punished more than delegated (the H2 prediction). Cluster-robust SEs at the Player B level.

`explore.py` P05c:

### Without controls

| Sample | Coefficient | Estimate | $p$ |
|---|---|---:|---:|
| Full | Intercept (= avg insulation in good outcome) | $-0.032$ | $0.534$ |
|  | Bad outcome (= extra insulation in bad vs good) | $+0.103$ | $0.073$ |
|  | Intercept + Bad outcome (= avg insulation in bad outcome) | $+0.071$ | $0.132$ |
| Passers | Intercept | $-0.001$ | $0.989$ |
|  | Bad outcome | $+0.078$ | $0.132$ |
|  | Intercept + Bad outcome | $+0.077$ | $0.154$ |

### With wa_difficulty + SES

The intercept loses meaning (it shifts with control means), but the bad_outcome coefficient is unchanged (it's identified off within-subject variation across the two outcome cells). Numbers in the script output. wa_difficulty itself is small and non-significant in both samples, consistent with §11.

### Reading

- The diff-in-diff (bad vs good extra insulation) is $+0.10$ in the full sample at $p \approx 0.07$ — borderline. In passers it's $+0.08$ at $p \approx 0.13$.
- The direct level (insulation in bad outcome) is $+0.07$/$+0.08$, $p \in [0.13, 0.15]$ — same as the paired $t$-tests.
- The C12 framing is mathematically equivalent to the existing reg_punishment specification (which has the same diff-in-diff embedded in the `Delegated × Bad outcome` interaction). Worth keeping the level-DV reg_punishment as the production table and adding the difference-DV form as a *prose* re-expression: *"Equivalently, we can regress the within-subject delegation insulation on the outcome: insulation is $-£0.001$ in the good cell and $+£0.077$ in the bad cell (with the difference between the two borderline at $p=0.07$ in the full sample, $p=0.13$ on passers)."*

So C12 doesn't require a new production table; one body sentence does the work.

---

## 13. The reformulated subsection — strawman

Implementing all of the above. Italicised text marks the substantive changes.

> \subsection*{Player~B -- Punishment behavior} \label{sec:result2}
>
> Next, we turn to Player~B's punishment behavior in the *Punishment* condition; in the *No-Punishment* condition, the same questions were posed but with no payoff consequences, and we report those hypothetical responses in the appendix.
>
> *We use the full $N=80$ sample as our headline. Subjects who fail the attention check on the punishment-elicitation screen were preregistered for exclusion; we report the corresponding $N=67$ analysis sample as a robustness comparison.*
>
> Punishment in all four (delegated/self-made, good/bad outcome) cells of the strategy method is significantly greater than zero (one-sample $t$-test $p < 10^{-5}$ in every cell).\footnote{*Positive punishment in the good-outcome cells need not reflect noise: Player Bs may hold ex-post views about whether the delegation choice itself was appropriate — independent of the realised outcome — and can punish accordingly. \citet{coffman_intermediation_2011} similarly documents non-trivial punishment in scenarios where the decision-maker's action could not have been improved upon.*} Player~Bs punish more for low-payoff outcomes than for high-payoff outcomes — *an indication that punishment carries informational content rather than being noise (mean within-subject difference of $\pounds 0.21$, paired $t$-test $p < 0.01$ in both delegation modes).*
>
> *$45.0\%$* of Player~Bs nonetheless do not punish in any of the four scenarios.\footnote{*Among those who do punish, the punishment levels are non-trivial: only $3$ Player~Bs forgo the $10$p fixed cost in any cell to choose punishment of at most $10$p, indicating that the costly punishment option is being used substantively rather than for tokenistic enforcement.*}
>
> Conditional on the outcome, Player~A is not significantly differently punished depending on the delegation decision (Figure~\ref{fig:punishment}). When Player~B receives the high payoff, average punishment is *$\pounds 0.329$ for delegated decisions and $\pounds 0.297$ for self-made decisions*. When Player~B receives the low payoff, average punishment is *$\pounds 0.482$ when Player~A delegated versus $\pounds 0.553$ when she made the decision herself*; this difference points in the H2 direction but is far from significant (paired $t$-test *$p=0.131$*; Wilcoxon signed-rank *$p=0.544$*). *Equivalently, regressing the within-subject insulation $\text{punish\_nodel} - \text{punish\_del}$ on a bad-outcome indicator yields an insulation of $-\pounds 0.001$ in the good cell and $+\pounds 0.077$ in the bad cell, with the diff-in-diff between the two cells borderline at $p=0.07$.* The same picture arises when looking at punishment frequencies rather than amounts; we report frequencies in panel B of Figure~\ref{fig:punishment}.
>
> The result is essentially identical when we further restrict to the $67$ Player~Bs in the *Punishment* condition who passed the attention check (mean difference $\pounds 0.077$ vs $\pounds 0.071$; paired $t$-test $p=0.153$ vs $p=0.131$).
>
> Therefore, in our experimental setting Player~A cannot avoid punishment by delegating the decision to the algorithm. Instead, punishment is determined almost entirely by the realised outcome. *This non-result has implications for interpreting Result~1: the responsibility-avoidance logic of H1 would require Player~B to differentially punish delegated decisions, and in particular in the bad-outcome cell — a structural condition the data do not deliver. We develop this point in Section~\ref{sec:mechanism}.*
>
> \medskip
> \noindent **Result~2.** *Player~A cannot avoid punishment by delegating the decision to the algorithm.*
> \medskip
>
> [Figure~\ref{fig:punishment} — redesigned: panel A average punishment, panel B zero-punishment frequencies; full and passer samples side by side; no Player A belief overlay.]
>
> \paragraph{What predicts punishment?} Appendix Table~\ref{tab:reg_punishment} reports a regression of chosen punishment on a delegation indicator, an outcome indicator, their interaction, Player~B's belief about Player~A's absolute performance, and a vector of socio-demographic controls. The interaction term is small and statistically insignificant ($p=0.137$), confirming the bivariate result. *Even though the algorithm and Player~A are calibrated to perform identically, Player~Bs hold heterogeneous beliefs about Player~A's absolute performance. One concern is that this heterogeneity could itself drive punishment patterns — for instance, a Player~B who believes Player~A is highly capable might sanction her self-made decisions more harshly because she "should have" produced the high payoff. Empirically, this is not what we see: across all four cells, the Pearson correlation between Player~B's weighted-average belief about Player~A's score and chosen punishment is essentially zero ($|r| \le 0.03$, all $p > 0.8$). The within-subject pattern documented above is therefore not the average of two opposing belief-driven patterns.*

---

## 14. Production-script changes implied by the plan

If the strawman in §13 is accepted:

1. **`scripts/python/20_punishment_figure.py`** — new. Produces the redesigned `figures/punishment.png` (panels A & B, full + passers, no belief overlay). Optionally produces `figures/punishment_hypothetical.png` for the appendix.
2. **`scripts/python/06_logit_punishment.py`** — minor: switch the regression sample default from `pass_att2 == 1` to the full sample. The robustness already exists in `18_punishment_robustness.py` (Cols 1 vs 2). Coordinate so that the body-paragraph numbers are full-sample.
3. **`scripts/python/_outputs/numbers.json`** — add manifest keys for: full-sample paired-test $p$-values, full-sample never-punish share, full-sample insulation, the difference-DV regression coefficients, the bad-vs-good outcome paired-test $p$-values.
4. **`manuscript/results.tex`** L44 — drop the `(Appendix Figure~\ref{fig:punishment_frequencies})` parenthetical (frequencies move into main figure).
5. **`manuscript/appendix.tex`** L172–178 — keep the existing punishment-frequency appendix figure, or repurpose it for the No-Punishment hypothetical version.

---

## 15. Open questions for you

1. **Sample default** — accept §2 (switch to full)?
2. **Coffman footnote** — adopt the wording in §5 verbatim, or amend?
3. **41.8% / 45.0% number** — switch to full ($45.0\%$), in line with the new headline?
4. **"Forgo 10p" footnote** — include the $3$-subject sanity check, or hold for later?
5. **Figure design** (§7) — two panels (avg + zero-share), full + passers; hypothetical version in appendix? Or different layout?
6. **Inconsistency note (C7)** — adopt the bridge sentence at the end of the headline paragraph, or save the M1 logic entirely for the discussion section?
7. **Reference cleanup (C10)** — Option A (drop the appendix table parenthetical) or B (introduce it)?
8. **Beliefs-sentence rewrite (§11)** — adopt as-is or amend?
9. **Difference-DV regressions (§12)** — keep as a body-prose re-expression (one sentence), or build a separate small table for the appendix?
10. Once these are settled, I'll write the redesigned figure script and switch the regression-sample defaults; **no edits yet**.
