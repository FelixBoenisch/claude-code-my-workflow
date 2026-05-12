---
title: "Algorithm Aversion: People Erroneously Avoid Algorithms After Seeing Them Err"
authors: Berkeley J. Dietvorst, Joseph P. Simmons, Cade Massey
venue: Journal of Experimental Psychology — General
year: 2015
volume: 144(1)
pages: 114–126
doi: 10.1037/xge0000033
bibtex_handle: dietvorst_algorithm_2015
pdf: ../dietvorst_algorithm_2015.pdf
relevance_to_manuscript: medium-high — coined "algorithm aversion"; cited in lit.tex ¶19 + design.tex ¶39
---

# Dietvorst, Simmons & Massey (2015) — *Algorithm Aversion: People Erroneously Avoid Algorithms After Seeing Them Err*

## Research question

Why do people prefer human forecasters over algorithmic ones, even when algorithms outperform? The paper coined the term "algorithm aversion" and tests one specific mechanism: **people lose confidence in algorithms more quickly than in humans after seeing equivalent errors**.

## Methods

Five studies, all forecasting tasks (MBA students' performance, MS Excel scores, etc.). Subjects can choose to tie their incentives to either their own forecast or the algorithm's forecast. Conditions vary whether subjects observed:
- Neither forecaster (control)
- Only the human
- Only the algorithm
- Both

Algorithm is described as built from historical data; human is themselves or another participant.

## Key results

- **Subjects who saw the algorithm perform are less likely to use it**, even when they saw it outperform the human alternative.
- People lose confidence in algorithms faster than in humans after seeing the same errors.
- Algorithm aversion is robust and costly: subjects choosing the worse forecaster make less money.

## Main takeaways

1. **Algorithm aversion is documented empirically** in forecasting tasks with monetary stakes.
2. **The mechanism is confidence asymmetry** — algorithm performance is "innocent until proven guilty" in the opposite direction from humans.
3. **The effect is robust** to seeing the algorithm outperform humans.

## Relation to "Algorithms and Responsibility" (this manuscript)

Dietvorst, Simmons & Massey (2015) is the seminal algorithm-aversion paper, cited in [literature.tex](../../../manuscript/literature.tex) paragraph 19 and used in [design.tex](../../../manuscript/design.tex) paragraph 39: "Algorithm preferences depend sensitively on the algorithm's perceived relative competence (Dietvorst 2015; Logg 2019)."

**Note on the design.tex citation**: Felix flagged this with `FB CHECK` — "Dietvorst 2015 is largely about confidence loss after observing errors rather than about ex-ante perceived competence." Reading the paper, this concern is correct. Dietvorst 2015 is about *dynamic* changes in confidence after observing performance, not about *ex-ante* perceived competence. The current claim in design.tex is therefore slightly off-mark. Suggested revision: "as motivated by work on confidence loss after observing algorithmic errors (Dietvorst 2015) and on perceived algorithmic ability (Logg 2019)." This separates the two papers' actual claims.

**Why this paper matters for the manuscript:**

**(1) Foundational anchor for the algorithm-aversion subsection.** Any literature review on algorithm preferences must engage with Dietvorst 2015. The manuscript correctly does so.

**(2) The manuscript's design closes off Dietvorst's mechanism by construction.** The manuscript provides equal-performance information *before* Player A decides whether to delegate — there's no observation of algorithm error to lose confidence over. So the Dietvorst mechanism shouldn't bite. Whatever depresses delegation in the manuscript is not the Dietvorst confidence-loss channel.

**(3) The 50% delegation rates in the manuscript are *informative against the Dietvorst pattern*.** Dietvorst found strong aversion (substantially below 50%); the manuscript finds rates near 50%. This may be because (a) the calibration removes the confidence-loss channel, (b) the visual prediction task is less subject to Dietvorst's effect than numerical forecasting, or (c) the moral-domain framing introduces other forces.

**Where in literature.tex:**

- Paragraph 19 cites correctly as foundational.
- Design.tex paragraph 39 needs the citation framing softened (see note above).
