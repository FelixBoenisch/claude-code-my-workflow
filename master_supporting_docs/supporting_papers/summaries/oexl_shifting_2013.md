---
title: "Shifting the blame to a powerless intermediary"
authors: Regine Oexl, Zachary J. Grossman
venue: Experimental Economics
year: 2013
volume: 16(3)
pages: 306–312
doi: 10.1007/s10683-012-9335-7
bibtex_handle: oexl_shifting_2013
pdf: ../oexl_shifting_2013.pdf
relevance_to_manuscript: very high — extends B&F with powerless intermediaries; cited in literature.tex ¶11
---

# Oexl & Grossman (2013) — *Shifting the blame to a powerless intermediary*

## Research question

Bartling & Fischbacher (2012) showed that dictators can shift blame to a delegee, but in their main treatment the delegee has *real choice* (fair vs unfair). Oexl & Grossman ask: **does blame shift even when the intermediary cannot choose a fair outcome?** And does the intermediary still absorb blame even if she is effectively powerless?

Two specific contrasts with B&F:
1. **Choice treatment**: the intermediary, if called upon, can only choose *between two unfair allocations* (differing only in which recipient is harmed more). Fair outcome is precluded by delegation.
2. **Random treatment**: the intermediary has no choice at all — she clicks a button that triggers a random selection between the two unfair allocations.

This separates "blame is shifted because the delegee chose the unfair outcome" from "blame is shifted because the delegee is *between* the dictator and the outcome."

## Methods

- **Lab experiment**, UC Santa Barbara, z-Tree, ORSEE. *N* = 256 across 22 sessions of 8 or 12, lasting 30–45 min. Average payment $11.18 incl. $6 show-up.
- **Game:** Adaptation of B&F's D&P treatment. Four players: Dictator (D), Intermediary (N), Recipient 1 (R1), Recipient 2 (R2). $20 endowment.
  - **Fair allocation:** $5 each.
  - **Unfair option A:** ($9, $9, $2, $0) — D and N get $9 each, R1 gets $2, R2 gets $0.
  - **Unfair option B:** ($9, $9, $0, $2) — same but R1 and R2 swapped.
  - D can directly pick any of these three allocations *or* delegate to N.
  - **Choice treatment**: if D delegates, N picks between A and B (cannot pick fair).
  - **Random treatment**: if D delegates, N triggers a random draw between A and B.
- **Punishment:** strategy method. One of R1 or R2 is randomly chosen, pays $1 to deduct up to $7 from any combination of D, N, and the other R (subject to non-negative payoffs).
- **Beliefs** elicited from D and N about deductions in 10 of 22 sessions.

## Key results

**Result 1 — Delegation shifts blame away from the dictator even when the intermediary is constrained to unfair options.**

In the *Choice* treatment, when the unfair allocation is the final outcome:
- D's punishment **drops** from $2.58 (direct) to $1.92 (delegated). *t* = 1.82, *p* = 0.04 (one-tailed); Wilcoxon *z* = 4.00, *p* < 0.01.
- N's punishment **rises** from $0.95 to $1.72. *t* = 2.91, *p* < 0.01.

In the *Random* treatment, when the unfair allocation is the final outcome:
- D's punishment drops from $2.01 to $1.59 (Wilcoxon *p* = 0.04; weaker but still significant).
- N's punishment *barely* increases from $0.64 to $0.72 — **not significant**. *t* = 0.30, *p* = 0.38.

**Result 2 — The intermediary absorbs blame only when she has *some* choice, even if all available choices are bad.** Having a choice between two unfair allocations is enough for the intermediary to be blamed; merely triggering a random process is not.

**Result 3 — Delegation maximises the dictator's expected profit** in both treatments. But many dictators don't choose this — 38% delegate in Choice, 43% in Random. 33% choose unfair directly in Choice, 9% in Random. The authors note this is puzzling: delegation strictly dominates direct unfairness in expected profit, yet many dictators avoid it.

**Result 4 — The B&F responsibility measure is challenged.** B&F defined a player's responsibility as their share in the probability increase of the unfair outcome. In Oexl's Choice treatment, the intermediary's decision *doesn't change* the probability of an unfair outcome (it's 100% unfair conditional on delegation) — yet she is punished. This is incompatible with the B&F measure.

## Main takeaways

1. **Powerlessness alone doesn't protect intermediaries from blame.** Choosing between two unfair options still draws punishment.
2. **Randomness does protect intermediaries** — a delegee who merely triggers a random process bears no extra blame.
3. **Punishment is more sensitive to the *choice* an actor made than to the *probability* their action contributed to a bad outcome.** This challenges B&F's responsibility measure.
4. **Delegation works as a profit-maximizing blame-shifting tool even when it precludes the fair outcome** — a stronger result than B&F.
5. **Some dictators avoid the profit-maximizing strategy** of delegation even in Choice, suggesting that the "psychological cost of delegating to harm" is not zero.

## Relation to "Algorithms and Responsibility" (this manuscript)

Oexl & Grossman is cited in [literature.tex](../../../manuscript/literature.tex) paragraph 11 alongside Coffman as part of the trio that establishes the robustness of blame-shifting through delegation: "punishment can be successfully avoided through delegation even to a powerless intermediary." It is the closest precedent for thinking about the manuscript's algorithm as a "powerless intermediary."

**Why this paper matters for the manuscript:**

**(1) The Random treatment is the cleanest precedent for the manuscript's algorithm.** Oexl's Random condition — where the intermediary merely triggers a random draw — is essentially what the manuscript's algorithm does. The algorithm in the manuscript's design is a Bernoulli draw at A's empirical accuracy; the algorithm doesn't "choose" anything, it just produces a stochastic outcome. **In Oexl's Random treatment, the intermediary is not significantly punished — but the dictator's punishment *still* drops.** This is potentially a useful comparator for thinking about the manuscript's H2 result: even when the algorithm is "powerless" (no choice), some blame should shift away from the principal. The manuscript's null on H2 is therefore not what Oexl's Random condition predicts.

**(2) The Choice treatment shows that having *some* choice draws blame.** In the manuscript's setup, the algorithm has no apparent choice — it produces a Bernoulli draw. But to the extent that subjects might imagine the algorithm "deciding" anything, it would look more like Oexl's Random treatment than Choice. This is consistent with the manuscript's null: the algorithm in your design is *too random* to absorb blame meaningfully.

**(3) Oexl's challenge to the B&F responsibility measure is highly relevant.** The B&F measure says: an actor is responsible to the extent that their action increased the probability of the bad outcome. In the manuscript's design, Player A delegating or not delegating produces *the same* Bernoulli outcome (the algo is calibrated to A's accuracy), so by the B&F measure A's responsibility is identical across the two paths. This *predicts* the H2 null. Oexl shows that this measure can fail (the intermediary in Choice is blamed even when she didn't change the probability) — but in the manuscript's specific design, the equal-probability calibration makes the B&F measure a clean prediction.

**(4) Oexl shows that some dictators avoid the profit-maximising delegation move.** 33% of dictators in Choice directly chose an unfair allocation despite this being dominated by delegation in expected profit terms. This is a small but real source of "non-strategic" behaviour in delegation decisions and anticipates the manuscript's finding that some Player As prefer direct engagement even when delegation is equivalently profitable. The manuscript's M3 (process ownership) reading is consistent with this: some people just want to *own* the decision.

**(5) Connection to results.tex paragraph 65 ("Departures from prior settings"):** Oexl, like B&F and Coffman, uses a dictator game with explicit fair/unfair alternatives. Your prediction task removes the choice-of-harm framing entirely. Oexl's results suggest that *some* blame-shifting through delegation persists even in stripped-down designs (Random treatment), but the magnitude shrinks. The manuscript's design may simply be *too stripped* for any residual shifting to be detected.

**Suggested integration:**

- Literature.tex paragraph 11 already cites Oexl correctly. Worth strengthening with one more sentence noting that the manuscript's algorithm is structurally similar to Oexl's Random intermediary (no choice; triggers a stochastic process), and that Oexl's Random treatment found blame-shifting only weakly. This makes the manuscript's H2 null less surprising than a strict reading of B&F would suggest.
- If you want to engage with the *responsibility measure* discussion in the discussion section, Oexl's Choice result (intermediary punished without contributing to probability) is the strongest existing critique of the B&F measure. Your design's null on H2 is *consistent* with the B&F measure in a setting where it actually applies (equal-probability outcomes), which is a small methodological point in your favour.

**Worth flagging:** Oexl notes that in their Random treatment, only 9% of dictators chose unfair directly — most either delegated (43%) or chose fair (48%). The pattern flips the more salient the "harm via delegation" framing becomes. The manuscript's prediction task makes this framing absent entirely, which probably contributes to delegation rates that look more like a coin flip than a strategic choice.
