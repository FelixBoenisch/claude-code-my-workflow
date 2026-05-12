---
title: "Reputational Algorithm Aversion"
authors: Gregory Weitzner
venue: arXiv working paper (also presented at AEA 2025)
arxiv_id: 2402.15418
year: 2024
version: v3 (31 July 2024)
affiliation: McGill University
bibtex_handle: weitzner_reputational_2024
pdf: ../weitzner_reputational_2024.pdf
relevance_to_manuscript: high — formal microfoundation for the signal-extraction reading of Feier; added in recent lit-review pass
---

# Weitzner (2024 WP) — *Reputational Algorithm Aversion*

## Research question

Can algorithm aversion be derived as a fully rational equilibrium outcome — without invoking psychological biases — when the choice to follow or override an algorithm signals information about a worker's ability?

The motivating intuition: a worker's decision to override an algorithm conveys that they *believe* they know better than the algorithm. Reputation-conscious workers will override even when they shouldn't, just to signal high skill.

## Methods

**Theoretical model.** A strategic communications (cheap talk) game.

- A worker forecasts a binary outcome based on (i) a private signal about the outcome and (ii) a public signal from an algorithm.
- The worker has private information about her own skill: she is either **high-skill** (private signal more accurate than algorithm) or **low-skill** (private signal less accurate).
- The firm observes the worker's forecast and the outcome, then updates beliefs about the worker's skill.
- The worker faces **reputational concerns** (à la Holmström 1999): she wants the firm to perceive her as high-skill.

The model derives equilibria and shows when efficient use of the algorithm fails.

## Key results

**Result 1 — First-best is unachievable.** If high-skill workers always override and low-skill workers always follow, then overriding instantly reveals the worker is high-skill. This makes overriding too tempting for low-skill workers, breaking the equilibrium.

**Result 2 — Informative equilibrium with algorithm aversion.** There exists an equilibrium where high-skill workers always report their own signal and low-skill workers report their own signal *with some positive probability* when it differs from the algorithm. In this equilibrium, the worker exhibits algorithm aversion — overriding the algorithm even when their private signal is less accurate.

**Result 3 — Algorithm aversion increases in the uncertainty of the algorithm.** As the algorithm becomes less accurate, overriding becomes less costly and the signaling value of overriding for low-skill workers rises.

**Result 4 — Forecasts are sometimes worse than the algorithm alone**, because reputational concerns cause workers to override the algorithm too often.

**Result 5 — Worker may provide zero short-run value to the firm** if the override frequency is high enough; this can put downward pressure on wages or motivate firms to fire workers.

## Main takeaways

1. **Algorithm aversion can be fully rational** when there's information asymmetry about the worker's skill and reputational concerns at stake.
2. **The model fits empirical evidence**: human forecasts often worse than algorithms even after seeing the algorithm's prediction (Angelova, Dobbie & Yang 2023; Agarwal et al. 2023). 90% of judges in Angelova et al.'s data underperform the algorithm when they override it.
3. **Mechanism distinct from behavioural explanations** (preferences for agency, anthropomorphic disutility from machine interaction). Weitzner offers a strategic/rational alternative.
4. **Policy implication**: design AI deployment to minimise reputational signaling pressure on workers, e.g., by making override decisions less visible to evaluators.

## Relation to "Algorithms and Responsibility" (this manuscript)

Weitzner is **not yet cited** in literature.tex. The bib entry was added in the recent lit-review pass. The recommended placement is at paragraph 39 of literature.tex — the reconciliation paragraph with Feier et al. — because Weitzner provides the **formal microfoundation** for the signal-extraction reading of Feier that the manuscript already adopts.

**Why this paper matters for the manuscript:**

**(1) Direct microfoundation for the manuscript's reading of Feier 2022.** Literature.tex paragraph 39 argues that Feier's punishment differential is best read as third parties extracting a signal about the principal's self-perceived ability. Weitzner's model formalises *exactly* this channel: when an algorithm is available, the worker's override-or-follow decision conveys information about her ability, and observers (the firm in Weitzner; Player B in Feier) update accordingly. The manuscript's design with individual-level calibration closes off this signal-extraction channel — which Weitzner's model would predict eliminates the algorithm-aversion / differential-punishment effect.

**(2) The "uncertainty of the algorithm" comparative static is useful.** Weitzner shows that algorithm aversion increases with the uncertainty / inaccuracy of the algorithm. In the manuscript, the algorithm's accuracy is *common knowledge* and pegged to A's own accuracy — i.e., it's *certain* relative to A. Weitzner's mechanism therefore predicts the lowest possible algorithm aversion in the manuscript's setting. The delegation rates of 42–59% are consistent with this.

**(3) Rational explanation for why eliminating signal extraction kills the differential punishment.** Under Weitzner's model:
- In Feier 2022 (session-level calibration; signal extraction operative): there's a differential punishment for delegation because observers use the delegation decision to infer worker skill, and low-confidence delegators are punished.
- In the manuscript (individual-level calibration; signal extraction closed): no differential punishment because Player B has no informational basis to update on Player A's skill from her delegation decision. The Bernoulli is calibrated to A's own performance, so the question "did A pick the right action?" becomes informationally trivial.

This is the *cleanest existing formal account* of why the manuscript's H2 null is theoretically expected. Worth citing prominently at literature.tex ¶39.

**(4) Weitzner is *not* a substitute for M3, but a complement.** Weitzner explains the third-party-side signal extraction. The manuscript's M3 explains the principal-side process-ownership preference. Both can be operating; they're answers to different questions.

**Recommended use in the manuscript:**

- **literature.tex ¶39**: Add citation: "The signal-extraction reading we adopt has a formal microfoundation in Weitzner (2024), who models algorithm aversion as a fully rational equilibrium in which a worker's choice to override or follow an algorithm conveys information about her ability. Individual-level calibration of the algorithm — as in our design — eliminates the signaling channel by construction, which Weitzner's model would predict eliminates the differential punishment that Feier et al. (2022) observe."

- **Mechanism section (M3 discussion)**: A footnote noting that Weitzner's reputational model is a separate channel from M3, and the two are complementary rather than competing.

**Caveat:** Weitzner is a working paper, not yet published. The model is well-developed and presented at AEA 2025, but the journal trajectory is uncertain. Cite as `unpublished` in the bib (already done).
