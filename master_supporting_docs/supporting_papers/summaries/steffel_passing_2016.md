---
title: "Passing the buck: Delegating choices to others to avoid responsibility and blame"
authors: Mary Steffel, Elanor F. Williams, Jaclyn Perrmann-Graham
venue: Organizational Behavior and Human Decision Processes
year: 2016
volume: 135
pages: 32–44
doi: 10.1016/j.obhdp.2016.04.006
bibtex_handle: steffel_passing_2016
pdf: ../steffel_passing_2016.pdf
relevance_to_manuscript: high — establishes credit-blame asymmetry; cited in lit.tex ¶13 and is the source of the asymmetry framing
---

# Steffel, Williams & Perrmann-Graham (2016) — *Passing the buck*

## Research question

**Are people more likely to delegate choices for others than for themselves?** And specifically, is the motive for delegation different when choosing on behalf of others — namely, **to avoid responsibility and blame**?

Four hypotheses:
- **H1**: People delegate choices for others more than choices for themselves, especially when negative outcomes are possible.
- **H2**: Both anticipated responsibility and blame drive this asymmetry.
- **H3**: Delegation is uniquely suited to avoid this burden — *not* other choice-avoidance tactics like delaying or flipping a coin.
- **H4**: People delegate to others who can *assume responsibility*, regardless of expertise.

## Methods

Multiple **vignette-based and behavioural lab studies** (Studies 1–7) with subjects from MTurk and university subject pools. Key designs:

- Subjects asked to choose between options for themselves or another person; some scenarios have only-negative outcomes, others mixed.
- Comparisons of delegation against (i) delay, (ii) coin flip, (iii) other passive choice avoidance methods.
- Manipulations of the surrogate's expertise vs ability to assume responsibility.

## Key results

- **Strong asymmetry**: subjects delegate choices for others much more than choices for themselves, especially for negative-valence decisions.
- **Mediated by anticipated responsibility and blame**: subjects report that they delegate to avoid feeling responsible and to avoid being blamed by others.
- **Delegation is uniquely suited** to this purpose: delaying or coin-flipping does not produce the same effect — those tactics don't transfer responsibility.
- **Expertise is secondary**: subjects delegate to anyone who can be held responsible, not just to experts. Surrogates who cannot bear responsibility (e.g., children) are *not* chosen, even if they would be competent.
- The **credit-blame asymmetry** (people care more about avoiding blame for bad outcomes than claiming credit for good ones) is a robust pattern in the data.

## Main takeaways

1. **People delegate to avoid being held responsible** — the motive is not laziness or lack of expertise but explicitly the desire to shed accountability.
2. **The asymmetry is sharpest for choices that affect others, with possible negative outcomes.** Personal choices stay personal; others' choices with downside risk get delegated.
3. **Delegation is uniquely a *responsibility-transfer* tactic**, not just a choice-avoidance tactic.
4. **The credit-blame asymmetry is a stable feature**: people care more about avoiding blame than claiming credit.
5. **Surrogate selection turns on responsibility-bearing capacity**, not competence.

## Relation to "Algorithms and Responsibility" (this manuscript)

Steffel et al. is cited in [literature.tex](../../../manuscript/literature.tex) paragraph 13, where the manuscript draws on its credit-blame asymmetry: "people care more about avoiding blame for bad outcomes than about claiming credit for good ones." This is a foundational result the manuscript uses to motivate the focus on punishment (rather than reward) as the elicitation device.

**Why this paper matters for the manuscript:**

**(1) Motivates the asymmetric focus on punishment.** The manuscript explicitly chose punishment over reward as the responsibility-elicitation mechanism (design.tex ¶60). Steffel et al. justify this choice: the moral psychology of delegation is *asymmetric* — blame matters more than credit. If you only could measure one, punishment is the right one.

**(2) The "delegate to someone who can be held responsible" finding is highly relevant for algorithm delegation.** Can an algorithm be held responsible? Steffel et al.'s finding suggests it can't, in the same way a coin or a die can't. If people only delegate to surrogates who can absorb responsibility (H4), then they should *not* delegate to algorithms at all — algorithms cannot be held responsible in the same way humans can. The manuscript's H1 reversal (subjects delegate *less* to the algorithm when punishment is possible) is consistent with this reading: when responsibility becomes salient, subjects pull back from the algorithm because the algorithm cannot bear responsibility on their behalf.

**(3) Connection to M3 (process ownership / identity).** Steffel et al. find that the *responsibility-transfer* function of delegation is its primary purpose. If delegation to an algorithm cannot transfer responsibility (because algorithms are incapable of bearing it), then delegation to an algorithm under conditions of high accountability salience becomes *self-defeating* — the principal still owns the responsibility, but has also given up the agency to act on the moral content of the decision. This is the M3 logic. The manuscript could engage with Steffel et al.'s framework more directly: the manuscript's M3 is a *consequence* of the Steffel et al. theory applied to algorithmic delegation.

**(4) Algorithm vs coin flip is the relevant analogy.** Steffel et al. show that coin flips don't satisfy the responsibility-transfer purpose of delegation. The manuscript's algorithm is closer to a coin flip than to a human surrogate (it's a Bernoulli draw at A's accuracy). Steffel et al.'s framework therefore predicts that delegating to such an algorithm should be less appealing than delegating to a competent human surrogate. The manuscript finds delegation rates of ~50% — substantially lower than the ~56% B&F find for delegation to a human delegate, consistent with Steffel et al.'s logic.

**(5) The discussion section could engage with Coffman vs Steffel asymmetry.** Coffman 2011 finds that intermediation reduces *both* punishment and reward (symmetric). Steffel et al. find asymmetric — blame > credit. The manuscript currently aligns with Steffel et al. (focusing on punishment) but could note the tension with Coffman in section 4. If credit also responds to delegation (Coffman), then the responsibility-shifting motive is symmetric and should bite under reward salience as well — a possible robustness check for the manuscript.

**Where in literature.tex:**

- Paragraph 13: correctly cites Steffel for the credit-blame asymmetry, and uses the framing as a foundational point.

**Worth borrowing more from Steffel:** The "delegating only to surrogates who can assume responsibility" finding (H4) is rhetorically strong. The manuscript could borrow it for the discussion: "Steffel et al. (2016) show that delegation serves the function of *transferring* responsibility, and that this only works when the surrogate is capable of bearing it. Algorithms in our design lack this capacity by construction. Our H1 reversal is consistent with this logic — when accountability becomes salient, principals pull back from delegating to an algorithm that cannot absorb the responsibility on their behalf."

**Limitation:** Steffel et al. is vignette-based; their findings are about stated preferences rather than incentivised choices. The manuscript's incentivised behavioural design is methodologically stronger but the conceptual framework Steffel et al. provide is robust enough to anchor the discussion.
