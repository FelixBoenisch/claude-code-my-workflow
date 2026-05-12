---
title: "Self-Interest through Delegation: An Additional Rationale for the Principal-Agent Relationship"
authors: John R. Hamman, George Loewenstein, Roberto A. Weber
venue: American Economic Review
year: 2010
volume: 100(4)
pages: 1826–1846
doi: 10.1257/aer.100.4.1826
bibtex_handle: hamman_self-interest_2010
pdf: ../hamman_self-interest_2010.pdf
relevance_to_manuscript: very high — complementary precedent to B&F, motivates the "diffusion of responsibility" framing in literature.tex ¶9
---

# Hamman, Loewenstein & Weber (2010) — *Self-Interest through Delegation*

## Research question

Does the principal-agent relationship serve a *non-efficiency* function — specifically, do principals hire agents to take self-interested actions that the principals themselves would be unwilling to take directly? The paper's central conjecture is that delegation allows accountability for morally questionable behaviour to be "vertically diffused, with no individual taking responsibility."

Three sub-questions:
1. Are dictator-game allocations *less* generous when made through an agent than when made directly?
2. Does this hold even when delegation is *chosen* (rather than imposed) and even when agents' intentions are announced?
3. Does the effect survive when there's a single agent (no competition between selfish agents)?

## Methods

- **Three lab experiments**, Pittsburgh PEEL, z-Tree. Subjects from CMU + Pitt. Total *n* ≈ 280 across the three experiments.
- **Game:** Dictator game with $10 endowment. Sharing in $0.10 increments. 12 rounds, random matching, one round paid.
- **Experiment 1 — three conditions:**
  - **Baseline**: dictator decides directly (standard DG).
  - **Agent**: principals select one of three agents to make the allocation on their behalf. Agents are paid a flat $5 regardless of choice — *no monetary incentive* to be selfish or generous.
  - **Agent/Choice**: principals can either decide themselves or pick an agent.
- **Experiment 2 — Announce condition**: same as Agent, but agents publicly announce their intended sharing amount (cheap talk) before being selected. Tests whether the effect requires uncertainty about agent behaviour.
- **Experiment 3 — single-agent condition**: each principal paired with a single agent (no competition between agents); can fire / hire across rounds. Tests whether agent competition is doing the work.

## Key results

**Experiment 1:**
- **Baseline mean sharing: ~$2.07** (typical DG result).
- **Agent mean sharing: ~$1.04** — half of baseline.
- Sharing drops over rounds in Agent treatment as principals select away from generous agents toward more selfish ones (logistic regression: positive coefficient on agent's amount shared in previous round predicts switching away). By round 10–11, sharing is *near zero* in Agent treatments.
- **Agent/Choice** treatment: principals often choose to delegate; resulting sharing is closer to Agent than to Baseline. Delegation is endogenously self-selected by those who want to share less.

**Experiment 2 (Announce):**
- Mean sharing $1.71 Baseline vs $0.65 Announce ($1.69 vs $0.43 excluding round 12) — **62–75% less giving via agents** with the strongest information available.
- Principals overwhelmingly select agents announcing $0–$0.10 (88% select the lowest-announcing agent in rounds 2+).
- Four agents in five sessions earn complete monopoly by reliably announcing $0 — *all* principals hire them.

**Experiment 3 (single agent):**
- Principals can only hire/fire one agent. Still: sharing significantly lower than Baseline ($1.11 vs $1.86).
- Agent competition is not the driver.

**Questionnaire:**
- Baseline subjects report **feeling responsible** for outcomes.
- Agent-condition principals report **not feeling responsible** — they shift moral blame to the agent.
- And — strikingly — **agent-condition principals judge their own behaviour as fairer** than Baseline subjects do, despite sharing substantially less.

## Main takeaways

1. **Delegation moves outcomes toward selfishness**, even when the agent has no monetary incentive to act selfishly. The principal is the source of the selfishness; the agent is the conduit.
2. **The mechanism is psychological diffusion of responsibility**, not strategic incentivisation of the agent. Principals report feeling less responsible and judge their actions as fairer when delegated.
3. **Information transparency doesn't undo it** (Experiment 2). Even when agent intentions are publicly announced and principals are clearly "ordering" selfish behaviour, the diffusion mechanism still operates.
4. **Agent competition is not necessary** (Experiment 3). Single-agent delegation produces the same drift toward selfishness.
5. The paper provides an *additional* economic rationale for the principal-agent relationship beyond skill / opportunity-cost / commitment — namely, the **moral wiggle room** delegation creates for the principal. This is a Dana-Weber-Kuang (2007) result implemented as a delegation result.

## Relation to "Algorithms and Responsibility" (this manuscript)

Hamman et al. is cited in [literature.tex](../../../manuscript/literature.tex) paragraph 9 as a complementary pattern to Bartling & Fischbacher: "dictators are more generous when they allocate directly than when they select an intermediary from a set of candidates." It is positioned alongside B&F as one of the canonical experimental demonstrations.

**Why this paper matters for the manuscript:**

**(1) Hamman provides the principal-side analogue of B&F's third-party-side result.** B&F shows that observers punish less when an action is delegated. Hamman shows that principals *behave* less generously when they delegate — they pre-empt the moral cost of selfishness by routing it through an agent. The manuscript engages with both sides: H1 is principal-side (does delegation rise under punishment?), H2 is observer-side (does punishment fall under delegation?). The manuscript's H1 reversal — punishment makes delegation *less* attractive — is therefore in direct tension with Hamman's principal-side reading, just as the H2 null is in tension with B&F's third-party-side reading. The manuscript's design is testing both branches of the canonical literature simultaneously, and finds both wanting in the algorithmic case.

**(2) The design difference is the same as with B&F: dictator game vs prediction task.** Hamman has explicit fair/selfish choices with self-interested motive; the manuscript has prediction outcomes with aligned incentives. The "moral wiggle room" mechanism in Hamman fires when the principal can pre-emptively avoid the dissonance of being seen (by themselves) as selfish. In the manuscript's prediction task, there is no equivalent dissonance to avoid because choosing to make the prediction yourself is not a selfish act. This is yet another reason why responsibility-shifting motives may not bite.

**(3) The "judged my own behaviour as fairer" finding is suggestive for M3 reasoning.** Hamman's principals who delegate also report their behaviour as fairer than the same outcome chosen directly would be. This is consistent with the manuscript's M3 (process ownership / identity) mechanism reading in reverse: if process ownership matters for self-image, then *not* owning the process when delegating allows the principal to maintain a positive self-image despite a less generous outcome. The manuscript's reversal — delegation falls when punishment is salient — could be read as principals choosing direct engagement to *signal to themselves* that they took the morally salient action. This is exactly the identity-as-asset reading from Bénabou & Tirole 2011.

**(4) Algorithmic delegation should be *easier* than human-agent delegation for moral wiggle room.** An algorithm has no preferences and no judgement of the principal's choices, so it's an even cleaner "moral wiggle room" device than a human agent. Hamman's mechanism predicts that algorithmic delegation should *strengthen* the responsibility-diffusion channel. The manuscript finds the opposite — punishment makes algorithmic delegation *less* attractive. This is a substantive puzzle that the manuscript's M3 mechanism needs to explain.

**(5) Hamman's three-experiment robustness anticipates concerns about the manuscript's design.** A skeptic might say the manuscript's null on H2 is driven by some specific feature of the visual prediction task or the Bernoulli calibration. Hamman shows that the delegation-to-selfishness effect is *robust* across very different operationalisations: forced agents, chosen agents, single agents, announced intentions. By contrast, the manuscript shows that algorithmic delegation under the manuscript's specific conditions does *not* produce equivalent effects. The contrast is informative.

**Where in the manuscript to use this paper more:**

- Literature.tex paragraph 9 already cites it correctly.
- Results.tex paragraph 65 ("Departures from prior settings") could explicitly invoke Hamman's design assumption (fair/unfair binary with monetary motive) as one of the dimensions where the manuscript's design departs.
- The mechanism section (section 4 / M3 discussion) could cite Hamman's "judged my behaviour as fairer" finding as the *psychological* counterpart to your M3 process-ownership reading.

**One missing point:** Hamman explicitly anticipates that the responsibility-diffusion channel should be *vertically* diffused — the principal feels less responsible because the agent is now between them and the outcome. The manuscript's algorithmic case has no "between" — the algorithm is a Bernoulli draw the principal can predict perfectly. The vertical structure of Hamman's diffusion is absent in your design. This may be the cleanest single explanation for why responsibility-shifting motives do not move delegation rates in the manuscript: there's no second moral agent to diffuse to.
