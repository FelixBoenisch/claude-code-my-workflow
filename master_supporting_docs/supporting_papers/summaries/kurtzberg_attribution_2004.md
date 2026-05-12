---
title: "Human reactions to technological failure: How accidents rooted in technology vs. human error influence judgments of organizational accountability"
authors: Charles E. Naquin, Terri R. Kurtzberg
venue: Organizational Behavior and Human Decision Processes
year: 2004
volume: 93(2)
pages: 129–141
doi: 10.1016/j.obhdp.2003.12.001
bibtex_handle: kurtzberg_attribution_2004
pdf: ../kurtzberg_attribution_2004.pdf
relevance_to_manuscript: high — foundational result on technology-vs-human attribution; cited in lit.tex ¶25
---

# Naquin & Kurtzberg (2004) — *Human reactions to technological failure*

## Research question

When an organisational accident is attributed to **technology** vs **human error**, do observers hold the organisation **less accountable** for technological failures? And if so, what is the cognitive mechanism — specifically, does **counterfactual thinking** mediate the asymmetry?

## Methods

Two vignette experiments.

**Study 1**: Subjects read about an organisational accident attributed to either computer error or human error. Rate the organisation's accountability and generate counterfactual thoughts (alternative scenarios that "could have" prevented the accident).

**Study 2**: Replicates Study 1 in a more natural setting using a less intrusive measure for counterfactual thoughts.

The theoretical anchor is **fairness theory** (Folger & Cropanzano 2001): for accountability to be established, three components must be present — injurious event, discretionary conduct, moral wrongdoing. Technological failures lack the "discretionary conduct" element because machines don't choose.

## Key results

- **Organisations are held *less* accountable when accidents are attributed to technology** vs. when attributed to human error.
- **Mechanism: reduced counterfactual thinking.** Technology-attributed accidents generate fewer counterfactual thoughts of "better possible outcomes" than human-attributed accidents. People don't easily imagine "what if the computer had decided differently?" because they don't perceive machine actions as discretionary.
- The effect is robust across both studies and across different measurement methods.

## Main takeaways

1. **Technology absorbs less accountability than human error** for organisational accidents. People perceive machine actions as less discretionary.
2. **Counterfactual thinking mediates this asymmetry.** When the actor is human, observers imagine alternative actions; when the actor is a machine, they don't.
3. **Foundation for the "algorithmic outrage asymmetry" literature**: Bigman & Gray, Shank et al., and others build on this finding for AI specifically. Naquin & Kurtzberg's contribution is showing the asymmetry exists for simple computers, not just for advanced AI.
4. **Policy implication**: organisations may have incentives to attribute failures to technology rather than to human decision-makers, because technology absorbs less blame.

## Relation to "Algorithms and Responsibility" (this manuscript)

Naquin & Kurtzberg is cited in [literature.tex](../../../manuscript/literature.tex) paragraph 25: "Kurtzberg attribution 2004 find that observers attribute less responsibility to a company when an accident involves technology." It's part of the foundational layer for the moral-attribution-to-machines literature.

**Why this paper matters for the manuscript:**

**(1) Foundational anchor for the manuscript's H2.** The intuition behind H2 — that algorithmic delegation might reduce punishment for the principal — has its empirical roots in Naquin & Kurtzberg. If technology absorbs less accountability than humans, then *not* delegating to technology means the human (Player A) absorbs more of the accountability. The manuscript's H2 null is therefore inconsistent with the Naquin & Kurtzberg prediction.

**(2) Counterfactual thinking is a useful mechanism candidate.** Naquin & Kurtzberg's specific mechanism — fewer counterfactual thoughts for machine actions — could in principle apply to the manuscript's design. When Player B considers a delegated prediction, she might imagine fewer alternative actions ("the algorithm just produced a Bernoulli draw") than when considering a self-made prediction ("Player A could have predicted differently"). This would predict less punishment for delegated decisions — i.e., H2 should hold. The manuscript finds it doesn't. Why?

The most likely answer: in the manuscript's design, the algorithm is *calibrated to Player A's own accuracy*, so the counterfactual question "could Player A have done better?" remains live whether she delegated or not. The counterfactual-thinking channel is therefore *closed off by construction* by the equal-performance calibration. Naquin & Kurtzberg's mechanism doesn't bite because there's no asymmetry in expected performance to generate counterfactual gap.

**(3) The "discretionary conduct" framing aligns with the M3 reading.** Naquin & Kurtzberg argue technology fails to be held accountable because it lacks discretion. The manuscript's M3 mechanism is about the *principal* exercising discretion. When the principal delegates to a non-discretionary algorithm, she effectively eliminates discretionary conduct from the decision chain — which by Naquin & Kurtzberg's logic should shed accountability. But the manuscript shows the principal *resists* this when accountability is salient (H1 reversal). This suggests that under conditions of salient accountability, principals *value* exercising discretion themselves — consistent with M3.

**(4) Methodological note: vignettes vs lab.** As with Bigman, Shank, Hill, Pezzo, Tobia — Naquin & Kurtzberg is vignette-based. The vignette literature is much more consistent about asymmetric machine-vs-human attribution than the incentivised lab literature. The manuscript fits the lab pattern.

**Where in literature.tex:**

- Paragraph 25: correctly cites the central finding.

**Worth noting:** The manuscript's bib entry has a `VERIFY` note from the original lit-review pass — the title and author order needed correction (was originally "Kurtzberg & Naquin" with a different title). The PDF confirms it should be Naquin (first author) and Kurtzberg, with the title above. This was verified earlier in the project; the bib is now correct.
