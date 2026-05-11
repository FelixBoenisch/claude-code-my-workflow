---
title: "Review of mechanism discussion (results.tex lines 119–173)"
date: "2026-05-11"
scope: "Heterogeneity-by-performance → Inherent uncertainty → Performance differences → Effort exertion → In sum"
---

# Flow and logical issues

These are problems I would flag independent of the inline comments.

## F1. Terminology drift: "Baseline" vs "Punishment"

Lines 140 and 167 still use "Baseline" where the rest of the section uses "\textit{Punishment}". Reading context:

- Line 140: "Finding this relationship in the \textit{Baseline} condition only…" — the relationship is the negative performance→delegation slope, which lives in the Punishment arm. So "Baseline" here = Punishment.
- Line 167: "…increased effort for the decision for Player B in the Baseline condition" — context (line 165) is that effort actually went up in No-Punishment, not Punishment; the sentence is the negation of the M2-style hypothesis "Player~A in Punishment exerts extra effort", so "Baseline" here also = Punishment.

Both are leftovers from an earlier naming convention. Replace with "\textit{Punishment}" for consistency with [results.tex:7](../../manuscript/results.tex#L7), [results.tex:24](../../manuscript/results.tex#L24), [results.tex:119](../../manuscript/results.tex#L119).

## F2. Line 119 says the same thing twice

Within one paragraph: "Player~As who performed better on the first ten rounds were less likely to delegate" and "This suggests that when punishment is possible, better-performing Player As are less inclined to delegate the decision." The two sentences are identical in content; the second can be cut or merged into the next-paragraph transition.

## F3. Broken sentence at line 123

"The pattern that Player~As who have a higher subjective probability of producing the high payoff for Player~B prefer to bring about that good outcome themselves rather than via the algorithm." — no main verb. Should read e.g. "The pattern \textit{suggests} that…" or "\textit{One reading of} the pattern is that…".

## F4. M3 ↔ M1 boundary is fuzzy (line 123 final sentence + line 125 comment)

The closing sentence at line 123 — "The absence of this relationship in the \textit{No-Punishment} condition is consistent with process ownership being amplified by the moral salience that the punishment possibility introduces" — is exactly the move the user flags in the line-125 comment as collapsing into the belief channel. See **C4** below for a longer treatment; the structural problem is that the paragraph offers process ownership *plus moral-salience amplification* as the M3 story, but moral-salience amplification is doing the work of M1 in a different vocabulary. Pick one.

## F5. Inherent uncertainty (line 144) is in the wrong place

The paragraph notes — correctly — that the inherent-uncertainty story "would apply to treatment and baseline equally" and therefore cannot explain Result~1. But it's presented inside the mechanism-for-Result-1 section, which sets a candidate-mechanism expectation. The natural home for this argument is either (a) earlier, alongside the candidate channels in the belief discussion, or (b) demoted to a footnote in the heterogeneity paragraph. As written it reads like a candidate the section forgot to dispose of.

## F6. M4 (experimenter demand) is missing

The earlier draft of "In sum" (visible to me in an earlier conversation snapshot) listed four candidate mechanisms M1–M4, with M4 = experimenter demand. The current text discusses M1 (belief channel, in the prior section), M2 (effort, line 161), M3 (process ownership, line 123). M4 is not addressed. The line-173 "In sum" should either reintroduce it or the paper should be explicit that the demand-effect interpretation has been parked.

## F7. Citation placeholders

- Line 144: "Bharti and Dietvorst" — not formatted as `\citet` and the bibkey isn't in the verbatim text (`\cite{...}` missing).
- The TODO list lines (205–211) reference "Gogoll and Uhl 2018" and "Feier et al." informally; these are notes, not body text, so this is fine — but worth confirming the Bharti–Dietvorst cite is added to `Bibliography_base.bib`.

## F8. Order-of-operations: heterogeneity vs. performance-balance-and-overconfidence

Line 146 (Performance differences and overconfidence) plays the role of a robustness check: it shows Result~1 isn't an artifact of ex-ante performance differences. Logically, this should run *before* the heterogeneity-by-performance discussion, not after — currently the reader is asked to find heterogeneity by performance interesting before being told that average performance is balanced across treatments. Consider promoting [results.tex:146](../../manuscript/results.tex#L146) to sit between Result~1 (line 24) and the Heterogeneity paragraph (line 119), or at minimum forward-referencing it from line 119.

---

# Per-comment responses

## C1 — line 119 footnote suggestion

> "Footnote – Similarly, the delegation decision of Player~A is negatively related to her own beliefs about her performance, even though not significantly so."

**Supported by the data; safe to add as a footnote.** Earlier today I ran the
`reg_belief_specs.tex` variant with `wa_confidence` in place of `overall_score`
(see the earlier comparison): `wa_confidence` carries a small negative
coefficient (b ∈ [−0.14, −0.06]) and is never significant (p ∈ [0.36, 0.75]).
That matches the "negatively related … but not significantly so" framing.

**Suggested footnote text:**
> "A similar relationship holds for \textit{perceived} performance: Player~A's
> weighted-average belief about her own task performance enters the Logit with
> a small negative coefficient but is never statistically significant (e.g.,
> $b=-0.06$, $p=0.75$ in the passers-with-controls specification)."

## C2 — line 121: Feier et al. contrast

> "Here it makes sense that the worse you are, the more likely you delegate, because it increases expected success for the third party. But in my experiment this is not clear and therefore more interesting. Maybe point this out?"

**Yes, worth pointing out — it's a clean contrast that motivates the puzzle.** In Feier et al.'s setting, the algorithm is *known to be better* than the human, so the negative-performance-to-delegation slope is rationalised by expected-utility: a worse subject delegates because the algorithm strictly dominates her on expected accuracy. In our design, the algorithm and Player~A are common-knowledge *equal* in expected accuracy on the final prediction, so an expected-utility benchmark predicts **no** performance gradient in delegation. Finding one in the Punishment arm is therefore not a mechanical consequence of the design — it has to come from something else (a non-EU preference like process ownership, or a misperception of relative ability).

**Suggested insertion** (after line 119, perhaps as a footnote or short transitional sentence):

> "This contrasts with \citet{feier_hiding_2022}, where worse-performing subjects rationally delegate more because the algorithm is known to be \textit{superior}; in our design, where the algorithm and Player~A are common knowledge to perform equally well in expectation, no such gradient is predicted by expected-utility maximisation, which makes the observed pattern in the \textit{Punishment} condition substantively informative."

## C3 — line 123: the "amplified by moral salience" sentence

This is the sentence the user already asked about earlier today; the analysis from that exchange still applies (process-ownership-as-latent-preference, moral salience as switch). The short version: as written, the sentence makes an extra theoretical commitment (a moderator the data can't separately identify) and ends up looking like a relabelling of M1. See F4 above and C4 below. **My recommendation: cut the sentence, or downgrade it to "one reading…" hedging.**

## C4 — line 125: M3-amplified vs M1 belief channel

> "If we say that only punishment makes this a relevant channel, then how is it different from this belief channel we discussed before?"

**The user is right that the boundary needs to be drawn explicitly.** The cleanest distinction:

- **M1 (anticipated differential punishment)** predicts that delegation responds to *expected punishment asymmetries* — specifically, that Player~A delegates less when she expects relatively harsher punishment for delegated decisions. The earlier section ruled M1 out on its own terms: A's elicited beliefs do *not* show the required asymmetry (we tested this — see C5a below — the difference of differences is +0.08 with p > 0.32).
- **M3 (process ownership)** predicts that delegation responds to *who is the proximate cause* of the outcome — Player~A wants to personally deliver a good outcome to Player~B regardless of what punishment she expects. Under M3, beliefs about punishment do nothing; the operative quantity is "who acts."

The punishment-availability condition is doing different work in each:

- Under M1, punishment availability matters because it changes the *expected payoff penalty* attached to delegation (and the data shows it doesn't change beliefs in the asymmetric way M1 requires).
- Under M3, punishment availability matters because it makes the *third-party stake real* — Player~B actually has skin in the game, in a way that activates the prosocial process-ownership preference even though no beliefs about being-punished-for-delegating change.

The current line 123 sentence ("moral salience … amplifies … process ownership") tries to graft this distinction onto the existing M1 vocabulary and ends up muddying it. **Cleaner phrasing for the M3 case (suggested replacement for the closing sentence of line 123):**

> "The pattern is consistent with process ownership being behaviourally consequential only when Player~B's payoff is at meaningful third-party stake — present in the \textit{Punishment} arm, where Player~B can sanction; absent in the \textit{No-Punishment} arm, where Player~B receives the payoff but has no enforcement role. Importantly, this does not require Player~A to anticipate \textit{differential} punishment for delegated vs.\ self-made decisions; the elicited beliefs show no such asymmetry (Result~2 footnote)."

This makes M3 and M1 verbally distinct: M3 = "Player~B has meaningful stake → I want to personally deliver"; M1 = "Player~B will punish me extra for delegating → I delegate less to avoid the penalty."

## C5a — line 140: "What does the analysis look like here?" (belief asymmetry)

> "Player~As expect a relatively larger punishment penalty for delegation in good-outcome states than in bad-outcome states"

**Tested. The data does not support this asymmetry.** Defining the punishment penalty for delegation as $\Delta^{\text{good}} = \text{belief\_del\_good} - \text{belief\_nodel\_good}$ and analogously for the bad outcome:

| Sample        | $\Delta^{\text{good}}$ | $\Delta^{\text{bad}}$ | $\Delta^{\text{good}} - \Delta^{\text{bad}}$ | t      | p      |
|---------------|-----------------------:|----------------------:|---------------------------------------------:|-------:|-------:|
| Punishment full (n=80)    | +0.018 | −0.057 | +0.075 | +0.99 | 0.325 |
| Punishment passers (n=61) | +0.017 | −0.068 | +0.085 | +0.89 | 0.376 |

Both penalties are small and not significantly different from zero; the difference of differences is null. So the line-140 claim is empirically defensible. (This is the within-subject paired version of the M1 asymmetry test.)

## C5b — line 140: "What does the analysis look like here?" (beliefs × performance)

> "Player~A's punishment beliefs do not vary systematically with Player~A's performance"

**Mostly supported, with one caveat.** Pearson correlations in the Punishment passers sample (n=61):

| Belief variable      | r vs `overall_score` | p     |
|----------------------|--------------------:|------:|
| belief_del_good      | −0.208             | 0.107 |
| belief_nodel_good    | −0.117             | 0.369 |
| belief_del_bad       | +0.048             | 0.713 |
| belief_nodel_bad     | −0.079             | 0.543 |
| nodel_del_good (diff)| +0.117             | 0.367 |
| nodel_del_bad  (diff)| −0.153             | 0.239 |

The **belief differences** (the regressors that enter `tab:reg_belief_specs`) show no systematic relationship with performance — both p > 0.23. So the claim that "beliefs do not vary systematically with performance" is true *for the operative regressors*.

The caveat: `belief_del_good` (expected punishment for the delegated-good cell, not the difference) is marginally negatively correlated with performance (r=−0.21, p=0.11). This implies *lower-performing* Player~As expect Player~B to punish them somewhat more in the delegated-good cell — interpretable as "subjects who know they performed worse expect to be punished more even when the outcome is good." Worth a one-line footnote acknowledgement, but it doesn't carry into the difference regressor that enters the regression, so the headline claim survives.

## C6 — line 142: non-linearity in performance → delegation

> "If I know it will fail, then I may want to delegate. If I know I will succeed, I may want to do it myself. Hence, my preference on delegation may change depending on the chance of success."

**Tested a quadratic term in performance; with this N, can't separate linear from quadratic.** Logit of delegation on `overall_score` + `overall_score`², by treatment (passers):

| Sample             | linear b (p)    | quadratic b (p)  |
|--------------------|-----------------|------------------|
| Punishment (n=61)  | −0.39 (p=0.57)  | +0.01 (p=0.96)   |
| No-Punishment (n=70)| +0.95 (p=0.21) | −0.16 (p=0.16)   |

The quadratic terms are not significant in either condition, and the linear-only coefficients collapse once a quadratic is added. With ~60–70 observations per condition we don't have power to estimate a kink reliably. **My recommendation:** flag the prediction in a footnote, but don't claim either direction from these data. The literature pointer the comment asks about is the **"better-than-the-average" overplacement** and **algorithm-aversion-as-a-function-of-decision-difficulty** strands — Dietvorst, Simmons & Massey (2015, JEP:G); Logg, Minson & Moore (2019); and the Bharti & Dietvorst paper already cited at line 144. The latter is the most directly relevant — but as F5 above notes, Bharti & Dietvorst is currently doing double duty (uncertainty story \emph{and} non-linearity story); the section should pick one role for it.

## C7 — line 159: figure split by delegation status

> "Could we include in the figure the split by who ended up delegating?"

[results.tex:148](../../manuscript/results.tex#L148) (`fig:performance`) currently shows the distribution of correct predictions over rounds 1–10 by treatment, with the message that average performance is balanced. The comment asks for a sub-split by delegation status. This is essentially the C8 question in graphical form — see the numbers below. Adding a four-bar grouping (Punishment delegators / Punishment non-delegators / No-Punishment delegators / No-Punishment non-delegators) at each score would make the "marginal-delegator pulls from a different segment in No-Punishment" point visible directly. Producible by extending [scripts/python/07_performance.py](../../scripts/python/07_performance.py) — I have not done so without explicit go-ahead.

## C8 — line 169: reconciling three facts

> "How do we go about no performance differences in first 10 rounds between the Player As that delegated in both treatments, the delegation share being higher if punishment is not possible and delegation decreasing with performance (in both or only one condition)?"

**There is no contradiction once you look at the within-treatment delegator distributions:**

| Sample  | Group                | n  | mean(`overall_score`) | sd   |
|---------|----------------------|---:|---------------------:|-----:|
| FULL    | Punishment delegators| 34 | 2.47                 | 1.28 |
|         | Punishment non-del.  | 46 | 2.98                 | 1.34 |
|         | No-Pun. delegators   | 48 | 3.06                 | 1.21 |
|         | No-Pun. non-del.     | 33 | 3.12                 | 1.45 |
| PASSERS | Punishment delegators| 24 | 2.38                 | 1.35 |
|         | Punishment non-del.  | 37 | 3.00                 | 1.35 |
|         | No-Pun. delegators   | 40 | 2.98                 | 1.21 |
|         | No-Pun. non-del.     | 30 | 3.13                 | 1.50 |

Two-sample test of **delegators across treatments**: Punishment delegators score **significantly lower** than No-Punishment delegators (t = −2.11, p = 0.039 in the full sample; t = −1.79, p = 0.080 in passers). So the premise of the comment — "no performance differences in first 10 rounds between the Player~As that delegated in both treatments" — is *not what the data shows*; delegators in Punishment have, on average, ~0.6 fewer correct rounds out of 10.

**The reconciliation, then:**
1. Within Punishment, delegation is concentrated among low performers (negative slope). The 42.5\% delegation share is essentially the low-performance tail opting in.
2. Within No-Punishment, the slope is flat (r ≈ −0.02). Delegation is drawn roughly uniformly from the performance distribution. The 59.3\% delegation share is "everyone, regardless of performance."
3. The extra ~17 percentage points of delegation in No-Punishment therefore come disproportionately from **mid- and high-performing** subjects — the ones who in Punishment would have refused to delegate (because process ownership / the channel of choice is active there).
4. Mean performance among delegators is higher in No-Punishment than in Punishment because the additional No-Punishment delegators sit higher on the performance distribution, dragging the delegator mean up.

This pattern is the data signature of process-ownership being active in Punishment and inactive in No-Punishment. It would not be the data signature you'd get from a story in which everyone delegates more in No-Punishment for the same reason (e.g., "delegation is psychologically cheaper without punishment"), because that would shift the whole delegator distribution leftward — and the delegator mean would either be unchanged or move parallel to the non-delegator mean. Instead, the delegator mean *rises* in No-Punishment while the non-delegator mean barely moves.

**Suggested addition (could sit at the end of the heterogeneity paragraph or in a footnote):**

> "Player~As who chose to delegate in the \textit{Punishment} condition scored on average $2.47/10$ in the first ten rounds, compared with $3.06/10$ for delegators in the \textit{No-Punishment} condition (two-sided $p=0.039$, $p=0.080$ in passers). The extra delegators in \textit{No-Punishment} therefore come disproportionately from the middle and upper portion of the performance distribution — subjects who, when punishment is on the table, choose to make the decision themselves."

## C9 — line 173: include conclusion paragraph

**Draft** (to be tightened/adapted; uses the M1–M4 nomenclature the earlier draft already established):

> "In sum, we have considered four candidate mechanisms for Result~1. M1 (anticipated differential punishment) is inconsistent with Player~A's elicited beliefs, which show no asymmetry in expected punishment between delegated and self-made decisions conditional on outcome (Section~\ref{sec:beliefs}). M2 (extra effort to outperform the algorithm) is inconsistent with the effort data, which run in the opposite direction: it is in the \textit{No-Punishment} condition, not in the \textit{Punishment} condition, that non-delegators improve from rounds 1--10 to the final round. M3 (process ownership of the outcome) is consistent with the data: the negative performance--delegation gradient in \textit{Punishment} and the higher performance of \textit{No-Punishment} delegators jointly indicate that Player~As who can deliver a good outcome to Player~B prefer to do so personally, but only when Player~B's payoff is at meaningful third-party stake. M4 (experimenter demand) cannot be separately identified from M3 with the present design --- the punishment manipulation that activates M3 is also the manipulation a demand-aware subject would respond to. The most parsimonious reading is therefore M3 with M4 as an alternative we cannot rule out; disentangling them is the cleanest direction for follow-up work."

---

# Summary punch list (priority order)

1. **F3** Fix the broken sentence at line 123 (no main verb).
2. **C4 / F4** Resolve the M3-vs-M1 boundary: pick one of the suggested rewrites for the closing sentence of line 123, and let M3 stand on "third-party stake activates process ownership" rather than "moral salience amplifies process ownership."
3. **C9** Write the "In sum" conclusion paragraph at line 173 (draft above).
4. **C8** Add the delegator-performance-by-treatment numbers either to the heterogeneity paragraph or as a footnote (the puzzle in comment 169 is resolved by data already in hand).
5. **F1** Replace remaining "Baseline" with "Punishment" at lines 140 and 167.
6. **F5 / F6** Decide where Inherent Uncertainty (line 144) sits and reinstate M4 in the summary (see C9).
7. **F8** Consider promoting Performance-differences/overconfidence (line 146) before the heterogeneity paragraph.
8. **C1** Add the perceived-performance footnote (text drafted).
9. **C2** Add the Feier et al. contrast (one sentence or footnote, drafted).
10. **C5a / C5b** No prose change required — the analyses confirm the existing claims. Optionally add a one-line footnote for the marginal `belief_del_good`-by-`overall_score` correlation.
11. **C6** Soft-cite the non-linearity in a footnote; the data don't support a quadratic claim.
12. **C7** Optionally extend [07_performance.py](../../scripts/python/07_performance.py) to add a delegator/non-delegator split — visualises C8.
