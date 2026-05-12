---
title: "Watch Me Improve — Algorithm Aversion and Demonstrating the Ability to Learn"
authors: Benedikt Berger, Martin Adam, Alexander Rühr, Alexander Benlian
venue: Business & Information Systems Engineering
year: 2021
volume: 63(1)
pages: 55–68
doi: 10.1007/s12599-020-00678-5
bibtex_handle: berger_watch_2021
pdf: ../berger_watch_2021.pdf
relevance_to_manuscript: medium — algorithm aversion + learning; cited in lit.tex ¶19
---

# Berger, Adam, Rühr & Benlian (2021) — *Watch Me Improve*

## Research question

Can **demonstrating an algorithm's ability to learn** reduce algorithm aversion? The motivation: prior work (Dietvorst 2015) shows that subjects lose confidence in algorithms after seeing them err. If subjects can see the algorithm *improve* over time, perhaps this dynamic-improvement evidence overcomes the static aversion.

Sub-questions:
- Do people exhibit general algorithm aversion, or only after observing errors?
- Does familiarity with the algorithm matter?
- Does the ability to learn offset familiarity-based aversion?

## Methods

- **Incentive-compatible online experiment**.
- Subjects make a non-personal, objective decision (forecasting).
- **3-factor between-subject design**:
  - Advisor: human vs algorithmic
  - Familiarity: unfamiliar vs familiar (subjects have prior experience)
  - Ability to learn: non-learning vs learning algorithm
- Subjects observe the advisor err, then decide whether to follow the advisor's judgment.

## Key results

- **No difference in reliance on *unfamiliar* human vs algorithmic advisors that err.** When subjects don't yet know the advisor, the human/algorithm distinction doesn't matter.
- **Differences appear for *familiar* advisors**: subjects rely less on familiar algorithmic advisors than on familiar human ones. This is the canonical Dietvorst-style aversion.
- **Demonstrating ability to learn offsets the familiarity effect**: when subjects see the algorithm improve, the aversion attenuates.

## Main takeaways

1. **Algorithm aversion is partly about post-observation confidence loss** — consistent with Dietvorst 2015.
2. **Demonstrating learning** (showing the algorithm getting better) is a design intervention that reduces aversion.
3. **The ability to learn is a key design feature** for AI deployment in decision-support contexts.
4. **Familiarity per se increases aversion** — counterintuitively, the more you know the algorithm, the less you trust it after errors.

## Relation to "Algorithms and Responsibility" (this manuscript)

Berger et al. is cited in [literature.tex](../../../manuscript/literature.tex) paragraph 19.

**Why this paper matters for the manuscript:**

**(1) The "familiarity" finding is relevant to the manuscript's design.** The manuscript's algorithm is *fully transparent and calibrated to A's accuracy* — subjects know exactly what to expect. Berger et al.'s finding that familiarity increases aversion suggests that the manuscript's calibration could *increase* aversion among certain subjects. The ~50% delegation rate doesn't appear to bear this out, but heterogeneity by perceived familiarity could be a robustness check.

**(2) The manuscript's algorithm doesn't "learn."** Berger et al.'s design intervention (showing learning) isn't available in the manuscript's static Bernoulli setup. The manuscript captures a snapshot rather than a dynamic; Berger et al.'s mechanism can't bite.

**(3) Methodological context.** Berger et al. is part of the broader push to identify *design levers* to overcome algorithm aversion (alongside Dietvorst 2018 on modifiability, Castelo 2019 on subjective vs objective framing). The manuscript's contribution is on a different axis (responsibility/accountability), but is part of the same field.

**Where in literature.tex:**

- Paragraph 19 cites correctly.

**Worth borrowing:** The Berger et al. result reinforces that *static* algorithm characteristics (transparency, error rates) are not the only determinant of aversion. *Dynamic* features (ability to learn) and *contextual* features (familiarity) also matter. The manuscript's focus on the *accountability context* is a complementary dimension.
