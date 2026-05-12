---
title: "Shifting the Blame: On Delegation and Responsibility"
authors: Björn Bartling, Urs Fischbacher
venue: Review of Economic Studies
year: 2012
volume: 79(1)
pages: 67–87
doi: 10.1093/restud/rdr023
bibtex_handle: bartling_shifting_2012
pdf: ../bartling_shifting_2012.pdf
relevance_to_manuscript: very high — canonical experimental demonstration, anchors literature.tex ¶7, and H1 builds on its punishment-avoidance result
---

# Bartling & Fischbacher (2012) — *Shifting the Blame: On Delegation and Responsibility*

## Research question

Two questions, both novel at the time:
1. **Is the responsibility for an outcome delegated along with the decision right?** I.e., can a principal *successfully* shift blame onto a delegate?
2. **Is punishment-avoidance through blame-shifting a strong motive for delegating in the first place?**

The paper also asks, methodologically, what model of social preferences (outcome-based inequity aversion, intention-based reciprocity, or a new responsibility measure) best predicts punishment behaviour.

## Methods

- **Lab experiment**, University of Zurich, z-Tree + ORSEE, conducted 2006–2010 across multiple sessions. No econ or psych students. Total *n* ≈ 750 across all treatments.
- **Game:** Groups of four — Player A (dictator), Player B (potential delegee), and two Player Cs (receivers). 20-point endowment. **Fair** allocation: (5, 5, 5, 5). **Unfair** allocation: (9, 9, 1, 1). A's and B's payoffs are *aligned* (both prefer unfair).
- **Punishment:** Player C (one of the two, randomly selected) can spend 1 point to assign up to 7 punishment points across A, B, and the other C (the other C as distractor against demand effects). Strategy method elicits punishment in every possible (A's action × B's action) configuration.
- **Treatments (between-subject):**
  - **noD&noP** — no delegation, no punishment (baseline)
  - **noD&P** — no delegation, with punishment
  - **D&noP** — delegation possible, no punishment
  - **D&P** — delegation possible, with punishment (main treatment)
  - **Random** — A can delegate to a die that picks unfair with prob 0.4 (matched to actual rate of unfair Bs); both die and unfair-direct are A's options
  - **Asymmetric** — A can only be fair *or* delegate (not unfair directly); B then chooses
  - **Repeated** — D&P played 10 times with rematching
- **Belief elicitation** ran in a separate session with 32 different subjects, to compute beliefs needed for the intention and responsibility measures.

## Key results

**On punishment patterns (Result 1 — blame is delegated):**

- If A is unfair: A receives heavy punishment, B receives none (since B did nothing).
- If A delegates and B is unfair: **B receives heavy punishment, A is almost spared.** Most of the punishment is shifted to the delegate.
- If A delegates and B is fair: minimal punishment to either.
- If A delegates to the die and die picks unfair: A is punished less than for choosing unfair directly, but more than when delegating to B (the die can't absorb blame as effectively as a human delegate).
- In the **asymmetric** treatment (A can only delegate or be fair): A's delegation receives more punishment than in D&P because the kindness of A's action is judged relative to the available action set; delegation is now A's *least kind* action.

**On delegation rates (Result 2 — punishment-avoidance drives delegation):**

- In **D&noP** (no punishment), only **17%** of As delegate.
- In **D&P** (punishment on), **56%** of As delegate — *more than three times higher* (Fisher exact *p* < 0.01).
- In **Random** (delegate to die), 39% delegate — less than D&P because the die absorbs less blame.
- In **Asymmetric** (delegate to escape unfair label), 78% delegate.
- In **Repeated**, delegation rises from 53% (first 5 periods) to 66% (last 5) — the motive is stable and even strengthens with experience.

**Pay-off ranking:** In D&P, delegation is highly significantly more profitable than either being fair or unfair directly. Expected pay-offs: delegation 5.93 > fair 4.80 > unfair 4.73. **Delegating maximises pay-off** even though it means losing control.

**Mechanism comparison:** A simple "responsibility measure" — defined as the share of the probability increase of the unfair outcome attributable to a player's action — outperforms inequity aversion (Fehr-Schmidt) and intention-based reciprocity (Rabin) in predicting punishment patterns (R² = 0.42 vs 0.21 outcome-only and 0.29 intention-only).

## Main takeaways

1. **Responsibility is delegated along with the decision right.** Principals are spared most punishment for the delegate's unfair choice. This is robust and replicable.
2. **Punishment-avoidance is a strong delegation motive.** Removing the punishment possibility cuts delegation rates from 56% to 17%.
3. **Some responsibility can also be shifted to chance** (die treatment), though less effectively than to a person.
4. **Even kindness-of-action matters**, not just outcome — in the asymmetric treatment delegation absorbs more blame because it's the *least kind* available action.
5. **Outcome-based and intention-based social preferences are both incomplete.** The responsibility measure (who shifted the probability of the unfair outcome upward) explains punishment best.
6. The paper anchored the experimental responsibility-shifting literature. Every subsequent paper in the manuscript's literature review derives from this design.

## Relation to "Algorithms and Responsibility" (this manuscript)

Bartling & Fischbacher is the **direct intellectual parent** of the manuscript. Three points of contact:

**(1) H1 is a literal translation of B&F's Result 2 to algorithmic intermediaries.**

The manuscript's H1 — "the introduction of potential punishment increases the likelihood that Player A delegates to the algorithm" — exactly mirrors B&F's 56% vs 17% comparison, transplanted from "delegate to another human" to "delegate to an algorithm." Literature.tex paragraph 7 and design.tex paragraph 66 both cite B&F as the foundation for the hypothesis. The fact that this hypothesis **fails in the manuscript's data** (and the effect runs in the opposite direction) is therefore a substantive contrast with B&F that needs to be reckoned with — which is what results.tex paragraph 65 begins to do.

**(2) The design differences explain at least part of the H1 reversal.**

| Feature | Bartling & Fischbacher (2012) | This manuscript |
|---|---|---|
| Task | Fair vs unfair allocation (dictator game) | Prediction task (visual weight estimation) |
| Outcome certainty | Deterministic | Genuinely uncertain |
| Self-interest | A keeps 9 if unfair vs 5 if fair → **strong selfish motive** | A's payoff doesn't depend on prediction outcome → **no selfish motive** |
| Aligned vs misaligned | A and B aligned; both vs C | A and B weakly aligned |
| Intent visible from action | Yes — choosing "unfair" is unambiguously selfish | No — bad outcome could be effort, luck, or both |
| Delegate type | Another human; or a die (random) | Algorithm calibrated to A's own performance |
| Punishment cost | 1 point flat, up to 7 in penalty | £0.10 flat, up to £2 in penalty |
| Punishment baseline | Heavy punishment for unfair allocations (~4.27 points to A if unfair) | Modest punishment, even for good outcomes (~£0.30); 45% of B's never punish |

The combination of (i) uncertain outcome and (ii) aligned incentives means the **intent-signalling content of "delegate vs not-delegate"** is much weaker in the manuscript's design than in B&F. A Player A who delegates in B&F is plausibly trying to dodge blame for an outcome she would benefit from; a Player A who delegates in the manuscript could just as plausibly be deferring to a presumed-competent algorithm. This is exactly the point results.tex paragraph 65 raises: "These aspects may obfuscate the intent of Player A, possibly diluting an intention-based punishment motive for Player B." B&F's Result 1 (responsibility *can* be shifted) requires that observers be able to read a delegation as morally suspect; the manuscript's design strips that signal.

**(3) B&F's "responsibility measure" anticipates the manuscript's M3 mechanism.**

B&F's preferred punishment model — a player's responsibility is their share in the probability increase of the unfair outcome — is the closest formal antecedent in the literature to what the manuscript calls M3 (process ownership). In the manuscript's setting, this responsibility measure would assign similar (negligible) shares to A and to the algorithm under delegation (since both produce the high payoff with the same probability), which is exactly why Player B does *not* differentially punish in the data (Result 2). The B&F mechanism, transplanted, *predicts* the manuscript's H2 null.

**(4) The "delegation to a die" result anticipates an ambiguity in the manuscript's algorithmic delegation.**

In B&F's random treatment, A successfully shifts some responsibility to the die but less than to a human delegate. This raises a deep question for the manuscript: is the algorithm in the manuscript's design more like B&F's die (impersonal randomness) or more like B&F's B (an agent that could absorb blame)? The individual-level Bernoulli calibration arguably makes the algorithm *more die-like* than human-like, which is yet another reason H2 might not find a punishment differential.

**(5) Where the two papers complement each other.**

B&F demonstrates that in a setting designed to make blame-shifting *easy and observable*, principals exploit it strongly. The manuscript demonstrates that in a setting designed to make the responsibility channel *clean and not confounded with signal extraction*, the same strategic exploitation is absent — and the responsibility motive even runs the other way (toward direct engagement). Together, the two papers bracket the range of how much the responsibility-shifting motive depends on the moral transparency of the underlying decision: a great deal.

**Where it appears in literature.tex:** Paragraph 7 introduces B&F as "the canonical experimental demonstration" and the methodological template; paragraph 66 in design.tex grounds H1 explicitly in B&F's Result 2. The paper is cited again in the H2 derivation (¶80) as a benchmark.

**Worth considering:** The asymmetric treatment in B&F (where A can only delegate or be fair) is methodologically interesting for thinking about your design. In the manuscript, Player A's choice set is symmetric (delegate or not, both producing equal expected outcomes for B), which is exactly the setup that *minimises* the intention-based punishment differential. B&F shows that when the choice set is asymmetric, the intention-based reading kicks in hard. The manuscript could use this as another argument for why H2 has weaker bite in your design than the B&F literature would suggest.

**One unused B&F insight worth quoting:** The interim-management example (CRO at AlixPartners) and the McShane Group's frank marketing pitch — "moves through these decisions and then move on, allows new, permanent leadership to take the helm untainted" — make the responsibility-shifting motive concrete in a way the manuscript's introduction could borrow if you want a real-world hook beyond AI specifically.
