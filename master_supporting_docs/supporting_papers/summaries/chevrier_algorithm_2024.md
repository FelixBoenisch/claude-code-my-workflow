---
title: "Algorithm Delegation and Responsibility: Shifting Blame to the Programmer?"
authors: Mathieu Chevrier, Vincent Teixeira
venue: GREDEG Working Paper No. 2024-04 (Université Côte d'Azur, CNRS)
year: 2024
url: https://ideas.repec.org/p/gre/wpaper/2024-04.html
bibtex_handle: chevrier_algorithm_2024
pdf: ../chevrier_algorithm_2024.pdf
relevance_to_manuscript: very high — cited in literature.tex ¶27, and again in ¶41 as the third node of the four-channel map
---

# Chevrier & Teixeira (2024 WP) — *Algorithm Delegation and Responsibility: Shifting Blame to the Programmer?*

## Research questions

1. Do users (dictators) try to shift blame to the programmer behind an algorithm by delegating?
2. Who is perceived as responsible for an inegalitarian algorithmic decision — the programmer or the user?
3. Does an AI programmer exploit the "moral wiggle room" afforded by AI autonomy to push the algorithm toward inegalitarian outcomes?

## Methods

- **Lab experiment** at LEEN Nice (CNRS), Jan 2024. oTree on Heroku. *n* = 360 (3 treatments × 120) plus a pre-study (n=46) to calibrate the AI.
- **Pre-registered** at AsPredicted: aspredicted.org/vi74k.pdf.
- **Game (extension of Bartling & Fischbacher 2012):** groups of four — A (dictator), B (intermediary or programmer), C & D (recipients). €20 endowment.
- **Player A's choice set:** (i) egalitarian allocation (5, 5, 5, 5), (ii) inegalitarian allocation (9, 9, 1, 1), or (iii) delegate to B. If A delegates, B faces the same binary choice.
- **Three between-subject treatments:**
  - **Human:** B is a human intermediary (replicates Bartling & Fischbacher).
  - **RA:** B is "programmer" of a rule-based algorithm with 100% control over algorithmic decisions; only the framing differs from Human.
  - **AI:** B is "programmer" of an AI algorithm; B's choice is applied 50% of the time; in the other 50%, the AI chooses autonomously from a pre-study-calibrated distribution (48% inegalitarian).
- **Punishment:** Recipients C and D each independently decide whether to pay €1 to administer up to €7 of punishment allocated across the other three players. Strategy method elicits punishment in all four (A's decision × B's choice) cells. Two-stage measurement: extensive margin (does C/D pay €1 to punish?) and intensive margin (how much, to whom).
- **Post-experiment battery:** Cognitive Reflection Test, NARS, Dohmen risk preference, Control Attitude Scale.

## Key results

- **Result 1 — Delegation rates do not differ across treatments.** Human 17%, RA 17%, AI 23% (n.s.). Replicates the canonical finding that delegation rates are insensitive to intermediary type.
- **Result 2 — Probability of paying to punish is lower under AI.** Conditional on an inegalitarian outcome, 58% of recipients pay €1 to punish in Human, 63% in RA, but only 36% in AI (RA vs AI: χ² = 7.5, *p* = 0.006; Human vs AI: *p* = 0.02). The ambiguity introduced by AI autonomy reduces the willingness to incur punishment cost at all.
- **Result 2.1 — AI programmer is punished less severely than RA programmer** (€2.50 vs €4.45, Wilcoxon *p* < 0.00001). The AI programmer enjoys a "responsibility gap" because the causal link to the algorithm's output is fuzzy.
- **Result 2.2 — AI user is punished more severely than RA user** (€3.91 vs €2.21, Wilcoxon *p* < 0.00001). The opposite-direction effect on the user.
- **Result 2.3 — Expected punishment of the user (probability × magnitude) is similar whether delegating to AI or RA**, because the lower probability of being punished cancels out the higher severity when punished. So delegation still effectively reduces the user's responsibility burden relative to choosing the inegalitarian allocation directly.
- **Result 3 — AI programmers exploit moral wiggle room.** 60% of AI programmers select the inegalitarian distribution, vs 47% of RA programmers and 30% of Human intermediaries (proportion test Human vs AI: *p* = 0.03; probit confirms with controls).
- **Risk attitude:** Risk-loving intermediaries are more likely to choose inegalitarian (exploratory finding, not pre-registered).

## Main takeaways

1. **AI vs RA matters.** The level of programmer control is the central design lever. When the programmer fully controls the algorithm (RA), it's just a relabelled human delegation. When the algorithm is partially autonomous (AI), a responsibility gap opens.
2. **Two opposing effects on user punishment.** Recipients punish AI-delegated users *less often* (extensive margin) but *more severely when they do* (intensive margin). Felix's manuscript only looks at intensive margin (with a fixed €0.10 cost for any positive punishment), so the extensive margin effect documented here is invisible in Felix's data by design.
3. **Moral wiggle room is exploited by programmers.** Programmers respond strategically to the anticipated responsibility gap by choosing inegalitarian more often — a behavioural welfare loss attributable directly to AI autonomy.
4. **Replicates Bartling & Fischbacher's punishment patterns** but with much lower baseline delegation rates (17% vs 55%), which the authors attribute to a higher preference for control or lower CRT in their sample.

## Relation to "Algorithms and Responsibility" (this manuscript)

Chevrier & Teixeira is one of the two **closest contemporaneous precedents** to Felix's paper — already cited in [literature.tex](../../../manuscript/literature.tex) paragraph 27 ("\citet{chevrier_algorithm_2024} extend the blame chain to include the programr behind the algorithm") and again in paragraph 41 as the third node of the four-channel map.

**Where the two designs diverge:**

| Feature | Chevrier & Teixeira (2024) | This manuscript |
|---|---|---|
| Task | Modified dictator game with clear fair/unfair allocations | Prediction task with genuine uncertainty in outcome |
| Delegator incentives | Self-interested (inegalitarian also pays delegator €9 vs €5) | Weakly aligned (better outcome reduces expected punishment) |
| Intermediary types | Human / RA / AI (three between-subject) | Algorithm only; comparison is delegation vs self-decision |
| Programmer present? | Yes — B is the programmer, can be punished separately | No — algorithm is calibrated to Player A's own performance; no human "behind" it |
| Algorithm calibration | Session-level pre-study distribution (48% inegalitarian) | Individual-level Bernoulli at each Player A's accuracy |
| Punishment manipulation | Always on; no between-subject on/off | **Between-subject Punishment vs No-Punishment** |
| Punishment mechanism | Pay €1 to punish + amount up to €7 | Fixed €0.10 cost per scenario, amount in £0.10 increments to £2 |
| Sample | LEEN Nice, 360 lab subjects | Prolific UK, 322 online subjects |

**Where the results agree:**

- Both find that **delegation rates do not respond to the responsibility-shifting margin** the design varies (Chevrier: not by intermediary type; Felix: not in the direction predicted by H1). This is consistent across designs and is a robust finding worth flagging.
- Both find some form of differential punishment treatment between human/self and algorithmic decisions, but the direction and significance differ across designs.

**Where the results disagree and why it matters:**

- **Chevrier finds a clear blame-shifting channel** (programmers exploit it, recipients punish less often under AI). **Felix finds essentially no punishment differential** (H2 borderline insignificant). The two designs differ on two crucial dimensions that almost certainly drive this:
  1. **Task type.** Dictator-game settings with explicit fair/unfair allocations have direct moral intent baked in. The recipient knows the dictator chose to be selfish. Prediction tasks have outcome uncertainty — a bad outcome could be effort, luck, or both. Intention-based punishment loses traction.
  2. **Aligned vs misaligned incentives.** Chevrier's dictator gains by inegalitarian (€9 vs €5); Felix's Player A gains nothing from delegation (her payoff is independent of the prediction's outcome). The "self-interested motive" that triggers blame is absent in Felix's design.
  - Both candidates are explicitly raised as candidate explanations for Felix's null in [results.tex](../../../manuscript/results.tex) paragraph 65 ("Departures from prior settings").
- **Chevrier identifies a programmer-blame channel that Felix's design cannot.** Felix's algorithm has no programmer because it's calibrated to A's own performance and presented as a Bernoulli draw with known probability. This is a *deliberate* design choice — Felix is studying the principal's accountability salience (M3), not the programmer's moral wiggle room.

**Where Felix's design produces evidence Chevrier's cannot:**

- The **punishment-on/off manipulation** is unique to Felix and identifies whether punishment *itself* moves the delegation decision. Chevrier's design has punishment always on, so it cannot answer this question. Felix's finding that punishment *reduces* delegation rate goes against the pure responsibility-shifting story that Chevrier's setup is designed to test.
- The **individual-level Bernoulli calibration** strips the signal-extraction channel (Player B can't infer overconfidence from Player A's delegation decision). Chevrier's session-level AI calibration leaves this channel partially open.

**How this currently appears in literature.tex:**

- Paragraph 27 introduces the paper as extending the blame chain to the programmer.
- Paragraph 41 places it as one of four nodes — alongside Feier (signal-extraction), Felix (process-ownership), and Köbis (compliance asymmetry) — in a single emerging map of how AI delegation affects responsibility.
- The "Departures from prior settings" discussion in results.tex paragraph 65 echoes this paper's design contrasts (task type, aligned incentives) as candidate explanations for Felix's failed H1.

**Worth considering for the discussion section:** Chevrier's finding that delegation rates are stable across intermediary types — combined with the manuscript's finding that they *fall* under punishment — together suggest that the responsibility-shifting motive is real but weaker than the literature has assumed, and that other forces (process ownership, accountability salience) may dominate when the incentive structure is sufficiently neutral.

**Worth considering for future work:** A natural design extension — combining Chevrier's programmer manipulation with Felix's individual-level calibration and punishment on/off — would isolate the four channels cleanly. The manuscript already gestures toward this in literature.tex paragraph 41 ("A unified design that varies the relative-performance calibration, the punishment possibility, and the visibility of the algorithm's compliance properties would be the natural next step.").
