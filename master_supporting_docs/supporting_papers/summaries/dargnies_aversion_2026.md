---
title: "Aversion to Hiring Algorithms: Transparency, Gender Profiling, and Self-Confidence"
authors: Marie-Pierre Dargnies, Rustamdjan Hakimov, Dorothea Kübler
venue: Management Science
year: 2026
volume: 72(1)
pages: 285–301
doi: 10.1287/mnsc.2022.02774
note: Special Issue on the Human-Algorithm Connection. WZB Discussion Paper SP II 2022-202.
bibtex_handle: dargnies_aversion_2026
pdf: ../dargnies_aversion_2026.pdf
relevance_to_manuscript: high — algorithm aversion in hiring; added in recent lit-review pass
---

# Dargnies, Hakimov & Kübler (2026) — *Aversion to Hiring Algorithms*

## Research question

What are the origins of algorithm aversion in hiring decisions? The paper examines this from **two perspectives** — workers (subject to hiring) and managers (making hiring decisions) — and tests four candidate moderators:
1. Self-interest (workers preferring the process they believe favours them)
2. Transparency about how the algorithm works
3. Gender profiling (whether the algorithm uses gender in its predictions)
4. Self-confidence (especially among managers, who may be overconfident in their own hiring ability)

## Methods

- **Online lab experiment**, programmed in oTree. WZB Berlin (Dargnies acknowledges Dorothea Kübler at WZB — the same institution as the manuscript's author).
- **Workers** do three real-effort tasks (task 1, task 2, and a "job task" that combines them).
- **Hiring decision** is between two workers, made by either a manager or an algorithm.
- **Workers choose** whether the hiring is by manager or algorithm.
- **Managers choose** whether to delegate hiring to the algorithm.
- **Treatments vary**:
  - Whether the algorithm uses workers' gender as a predictor (and whether workers know this).
  - Whether subjects receive detailed information about how the algorithm works.
  - Whether managers receive feedback about their own hiring accuracy.

## Key results

- **Baseline**: workers choose the *manager* more often than the algorithm; managers prefer to make hiring decisions themselves rather than delegate.
- **Gender transparency**: when the algorithm does *not* use workers' gender, and workers know this, they choose the algorithm more often. **Gender profiling is the salient algorithm-aversion driver in hiring.**
- **Transparency about algorithm internals**: providing details on how the algorithm works does *not* increase the preference for the algorithm — neither for workers nor for managers. This is a striking null: explainability per se isn't enough.
- **Manager feedback**: providing managers feedback about their own hiring accuracy *increases* their preference for delegating to the algorithm, because managers are overconfident and the feedback corrects this.

## Main takeaways

1. **Algorithm aversion in hiring is real** but specific in its drivers.
2. **Gender profiling is a major driver**: workers reject algorithms partly because they fear gender discrimination.
3. **Transparency doesn't work**: providing details about algorithmic decision-making doesn't increase trust or use.
4. **Overconfidence drives manager aversion**: managers think they're better at hiring than they are; correcting this via feedback helps.
5. **Policy implication**: increasing algorithm uptake in hiring requires addressing specific concerns (gender profiling) and correcting overconfidence — not just providing transparency.

## Relation to "Algorithms and Responsibility" (this manuscript)

Dargnies et al. is **not yet cited** in literature.tex but was added to the bib in the recent lit-review pass. It's the published version of WZB DP SP II 2022-202 (originally 2022 working paper; published in MS 72(1) 2026).

**Why this paper matters for the manuscript:**

**(1) Direct algorithm-aversion result in a moral-domain setting (hiring).** Hiring decisions involve fairness concerns about a third party (the worker not hired). This is structurally similar to the manuscript's setup where Player A's prediction affects Player B's payoff. Dargnies et al. shows algorithm aversion is strong in hiring; the manuscript shows algorithm aversion is moderate in prediction. The contrast may be informative: hiring involves *who* the algorithm includes, while prediction involves only *what* it predicts. The fairness concern is more direct in hiring.

**(2) The "transparency doesn't work" finding is highly relevant for the manuscript's M3 discussion.** Dargnies et al. shows that providing algorithm transparency doesn't increase use. The manuscript's algorithm is *maximally* transparent (a Bernoulli draw at known probability with common-knowledge calibration), yet delegation rates remain only ~50%. This is consistent with Dargnies et al. — transparency is not sufficient to drive algorithm adoption. The implication: whatever's depressing delegation in the manuscript is not opacity. M3 (process ownership / accountability salience) is a candidate explanation that doesn't depend on opacity.

**(3) WZB Berlin connection.** Dorothea Kübler is at WZB Berlin — the same institution as the manuscript's author. This creates a natural opportunity for the manuscript to engage with this paper specifically as a recent neighbour piece. The manuscript can cite Dargnies et al. and frame it as the closest moral-domain algorithm-aversion result with an institutional connection.

**(4) Manager overconfidence is a useful complementary point.** The manuscript could note: Dargnies et al. find that managerial overconfidence drives manager-side algorithm aversion in hiring. The manuscript's Player A faces a similar self-confidence question (am I better than the algorithm?). Felix's manuscript explicitly calibrates the algorithm to *equal* A's performance, which removes overconfidence as a confound — closing a channel that Dargnies et al. identify as important.

**Where to cite in literature.tex:**

- Paragraph 19 (algorithm aversion subsection), alongside Kormylo et al. 2025. Both are MS 72(1) Special Issue papers from 2025/2026. Suggested addition: "Dargnies, Hakimov & Kübler (2026) study algorithm aversion in hiring — finding that workers reject algorithmic deciders especially when the algorithm uses gender as a predictor, and that transparency about algorithmic internals does *not* increase use. Managerial overconfidence, however, can be corrected by performance feedback, raising algorithm uptake."

**Worth borrowing for the discussion:**

- The "transparency null" is rhetorically useful. The manuscript could note: "Dargnies et al. (2026) show that providing detailed information about how the algorithm works does not increase its uptake. Our design provides the strongest possible transparency — a fully calibrated Bernoulli draw with common-knowledge accuracy — and finds delegation rates around 50%. Together, these results suggest that explainability is not the binding constraint on algorithmic delegation in moral-domain settings."

**Limitation:** Dargnies et al.'s setting (hiring with gender stakes) is different from the manuscript's setting (prediction with no fairness stakes). Direct quantitative comparison isn't apt; the qualitative convergence (transparency doesn't drive adoption) is the useful point.
