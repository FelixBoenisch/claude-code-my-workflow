---
title: "Sharing Responsibility with a Machine"
authors: Oliver Kirchkamp, Christina Strobel
venue: Journal of Behavioral and Experimental Economics
year: 2019
volume: 80
pages: 25–33
doi: 10.1016/j.socec.2019.02.010
bibtex_handle: kirchkamp_sharing_2019
pdf: ../kirchkamp_sharing_2019.pdf
relevance_to_manuscript: high — cited in lit.tex ¶27 (incentivised precedent); design.tex ¶66 (grounds H2)
---

# Kirchkamp & Strobel (2019) — *Sharing Responsibility with a Machine*

## Research question

Does sharing a decision with a *machine* (vs another human) affect:
1. How responsible / guilty the decision-maker feels?
2. Whether the decision-maker behaves more selfishly?

The motivating idea is the diffusion-of-responsibility literature (Darley & Latané 1968; Engel 2011 meta on dictator games): people behave more selfishly when decisions are shared. The authors ask whether this generalises when the second decision-maker is non-human.

## Methods

- **Lab experiment**, FSU Jena.
- **Binary dictator game** with three treatments (between-subject):
  1. **Single human dictator** (baseline).
  2. **Two human dictators** sharing the decision (joint responsibility).
  3. **One human dictator + computer** sharing the decision.
- Dictators must agree (or sequential agreement protocol) on whether to keep the larger share for themselves at the cost of the recipient.
- Outcomes elicited: chosen allocation; self-reported responsibility; self-reported guilt.

## Key results

- **No significant effect** of partner type (human vs machine) on perceived responsibility or guilt.
- **Small and statistically insignificant** effect on actual choices — there is a *trend* toward more selfish decisions in the human-machine treatment, but not reliable.
- When decision-makers decide alone, selfish choices are rare; selfish choices are more common in shared-decision treatments, but the increase is similar whether the partner is human or machine.

## Main takeaways

1. **Humans behave similarly when deciding with a machine as when deciding with another human** — at least on responsibility, guilt, and (with a small, insignificant trend) on choices.
2. **The diffusion-of-responsibility mechanism appears to operate** regardless of partner type. Sharing a decision with a machine isn't categorically different from sharing with a human.
3. The result is a *null on the human-machine distinction*, which is informative for theory: it suggests that machines, like humans, can absorb some responsibility — at least in the eyes of the decision-maker.
4. The effect sizes are small. The authors flag this as preliminary evidence rather than a definitive resolution.

## Relation to "Algorithms and Responsibility" (this manuscript)

Kirchkamp & Strobel is cited in [literature.tex](../../../manuscript/literature.tex) paragraph 27 as one of the small incentivised experimental literature on responsibility perceptions involving algorithms: "they find no significant differences in self-reported responsibility between human-computer and human-human teams, although a (statistically insignificant) tendency towards more selfish allocations under shared responsibility with humans." It's also cited in [design.tex](../../../manuscript/design.tex) paragraph 66 as one of the foundations for H2.

**Why this paper matters for the manuscript:**

**(1) Closest *null* precedent.** Most of the relevant prior literature finds *some* effect of algorithmic delegation on responsibility (Feier, Chevrier, Tontrup, Bartling, Hamman). Kirchkamp & Strobel is one of the few studies that finds *no significant effect* on responsibility perceptions or choices. The manuscript's null on H2 (Result 2) is therefore not unique in this literature — Kirchkamp & Strobel reached a similar conclusion in 2019. This is worth flagging in the discussion section: there is a small but real "no effect" subliterature, and the manuscript's H2 result joins it.

**(2) Design differences explain the partial-overlap result pattern.**

| Feature | Kirchkamp & Strobel (2019) | This manuscript |
|---|---|---|
| Task | Binary dictator game (fair vs unfair allocation) | Visual prediction task |
| Self-interest of dictator | Strong (unfair = higher payoff) | Absent (payoff doesn't depend on outcome) |
| What the machine does | *Shares* the decision with the human (not full delegation) | *Replaces* the human if delegated; full delegation |
| Calibration | Not relevant — machine has its own decision rule | Individual-level Bernoulli at A's accuracy |
| Outcome variables | Self-reported responsibility, guilt; choice | Player B's costly punishment; delegation rate |

The Kirchkamp design has *shared* decision-making (both human and machine contribute), whereas the manuscript has *full delegation* (one or the other). The manuscript's H2 setup is therefore closer to Feier or Chevrier than to Kirchkamp. The fact that *both* designs find a null on the human-machine distinction (Kirchkamp on choices; manuscript on punishment) is therefore moderately convergent evidence.

**(3) Kirchkamp's finding of similar perceived responsibility supports the manuscript's M3 framing.** If subjects feel equally responsible whether they share a decision with a human or a machine, then "process ownership" / "accountability salience" is a candidate explanation for the manuscript's H1 reversal that doesn't require subjects to view algorithms as morally distinct entities. The principal feels responsible for the *act of delegating itself* — and the type of delegate matters less than the *fact* of delegation.

**(4) The dictator-game design with strong self-interest is the standard contrast point.** As with B&F, Hamman, Oexl, Coffman, Chevrier, Tontrup — Kirchkamp & Strobel uses a dictator-game setup where being unfair has direct self-interest. The manuscript's prediction task does not. The pattern across the literature is becoming clearer:
- In dictator games with self-interested motive: responsibility-shifting effects are *strong but heterogeneous* across designs.
- In aligned-incentive prediction settings (this manuscript): responsibility-shifting effects are *weak or null*.

This is worth making more explicit in the manuscript's discussion: the contrast in task type is becoming a key moderator in this literature.

**Where in literature.tex:**

- Paragraph 27 cites it correctly with appropriate framing.
- Design.tex paragraph 66 includes it as part of the foundation for H2. Reading the paper, this citation supports H2 only weakly — Kirchkamp's finding is *not* that delegated decisions get punished less; it's that perceived responsibility doesn't differ between human-machine and human-human teams. The H2 derivation might lean more on Feier, Bartling, and Hamman than on Kirchkamp.

**Worth noting:** Kirchkamp & Strobel is one of the earliest econ experiments on shared human-machine decision-making. Its null result was somewhat overlooked in subsequent work that emphasized the positive findings (Feier 2022). The manuscript's H2 null result is therefore not new in spirit — but the manuscript provides a much cleaner identification (individual-level calibration, separate delegator/evaluator pools) for *why* the null might hold.

**Limitation worth flagging:** Kirchkamp's machine has its own decision rule but no individual calibration. The choices the machine "makes" are effectively predetermined. This makes the design closer to "rolling a die" than to "delegating to a competent agent" — and the small effect sizes may partly reflect that. The manuscript's individual-level Bernoulli calibration is a methodologically cleaner version of the same idea.
