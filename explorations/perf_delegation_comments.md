# Responses to inline comments: "Performance and delegation" (results.tex, lines 112-156)

Each comment is quoted, then answered. New numbers in this file were computed ad hoc from `data/clean` (same pipeline loaders); none are in the manifest yet. Where a reformulation is suggested, it feeds the rebuilt paragraph at the end. The intact copy of the old paragraph at line 151 should be deleted once a rebuilt version is adopted.

---

## Comment 1 (line 118)

> Across conditions, we have seen that performance loads negatively... (weakly significant) [only refer to first table.]

**Agree, with one precision.** Referring only to Table `tab:del_decision_determinants` also fixes a factual problem: `tab:reg_belief_specs` is restricted to the Punishment condition, so citing it as evidence "across conditions" was wrong. The precision: in Table 1, performance is negative but *insignificant* in the pooled specification (Column (3): $-0.119$, SE $0.079$) and weakly significant only among attention-check passers (Column (5): $-0.158$, $p=0.068$). The sentence should not attach "weakly significant" to the pooled sample, which would also contradict the earlier characterization at the top of the results section ("neither actual nor perceived performance is significantly associated... although... weakly significant under the attention restriction").

Suggested sentence:

```latex
A first indication appears in Table~\ref{tab:del_decision_determinants}, in which task performance enters negatively, weakly significantly so among attention-check passers (Column~(5)).
```

## Comment 2 (line 122)

> Do not argue with the correlation but with the regression coefficients. In doing so, do not put the info on passers into a footnote, but into the main text. Refer to tab:reg_belief_specs

**Agree, and the regression evidence is stronger than the correlation.** In `tab:reg_belief_specs` (Punishment condition throughout, conditional on the belief measure and socio-demographic controls), task performance enters:

| Column | Sample | Coefficient | p |
|---|---|---|---|
| (2) | full Punishment | $-0.208$ | $0.061$ |
| (3) | passers | $-0.362$ | $0.008$ |
| (4) | passers, weighted beliefs | $-0.342$ | $\approx 0.016$ |
| (5) | passers, decomposition | $-0.381$ | $\approx 0.006$ |

So the within-Punishment statement can be made with a weakly significant full-sample coefficient and a significant passers coefficient in the main text, no footnote needed. Suggested sentences:

```latex
Within the \textit{Punishment} condition, the relationship is considerably stronger. In the regressions of Table~\ref{tab:reg_belief_specs}, task performance enters negatively throughout, weakly significant in the full sample ($-0.21$, $p=0.061$, Column~(2)) and significant among attention-check passers ($-0.36$, $p=0.008$, Column~(3)).
```

(If preferred, the coefficients can be converted to AMEs for interpretability; the table currently reports AMEs only for the belief measure.)

## Comment 3 (line 126)

> Refer to figure here instead of before. Include correlation coefficients and the significance stars in the figure itself.

**Agree on both.** Moving the figure reference to the No-Punishment sentence works well because the figure's top panel is exactly the cross-condition comparison. The numbers for that sentence (computed, full samples): Punishment $r=-0.19$ ($p=0.092$); No-Punishment $r=-0.02$ ($p=0.84$). Among passers: $-0.22$ ($p=0.083$) and $-0.06$ ($p=0.63$). So "weaker" understates it; the relationship is absent in the No-Punishment condition, which is the better sentence.

For the figure: annotate the top panel of `performance_overview.png` with the per-condition correlation next to each series (legend entries "Punishment ($r=-0.19^{*}$)" and "No-Punishment ($r=-0.02$)"), stars per the house convention with p-values in the note. Implementation goes into `07_performance.py`; I will implement on approval and add `perf_del_corr_*` manifest keys for the four correlations.

Suggested sentence:

```latex
In the \textit{No-Punishment} condition, by contrast, performance and delegation are essentially unrelated ($r=-0.02$, against $r=-0.19$ in the \textit{Punishment} condition; Figure~\ref{fig:performance_overview}).
```

## Comment 4 (line 130)

> Remind me of the regression results in a separate .md file. What does tab:reg_belief_specs look like with perceived performance instead of actual performance.

**Computed.** Replacing `overall_score` with `wa_confidence` (weighted-average belief about own performance) in the Table 3 specifications:

| Spec | Belief measure | p | Perceived perf. | p |
|---|---|---|---|---|
| (2) full + controls | $+0.416$ | $0.367$ | $-0.080$ | $0.369$ |
| (3) passers + controls | $+1.329$ | $0.039$ | $-0.032$ | $0.776$ |
| (4) weighted, passers | $+1.742$ | $0.021$ | $-0.060$ | $0.579$ |
| (5) decomposition, passers | good $+0.696$ ($p=0.083$), bad $+0.607$ ($p=0.094$) | | $-0.032$ | $0.776$ |

For comparison, the production (actual-performance) versions of (2)/(3) have belief coefficients $+0.398$ ($p=0.374$) and $+1.661$ ($p=0.018$), with performance at $-0.208$ ($p=0.061$) and $-0.362$ ($p=0.008$).

Reading: perceived performance is never remotely significant in any specification, while the belief-measure coefficients survive the swap essentially unchanged (marginally attenuated among passers, $p=0.018 \to 0.039$). This directly supports the footnote's claim and can be cited as such. It does not warrant its own table in my view; a footnote sentence citing the passers numbers suffices (included in the rebuilt footnote below).

## Comment 5 (line 134)

> Which question do we answer with the figure in the Appendix? Do we need the figure?

**The question it answers:** "Do delegators differ from non-delegators in *actual* ability but not in *perceived* ability, and is this pattern specific to the Punishment condition?" The figure shows, for passers, the distributions of both measures by delegation choice in both conditions. It is the only place the No-Punishment delegator/non-delegator comparison is visible at all (means 2.98 vs 3.13 for actual, 4.85 vs 5.33 for confidence), and the overlapping confidence densities in the Punishment panel are the visual backing for "confidence does not reflect it."

**Do we need it?** Strictly, no — the claim in the footnote rests on two mean comparisons that can carry their own tests in text. Newly computed (passers, Punishment): actual $2.38$ vs $3.00$, $t$-test $p=0.083$; perceived $4.69$ vs $4.71$, $p=0.97$. Note the first is only weakly significant, so the current word "sharply" overclaims and should go regardless. My recommendation is to keep the figure: it is cheap (appendix), it backs a mechanism-relevant contrast with distributions rather than means, and dropping it would leave the "confidence does not reflect it" claim resting on a $p=0.083$ mean comparison alone. If it stays, its appendix note should state the question it answers in one sentence.

## Comment 6 (line 138)

> Explain in easier words...I don't know what this is supposed to mean: "framed at the level of treatment differences".

**What it was supposed to mean:** the previous sentences describe a within-condition association (inside the Punishment condition, better performers delegate less). The sentence then re-expresses the same fact as treatment-effect heterogeneity: comparing conditions, the delegation *gap* is larger among better performers — the treatment bites hardest at the top of the performance distribution.

**The problem is not only the phrasing.** As a standalone statistical claim, treatment-effect heterogeneity needs the interaction, and the interaction is not significant: a pooled Probit of delegation on Punishment $\times$ performance gives $-0.164$ ($p=0.286$) — right direction, no significance. The cross-condition evidence that *is* significant is the composition comparison (delegators' scores $2.47$ vs $3.06$, $p=0.039$), which the paragraph already contains. **Recommendation: delete the sentence** and let the composition comparison carry the cross-condition point, optionally with an honest footnote:

```latex
\footnote{A Probit interaction of the Punishment indicator with task performance points in the same direction but is not statistically significant ($-0.16$, $p=0.29$).}
```

This also protects the intro's "selectively among the decision-makers most likely to succeed," which should rest on the significant composition result rather than an unreported interaction.

## Comment 7 (line 142)

> the whole paragraph seems very convoluted. Can you please outline step by step the core line of reasoning? For each element, assess whether it is an important element and whether keeping it in is warranted. Which goal do we pursue and do we need a statement/analysis to reach that goal?

**Goal.** Establish that punishment does not reduce delegation uniformly but changes *who* delegates: it deters delegation specifically among better performers. This matters for three reasons. It deepens Result 1 from a level effect to a selective effect; it feeds the signaling mechanism (those with the most to signal keep the decision); and it grounds the intro claim "selectively among the decision-makers most likely to succeed."

**The core chain, step by step:**

1. *Pooled hint* (Table 1): performance enters negatively, weakly significant among passers. — **Keep, one sentence.** Honors the forward pointer from the Result-1 robustness paragraph; honestly weak.
2. *Within-Punishment association* (Table 3 regressions): negative, significant among passers ($-0.36$, $p=0.008$). — **Keep; this is the paragraph's central fact** (per Comment 2, regression-based, main text).
3. *No-Punishment contrast*: the association is absent there ($r=-0.02$). — **Keep, quantified**; without it the pattern is not treatment-specific and the paragraph has no case.
4. *Actual vs perceived*: perceived ability plays no role (never significant; delegators and non-delegators have identical confidence). — **Keep as footnote.** Mechanism-relevant (rules out a confidence story; delegators do not feel worse, they are worse) but supporting, not central.
5. *"Framed at the level of treatment differences..."* — **Delete** (Comment 6): unsupported as a standalone claim, and redundant with step 6.
6. *Composition comparison*: delegators under Punishment score 2.47 vs 3.06 under No-Punishment ($p=0.039$). — **Keep; the significant cross-condition statement** and the basis of Result 4's second sentence.
7. *"Middle and upper part of the performance distribution"* — **Soften to "better performers."** A distributional claim from a mean comparison; the defensible version costs nothing.
8. *Closing sentence* ("It is precisely these subjects...") — **Keep.** It converts the statistics into the sentence the mechanism section needs.

Every retained element has a distinct job: 1 = continuity, 2 = the fact, 3 = treatment-specificity, 4 = mechanism discrimination, 6 = cross-condition significance, 8 = the takeaway. The convolution came from elements 5 and 7 (claims without tests) and from the correlation/regression mixture, not from the chain itself.

## Rebuilt paragraph

```latex
\paragraph{Performance and delegation.} What differs across conditions is \textit{who} delegates. A first indication appears in Table~\ref{tab:del_decision_determinants}, in which task performance enters negatively, weakly significantly so among attention-check passers (Column~(5)). Within the \textit{Punishment} condition, the relationship is considerably stronger. In the regressions of Table~\ref{tab:reg_belief_specs}, task performance enters negatively throughout, weakly significant in the full sample ($-0.21$, $p=0.061$, Column~(2)) and significant among attention-check passers ($-0.36$, $p=0.008$, Column~(3)). In the \textit{No-Punishment} condition, by contrast, performance and delegation are essentially unrelated ($r=-0.02$, against $r=-0.19$ in the \textit{Punishment} condition; Figure~\ref{fig:performance_overview}).\footnote{Perceived performance plays no comparable role. Replacing actual with perceived performance (the weighted-average belief about own performance) in Table~\ref{tab:reg_belief_specs} leaves the belief coefficients essentially unchanged, while perceived performance is never significant (e.g., $-0.03$, $p=0.78$, among passers). Accordingly, actual performance differs between delegators and non-delegators ($2.38$ vs.\ $3.00$ correct out of ten among attention-check passers; $t$-test $p=0.083$) while perceived performance does not ($4.69$ vs.\ $4.71$; $p=0.97$; Appendix Figure~\ref{fig:performance_by_delegation}). Delegators under punishment are not subjects who believe they perform badly, but subjects who do perform badly, and whose confidence does not reflect it.} The composition of delegators shifts accordingly. Player~As who delegated in the \textit{Punishment} condition scored on average $2.47$ out of ten in the first ten rounds, whereas delegators in the \textit{No-Punishment} condition scored $3.06$ ($t$-test $p=0.039$).\footnote{A Probit interaction of the Punishment indicator with task performance points in the same direction but is not statistically significant ($-0.16$, $p=0.29$).} The additional delegation in the \textit{No-Punishment} condition thus comes disproportionately from better performers. It is precisely these subjects who, when punishment is on the table, keep the decision for themselves.
```

Changes to other artifacts if adopted:

- `07_performance.py`: annotate the top panel with per-condition correlations and stars (Comment 3); add the four correlations, the interaction estimate, and the delegator/non-delegator tests to the manifest so every number above is pipeline-backed.
- The footnote replaces "worse than their algorithm" (a comparison the calibrated design rules out) with believed vs actual own performance, and drops "sharply" (the $p=0.083$ does not carry it).
- Delete the old duplicate paragraph at line 151 and the exploded working copy once merged.
```
