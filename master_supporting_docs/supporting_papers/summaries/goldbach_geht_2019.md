---
title: "Transferring decisions to an algorithm: A simple route choice experiment"
authors: Carina Goldbach, Deniz Kayar, Thomas Pitz, Jörn Sickmann
venue: Transportation Research Part F: Traffic Psychology and Behaviour
year: 2019
volume: 65
pages: 402–417
doi: 10.1016/j.trf.2019.08.011
bibtex_handle: goldbach_geht_2019
pdf: ../goldbach_geht_2019.pdf
relevance_to_manuscript: medium — algorithm delegation in route-choice game; cited in lit.tex ¶21
---

# Goldbach, Kayar, Pitz & Sickmann (2019) — *Transferring decisions to an algorithm: A simple route choice experiment*

## Research question

Do people delegate route-choice decisions to a reinforcement-learning algorithm, and **what personality factors moderate** delegation behaviour? The applied motivation is autonomous traffic: when humans share or delegate driving decisions to algorithms, who does so more readily?

## Methods

- **Lab experiment**, Rhine-Waal University of Applied Sciences, Germany.
- **Task**: route choice game (Selten et al. 2007). 18 players choose between the main road or the side road for 200 periods. Subjects can delegate the decision to a reinforcement algorithm.
- **N = 216** participants.
- Measure: delegation rates, conditional on traffic information and personality.

## Key results

- **Delegation rates average around 10%** — quite low.
- Substantial heterogeneity across players and across levels of traffic information.
- **Extraverted individuals delegate more** than introverts.
- Other personality factors don't show robust effects.

## Main takeaways

1. **Delegation to algorithms is low (10%)** in a non-moral-domain task with clear outcomes.
2. **Personality matters**: extraversion predicts delegation.
3. **Context matters**: traffic information availability affects delegation.
4. **External-validity caveat**: 10% delegation is much lower than the ~50% the manuscript observes.

## Relation to "Algorithms and Responsibility" (this manuscript)

Goldbach et al. is cited in [literature.tex](../../../manuscript/literature.tex) paragraph 21: "Goldbach et al. (2019) report similar aversion when the decision affects both the decision-maker and a third party."

**Note on bib entry:** This entry originally had a `VERIFY` flag in the bib because the original title was a German title that couldn't be located. The verifier replaced it with the indexed Goldbach 2019 Transportation Research paper. The PDF confirms this is the right paper. The author "Kayar, Devran" in the bib was also corrected to "Kayar, Deniz" based on the PDF.

**Why this paper matters for the manuscript:**

**(1) Low delegation rate (10%) is a useful comparator.** Goldbach et al.'s 10% delegation rate is substantially lower than the manuscript's ~50%. Possible explanations:
- Route choice has high subject investment (200 periods); delegating means giving up substantial agency over a sustained task.
- The task is iterative and learnable; subjects may prefer their own learning over algorithm's.
- The manuscript's calibration of the algorithm to A's accuracy creates a stronger "indifference" frame.
- The manuscript's prediction task is one-shot; Goldbach is repeated.

**(2) Personality moderator (extraversion).** The manuscript doesn't currently measure personality. Adding a Big-Five battery would allow testing whether extraversion predicts delegation in the prediction-task context — a small extension that could be incorporated in revision or future work.

**(3) Different domain (transportation), different moral content (none direct).** Goldbach et al. is not strongly moral-domain — there's no third party harmed. The manuscript's moral content is stronger.

**Where in literature.tex:**

- Paragraph 21 cites correctly. The framing — "Goldbach et al. report similar aversion when the decision affects both the decision-maker and a third party" — is a slight overreach: the route-choice task doesn't have an explicit third party. Suggest softening: "Goldbach et al. (2019) report low delegation rates (~10%) in a route-choice task, and find that personality factors (notably extraversion) predict the propensity to delegate."

**Limitation:** This is a relatively niche paper (transportation journal, applied focus). Its main value for the manuscript is providing a comparator delegation rate from a different task domain, and a personality-moderator finding.
