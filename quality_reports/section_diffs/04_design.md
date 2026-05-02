# `design.tex` — old vs new

## Overview

The old `design.tex` is **mostly intact prose** (104 lines) covering the
overview figure, sample, procedure for Player A, procedure for Player B, and
two preregistered hypotheses. It includes several `\textcolor{red}` notes
(missing references, ad-hoc citations to Logg et al. 2019), a `\todo` block
on whether H1 covers delegation only or also punishment, and a long
end-of-file block of bracketed planning notes.

The new `design.tex` is a polished version of the same content (78 lines)
with several substantive additions:

- Explicit "we label the two between-subject conditions Punishment and No-Punishment" naming convention.
- The Bernoulli calibration of the algorithm **promoted from a footnote into a full main-text paragraph** with explicit framing as the central design innovation.
- MPL citation filled in (`\citet{holt_risk_2002}`).
- Prolific quality screens specified explicitly (95% prior approval rate, no warnings, fluent-English filter).
- An explicit pointer to the new appendix CONSORT diagram.
- An explicit pointer to the appendix preregistration / deviations table.
- Earnings figures filled in ($\pounds 2.49$ Player A bonus, $\pounds 2.30$ Player B bonus, with a footnote spelling out the methodology).
- The Figure 1 condition labels disambiguated (Punishment cond.: punishment possible / No-Punishment cond.: no punishment).

## What changed in the prose

- **Condition naming**: `Baseline (punishment)` / `Treatment (no punishment)` → `\textit{Punishment}` / `\textit{No-Punishment}`. Renamed throughout the section and propagated to results, conclusion, appendix.
- **Algorithm-calibration paragraph**: was a single footnote in the old draft ("Concretely, the algorithm draws a Bernoulli outcome..."), now a 4-sentence main-text paragraph explicitly framing this as the design's central innovation relative to Feier et al.
- **Prolific eligibility**: was "EXCLUSION CRITERIA" placeholder in the old (in `results.tex` line 3, not `design.tex`); now an explicit list of standard Prolific quality screens.
- **Sample-size paragraph**: now references an "underlying ex-ante power calculation reproduced in Appendix~\ref{appendix:pap}" and a CONSORT-style flow diagram in the appendix; the old draft just stated "Due to attrition and subsequent re-matching" without elaboration.

## Dropped items

### Notes attached to the algorithm-calibration discussion

- **`\textcolor{red}{[evidence]}` placeholders** at three points: after "depend on the algorithm's perceived relative competence", after "can reinforce the belief that the algorithm can err", and "BMI from such images [evidence]". The new prose simply removes these as planned literature ties that were cut down. **Worth verifying**: the BMI / facial-image accuracy claim was supported by Logg et al. 2019 in the old text but is now phrased more cautiously without the BMI-prediction-accuracy point.
- **`\textcolor{red}{[even though it is about the performance in the first 10 tasks...subjects could now say...ok I put much more effort now, so I will outperform the algorithm, or they could say that they put little effort and delegate. maybe this motive of trying harder is more at play when punishment is possible, so that with punishment, they delegate less? This would be in line with results.]}`** — **A pre-data note that anticipated exactly the M2 effort mechanism** the manuscript ends up exploring in §sec:mechanism. The new draft addresses this in the results, but the note documenting that the author had this hypothesis pre-data (or at least early) is gone. Could matter for transparency.
- The bracketed prediction reference: **"recent findings show that modern machine learning models achieve comparable accuracy to humans when predicting BMI from such images"** — the substantive claim that models can match humans on facial-feature → body-weight prediction, with `[evidence]` placeholder. **Cut entirely from the new text.** The author may want to bring this back if a referee asks how plausible the equal-performance framing is.
- The aside: **"to enhance the clarity and intuitiveness of the task for participants, we chose to use weight rather than BMI as the prediction target"** — a small design-choice justification. Currently absent from the new design section.
- The Highhouse 2008 / Longoni et al. 2019 quote in brackets: **"Others argue that decision makers perceive algorithms as unable to account for unique and individual circumstances"** — a parenthetical citation to the algorithm-aversion literature on perceived inflexibility. **Not in the new draft.**

### Explicit hypothesis question

- **`\todo[inline]{Only the delegation behavior, or also the punishment?}`** — the author was unsure whether H1 should cover delegation only or also punishment. The new manuscript settles this: H1 is delegation only, H2 is punishment.
- **`[were they asked whether they would have chosen sth else if they could be punished?]`** — bracketed self-question about whether the No-Punishment subjects were asked a hypothetical "would you delegate if you could be punished?" question. Looking at the cleaned data, there IS a `delegation_hypo` column for the No-Punishment subjects, so the answer is **yes**. The new manuscript does not currently exploit this column anywhere. **Worth bringing in** as additional evidence for H1 — the conclusion of the old draft mentions this hypothetical decision is "in line with the treatment effect they delegated less".

### One additional hypothesis sketch

- **The bracketed quote in the H2 motivation**: "Given that the discourse on algorithm aversion suggests that delegating to an algorithm reduces perceived process ownership (Önkal and Gönül, 2005; Petropoulos et al., 2016), and given that the discourse on blame avoidance suggests reduced ownership is a behavioral strategy to cope with mental burdens in challenging choice situations" — explicit citations to the **process-ownership literature** that the new manuscript invokes by name in §results but doesn't ground in literature. Önkal & Gönül 2005 and Petropoulos et al. 2016 are **not currently cited**. Bringing them into the literature section would strengthen the M3 mechanism story.

### End-of-file planning notes (lines 76–86)

A long bracketed list:

- `[we will test three things: how is actually punished? is how will be punished anticipated? does this difference translate into the delegation decision]` — three-things framing. The new manuscript does test all three but doesn't preview them as a "three things" list.
- `[what sets this design apart, how will we answer research questions]` — the new design section addresses this in the §Identification subsection.
- `[more hypothesis on amount of delegation? on punishment for good outcomes? on performance related to delegation behavior?]` — the author was considering more preregistered hypotheses. **Currently the manuscript has only H1 and H2.** Worth noting that the performance-related-to-delegation analysis (the heterogeneity that drives the M3 story) is **not preregistered**.
- `[depending on how we present results, include where we include an attention check]` — done implicitly in the new prose.
- `[check tense]` — author note.
- `[blame avoidance vs responsibility avoidance]` — terminology choice. The new manuscript settles on "responsibility avoidance" / "responsibility shifting" but uses both terms.
- `[why punishment a good measure, often employed before, bartling fischbacher and feier et al (even though also reward possible) and public goods experiments] Justification why no reward.` — **A planned methodological defence of using punishment rather than reward** (which Feier et al. emphasise). Currently absent from the new design.
- `[While the decision itself is not moral, the setup qualifies as part of the moral domain according to the definition applied in the literature: We argue that this makes our experiment relevant for ethical deliberations. Because we have no reason to believe that a rational participant would prefer less money to more, the decision could do actual, albeit monetary, harm to another person.]` — **a justification for why this counts as a "moral domain" experiment**. Currently absent from the new design. Worth bringing in if a referee questions whether the weight-prediction setup is genuinely moral.
- `[how will we assess the hypothesis --> next section; maybe incorporate into design figure (similar to the slide deck?)?]` — placeholder for an Identification subsection. The new design does have a §Identification subsection.

## Why the changes (where I can infer)

- The Bernoulli-calibration promotion came directly from both peer-review referees flagging it as the design's strongest selling point.
- The MPL citation, Prolific specs, condition rename, and CONSORT/PAP appendix pointers came from the methods referee's feedback.
- The bonus-earnings filling came from the standalone payoff computation script.
- The dropped `[evidence]` placeholders are simply omissions of references that were never filled; **worth a pass to confirm whether any of these claims need a supporting citation that's currently missing**.
