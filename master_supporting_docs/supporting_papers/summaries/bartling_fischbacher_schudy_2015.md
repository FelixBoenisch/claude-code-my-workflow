---
title: "Pivotality and responsibility attribution in sequential voting"
authors: Björn Bartling, Urs Fischbacher, Simeon Schudy
venue: Journal of Public Economics
year: 2015
volume: 128
pages: 133–139
doi: 10.1016/j.jpubeco.2015.03.010
bibtex_handle: bartling_fischbacher_schudy_2015
pdf: ../bartling_fischbacher_schudy_2015.pdf
relevance_to_manuscript: high — extends B&F's responsibility-shifting result to collective decision-making; added for subsection 1 breadth
---

# Bartling, Fischbacher & Schudy (2015) — *Pivotality and responsibility attribution in sequential voting*

## Research question

In collective decision-making settings reached by a transparent voting process, **are decision-makers blamed differently depending on whether their vote is pivotal** for an unpopular outcome? Specifically, the paper asks whether non-pivotal voters can escape responsibility while pivotal voters bear the full weight of the group's choice.

This is a direct extension of Bartling & Fischbacher (2012) into the *group decision-making* domain — where delegation is implicit (passing responsibility to subsequent voters by voting strategically early) rather than explicit (handing the decision to an agent).

## Methods

- **Incentivised laboratory experiment**, University of Zurich, z-Tree + ORSEE. *n* = 144 across 4 sessions (Nov–Dec 2012).
- **Game setup**: groups of six — three voters and three recipients without voting rights.
  - **Equal allocation**: (5, 5, 5, 5, 5, 5).
  - **Unequal allocation**: (9, 9, 9, 1, 1, 1) — favours voters at recipients' expense.
- **Sequential voting**: Voter 1 votes first; Voter 2 observes V1 and votes; Voter 3 observes V1 and V2. Simple majority. No abstentions.
- **Punishment phase**: one randomly selected recipient can punish individual voters at a cost of 1 point per 7 points deducted. Strategy method elicits punishment for every possible voting history.
- **Voters also use the strategy method**: each subject decides at every decision node (as V1, V2, V3 across all pre-play histories) before learning their assigned role.

## Key results

**Result 1 — Pivotal voters are punished more.**
Recipients assign significantly more punishment to the *pivotal* voter (the one whose vote actually decided the outcome) than to the other voters who supported the same unequal allocation. The effect holds controlling for outcome-based fairness (Fehr-Schmidt, Bolton-Ockenfels), intention-based reciprocity (Rabin, Dufwenberg-Kirchsteiger), and combined outcome-intention models (Falk-Fischbacher).

**Result 2 — Voters strategically avoid being pivotal.**
About **one-fifth** of voters who reveal a preference for the unequal allocation when voting last (decisive) instead vote for the *equal* allocation when given the option to "delegate" the pivotal vote to a later voter. They exploit the sequential structure to shift the blame to whoever votes after them.

**Result 3 — Standard social preference models cannot explain the data.**
- Outcome-based models predict no difference across voters (only outcome matters).
- Intention-based models predict equal punishment for all voters of the unequal allocation.
- The pivotality effect is *additional* to these standard motives.

## Main takeaways

1. **Pivotality is itself a responsibility-attribution dimension** that outcome-based and intention-based social preference models miss.
2. **Group decision-making provides a "soft delegation" path**: by voting strategically to avoid being pivotal, voters can shift responsibility to subsequent voters without ever formally delegating.
3. **The Shapley-Shubik intuition is confirmed**: "the member who voted last is given credit for having passed it" — pivotal voters bear the burden.
4. **One-fifth strategic-pivotality-avoidance rate** is substantial — voters actively use this mechanism in practice.
5. The paper extends the B&F (2012) responsibility-shifting tradition into committee/voting/board settings where delegation is implicit through the timing and order of decisions.

## Relation to "Algorithms and Responsibility" (this manuscript)

Bartling, Fischbacher & Schudy is **not yet cited** in literature.tex but should be added to subsection 1 (Responsibility avoidance through delegation) per the recent restructuring discussion. It's the canonical voting / group-decision domain extension of B&F (2012).

**Why this paper matters for the manuscript:**

**(1) Demonstrates the responsibility-shifting motive in non-dictator-game settings.** This is the strongest argument for citing it in subsection 1: the result generalises to a fundamentally different setting (sequential voting in committees) without losing the core finding. The dictator-game-centric literature gets a clean parallel in the voting domain.

**(2) "Soft delegation" through strategic voting.** Where B&F (2012) shows explicit delegation reduces blame, Bartling-Fischbacher-Schudy shows that even *implicit* delegation through vote ordering can shift responsibility. This widens the empirical case for the responsibility-shifting motive — it's not just about handing decisions to a designated agent; it's about any path that distances the principal from the marginal decision.

**(3) The pivotality framework is conceptually related to the manuscript's algorithm.** The manuscript's algorithm is, in a sense, *non-pivotal* in the responsibility-attribution sense: it's a Bernoulli draw calibrated to A's empirical accuracy, so its "vote" doesn't change the probability of any outcome relative to A's own performance. By B-F-S's logic, the algorithm should absorb very little blame — which is broadly consistent with the manuscript's H2 null. The pivotality framing could be worked into the H2 discussion if the manuscript wants a more formal account of why the algorithm doesn't absorb blame.

**(4) Shapley-Shubik framing for the conclusion section.** The Shapley-Shubik intuition that "the marginal contributor takes the credit" is a useful theoretical anchor for thinking about how responsibility gets distributed in mixed human-algorithm decision chains. Worth referencing if you write a section on policy implications.

**Where to cite in literature.tex:**

- Paragraph 15 (subsection 1 breadth-list): cite as the voting/group-decision domain extension of responsibility-shifting. Already drafted in earlier discussion:
  > "...the responsibility-shifting motive has been documented across a range of practical domains: ... sequential voting where non-pivotal voters are punished less than pivotal ones for the same group outcome \citep{bartling_fischbacher_schudy_2015}..."

**Cross-references in the manuscript's existing citations:**

- The paper is cited in Argenton et al. 2023 as evidence of strategic responsibility-avoidance through the voting structure.
- Kirchkamp & Strobel 2019 cites it in their reference list.

**Methodological note for the manuscript**: B-F-S uses the strategy method for both voters and recipients, with a randomly drawn recipient as the binding punisher. The manuscript uses a similar structure (Player B uses strategy method for punishment across the four (delegation, outcome) cells). The methodological alignment is natural and worth flagging in the manuscript's methodological discussion if relevant.

**Important caveat**: The B-F-S effect operates through *sequence* of voting, which has no analog in the manuscript's binary delegation choice. The conceptual parallel is closer to "the algorithm acts after the principal's delegation decision is made, so its contribution to the probability of any outcome is determined" — which is structurally different from voting. Cite for breadth, but don't lean on it for mechanism claims.
