---
title: "Hiding Behind Machines: Artificial Agents May Help to Evade Punishment"
authors: Till Feier, Jan Gogoll, Matthias Uhl
venue: Science and Engineering Ethics
year: 2022
doi: 10.1007/s11948-022-00372-7
bibtex_handle: feier_hiding_2022
pdf: ../feier_hiding_2022.pdf
relevance_to_manuscript: very high — direct precedent, reconciled in literature.tex paragraph 39
---

# Feier, Gogoll & Uhl (2022) — *Hiding Behind Machines*

## Research question

Do third parties judge decisions delegated to algorithmic agents differently from decisions delegated to human agents, in a setting where outcomes matter for a recipient and punishment is possible? And, if so, do delegators strategically exploit that judgment differential by delegating more to algorithms?

The authors frame the question around the *retribution gap* (Danaher 2016): the worry that algorithmic delegation could become a strategy for "self-exculpation" because algorithms cannot themselves be coherently punished.

## Methods

- **Lab experiment**, major German university, Feb–May 2019, *n* = 149 subjects, six sessions, z-Tree + ORSEE.
- **Stage 1 — Logic task.** Subjects solve ten Raven-style visual logic puzzles in five minutes. Visual rather than mathematical, deliberately, so that algorithmic error is plausible.
- **Stage 2 — Delegation decision.** Subjects choose whether their own performance or a delegate's performance determines a third party's payoff. Their own payoff is unaffected by this choice — payoff alignment between delegator and recipient is therefore weak.
- **Between-subject manipulation:** the delegate is either **another participant** (Human treatment) or **an algorithm calibrated to mimic the session-level performance of human participants** (Machine treatment). Subjects are shown a histogram of the delegate's performance before deciding. The algorithm is intentionally not anthropomorphised (no name, voice, depiction).
- **Stage 3 — Strategy-method punishment.** Each subject also acts as evaluator for a matched delegator (same role pool). Using the strategy method, the evaluator specifies a reward / punishment (−40 to +40 ECU) in each of the four (delegation, outcome) cells. Only the realised cell is implemented.
- **Stage 4 — Self-assessment + Holt-Laury risk.**

## Key results

- **Result 1 — Good outcomes:** No significant difference in reward when the good outcome is brought about by the principal vs by either kind of delegate. (Human: 20.28 vs 20.94 ECU, *p* = 0.72. Machine: 23.78 vs 27.00, *p* = 0.106.)
- **Result 2 — Bad outcomes:** When the bad outcome is brought about by **another human delegate**, punishment is not significantly different from self-imposed bad outcomes (7.29 vs 8.26 ECU, *p* = 0.56). But when the bad outcome comes from the **algorithm**, the principal is rewarded *significantly more* (i.e., punished less) than for the self-caused bad outcome (8.53 vs 12.96, *p* = 0.041).
- **Delegation rates:** 46.1% (Human) vs 56.2% (Machine), difference *not significant* (*p* = 0.28). Logit shows the propensity to delegate is driven primarily by self-assessed errors in the logic task, not by the agent type.
- The authors conclude (i) that the punishment asymmetry is real but (ii) subjects in this sample did not yet strategically exploit it.

## Main takeaways

1. **Algorithmic delegation works as a blame-shield conditional on a bad outcome**, even when the agent is calibrated to match human performance.
2. **Delegators don't (yet) exploit the asymmetry** — delegation rates depend on perceived own ability, not on agent type.
3. **No corresponding asymmetry for good outcomes** — credit is not lost by delegating, but blame is partially deflected. The credit-blame asymmetry has the same sign as Steffel et al. (2016).
4. **Policy implication:** institutional accountability rules are needed because the behavioural tendency could be exploited at scale once recognised.
5. **Limitations the authors flag themselves:** stylised setting; explorative; no anthropomorphism manipulation; same subject pool acts as both delegator and evaluator.

## Relation to "Algorithms and Responsibility" (this manuscript)

Feier et al. is the **direct precedent** the manuscript engages with. Literature.tex paragraph 27 cites it as the "most closely related study"; paragraph 29 catalogues the three design features that motivate departures in your design; paragraph 39 is the explicit reconciliation paragraph.

**How the design features differ:**

| Feature | Feier et al. (2022) | This manuscript |
|---|---|---|
| Algorithm calibration | Session-level (algo error rate = aggregate of human participants) | **Individual-level Bernoulli** calibrated to each subject's empirical accuracy in 10 pre-rounds; common knowledge between A and B |
| Delegator vs evaluator | Same subject pool acts as both | **Separate pools** (Player A delegator, Player B evaluator, perfect-stranger matching) |
| Punishment possibility | Always on | **Between-subject on/off manipulation** (Punishment vs No-Punishment) |
| Task | Logic puzzles | Weight prediction from face image |
| Payoff alignment | Weak (self payoff unaffected by delegation) | Weakly aligned (better outcome reduces expected punishment) |
| Sample | German university lab, n=149 | Online (Prolific UK), n=322 |

**How the results relate:**

- **On H2 (conditional-on-outcome punishment differential):** Feier finds it (bad-outcome cell, machine treatment); your manuscript finds it *only at the margin and not significant* (paired *t*-test *p* = 0.131; diff-in-diff *p* = 0.07). The manuscript reads the disappearance as evidence that Feier's differential was driven by **third-party signal extraction** about Player A's self-perceived relative ability — a channel that your individual-level common-knowledge calibration *closes off by construction*. Under your design, Player B has no informational basis on which to read delegation as overconfidence, laziness, or selfishness, and the differential dissolves. This is consistent with, not contradictory to, Feier — the two papers are reading the same fact from different design vantage points.
- **On H1 (delegation rate by punishment regime):** Feier does not run this comparison (punishment is always on in their design). Your manuscript's reversal — punishment makes delegation *less* attractive — is therefore not directly addressed by Feier's data. It does, however, sit in apparent tension with the natural reading of Feier's results: if delegators could reduce expected punishment by delegating, they should delegate more when punishment is possible, but in your data they delegate *less*. Your manuscript interprets this through M3 (process ownership / identity / accountability salience) — the moral salience of accountability makes the principal pull *toward* direct engagement with the decision rather than toward distancing.
- **On preferences vs strategic behaviour:** Feier finds delegation driven primarily by self-assessed ability. Your manuscript finds the same in the pooled sample (actual and perceived performance are not significantly associated with delegation), with actual performance loading negatively only under the attention-check restriction. The two papers therefore agree that strategic punishment-avoidance is *not* the dominant motive in the delegation decision itself — even though Feier shows that the strategy would work if exploited.

**What the manuscript uses Feier for in literature.tex:**

- Paragraph 27 — introduces Feier as immediate precedent.
- Paragraph 29 — itemises the three design features that motivate departures.
- Paragraph 39 — explicit reconciliation of the apparent tension (punishment differential present in Feier, absent in ours; delegation reversal in ours, not directly tested in Feier).
- Paragraph 41 — situates Feier (signal-extraction channel) alongside this manuscript (process-ownership channel) and Chevrier & Teixeira 2024 (programmer-blame channel) and Köbis et al. 2025 (compliance-asymmetry channel) as four nodes of a single emerging map.

**What's worth adding (suggestion):** The Feier result that *delegators don't strategically exploit the asymmetry they could* is a useful additional citation in your H1 discussion. It reinforces the point that the strategic-avoidance reading of H1 is fragile across studies, not just yours.
