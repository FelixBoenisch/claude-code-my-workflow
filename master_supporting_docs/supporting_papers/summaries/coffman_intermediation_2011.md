---
title: "Intermediation Reduces Punishment (and Reward)"
authors: Lucas C. Coffman
venue: American Economic Journal — Microeconomics
year: 2011
volume: 3(4)
pages: 77–106
doi: 10.1257/mic.3.4.77
bibtex_handle: coffman_intermediation_2011
pdf: ../coffman_intermediation_2011.pdf
relevance_to_manuscript: very high — reinterprets the B&F mechanism; literature.tex ¶11 + ¶32 footnote
---

# Coffman (2011) — *Intermediation Reduces Punishment (and Reward)*

## Research question

Does intermediation in moral decisions — putting another party between the actor and the affected — reduce punishment, **and if so, why?** The motivating example is Merck selling a cancer drug to Ovation, which then raised prices 10×; the public outrage that did *not* fall on Merck.

The paper engineers a sequence of treatments to *isolate the mechanism* behind a result already known qualitatively (Bartling & Fischbacher 2012 had a working paper at the same time): is the effect driven by (i) responsibility diffusion across two agents, (ii) the presence of a market or transactional frame, (iii) the act of "taking" being more outrageous than the act of "keeping," or (iv) something else?

## Methods

- **Lab experiment**, Harvard Business School (CLER lab), 2008–2009. z-Tree 2.1.4. *n* per treatment ≈ 24–36. All subjects under 30 (recruitment glitch flagged in paper).
- **Game — The Intermediation Game.** Four players: first mover, intermediary, receiver, punisher.
  - First mover owns a $10 DG with the receiver. She can either play it herself or **sell** it to the intermediary at a price $X ∈ {5, 6, 7, 8, 9, 10}. If sold, intermediary plays the DG with the receiver, but must keep at least $X.
  - Intermediary endowed with $5. Punisher endowed with $5.
  - Punisher can **costlessly** reduce the first mover's payoff. (Costless to maximise power; pilot results with costly punishment qualitatively the same.) **Punishment only of the first mover** in the main game.
  - Strategy method elicits punishment in all 27 scenarios.
- **Five treatments (between-subject):**
  - **Intermediation Game** (main): as above.
  - **No Intermediary** (control): standard Third Party Punishment DG (Fehr & Fischbacher 2004).
  - **Two Punishments:** punisher can punish both first mover and intermediary.
  - **Reflection:** subjects spend 4 minutes writing about motives before playing (Paharia et al. 2009 intuition-vs-deliberation hypothesis).
  - **Allow-Taking Game:** First mover first plays the $10 DG directly with receiver, then decides whether to *allow* the intermediary to take from the amount sent to the receiver. **Direct interaction with the receiver is preserved** even when the intermediary is included.
  - **Forced-Taking Game:** First mover decides whether to start with $10 or have receiver start with $10; in the latter case, intermediary takes from receiver to pass to first mover. Tests whether "taking vs keeping" framing matters.
- **Belief elicitation** runs after the four-period game.

## Key results

**Result 1 — Intermediation reduces punishment.** When first mover extracts more than $7 from the DG, average punishment for "directly keeping $X" is significantly higher than for "selling the DG for $X" (matched signed-rank tests, *p* < 0.05 at $8, $9, $10). At $10 of self-extracted earnings, direct keeping draws ~$5 average punishment vs ~$3 for indirect.

**Result 2 — The mechanism is "direct interaction," not responsibility diffusion.**

This is the central finding. Three pieces of evidence:

1. **Two-Punishments treatment**: punishers can punish both first mover and intermediary, yet first movers in the intermediated game are still punished less than in the direct game. So it's not that "the intermediary absorbs the punishment quota."
2. **Reflection treatment**: forcing subjects to think carefully about motives does *not* eliminate the intermediation effect. Not driven by intuitive haste.
3. **Allow-Taking Game**: punishment is *not* reduced by intermediation in this design. The first mover plays the DG directly with the receiver first, then permits the intermediary to take; same final allocation, same intermediary, same payoff vector — but the first mover directly interacted with the receiver. **No punishment reduction.**

The combined evidence rules out diffusion of responsibility, outcome-based fairness, intention-based fairness, and framing effects (taking vs keeping). The remaining mechanism that fits is **direct interaction**: punishers care about whether the first mover *interacted with* the affected party, independent of the actual harm or the path.

**Result 3 — Welfare consequence.** When intermediation is available, pro-social norms become difficult to enforce. The poorest player ends up with ~36% of what she would have made in the standard third-party punishment game; if the intermediary is actually used, she ends up with less than 5%.

**Result 4 — Reward also falls under intermediation** (follow-up charity study). The "indirectness reduces moral salience" effect is symmetric across the credit-blame dimension, contrary to Steffel et al. (2016).

## Main takeaways

1. **Intermediation reduces punishment robustly**, but not for the reasons typically given by outcome- or intention-based social preference models. Both predict *more* punishment for intermediation since it weakly hurts equity and the poorest player.
2. **The mechanism is direct interaction.** A first mover who never directly interacts with the affected party is judged less harshly than one who does, even when the final allocation is identical and the responsibility logic is identical.
3. **This mechanism is distinct from responsibility diffusion / blame-shifting** that Bartling & Fischbacher 2012 emphasise. Coffman explicitly designs the Allow-Taking Game to separate the two and finds the diffusion explanation fails.
4. **The effect is welfare-significant** — the availability of intermediation effectively neutralises third-party punishment as a pro-social enforcement mechanism.
5. The mechanism generalises to **rewards**: indirectness reduces both punishment for selfish actions and praise for generous ones.

## Relation to "Algorithms and Responsibility" (this manuscript)

Coffman is cited in [literature.tex](../../../manuscript/literature.tex) paragraph 11 as reinterpreting the B&F mechanism: "He finds that punishment decreases not because of any inherent shifting of blame to the intermediary, but because the dictator no longer 'directly interacts' with the affected party." It is also cited in [results.tex](../../../manuscript/results.tex) footnote (paragraph 32) for the non-trivial punishment in scenarios where the decision could not have been improved upon.

**Why this paper matters for the manuscript:**

**(1) Coffman's mechanism (direct interaction) is highly relevant to the algorithmic-delegation case.** When Player A delegates to an algorithm, A no longer directly interacts with Player B in any meaningful sense — even when not delegating, A's interaction with B is mediated by the prediction task. The algorithm is a *more extreme* form of intermediation than Coffman's: there's no human agent at all. If Coffman's mechanism is doing real work, the manuscript should see reduced punishment for delegated decisions. The fact that the manuscript finds **no significant punishment differential** (Result 2) is therefore evidence *against* Coffman's mechanism applying to algorithmic intermediation in this setting.

**(2) The manuscript's design is closer to Coffman's Allow-Taking Game than to his Intermediation Game.**
- In Coffman's *Allow-Taking* setup, the first mover plays the DG directly with the receiver and then permits intermediation. No punishment reduction.
- In the manuscript, Player A always interacts with Player B's payoff via the prediction task; the algorithm only changes who *makes* the prediction, not who is in the causal chain.
- This is a useful framing for the H2 null in your data: the prediction-task setup is structurally similar to Allow-Taking, where Coffman *also* finds no punishment reduction for intermediation.

**(3) Coffman's intermediary is similarly "powerless" to the manuscript's algorithm.** The intermediary in Coffman's main game has no choice over rents extracted — the first mover sets the price. So punishment for the intermediated outcome falls on the first mover, not the intermediary. The manuscript's algorithm is even more powerless (it produces a Bernoulli draw with predetermined probability). The fact that Coffman *still* finds reduced punishment for intermediation despite the intermediary's powerlessness is informative — it shows the effect isn't about transferring blame to an agent that "deserves" it.

**(4) The credit-blame symmetry contrasts with Steffel et al. 2016.** Coffman's follow-up reward study shows that indirectness reduces *both* punishment and reward. Steffel et al. find an asymmetry — people care more about avoiding blame than claiming credit. The manuscript could engage with this tension when discussing Steffel et al. (cited in lit.tex ¶13).

**Suggested integration into literature.tex:**

- Paragraph 11 already cites Coffman correctly for the mechanism reinterpretation.
- Worth adding a sentence in results.tex paragraph 65 ("Departures from prior settings") noting that the manuscript's design is structurally close to Coffman's Allow-Taking Game (where intermediation does not reduce punishment) rather than to his Intermediation Game (where it does). This sharpens the explanation of why H2 is null.
- Consider citing Coffman's welfare result — that intermediation neutralises pro-social punishment as enforcement — when discussing the policy implications of widespread AI delegation in section 5 (conclusion). The Köbis et al. 2025 compliance asymmetry result and Coffman's welfare result tell the same story from different sides.

**Where the manuscript and Coffman diverge:**

Coffman uses a dictator game with clear selfish intent (you choose to keep $X). The manuscript uses a prediction task with uncertain outcomes. As with Bartling & Fischbacher, this difference may explain why mechanisms that work in Coffman's setting don't translate. The "direct interaction" channel needs a salient direct interaction to *not* have — in the manuscript's design, there's barely any direct interaction even in the no-delegation case (Player A and Player B never communicate; A just generates a prediction). The mechanism may simply have nowhere to bite.

**Worth flagging:** Coffman's framing question — "what would it teach us more generally about how we punish?" — is exactly the framing the manuscript's M3 (process ownership) tries to update for the algorithmic case. Coffman's mechanism is third-party-side ("how the punisher sees the act"); the manuscript's M3 is principal-side ("how the actor anticipates the moral salience of accountability"). These are complementary, not competing, and could be discussed together in the mechanism section.
