# Lens 4 — Results and Tables

Seven-pass adversarial review, pass 4 of 7.
Manuscript: "Accountability and Algorithmic Delegation: Experimental Evidence"
Scope reviewed: `manuscript/results.tex`, `manuscript/appendix.tex`, all `tables/*.tex` reached by `\input`, all `manuscript/figures/*.png`, cross-checked against `abstract.tex`, `introduction.tex`, `design.tex`, `conclusion.tex`.
Not reviewed (not compiled): `literature_revised.tex`, `results_pre_restructure_2026-05-06.tex`.

**Counts: 3 CRITICAL, 12 MAJOR, 12 MINOR.**

---

## What passes cleanly

Before the findings, the arithmetic that does check out. I verified every headline number in the prose against the tables, the figures, and (where the manuscript is silent) the cleaned data in `data/clean/delegator_cleaned.parquet`.

- 42.5% / 59.3% / 16.8 pp delegation shares reconcile exactly with n=80 and n=81, with `delegation_shares.png`, with the abstract, and with the introduction's "roughly 17 percentage points".
- The hypothetical-switching footnote (`results.tex:10`) is arithmetically exact: 48 delegators, 12 switch off (25.0%), 33 non-delegators, 5 switch on (15.2%), implied rate 41/81 = 50.6%.
- All five AMEs in `tables/reg_delegation.tex` (−16.8 to −19.4, max p = 0.031) match `results.tex:29`.
- The four punishment cell means (0.33 / 0.30 / 0.48 / 0.55) reconcile with `punishment.png`, with the £0.20 outcome effect, and with the regression decomposition in `tables/reg_punishment.tex` (0.032 and 0.032 − 0.103 = −0.071).
- All belief AMEs (4.7 / 5.5 / 2.7 / 1.7 pp per £0.10 and their p-values) match `tables/reg_belief_specs.tex` exactly.
- Performance means reconcile across every cut: 2.76 / 3.09 overall, 2.47 / 3.06 among delegators (Welch p = 0.039, confirmed), 2.98 / 3.12 among non-delegators (p = 0.653, confirmed), 21.7% / 45.5% final-prediction success (10/46 and 15/33, confirmed).
- Extensive-margin appendix numbers (18 pp, −1.8 pp p=0.46, −2.9 pp p=0.29) match `tables/reg_punishment_extensive.tex`.
- Ns reconcile with 161 per role throughout (80 + 81; 159 after two missing-covariate drops; 78 within the Punishment condition, consistent with both drops being Punishment-condition subjects).
- Every compiled table and figure is referenced in the text; nothing referenced is missing; the LaTeX log shows zero undefined references.
- **Ordering (rubric 6) passes.** H1 is stated first in `design.tex:93` and tested first (`results.tex:7`); H2 second (`design.tex:99`, tested at `results.tex:33`); mechanisms follow. Result numbering 1–5 is monotone in the file.

The internal-consistency problems below are therefore not sloppy arithmetic. They are mislabelled quantities, claims contradicted by the figures they cite, and evidence that is asserted but never shown.

---

## CRITICAL

### C1. A footnoted claim is contradicted by the appendix figure it cites, and by the data

`results.tex:81`, footnote:

> "The same holds for the fully hypothetical beliefs elicited in the \textit{No-Punishment} condition, which closely track those in the \textit{Punishment} condition (Appendix Figure~\ref{fig:punishment_hypothetical}). The treatment manipulation itself therefore appears not to have changed what subjects expected punishment to be."

The cited figure shows the opposite. Player A's anticipated punishment, by condition:

| Scenario | Punishment (Fig. 3) | No-Punishment (Fig. A3) | difference | Welch p |
|---|---|---|---|---|
| Delegated, good | 0.62 | 0.51 | −0.11 | 0.299 |
| Self-decided, good | **0.60** | **0.40** | **−0.21** | **0.038** |
| Delegated, bad | 0.92 | 0.89 | −0.03 | 0.768 |
| Self-decided, bad | 0.98 | 0.87 | −0.11 | 0.250 |

(Verified against `data/clean/delegator_cleaned.parquet`, columns `belief_*`; the figure values are exact.)

Two problems. First, one of the four cells differs across conditions at p = 0.038, so "the treatment manipulation appears not to have changed what subjects expected punishment to be" is a claim the data reject at the 5% level. Second, and worse for the argument, the *belief difference* that Result 3 is built on flips sign:

- Good-outcome difference (no delegation − delegation): **−0.018** in *Punishment*, **−0.117** in *No-Punishment*.
- Bad-outcome difference: **+0.057** in *Punishment*, **−0.022** in *No-Punishment*.

The good-outcome difference is precisely the variable that `results.tex:101` says "carries the relationship" with delegation. A sign flip across conditions in the mechanism variable is material, and the footnote currently tells the reader the two conditions are interchangeable. Either drop the "closely track" sentence and report the four comparisons honestly, or make the sign flip part of the mechanism discussion.

### C2. The H2 interaction coefficient is described as a quantity it is not

`results.tex:54`:

> "The \textit{Delegated}~$\times$~\textit{Bad outcome} interaction, which captures any insulation from punishment after bad outcomes, amounts to $-0.103$ and is weakly significant ($p=0.08$)."

The interaction does not capture insulation after bad outcomes. It captures the difference-in-differences, that is, the bad-outcome delegation gap *minus* the good-outcome delegation gap. Insulation after a bad outcome is `Delegated + Delegated × Bad outcome` = 0.032 − 0.103 = **−0.071**, which is exactly the £0.07 with p = 0.13 already reported eleven lines earlier at `results.tex:48`.

So the manuscript reports two different numbers for the same H2 quantity, £0.07 (p = 0.13) and £0.103 (p = 0.08), never reconciles them, and attaches the "weakly significant" label to the mislabelled one. Because Hypothesis 2 is stated in levels ("Conditional on a low-payoff outcome, Player~B punishes Player~A less when she delegated", `design.tex:99`), the correct test is the £0.07 gap. A referee who checks the saturated within-subject arithmetic will find this immediately. Fix by describing −0.103 as the difference-in-differences and reporting the bad-outcome linear combination separately.

### C3. "Overconfidence" is reported as a level, not as a difference

`results.tex:110`:

> "Player~As in both conditions also exhibit similar overconfidence about their own performance ($4.65$ vs.\ $4.87$, respectively)."

4.65 and 4.87 are the means of `wa_confidence`, the weighted-average *belief about own score* (verified: 4.653 and 4.871). They are perceived-performance levels on the 0–10 score scale, not overconfidence. Overconfidence is perceived minus actual, that is **1.89** and **1.78**. Presenting a belief level under the label "overconfidence" is a units error of exactly the kind rubric 4 targets, and it sits in the sentence that is supposed to rule out a composition artifact. Note that `tables/reg_delegation_robustness.tex` (uncompiled) defines overconfidence correctly as "the weighted-average belief about own performance minus actual performance", so the manuscript and the table code disagree on the definition.

---

## MAJOR

### M1. Result 5 rests on evidence that is never quantified or tested

`results.tex:139`:

> "By this measure, non-delegators in the \textit{No-Punishment} condition improve, whereas non-delegators in the \textit{Punishment} condition do not."

and `results.tex:142`, Result 5:

> "Non-delegators improve on their performance less in the \textit{Punishment} condition than in the \textit{No-Punishment} condition."

No magnitude, no test statistic, no table, no figure. This is the sole quantitative evidence for a numbered Result and for the intro's claim that "improvement concentrates where punishment is impossible" (`introduction.tex:14`) and the conclusion's "Prediction outcomes and screen times do not indicate punishment-induced additional effort" (`conclusion.tex:8`). Rubric 2 is violated at its strongest point, an effect reported with neither magnitude nor significance.

I reconstructed the measure from the raw data (mean absolute prediction error over rounds 1–10 minus absolute error on the final prediction, non-delegators only):

| Condition | n | improvement (lbs) | vs. zero | median |
|---|---|---|---|---|
| Punishment | 46 | +0.51 | p = 0.79 | −1.30 |
| No-Punishment | 33 | +10.94 | p = 0.005 | +12.10 |
| Between conditions | | | t-test p = 0.007, Mann-Whitney p = 0.006 | |

The claim is correct and the effect is large. There is no reason to leave it unstated. Report the two improvements in pounds of prediction error and the between-condition test.

### M2. The outcome comparison behind Result 5 is reported with no test

`results.tex:139`: "$45.5\%$ of non-delegators in the \textit{No-Punishment} condition earn the high payoff for Player~B, compared with $21.7\%$ in the \textit{Punishment} condition". A 23.8 pp difference is presented bare while the *balance* comparison in the same sentence gets a t-test and a p-value. Fisher's exact on 15/33 versus 10/46 gives p = 0.030. Report it.

### M3. The improvement comparison is justified by balance on a different metric than the one it uses

Same sentence, `results.tex:139`: the contrast is defended on the grounds that "the two groups' performance over the first ten rounds is statistically indistinguishable ($3.12$ vs.\ $2.98$ correct predictions; $t$-test, $p=0.66$)". But the improvement measure is built on **absolute prediction error**, not on the binary hit count, and on that metric the two groups are not similar at all. Mean first-ten-round absolute error is 22.47 lbs (Punishment) versus 30.85 lbs (No-Punishment), with a standard deviation of 4.67 versus 33.23. The No-Punishment non-delegator group contains extreme-error outliers (top improvement values include +90.2 lbs), and a group starting from a higher baseline error mechanically shows more mean reversion.

The result survives the concern (medians 21.2 versus 22.4, Mann-Whitney on baseline error p = 0.62, Mann-Whitney on improvement p = 0.006), so this is fixable rather than fatal. But the manuscript must justify the comparison on the metric it actually uses, and should report the median or a trimmed version alongside the mean.

### M4. Two compiled regression tables display significance stars with no legend

`tables/reg_punishment.tex` shows `0.256^{***}` and `-0.103^{*}`; `tables/reg_belief_specs.tex` shows `1.661^{**}`, `-0.362^{***}`, `0.950^{**}` and others. Neither note defines what one, two, or three stars mean. `tables/reg_delegation.tex` and `tables/reg_punishment_extensive.tex` both carry the legend. The tables therefore cannot be read on their own (rubric 1), and the four compiled tables are mutually inconsistent in whether they explain their own notation.

### M5. Standard-error type is stated inconsistently across the paper

`results.tex:5` makes a blanket claim: "Regressions report robust (HC1) standard errors." This is false for two of the four compiled regression tables. `tables/reg_punishment.tex` and `tables/reg_punishment_extensive.tex` both say "Standard errors clustered at the Player~B level", which is the correct choice for a design stacked over four scenarios per subject. The blanket footnote should be scoped, or each table's note should be the single source of truth. As it stands a reader is told the punishment regressions use HC1 when they do not.

### M6. Significance-star policy is inconsistent across the repository's own tables

`tables/reg_delegation_robustness.tex` and `tables/reg_punishment_robustness.tex` both state in their notes: "Following AEA editorial policy, significance stars are not reported." Every compiled table does report them, as do Figure 1 (`^{**}\,p<0.05` in the note at `results.tex:23`) and Figure 2 (`+£0.20***` printed inside `punishment.png`). Whichever convention the paper settles on, the artifacts currently contradict each other in writing. This needs harmonising before submission.

### M7. "Considerably stronger under punishment" is asserted without a comparable estimate

`results.tex:112`:

> "this relationship is considerably stronger in the \textit{Punishment} condition (Table~\ref{tab:reg_belief_specs}) than in the \textit{No-Punishment} condition (Figure~\ref{fig:performance_overview})."

This is the load-bearing claim for Result 4 and for the "activation by the prospect of punishment" argument at `results.tex:135` and `conclusion.tex:8`. The comparison is between a probit coefficient from Table 3 (Punishment condition, attention-check passers only, belief regressors included, −0.362) and a figure. No No-Punishment estimate is ever reported, and no treatment-by-performance interaction is ever estimated. The two objects being compared differ in sample, in covariate set, and in one being a coefficient and the other a picture. Either add a pooled specification with a `Punishment × Task performance` interaction, or downgrade the claim to descriptive language.

### M8. Figure 4's only quantitative content is undocumented and unmentioned

`performance_overview.png` prints `r = −0.19*` and `r = −0.02` on the top panel. These two numbers are the closest thing the paper has to a formal contrast for M7, and:

- the figure note (`results.tex:125`) never mentions them, so the reader cannot tell what correlation this is (point-biserial between the binary delegation indicator and score, presumably), on what sample, or what the star means;
- the main text never cites them either.

Add them to the note with the correlation type, n, and p-value, and use them in the text.

### M9. The results section contradicts itself on whether performance predicts delegation

`results.tex:29`: "Neither actual nor perceived performance is significantly associated with delegation in the pooled sample, although actual performance enters negatively and is weakly significant under the attention restriction ($p=0.068$)."

`results.tex:112`: "Task performance is negatively associated with the decision to delegate across conditions (Table~\ref{tab:del_decision_determinants}, Column~(5))."

Column (5) *is* the attention restriction, so the second sentence quietly promotes a p = 0.068 result to an unqualified association and describes it as holding "across conditions" without flagging that the pooled full-sample estimate (Column 3, −0.119, SE 0.079) is insignificant. Pick one characterisation and state the sample restriction in both places.

### M10. Attention-check pass rates are never reported, yet the belief mechanism exists only among passers

The paper conditions on attention-check passers in Table 1 Column (5), Table 2 Column (2), Table 3 Columns (3)–(5), and three appendix figures. It never states how many subjects passed or failed, per role or per condition. From the tables, Player A goes from 161 (159 with covariates) to 130, implying roughly a 19% failure rate. Player B goes from 80 to 67 in the Punishment condition, roughly 16%.

This matters because Table 3 tells a stark story: the belief–delegation relationship is flatly null in the full Punishment sample (Columns 1–2, AMEs 1.3 and 1.4 pp, p = 0.388 and 0.370) and appears only among passers (Columns 3–5, 4.7 and 5.5 pp, p = 0.011 and 0.006). The text at `results.tex:99` handles this with two words, "the relationship sharpens". A referee will read a null that becomes significant when 25% of the sample is dropped, and will want the pass rate, the pre-registration status of the exclusion (the appendix at `appendix.tex:110` says the preregistration "left open whether participants who failed the attention checks would be excluded"), and a statement of how many observations the restriction removes.

### M11. Table covariates are defined only in an appendix note that appears after the tables that use them

Tables 1 and 3 both include `Socio-economic status`, `Technology score`, `Went to uni`, `Leadership position`, `Task performance`, and `Perceived performance`. None of these is defined in either table's note. The definitions live in the note to `tables/balance_player_a.tex`, which appears in Appendix A, roughly twenty pages later. Table 1 also never states its sample (both conditions pooled, Player A only), the coding of the dependent variable, or the sign convention of the `Punishment indicator`. Rubric 1 fails for the paper's two central tables. The fix is mechanical: one added sentence per note giving sample, units for `Task performance` (0–10 correct predictions) and `Perceived performance` (weighted-average belief on the same 0–10 scale), and a one-line covariate gloss.

### M12. No power or equivalence analysis anywhere, despite an MDE table sitting in `tables/`

Result 2 (`results.tex:51`) is a null: "Player~B does not punish delegated decisions significantly less than self-made ones." The abstract and conclusion both promote it to a positive claim ("Recipients punish delegated and self-made predictions alike"). With 80 Player Bs and an £0.07 point estimate, the paper needs to show that it could have detected an economically meaningful gap. It never does. `grep` over the compiled files finds one hit for "power", a commented-out `\todo` at `results.tex:169`.

Meanwhile `tables/power_mde.tex` exists, is not `\input` anywhere, and its note refers to "the equivalence bound used in Result~2 in the body of the paper, equal to $10\%$ of the maximum punishment of \pounds 2" — an equivalence bound that does not exist in the current body text. So the manuscript has a stale artifact describing an analysis that was removed. Either restore the equivalence framing and include the MDE table in the appendix, or delete `power_mde.tex`. For AER/QJE, a headline null without a power statement is a predictable desk-stage objection.

---

## MINOR

1. **Five orphan figures.** `belief_distributions.png`, `beliefs_vs_performance.png`, `performance_by_delegation.png`, `punishment_vs_beliefs.png`, `punishment_vs_beliefs_shares.png` are in `manuscript/figures/` and referenced by nothing compiled. Two of them (`beliefs_vs_performance`, `performance_by_delegation`) are referenced only inside commented-out appendix blocks at `appendix.tex:21-45` and `appendix.tex:91-102`.

2. **Claims whose supporting appendix material is commented out.** `results.tex:81` asserts "The expected punishment penalty for delegation is statistically indistinguishable from zero in both outcome states, and a within-subject test finds no asymmetry between the two"; `results.tex:104` repeats "We find no such asymmetry"; `results.tex:129` asserts "perceived performance is statistically indistinguishable between delegators and non-delegators". All three numbers live in the commented block at `appendix.tex:24-28` and `appendix.tex:100` (the difference-of-differences of +0.075, t = 0.99, p = 0.325; the 4.69 versus 4.71 comparison). As compiled, three claims have zero numerical support. Either restore the appendix subsections or inline the statistics.

3. **Passers N mismatch, 60 versus 61.** `appendix.tex:72` states Player A passers n = 61; `tables/reg_belief_specs.tex` reports N = 60 in Columns (3)–(5). The one-observation gap is presumably a missing covariate, consistent with the two drops elsewhere, but nothing says so. Add a clause to the table note.

4. **Performance balance asserted without a test.** `results.tex:110`: "Average performance in the first ten rounds is balanced across conditions ($2.76$ vs.\ $3.09$ ...)". No p-value (it is 0.121, confirmed), and performance does not appear in `tables/balance_player_a.tex`. Add the row to the balance table or the p-value to the sentence.

5. **Balance table reports no N and no dispersion.** `tables/balance_player_a.tex` gives means and p-values only. Add per-condition N (80 / 79 after the two drops, per the F-test at `appendix.tex:11` with N = 159) and standard deviations.

6. **Punishment magnitudes are never anchored economically.** `results.tex:35` calls punishment "substantial" at £0.30 to £0.55 without relating it to the £2 cap (15% to 28%) or to Player A's mean earnings of £3.63 stated at `results.tex:3`. The £0.20 outcome effect likewise never gets a share interpretation. Rubric 2 is only partly satisfied here.

7. **Extensive-margin shares called "indistinguishable" with no test.** `results.tex:60` says the shares are indistinguishable and points to `punishment.png`'s right axis (32% versus 32%, 49% versus 52%). The figure note's bracket p-values (`results.tex:44`) cover only average punishment, not the shares. The supporting test exists in Appendix Table A2, so a cross-reference in that sentence is enough.

8. **Figure annotations use stars with no in-figure legend.** `punishment.png` prints `+£0.20***`; `performance_overview.png` prints `r = −0.19*`. Neither figure note defines the symbols.

9. **"Weighted-average belief about own performance" is never formally defined.** `design.tex:76` describes the elicitation (probability mass over scores 0–10) but never names or defines the summary statistic. The construct is first named at `results.tex:29` and glossed circularly in the footnote at `results.tex:110`. One sentence in the design section fixes it.

10. **Ambiguous column-group header.** `tables/reg_belief_specs.tex` labels Columns (1)–(2) "Full Punishment", which reads as a treatment name rather than "full sample, Punishment condition". Rename to "Punishment, full sample" to match the sibling label "Punishment, passers".

11. **Thin bootstrap.** `tables/reg_punishment_extensive.tex` computes AME p-values from "a seeded $400$-replication subject-cluster bootstrap". 400 replications is low for p-values reported to three decimals; 2,000 or more is the usual floor.

12. **Appendix figure sizing.** `punishment_passers.png` and `punishment_hypothetical.png` are set at `width=0.65\linewidth`. At 200 dpi and a 6.7 in natural width against a 17 cm text block, axis text renders at roughly 6.5 pt, the smallest type in the document. Body figures at 0.75 and 0.9 render at roughly 7.5 pt and are fine. Consider 0.8 for the two appendix figures, particularly `punishment_hypothetical.png` with its five-entry legend.

---

## Cross-lens notes (out of my scope, flagged for whoever owns them)

- `results.tex:3` dates collection "between February and June 2023" while `appendix.tex:108` states preregistration on May 30, 2023, "after the collection of a pilot sample and before the collection of the main sample". The pooling decision is settled and correct; my only observation is that the *results section* never tells the reader the sample has two waves, so the appendix is where a reader first learns that part of a "preregistered" sample predates the preregistration. Disclosure wording, not analysis. Likely Lens 3 or Lens 5.
- Two overfull hboxes in `main.log` at lines 789 and 800 (14.7 pt and 1.8 pt). Typesetting, likely Lens 6.
- `main.tex:73` still carries `\hl{[To do: Add acknowledgments]}`.

---

## Top 3

1. **C1** — the `results.tex:81` footnote claims the two conditions' punishment beliefs "closely track" each other and that the manipulation did not move beliefs. The appendix figure it cites shows a £0.21 gap in one cell (p = 0.038) and a sign flip in the good-outcome belief difference, which is the variable Result 3 is built on.
2. **C2** — `results.tex:54` describes the −0.103 `Delegated × Bad outcome` interaction as "insulation from punishment after bad outcomes". It is the difference-in-differences. The bad-outcome insulation is −0.071 with p = 0.13, already reported six lines earlier, so the paper carries two numbers for the same H2 quantity and labels the wrong one weakly significant.
3. **M1** — Result 5 states a numbered finding with no magnitude, no test, no table, and no figure. The underlying effect is large and clean (+10.94 versus +0.51 lbs of error reduction, between-condition p = 0.007) and simply needs to be reported.

## Score

**6 / 10.**

The numerical spine is sound. Every headline share, coefficient, AME, and N reconciles across prose, tables, figures, abstract, introduction, and conclusion, and the results follow the hypothesis order. What holds the score down is that the three mechanism Results (3, 4, 5) are each supported by something the paper does not show: a footnote contradicted by its own figure, a "considerably stronger" comparison with no comparable estimate, and an improvement claim with no numbers at all. Add the mislabelled interaction, the missing table-note infrastructure, and the absent power analysis behind a headline null, and the results section is not yet at AER/QJE standard. None of it is hard to fix, and most of the missing numbers already exist in the data.
