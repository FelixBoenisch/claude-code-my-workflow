# `conclusion.tex` — old vs new

## Overview

The old `conclusion.tex` is **28 lines, mostly bullet-point notes**, no
proper Discussion/Conclusion structure: a paragraph fragment on "two channels
through which a lower propensity to delegate when punishment is possible can
be rationalized", a 4-bullet results recap, and 7 lines of bracketed
TODO/discussion notes ("Discuss why there are no delegation costs", "all
performance perceptions are done given the information that they perform
equally well", etc.).

The new `conclusion.tex` is **a full Discussion + Conclusion section**
(21 long-line paragraphs) covering: brief paper recap, two findings (with
hedges), mechanism (with M3 candidate framing + experimenter-demand caveat),
relation to the responsibility-avoidance literature, **a new "Implications,
with explicit bounds" subsection** (EU AI Act framing + explicit
external-validity bounds), Limitations (including new manipulation-comprehension
caveat and modest-stakes caveat), Demand-effect discussion, and Future research
directions.

## What changed in the prose

Almost entirely a fresh draft. The old conclusion was a planning note for a
section that hadn't been written yet; the new conclusion is a complete
Discussion section.

The most substantive *new* content vs the old draft:

- **A bounded "Implications" subsection** — frames the EU AI Act regulatory connection but is explicit about the bounds: "Our evidence is a single online experiment with 322 UK Prolific participants on a stylised weight-prediction task... we view the result as identifying a behavioural channel that exists in principle and is detectable in our setting, not as a calibration of how big a lever accountability is in any specific applied domain". This came directly from the domain referee's external-validity critique.
- **The mechanism paragraph** explicitly treats process ownership as a candidate hypothesis supported by exploratory evidence, not a confirmed mechanism.
- **The demand-effect paragraph** is more measured ("two patterns weakly inconsistent with a strong demand reading") and points to de Quidt et al. (2018) as the right direct test.
- **The future-research paragraph** is much more concrete: stake-magnitude robustness, demand probe, professional-population replication, direct-method companion, larger-sample tightening of the H2 CI, the visibility-to-Player-B treatment for the relative-performance signal.

## Dropped items

### Items from the old draft

- **The fragmentary opening sentence**: "We explore two particular channels through which a lower propensity to delegate when punishment is possible can be rationalized. Neither do we find evidence for an increase in effort in the face of possible punishment, nor do elicited beliefs about the punishment pattern of Player B suggest that Player A anticipates stronger punishment when delegating, for example due to them shirking effort or the moral nature of the decision. However, [critique belief measure, small sample size,...]"

  The "two channels" structure (effort and anticipated punishment) survives in §sec:mechanism (M2 and M1 respectively). The "shirking effort or the moral nature of the decision" framing is partly preserved (the M2 paragraph mentions effort) but the **explicit "moral nature of the decision" interpretation is dropped**. Worth considering bringing back.

- **The 4-bullet result recap** was:
  1. No differential punishment for a delegated and non-delegated decision, if anything tendency towards less blame when delegating
  2. Beliefs in line with actual punishment
  3. Within-subject, delegation consistent with punishment beliefs
  4. **Strong treatment effect of potential punishment, which is also supported by another hypothetical decision delegators that can't be punished had to make. After making their delegation decision I aksed them what they would do if they could be punished and in line with the treatment effect they delegated less.**

  Item 4's second sentence is a **specific finding from the `delegation_hypo` column**: No-Punishment subjects, when asked the hypothetical "would you have delegated if you could be punished?", responded **less delegation** — corroborating H1 with a within-subject hypothetical comparison. **This is currently absent from the new manuscript** and is a meaningful piece of evidence for H1. **Strongly worth bringing back.**

### Bracketed planning notes

- **"Potential additional treatments?"** — open-ended question. Some are now in the Future Research paragraph (visibility, performance variation).
- **"maybe include critique of experimenter demand, so perhaps dont use strategy method but then need much more observations unless only focus on bad. ALSO: not clear in which direction the experimenter demand goes?"** — a methodological note about strategy method vs direct method as part of the demand discussion. Captured in the new manuscript (the "direct-method companion" item in Future Research).
- **"Discuss why there are no delegation costs. With costs of delegation there would have clearly been a rational choice (no delegation) in the treatment without punishment. But then if the outcome is actually that you are punished more if you delegate, then there is no treatment effect to be expected. So fine to not do it I believe."** — a **defence of the no-delegation-cost design choice**. Currently absent from the new conclusion. Useful if a referee asks about choice architecture.
- **"all performance perceptions are done given the information that they perform equally well, which is obviously a signal. This could have been prevented by telling them the causality that the algorithm was made to perform as well as they did. This also means that the better they think they were, the better they think the algorithm is, or after being told that the algorithm is as good as them they conclude that they update beliefs according to how good they think the algorithm is."** — **a substantive point about how the equal-performance information acts as a signal for performance beliefs**. Currently absent from the new manuscript. This is interesting because it has implications for the §sec:beliefs interpretation: subjects who think they're good will think the algorithm is good (equally), and conversely. Worth bringing back, possibly in §sec:beliefs or in Limitations.
- **"Why not punishment between subjects? Answer: because it would have needed many more subjects, even if I fine tuned the difficulty of the task."** — design-choice rationale for why punishment is within-subject (strategy method) rather than between-subject. Currently absent. Useful if a referee asks why the strategy method.
- **"Always italize and capitalize Baseline and Treatment."** — typesetting note. Now moot (renamed to Punishment / No-Punishment).
- **"[in the discussion in the end: either one treatment where the delegator is explicitly told that the evaluator will not be aware of the equal performance (but this is maybe more a robustness exercise); maybe a treatment where they are being told that algo performed beeter/worse in the first 10 tasks and partner is/is not aware.]"** — **two specific follow-up treatment ideas** that survive in the new Future Research paragraph in compressed form ("A condition in which Player A is told explicitly that Player B is unaware of the equal-performance calibration"; "Conditions that experimentally vary the algorithm's performance relative to Player A").

## Why the changes (where I can infer)

- The conclusion is essentially a new section. The old draft had not been written; what was there was planning notes.
- The structure (recap → mechanism → implications → limitations → demand → future) reflects the peer-review feedback: domain referee wanted bounded policy claims; methods referee wanted hedged mechanism + explicit MDE / power language; both wanted a serious demand-effect discussion.
- The de Quidt et al. (2018) reference for direct-test demand-effects is new (added to the bib in this session).

## High-leverage items to bring back

1. **The `delegation_hypo` finding** (No-Punishment hypothetical "would you delegate if punishment possible" → less delegation, corroborating H1 within-subject). This is the highest-leverage item — direct corroborating evidence for the headline result that's currently absent.
2. **The signal-from-equal-performance-information observation** (subjects who think they're good think the algorithm is good, etc.) — could go in §sec:beliefs or Limitations.
3. **The "no delegation costs" design defence** — proactive answer to a likely referee question.
4. **The "between-subject punishment would need many more subjects" defence** — also a likely referee question.
