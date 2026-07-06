---
title: "Comparison: discussion-subsection draft (v2) vs. current results.tex"
date: "2026-07-02"
scope: "Each unit of the draft in 07_discussion_subsection_DRAFT.md, paired with the passage in manuscript/results.tex that currently makes the same point"
status: "Reference document for review — no manuscript files edited"
---

How to read this file: units follow the **order of the draft**. For each unit, **DRAFT** gives the v2 text (verbatim, except that the `% [...]` flags are stripped for readability — they remain in `07_discussion_subsection_DRAFT.md`), and **CURRENT** quotes the corresponding passage(s) from `results.tex` verbatim, with line numbers, including your inline `[Comment: ...]` markers. *Mapping* notes (one or two lines) state what moved or changed. Units with no counterpart are marked **CURRENT: none**. A final section lists current passages that have no place in the draft.

---

## 1 — Opening paragraph

**DRAFT:**
```latex
Result~1 does not merely fail to support \textit{Hypothesis~1}: the effect is
statistically significant in the opposite direction. The possibility of punishment
discourages, rather than encourages, delegation to the algorithm. Read together with
Result~2, this is puzzling. The prospect of punishment changes Player~A's delegation
decision, even though the punishment Player~B actually imposes attaches to outcomes,
not to delegation---conditional on the outcome, we detect no penalty for delegating. In
this subsection, we first ask why the responsibility-shifting motive underlying
\textit{Hypothesis~1} may have had little force in our setting; we then turn to
explanations that could actively reverse its prediction.
```

**CURRENT (results.tex:63):**
> We not only fail to support \textit{Hypothesis~1}, but the observed effect points in the opposite direction, suggesting that the possibility of punishment discourages delegation to the algorithm. In this section we explore various candidate mechanisms that... [Comment: complete, once the mechanism paragraphs are worked out.].

**CURRENT, related (results.tex:57, end of the Player B subsection):**
> This result also bears on \textit{Result 1} as any treatment difference in delegation frequencies driven by punishment avoidance would be inconsistent with Player~B's observed punishment behavior.

*Mapping:* completes the unfinished opening; the joint R1–R2 puzzle is new as an explicit frame and absorbs the point currently made at line 57 — once the draft is pasted, that sentence may be trimmed or turned into a forward pointer to avoid duplication.

---

## 2 — Departures, paragraph 1 (canonical-settings contrast)

**DRAFT:**
```latex
\paragraph{Departures from canonical settings.} \textit{Hypothesis~1} was grounded in
evidence from settings that differ from ours in ways that plausibly matter. In the
modified dictator games of \citet{bartling_shifting_2012, coffman_intermediation_2011,
hamman_self-interest_2010, oexl_shifting_2013}, the decision-maker chooses between a
fair and an unfair allocation: her intent is transparent, the chosen allocation is
implemented with certainty, and the unfair option benefits her directly. Punishment in
these settings sanctions a deliberate, self-serving act, and delegation is attractive
precisely because it blurs the link between the principal and that act. Our prediction
task removes these ingredients. The outcome is uncertain, so a bad outcome may reflect
bad luck rather than bad intent; and neither option affects Player~A's own monetary
payoff, so the incentives of the two players are aligned and there is no self-serving
choice to police.\footnote{We consider the incentives aligned even though Player~A's
payoff is only indirectly affected by her decision, insofar as a better outcome for
Player~B weakly reduces Player~A's expected punishment in the \textit{Punishment}
condition.} With little intent worth sanctioning, the intention-based punishment motive
loses its bite---and with it, the value to Player~A of placing an intermediary between
herself and the outcome. We accepted this trade-off deliberately: prediction under
genuine uncertainty, by a decision-maker with no material stake in the affected party's
outcome, is the environment in which real-world algorithmic delegation typically
operates (Section~\ref{design}).
```

**CURRENT (results.tex:65):**
> \paragraph{Departures from prior settings.} Our hypothesis was grounded in previous empirical evidence, though these studies were conducted in settings that differ from ours in various important ways. Most notably, our task departs fundamentally from the modified dictator games used in \cite{bartling_shifting_2012, coffman_intermediation_2011, hamman_self-interest_2010, oexl_shifting_2013}. In such games, the decision intent is more transparent as participants make either fair or unfair allocations that are directly payoff-relevant to themselves and implemented with certainty. In contrast, our prediction task involves uncertainty (subjects may err even though they put in substantial effort) and the incentives of Player A and Player B are aligned.\footnote{We consider the incentives of Player A and B to be aligned, even though Player A's payoff is only indirectly affected by her own decision, insofar as a better outcome for Player B reduces expected punishment.} These aspects may obfuscate the intent of Player A, possibly diluting an intention-based punishment motive for Player B, and thus the need to avoid punishment by Player A. Nevertheless, we chose a prediction task because prediction under uncertainty is precisely the domain where algorithmic decision-making is most prevalent.

*Mapping:* same content; the dictator-game triple (transparent intent / certainty / self-serving) and its removal are made strictly parallel, and the causal chain (intent obscured → punishment motive loses bite → intermediary loses value) is one sentence.

---

## 3 — Departures, paragraph 2 (null vs. reversal) + moral-cover footnote

**DRAFT:**
```latex
This reasoning, however, explains at most a null result: if shifting responsibility
onto the algorithm is worth little here, delegation should simply differ little across
conditions. It cannot explain why punishment pushes delegation \textit{down}. Some
force must actively discourage delegation when punishment is
possible.\footnote{Recent evidence that algorithmic delegates can serve as moral cover
\citep[e.g.,][]{tontrup_strategic_2025, hueholt_trusting_2026} sharpens the puzzle; we
return to it at the end of this section.}
```

**CURRENT (results.tex:69, with your comments at 67 and 71):**
> [FB comment: What about the more recent literature on Responsibility Avoidance through delegation to algorithms?]
>
> While this story is consistent with the obsrvation of a lack of a difference in punishment between delegated and self-made decisions, it can not explain the reversal. Moreover, it would be reflected in punishment beliefs, which we discuss next.
>
> [FB comment: Given how noisy of a measure these beliefs are, I am not sure if we need beliefs to align with this story in order to believe it. Maybe take some weight away.]

*Mapping:* the null-vs-reversal point is kept and sharpened into the section's pivot; the reliance on beliefs ("would be reflected in punishment beliefs") is dropped per your line-71 comment; the footnote answers your line-67 comment by pointing forward to the two-channel paragraph.

---

## 4 — Anticipated differential punishment (channel statement + variants)

**DRAFT:**
```latex
\paragraph{Anticipated differential punishment.} The most natural candidate is
anticipation: Player~A may expect a delegated decision to be punished more harshly than
a self-made one, and delegate less in response. Such an expectation would be consistent
with evidence that observers view the delegation of morally consequential decisions to
machines critically \citep[e.g.,][]{gogoll_rage_2018, bigman_people_2018,
jauernig_people_2022, bonnefon_moral_2024}. The same logic admits two variants.
Player~A may expect to be punished for \textit{shirking}: delegation visibly outsources
the effort of deciding on Player~B's behalf, and Player~B may sanction the outsourcing
itself. Or Player~A may believe that Player~B simply prefers a human---rather than a
machine---to determine his payoff, a procedural preference that the punishment option
makes enforceable. All three variants carry the same testable implication: Player~A
must expect a punishment penalty attached to delegation \textit{as such}, conditional
on the outcome.
```

**CURRENT (results.tex:73):**
> \paragraph{Anticipated differential punishment.} A natural reading of Result~1 is that Player~A anticipates stronger punishment for a decision delegated to the algorithm than for a self-made decision and delegates less in response. This belief pattern would be consistent with parts of prior work suggesting that observers view delegating moral decisions to algorithms relatively critically \citep[e.g.,][]{gogoll_rage_2018, bigman_people_2018, jauernig_people_2022, bonnefon_moral_2024}. Alternatively, the same belief pattern would be consistent with a simple shirking motive, in which Player~A expects greater punishment for shirking the effort to make a decision for Player~B but, in the absence of punishment, can shirk without monetary consequences. We have already seen that Player B punishment is outcome-based, rather than delegation-based, yet a shirking motive --- which would predict additional punishment for delegation --- could at least rationalize the positive punishment observed in the good outcome--delegated scenario. In either case, delegation behavior should be consistent with observed beliefs about punishment.

*Mapping:* the procedural-preference variant is new (D5); the "could at least rationalize the positive punishment in the good-outcome–delegated scenario" aside is dropped (see Leftovers, item 3); the closing sentence is upgraded into the explicit testable implication.

---

## 5 — Identification paragraph (why only the asymmetry can matter)

**DRAFT:**
```latex
This implication gives the belief data a precise role. The algorithm reproduces
Player~A's own success probability, and both players know it, so the outcome lottery
faced by Player~B is the same whether or not Player~A delegates. Punishment that
responds only to the outcome therefore burdens both options equally and cannot tilt the
choice between them. What can tilt the choice is an asymmetry: expected punishment
attached to the delegation decision itself, conditional on the outcome. This is the
quantity the elicited beliefs measure.\footnote{The equivalence of the two options
presumes that Player~A does not expect to beat her own record through extra effort on
the final prediction; we take up this possibility below.}
```

**CURRENT: none.** (The germ is the last sentence of results.tex:73, quoted in unit 4: "In either case, delegation behavior should be consistent with observed beliefs about punishment.")

*Mapping:* new. It also does the work that "the overestimation cannot explain Result 1" needs later, and its footnote pre-announces the effort candidate.

---

## 6 — Punishment beliefs: elicitation sentence

**DRAFT:**
```latex
\paragraph{Punishment beliefs.} \label{sec:beliefs} After the delegation decision but
before learning the outcome, we elicited Player~A's beliefs about Player~B's punishment
in each of the four \textit{(delegation, outcome)} scenarios.
```

**CURRENT (results.tex:75):**
> \paragraph{Punishment beliefs.} \label{sec:beliefs} After making the delegation decision but before learning the outcome, we elicited Player~A's beliefs about Player~B's punishment in each of the four scenarios.

*Mapping:* unchanged apart from the scenario notation.

---

## 7 — Caveats paragraph

**DRAFT:**
```latex
We interpret the belief measure with caution for several reasons. The elicitation was
unincentivised and took place after the delegation decision, so reports may reflect
hedging across scenarios or post-hoc rationalization rather than the beliefs that
actually drove the choice. As a corollary, any within-subject correlation between
beliefs and delegation cannot identify direction: we cannot distinguish whether
subjects delegated \textit{because} they held these beliefs about punishment, or hold
these beliefs \textit{because} they delegated. Hypotheticality compounds the noise:
only two of the four scenarios remained payoff-relevant after the delegation decision
in the \textit{Punishment} condition, and all four were purely hypothetical in the
\textit{No-Punishment} condition. We therefore restrict the belief--delegation analysis
to the \textit{Punishment} condition. The motivation is structural rather than
statistical: the punishment-anticipation channel can only operate where punishment is
possible, so beliefs about a counterfactual that cannot materialise do not enter
Player~A's decision rule in the \textit{No-Punishment} arm. The exercise that follows
should accordingly be read as suggestive evidence on whether the channel is alive among
those exposed to it, not as a mediation analysis of the treatment-level delegation gap
(Result~1).
```

**CURRENT (results.tex:77):**
> However, we interpret the belief measure with caution for several reasons. The elicitation was unincentivised and took place after the delegation decision, so reports may reflect hedging across scenarios or post-hoc rationalization rather than the beliefs that actually drove the choice. As a corollary, any within-subject correlation between beliefs and delegation cannot identify direction: we cannot distinguish whether subjects delegated \textit{because} they held these specific beliefs about punishment, or hold these beliefs \textit{because} they delegated. Hypotheticality compounds the noise: only two of the four \textit{(delegation, outcome)} scenarios remained payoff-relevant after the delegation decision in the \textit{Punishment} condition, and all four were purely hypothetical in the \textit{No-Punishment} condition. We therefore restrict the belief--delegation analysis to the \textit{Punishment} condition. The motivation is structural rather than statistical: the punishment-anticipation channel can only operate where punishment is possible, so beliefs about a counterfactual that cannot materialise do not enter Player~A's decision rule in the \textit{No-Punishment} arm. The exercise that follows should accordingly be read as suggestive evidence on whether the channel is alive among those exposed to it, not as a mediation analysis of the treatment-level delegation gap (Result~1).
>
> [FB comment: Given how noisy of a measure these beliefs are, I am not sure if we need beliefs to align with this story in order to believe it. Maybe take some weight away.]

*Mapping:* kept essentially verbatim (settled in the May pass); only micro-trims ("these specific beliefs" → "these beliefs"; scenario notation moved to unit 6).

---

## 8 — Two patterns (levels; absent asymmetry; blue bars)

**DRAFT:**
```latex
Two patterns emerge (Figure~\ref{fig:realized_vs_anticipated}). First, Player~As
substantially \textit{overestimate} punishment: average anticipated punishment exceeds
average realized punishment in every scenario. By the argument above, however, an error
that concerns both options alike cannot tilt the choice between them; what matters is
the asymmetry. Second, the asymmetry is absent: Player~As expect essentially the same
punishment for delegated and self-made decisions, conditional on the outcome, correctly
anticipating the pattern in Player~B's actual behavior (Result~2).\footnote{The
expected punishment penalty for delegation is small and statistically indistinguishable
from zero in both outcome states, and a within-subject test finds no asymmetry between
the two ($p=0.376$ among passers); see Appendix~\ref{appendix:beliefs_vs_performance}.}
The same holds across conditions: hypothetical beliefs elicited in the
\textit{No-Punishment} condition closely track those in the \textit{Punishment}
condition (Figure~\ref{fig:realized_vs_anticipated}, blue bars). The manipulation
appears to have changed whether punishment could materialise, not what subjects
expected it to look like; a cross-condition difference in beliefs about the punishment
schedule is therefore unlikely to drive the delegation gap.
```

**CURRENT (results.tex:79):**
> Two patterns emerge. First, Player~As substantially \textit{overestimate} the level of punishment they will face: average expected punishment exceeds average realized punishment in every scenario (Figure~\ref{fig:realized_vs_anticipated}, green vs.\ magenta bars). The same pattern is visible in the \textit{No-Punishment} condition, where Player~A's hypothetical beliefs (blue bars) closely track the Punishment-condition beliefs. Second, however, Player~As correctly anticipate the \textit{relative} pattern of punishment in that they expect no significant difference in punishment between delegated and non-delegated decisions, conditional on outcome---a pattern that closely tracks the actual punishment behavior of Player~B documented in Result~2. \textit{It is this relative-pattern finding---on punishment beliefs alone---that provide no support for a punishment anticipation mechanism for Result~1.} If Player~A had reduced delegation in the \textit{Punishment} condition because she anticipated being punished more harshly for delegation than for self-made decisions, we would expect to see this asymmetry in the elicited beliefs. We do not. [Comment: Let's consider to just leave out te hypotheical punishment beliefs. We do not do anything with them.]

*Mapping:* same two patterns; the levels point now cites the unit-5 argument instead of standing alone; the blue-bar sentence is moved after the asymmetry point and given the repurposed role (D2 — this answers your inline comment by giving the hypothetical beliefs a job); the italicized verdict and the "If Player A had reduced delegation... We do not." sequence are absorbed into unit 11.

---

## 9 — Belief regression: description, table, decomposition footnote

**DRAFT:**
```latex
Even so, the beliefs carry within-subject information.
Table~\ref{tab:reg_belief_specs} reports a Logit regression of the delegation decision
on Player~A's belief difference (\textit{no delegation}~$-$~\textit{delegation}) in
expected punishment, restricted throughout to the \textit{Punishment}
condition.\footnote{The two underlying belief measures compare expected punishment of a
self-made and a delegated decision for each of the two possible outcomes for Player~B,
so that higher values correspond to relatively higher expected punishment for self-made
decisions.} Columns~(1)--(3) use the simple average of the two outcome-conditional
belief differences as the single regressor: Column~(1) reports the unconditional
specification on the full \textit{Punishment} sample, Column~(2) adds task-performance
and socio-demographic controls, and Column~(3) restricts the sample to subjects who
passed the attention check on the belief-elicitation screen. Column~(4) replaces the
simple average with a weighted average, using Player~A's elicited probability of
producing the high payoff as the weight---the statistic that enters an expected-utility
calculation. Column~(5) enters the two outcome-conditional differences
separately.\footnote{The two differences are nearly orthogonal in this sample (Pearson
correlation $-0.10$ among passers), so the coefficients in Column~(5) are additive
partial slopes rather than competitors for the same variance. Under expected-utility
reasoning, however, only their probability-weighted sum should enter the decision rule;
we therefore treat the single-regressor specifications as the structural mappings of
the channel and Column~(5) as a descriptive decomposition.}

\input{../tables/reg_belief_specs.tex}
```

**CURRENT (results.tex:92):**
> Even though the belief measure was not incentivized, and even though at the time of the belief elicitation, two of the four scenarios could not materialize anymore, punishment beliefs carry within-subject information. Table~\ref{tab:reg_belief_specs} reports a Logit regression of the delegation decision on Player~A's belief difference (\textit{no delegation}~$-$~\textit{delegation}) in expected punishment, restricted throughout to the \textit{Punishment} condition.\footnote{The two underlying belief measures compare expected punishment of a self-made and delegated decision for each of the two possible outcomes for Player~B, so that higher values correspond to higher expected punishment for non-delegated decisions relative to delegated decisions.} The first three columns use the simple average of the two outcome-conditional belief differences as the single regressor; this maps cleanly onto a punishment-anticipation channel under expected-utility reasoning, in which only the expected punishment penalty for switching from delegation to self-decision matters. Column~(1) reports the unconditional specification on the full \textit{Punishment} sample; Column~(2) adds task performance and socio-demographic controls; Column~(3) restricts to subjects who passed the attention check on the belief-elicitation screen, as preregistered. Column~(4) replaces the simple average with the more theoretically appropriate weighted average, using Player~A's elicited probability of producing the high payoff as the weight ($\Pr(\text{good})=$\textit{wa\_confidence}$/10$). Column~(5) instead enters the two outcome-conditional belief differences separately.

**CURRENT (results.tex:100–101, the decomposition paragraph):**
> \paragraph*{Interpretation of the two-difference decomposition.}
> The five-column table treats the simple- and weighted-average specifications as the primary structural mappings of the channel and the two-difference decomposition (Column~(5)) as a descriptive complement. Two interpretive points are worth flagging. First, the two outcome-conditional differences are nearly orthogonal in this sample (Pearson correlation $-0.10$ in the passers sample), so the two coefficients in Column~(5) are essentially additive partial slopes rather than competing for the same variance. Second, under expected-utility reasoning only the weighted sum of the two differences should enter the decision rule; entering both separately therefore answers the partial question ``conditional on the bad-outcome asymmetry, how does delegation respond to the good-outcome asymmetry?'' rather than the structural question the channel poses. We therefore lead with the simple-average and weighted-average specifications and treat the decomposition as a robustness check that confirms the action sits in the good-outcome cell. [Comment: this whole pararaph should become a footnote.]

*Mapping:* opening clause shortened (its content is already in the caveats paragraph); the decomposition paragraph becomes the Column-(5) footnote, as your comment requests; "as preregistered" and the $\Pr(\text{good})$ implementation detail dropped from the prose (the latter can live in the table note).

---

## 10 — Belief regression: results

**DRAFT:**
```latex
The estimated relationship is weak in the full sample but sharpens among attentive
subjects. In Columns~(1)--(2) the belief coefficient is positive but far from
significant ($p>0.39$): in the unrestricted \textit{Punishment} sample, expected
differential punishment does not predict delegation. Among attention-check passers,
subjects who expect a one-pound larger punishment penalty for deciding themselves are
markedly more likely to delegate (simple average: $2.71$, $p=0.035$; weighted average:
$3.33$, $p=0.030$). In the decomposition, the good-outcome belief difference carries
the relationship ($1.58$, $p=0.033$), while the bad-outcome difference is positive but
noisier ($0.94$, $p=0.21$).
```

**CURRENT (results.tex:98):**
> The pattern is consistent with the punishment-anticipation channel \textit{conditional on attention}, but unconditionally weak. In Columns~(1)--(2), the belief coefficient is positive but small and far from significant ($p>0.39$): in the unrestricted \textit{Punishment} sample, expected differential punishment does not predict delegation. Restricting to attention-check passers (Column~(3)) sharpens the relationship substantially: the simple-average belief coefficient is~$2.71$ ($p=0.035$), implying that subjects who expect a one-pound larger punishment penalty for not delegating are markedly more likely to delegate. The weighted-difference specification (Column~(4)) yields a similar conclusion with a slightly larger coefficient ($3.33$, $p=0.030$), supporting the expected-utility interpretation. In Column~(5), the good-outcome belief difference carries the regression: its coefficient of~$1.58$ ($p=0.033$) is in line with the single-regressor specifications, while the bad-outcome belief difference is positive but statistically noisier ($0.94$, $p=0.21$). If taken at face value this would mean that the delegation decision is primarily made by thinking about punishment consequences after a good outcome, rather than a bad outcome.

*Mapping:* same numbers, compressed; the closing "thinking about punishment consequences after a good outcome" sentence is relocated to Taking stock as the optional D6 sentence (unit 15).

---

## 11 — Belief verdict

**DRAFT:**
```latex
Taken together, the belief evidence leaves the anticipation channel alive at the margin
but rules it out as the source of the reversal. Within the \textit{Punishment}
condition, subjects whose beliefs embody a larger penalty for deciding themselves are
more likely to delegate---the choice responds to belief asymmetries where they exist.
But a margin whose average is zero provides no aggregate push. For anticipation to
generate a $17$~percentage-point delegation gap, Player~As would need to expect
systematically harsher punishment for delegated decisions, and they do not---nor would
such an expectation have been correct, since Player~B's realized punishment exhibits no
delegation penalty either (Result~2), with a point estimate that, if anything, runs the
other way. Anticipated differential punishment is a dimension along which subjects
differ, not a force that could reverse the average delegation decision.
```

**CURRENT (results.tex:118):**
> Taken together, the belief evidence is mixed: within the Punishment sample, individual heterogeneity in belief differences does predict delegation in the direction M1 predicts (Table~\ref{tab:reg_belief_specs}, Cols.\ 3--4), but this within-condition signal is not conclusive for the treatment-level gap (Result~1). Moreover, Player~B does not deliver the asymmetric punishment that would justify the belief asymmetry on which the channel rests (Result~2). Anticipated differential punishment as the driver of Result~1 is therefore only partly consistent with elicited beliefs and inconsistent with realized punishment.

*Mapping:* same verdict, with the reasoning made explicit (why a zero-mean margin cannot produce the 17-point gap); also absorbs "If Player~A had reduced delegation... We do not." from results.tex:79 (unit 8); the M1 label is dropped (D7).

---

## 12 — Effort: channel statement and prediction

**DRAFT:**
```latex
\paragraph{Effort to outperform the algorithm.} A second candidate turns on effort.
The algorithm is calibrated to Player~A's past performance, but her final prediction is
not yet made: a Player~A who believes that she can beat her own ten-round record by
trying especially hard can raise Player~B's chances above the algorithm's---but only by
keeping the decision. The prospect of punishment, which falls as Player~B's outcome
improves, would then push her toward deciding herself. This is precisely the
possibility set aside in the previous section, and it makes a clean prediction:
non-delegators should improve on their ten-round record specifically in the
\textit{Punishment} condition. Improvement in both conditions would instead indicate a
treatment-independent (for instance, altruistic) motive, which cannot explain
Result~1.
```

**CURRENT (results.tex:183 and 185):**
> \paragraph{(M4) Effort exertion to outperform the algorithm.} Although our design controls for relative performance based on the first ten rounds---making the algorithm and Player~A equivalent in expectation on the final prediction---potential punishment may motivate Player A to exert greater effort in making the decision for Player B, thereby choosing not to delegate in hopes of outperforming the algorithm.
>
> If effort, measured by performance, increased in both conditions, effort exertion could be interpreted as altruistic, and would be treatment-independent. However, if effort only increases with punishment, then the motive would be driven by the expectation to decrease the likelihood of punishment, which could explain Result~1.

*Mapping:* same channel; the prediction is stated before the test and the altruism-conditional is compressed to one sentence; the link back to the unit-5 equivalence footnote is new.

---

## 13 — Effort: evidence

**DRAFT:**
```latex
The data show the opposite. Delegators do not make a final prediction themselves, so
effort on the final prediction is observable exactly for the group the story concerns:
non-delegators. Measuring improvement as the difference between a subject's average
absolute prediction error over the first ten rounds and her absolute error on the final
prediction, non-delegators in the \textit{No-Punishment} condition improve on their
record, whereas non-delegators in the \textit{Punishment} condition do not. Because all
Player~As faced the same image on the final prediction, this differential cannot
reflect task-specific variation. The realized outcomes tell the same story: $45.5\%$ of
non-delegators in the \textit{No-Punishment} condition earned the high payoff for
Player~B, compared with $21.7\%$ in the \textit{Punishment} condition, even though the
two groups are statistically indistinguishable over the first ten rounds ($3.12$ vs.\
$2.98$ correct predictions; two-sided $p=0.66$).\footnote{Because non-delegation is a
choice, comparisons among non-delegators across conditions condition on an endogenous
decision. The ex-ante balance in measured performance is reassuring, but selection on
unobservables cannot be excluded.} If anything, effort rises where punishment is
impossible---the opposite of what a punishment-motivated effort story requires.
```

**CURRENT (results.tex:187 and 189):**
> The data are inconsistent with the simple form of this story. Measuring performance change as the difference between the average absolute prediction error across the first ten rounds and the absolute prediction error on the final prediction, we find that Player~As in the \textit{No-Punishment} condition improve their performance from rounds~1--10 to round~11, whereas Player~As in the \textit{Punishment} condition do not improve. Because all Player~As across both conditions faced the same image on the final prediction, this differential improvement cannot be attributed to task-specific variation. Therefore, increased effort appears concentrated among non-delegators in the \textit{No-Punishment} condition, where punishment is \textit{not} on the table---incompatible with a story in which Player~A in the \textit{Punishment} condition tries especially hard to outperform the algorithm in order to avoid punishment. In fact, among Player~As who chose not to delegate, those in the \textit{No-Punishment} condition (where punishment is not possible and the delegation share is higher) outperformed those in the \textit{Punishment} condition: $45.5\%$ of non-delegating Player~As in the \textit{No-Punishment} condition earned the high payoff for Player~B, compared to $21.7\%$ in the \textit{Punishment} condition. This difference is not driven by ex-ante performance differences across the first ten rounds of those that decided not to delegate (\textit{No-Punishment}: $3.12/10$; \textit{Punishment}: $2.98/10$; two-sided $p=0.66$).\footnote{Player~As who chose to delegate in the \textit{Punishment} condition scored on average 2.47/10 in the first ten rounds, compared with 3.06/10 for delegators in the \textit{No-Punishment} condition (two-sided p=0.039, p=0.080 in passers). The extra delegators in \textit{No-Punishment} therefore come disproportionately from the middle and upper portion of the performance distribution — subjects who, when punishment is on the table, choose to make the decision themselves.}
>
> Thus, treatment differences in the propensity to delegate do neither stem from ex-ante differences in performance between both treatments, nor from increased effort for the decision for Player B in the \textit{Punishment} condition.

*Mapping:* the improvement claims are now explicitly about non-delegators (the resolved design fact — delegators make no final prediction — is stated and turned into a feature); the delegator-composition **footnote moves into the text of unit 14b**; the selection-caveat footnote is new; the line-189 summary sentence is absorbed by the closing verdict here and the opener of unit 14a.

---

## 14a — Selection block: composition-artifact opener

**DRAFT:**
```latex
\paragraph{Selection on performance and process ownership.} If neither anticipated
punishment nor effort explains the reversal, what does? We can first establish what
Result~1 is \textit{not}: an artifact of sample composition. Average performance in the
first ten rounds is balanced across conditions ($2.93$ correct predictions out of ten;
Figure~\ref{fig:performance}), Player~As in both conditions exhibit similar---and
similarly significant---overconfidence about their own performance,\footnote{Measured
by the weighted-average belief about own performance. This overconfidence may partly
reflect the information that the algorithm performs equally well; it does not differ
across conditions.} and the treatment effect is robust to controlling for actual and
perceived performance (Table~\ref{tab:del_decision_determinants},
Columns~(3)--(4)).
```

**CURRENT (results.tex:143, the "(M3)" paragraph):**
> \paragraph{(M3) Performance differences and overconfidence across conditions.} If delegation is to some extent dictated by task performance, Result~1 could be a direct artifact of performance differences between treatments. However, treatment differences in delegation are not driven by performance differences across conditions in the first ten rounds. The average subject scores correctly in roughly three of the first ten rounds and performance is balanced across conditions (Figure~\ref{fig:performance}). Subjects also exhibit significant overconfidence, measured by the weighted-average belief about own performance; while this overconfidence may partly reflect the information that the algorithm is performing equally well, it is not statistically different across conditions.

*Mapping:* moved from its current position (after process ownership) to open the selection block; reframed from candidate mechanism to validity check; "roughly three" replaced by the exact $2.93$ (promoted from the `fig:performance` note); the pointer to the regression controls is new.

---

## 14b — Selection block: who delegates (gradient + composition)

**DRAFT:**
```latex
What differs across conditions is \textit{who} delegates. Within the
\textit{Punishment} condition, better-performing Player~As are less likely to delegate:
the correlation between the first-ten-rounds score and delegation is negative (Pearson
$r=-0.19$, $p=0.092$ among passers; Figure~\ref{fig:performance_delegation_scatter}), a
pattern also visible in the pooled delegation regression, where performance loads
negatively and approaches significance under the attention restriction
(Table~\ref{tab:del_decision_determinants}, $p=0.068$).\footnote{A similar relationship
holds for \textit{perceived} performance: Player~A's weighted-average belief about her
own performance enters with a small negative coefficient but is never statistically
significant (e.g., $b=-0.07$ in the passers-with-controls specification).} In the
\textit{No-Punishment} condition there is no comparable gradient. The composition of
delegators shifts accordingly: Player~As who delegated in the \textit{Punishment}
condition scored on average $2.47$ out of ten in the first ten rounds, compared with
$3.06$ for delegators in the \textit{No-Punishment} condition (two-sided $p=0.039$;
$2.38$ vs.\ $2.98$, $p=0.080$, among passers). The additional delegation in the
\textit{No-Punishment} condition thus comes disproportionately from the middle and
upper part of the performance distribution---precisely the subjects who, when
punishment is on the table, keep the decision for themselves.
```

**CURRENT (results.tex:120, plus the scatter-figure note at 133 and the footnote at 187):**
> \paragraph{Heterogeneity by performance.} The regression framework also lets us explore which other factors influence the delegation decision. Already in Table~\ref{tab:del_decision_determinants} we observe a weak negative correlation between delegation and Player~A's task performance across conditions, which is borderline significant when restricting the sample to subjects passing the attention check. Within the \textit{Punishment} condition, this relationship is even more pronounced and Player~As who performed better on the first ten rounds were less likely to delegate.\footnote{A similar relationship holds for \textit{perceived} performance: Player~A's weighted-average belief about her own task performance is negatively related to the delegation decision, e.g. coef. = -0.07 in the passers with controls specification} In the \textit{No-Punishment} condition, the relationship between performance and delegation is much less pronounced. Figure~\ref{fig:performance_delegation_scatter} visualises this asymmetry.

> (figure note, results.tex:133) The downward slope in the \textit{Punishment} condition is the Pearson $r=-0.19$ ($p=0.092$); no comparable slope in \textit{No-Punishment}. Restricted to attention-check passers.

> (footnote at results.tex:187) Player~As who chose to delegate in the \textit{Punishment} condition scored on average 2.47/10 in the first ten rounds, compared with 3.06/10 for delegators in the \textit{No-Punishment} condition (two-sided p=0.039, p=0.080 in passers). The extra delegators in \textit{No-Punishment} therefore come disproportionately from the middle and upper portion of the performance distribution — subjects who, when punishment is on the table, choose to make the decision themselves.

*Mapping:* the gradient statistics are promoted from the figure note into the text; the delegator-composition footnote (currently attached to the effort paragraph) is promoted into the text here, where it is evidence for the selection story; the transitional first sentence of line 120 is dropped.

---

## 14c — Selection block: Feier/EU contrast

**DRAFT:**
```latex
This gradient is informative because our design rules out the standard explanation for
it. In \citet{feier_hiding_2022}, the algorithm's performance distribution is matched
to the human distribution at the \textit{population} level: a high-performing subject
who recognizes her position in that distribution rationally believes she outperforms
the algorithm in expectation, and a low-performing one rationally believes the reverse,
producing an expected-utility-rational performance-to-delegation gradient. In our
design, performance is equalised at the \textit{individual} level and this is common
knowledge, so expected utility predicts no gradient at all. The pattern in the
\textit{Punishment} condition must therefore reflect something other than beliefs about
relative ability.
```

**CURRENT (results.tex:122):**
> This contrasts with the setting of \citet{feier_hiding_2022}, in which the algorithm's performance distribution is matched to the human distribution at the \textit{population} level: a high-performing subject who recognizes her position in that distribution rationally believes she outperforms the algorithm in expectation and a low-performing one rationally believes the reverse, producing an expected-utility-rational performance-to-delegation gradient. In our design, performance is equalised at the \textit{individual} level and is common knowledge, so expected utility predicts no gradient at all; the pattern documented here in the \textit{Punishment} condition is therefore informative about preferences rather than about beliefs over relative ability.

*Mapping:* nearly verbatim; only the framing sentence at the start and a slightly more cautious closer ("something other than beliefs about relative ability" instead of asserting "preferences" directly, which is now earned two paragraphs later).

---

## 14d — Selection block: two further checks (beliefs; perceived ability)

**DRAFT:**
```latex
Two further checks sharpen the interpretation. The gradient does not run through
punishment beliefs: Player~As do not expect a larger delegation penalty in good-outcome
states than in bad-outcome states, and punishment beliefs are uncorrelated with task
performance ($|r|\leq 0.21$, none significant at conventional levels;
Appendix~\ref{appendix:beliefs_vs_performance}). Nor does it run on \textit{perceived}
ability: among passers in the \textit{Punishment} condition, actual performance
discriminates sharply between delegators and non-delegators ($2.38$ vs.\ $3.00$ correct
out of ten) while perceived performance does not ($4.69$ vs.\ $4.71$;
Figure~\ref{fig:performance_by_delegation}). Delegators under punishment are not
subjects who \textit{believe} they are worse than their algorithm; they are subjects
who \textit{are} worse, and whose confidence does not reflect it.
```

**CURRENT (results.tex:137):**
> Finding this relationship in the \textit{Punishment} condition only indicates that Player A does not merely avoid directly causing a bad outcome and savoring directly causing a good outcome for Player B. Instead, it suggests a connection to anticipated punishment, such that either (i) Player~A expects more severe punishment for delegated decisions (relative to non-delegated ones) when the outcome is good than when it is bad, or (ii) better performing Player As hold systematically different punishment beliefs than worse-performing Player As. However, neither do we find evidence that Player~As expect a relatively larger punishment penalty for delegation in good-outcome states than in bad-outcome states, nor do Player~A's punishment beliefs do vary systematically with Player~A's performance.\footnote{See Appendix~\ref{appendix:beliefs_vs_performance} for the supporting numerical and graphical evidence: a within-subject test that $\Delta^{\text{good}}=\Delta^{\text{bad}}$ ($p=0.376$ in the passers sample), and all six correlations between Player~A's punishment beliefs and her task performance ($|r|\leq 0.21$, none significant at conventional levels).}

**CURRENT (fig:performance_by_delegation caption, results.tex:165–179, excerpt):**
> In the \textit{Punishment} condition, actual performance discriminates between delegators and non-delegators (means $2.38$ vs.\ $3.00$) while perceived performance does not (means $4.69$ vs.\ $4.71$). In the \textit{No-Punishment} condition, neither actual nor perceived performance discriminates (actual: $2.98$ vs.\ $3.13$; perceived: $4.85$ vs.\ $5.33$). The additional delegators in \textit{No-Punishment} therefore come disproportionately from the middle and upper portion of the actual performance distribution.

*Mapping:* line 137's two belief-based routings become the first check (its "(i)/(ii)" structure flattened; the double-"do" typo disappears); its opening sentence ("does not merely avoid... and savoring...") reappears as the arm-specificity logic in unit 14e; the perceived-vs-actual contrast is promoted from the figure caption into the text as the second check.

---

## 14e — Selection block: process-ownership interpretation

**DRAFT:**
```latex
The reading that remains is a preference over \textit{process}. Player~As who have a
good chance of producing the high payoff prefer to bring it about themselves rather
than through the algorithm: they attach value to being the one who acts, beyond the
consequences of acting. We refer to this as \textit{process ownership} of the outcome.
The arm-specificity then says when the preference binds. A pure intrinsic taste for
producing good outcomes would depress delegation in both conditions; the gradient
appears only where Player~B can sanction. On this reading, process ownership is
activated by accountability: it becomes behaviorally consequential when Player~B's
stake in the decision is enforceable, not merely material. Importantly, the account
requires no anticipation of differential punishment---and the elicited beliefs show
none.\footnote{An observationally equivalent variant loads on the other tail of the
performance distribution: Player~As with little chance of success may delegate to avoid
being the proximate cause of a likely failure. Both variants predict delegation
declining in performance, and both locate the operative margin in who produces the
outcome rather than in expected punishment.}
```

**CURRENT (results.tex:124):**
> \paragraph{(M2) Process ownership of the outcome.} This pattern suggests that Player~As who have a higher chance of producing the high payoff for Player~B prefer to bring about that good outcome themselves rather than via the algorithm. The intuition draws on the psychological-ownership literature: people derive utility from being the proximate cause of a good outcome for another, and this utility is asymmetric with respect to outcomes \citep{steffel_passing_2016}. The pattern is consistent with process ownership being behaviourally consequential only when Player~B's payoff is at meaningful third-party stake — present in the \textit{Punishment} arm, where Player~B can sanction; absent in the \textit{No-Punishment} arm, where Player~B receives the payoff but has no enforcement role. Importantly, this does not require Player~A to anticipate \textit{differential} punishment for delegated vs.\ self-made decisions; the elicited beliefs show no such asymmetry. [Comment: check Steffel paper: Steffel (2016) is cited, but Steffel's setting is about delegating decisions through agents — whether her finding specifically supports "stake-conditional activation" of process ownership is worth verifying. If it doesn't, weaken to "consistent with the broader psychological-ownership literature, in which intensity of caring tracks the size of the stake.]

*Mapping:* acts on your Steffel comment — the citation is removed here (pending the decision-rights/control anchors flagged in the draft) and Steffel is reserved for the two-channel paragraph; the "utility is asymmetric with respect to outcomes" claim is dropped; the third-party-stake formulation is kept as "enforceable, not merely material"; the arm-specificity logic (from line 137's opening) is made explicit; the footnote on the observationally equivalent avoid-bad-tail variant is new.

---

## 14f — Selection block: alternatives (uncertainty; demand)

**DRAFT:**
```latex
Two alternative readings deserve mention. First, the gradient could reflect preferences
over uncertainty rather than over process. \citet{dietvorst_people_2020} document that
the preference for algorithms declines as the uncertainty inherent in a decision rises;
in our task, where most subjects score below five out of ten, better performance moves
the success probability toward one half---the point of maximal outcome uncertainty.
But this preference is condition-invariant: it predicts the same gradient in both
conditions and no treatment difference in delegation, so it can explain neither the
arm-specificity of the gradient nor Result~1 itself. Second, we cannot exclude an
experimenter-demand account, in which the salience of being evaluated---rather than a
preference over process---cues Player~A toward handling the decision herself. The two
accounts are observationally similar in our design; we take up the direction and
testability of demand effects in Section~\ref{conclusion}.
```

**CURRENT (results.tex:141, "Inherent uncertainty"):**
> \paragraph{Inherent uncertainty.} Alternatively, differences in the chances of success for Player~B may also be interpreted as differences in uncertainty inherent in the task. \cite{dietvorst_people_2020} provide suggestive experimental evidence on how the amount of uncertainty inherent in a decision affects the preference for algorithms. They find that with increasing task uncertainty, subjects' preference for algorithms over their own prediction decreases, even though they were aware that the algorithm performs better on average. In our setting, arguably, uncertainty is maximized at a score of 50\%, and most Player~A's perform worse, so that the performance distribution largely sits below 50\%. In turn, better performance comes with greater outcome uncertainty and is linked to lower delegation rates. Therefore, the mechanism \cite{dietvorst_people_2020} describe is consistent with what we find in a setting in which the decision is payoff-relevant to another participant, equal relative performance is common knowledge and punishment is possible. However, this reasoning would apply to treatment and baseline equally and thus not explain Result~1.

**CURRENT for the demand sentence: none in results.tex.** (Related passage in conclusion.tex:17, which keeps the full treatment: "A natural concern is whether the punishment possibility cues Player~A to behave more conservatively for reasons unrelated to the substantive question---an experimenter-demand effect. We cannot rule this concern out from the data. ...")

*Mapping:* the uncertainty paragraph is demoted from a standalone `\paragraph` to a dispatched alternative (D4) — same logic, compressed, and now also dispatched by the gradient's arm-specificity, not only by Result 1; the demand mention in the results section is new (it restores the missing candidate) while the full discussion stays in the conclusion.

---

## 15 — Taking stock

**DRAFT:**
```latex
\paragraph{Taking stock.} The reversal in Result~1 is not a composition artifact: the
conditions are balanced in performance and confidence, and the treatment effect
survives the corresponding controls. It is not explained by anticipated differential
punishment: the delegation-specific asymmetry that channel requires is absent from
Player~A's beliefs on average---consistent with Player~B's realized punishment
(Result~2)---even though belief heterogeneity predicts delegation at the margin. It is
not explained by punishment-induced effort, which the final-prediction data contradict:
improvement concentrates where punishment is impossible. What remains standing is
process ownership: when Player~B can hold her to account, a Player~A who is likely to
deliver the high payoff prefers to deliver it herself. We are explicit about what this
evidence is and is not. It consists of a heterogeneity pattern and a
delegator-composition comparison, both exploratory and both in modest samples; it
identifies the most consistent reading of the data we have, not a confirmed mechanism;
and an experimenter-demand account of the same facts cannot be ruled out by design.
Suggestively, the belief evidence points the same way: where punishment beliefs predict
delegation at all, it is the good-outcome belief difference that carries the
relationship (Table~\ref{tab:reg_belief_specs}, Column~(5)), as if the good-outcome
state is the one on Player~A's mind when she decides who decides.
```

**CURRENT (results.tex:193, "In sum"):**
> In sum, we considered four candidate mechanisms behind Result~1. M1 (anticipated differential punishment) is inconsistent with Player~A's elicited beliefs: she does not expect a relatively larger punishment penalty for delegation in the good-outcome state than in the bad-outcome state. M2 (process ownership of the outcome) is the only candidate the data support: the negative performance--delegation gradient in \textit{Punishment} and the absence of any comparable gradient in \textit{No-Punishment} (Figure~\ref{fig:performance_delegation_scatter}, Figure~\ref{fig:performance_by_delegation}) jointly indicate that Player~As who are likely to deliver the high payoff to Player~B prefer to do so personally, but only when Player~B's payoff is at meaningful third-party stake. M3 (ex-ante differences in task performance between conditions) is inconsistent with the balance documented in Figure~\ref{fig:performance}: average performance over rounds~1--10 is statistically indistinguishable across treatments. M4 (extra effort to outperform the algorithm under the threat of punishment) is inconsistent with the round-11 effort data, which run in the opposite direction: it is in the \textit{No-Punishment} condition, not in the \textit{Punishment} condition, that non-delegators improve from rounds 1--10 to the final prediction. However, we are explicit that the supporting evidence for M2 consists of a single heterogeneity pattern in a sub-sample and a comparison of delegator success rates; the pattern is the most consistent reading of the data we have, but not a confirmed mechanism.

**CURRENT for the final sentence (results.tex:98, tail — see unit 10):**
> If taken at face value this would mean that the delegation decision is primarily made by thinking about punishment consequences after a good outcome, rather than a bad outcome.

*Mapping:* M-numbers dropped (D7); verdicts reordered to match the new block order; "the only candidate the data support" softened to "the most consistent reading... not a confirmed mechanism" throughout; the demand caveat is added to the summary (currently missing); the relocated good-outcome sentence is the optional D6 closer.

---

## 16 — Relation to prior evidence: Feier reconciliation

**DRAFT:**
```latex
\paragraph{Relation to prior evidence.} Our results sit in apparent tension with the
closest precedent. \citet{feier_hiding_2022} document that decision-makers are punished
\textit{less} for algorithmically delegated decisions, where we detect no punishment
differential; and a natural extrapolation from their finding is that the prospect of
punishment should make delegation \textit{more} attractive, where we find the opposite.
Neither contrast is a contradiction. On the first, the differential punishment in
\citet{feier_hiding_2022} is plausibly read, at least in part, as signal extraction:
under session-level calibration, the delegation decision reveals the principal's
beliefs about her ability relative to the algorithm, and evaluators can respond to what
the decision reveals---sanctioning a non-delegator's apparent overconfidence,
say---rather than to the assumption of responsibility itself.\footnote{Signal
extraction alone does not explain every feature of their data: the delegation decision
carries signal value for human delegates in their design as well, yet only algorithmic
delegation reduces punishment significantly. Our claim is accordingly narrow: whatever
mixture of channels generates their differential, the relative-ability signal is closed
off in our design---in both conditions---by the individual-level, common-knowledge
calibration, so it can contribute neither to punishment differentials nor to the
delegation gap here.} The disappearance of the punishment differential in our data,
where the signal is closed off by construction, is consistent with this reading rather
than in conflict with it. On the second, the extrapolation was never tested in their
design: \citet{feier_hiding_2022} vary the type of delegate while evaluation is always
possible, whereas we vary whether punishment is possible at all. The two designs answer
different questions, and ours is the first to identify the motivational effect of the
punishment prospect itself. Which design feature is responsible for the sign reversal
cannot be settled without varying the calibration directly---a manipulation our design
does not include.
```

**CURRENT (results.tex:212–214, in subsection "Other"):**
> \paragraph{Reconciling our findings with \citet{feier_hiding_2022}.} Two of our results sit in apparent tension with the closest precedent. First, \citet{feier_hiding_2022} document that decision-makers are punished \textit{less} for algorithmically delegated decisions; we find no significant punishment differential. Second, the natural prediction from \citet{feier_hiding_2022}'s own findings is that the prospect of punishment should make algorithmic delegation \textit{more} attractive; we find the reverse. We do not view these contrasts as contradictions, but as evidence that the design features which differ between the two studies are doing real work. The differential punishment in \citet{feier_hiding_2022} is most plausibly read as third parties extracting a signal from the delegation decision about the principal's self-perceived ability relative to the algorithm---a signal that is maximally informative when (as in their design) the algorithm is calibrated at the session level and when the principal's relative ability is uncertain. Our individual-level calibration, made common knowledge, closes off this signal-extraction channel by construction: a Player~B in our setting has no basis to read delegation as overconfidence, laziness, or ability avoidance. The disappearance of the punishment differential in our data is therefore consistent with, rather than refutes, the signal-extraction reading of \citet{feier_hiding_2022}'s result. By the same logic, the responsibility-shifting motive that \citet{feier_hiding_2022}'s setup leaves on the table is muted in ours, isolating a different and milder margin: the moral salience of accountability for the principal herself, independent of any third-party inference. The reversal we observe in the delegation decision speaks to that margin---and we are explicit that the question of which design feature is causally responsible for the sign reversal cannot be resolved without an experiment that varies relative-performance calibration directly, which we do not do here.
>
> [Comment: The second point is not a contradiction, because in Feier the two treatments that are compared are different to the two treatments that are compared in our paper.]
>
> [Comment: Issue here is that the relative performance concern applies to both treatments.]

*Mapping:* moved from "Other" into the discussion; your first comment becomes the "the extrapolation was never tested in their design" sentence; your second comment is handled by the new footnote, which explicitly narrows the signal-extraction claim ("most plausibly read" → "plausibly read, at least in part," and the human-delegate hole in the signal story is acknowledged); the "muted margin / moral salience" sentences are dropped here because the two-channel paragraph (unit 17) now does that work.

---

## 17 — Relation to prior evidence: two channels + map

**DRAFT:**
```latex
The broader pattern is best organized by distinguishing two channels that the canonical
literature conflates. \citet{steffel_passing_2016} show that delegation relieves both
\textit{felt} responsibility (the principal's own moral burden) and \textit{anticipated
blame} (the judgement she expects from others), and that both independently motivate
delegation. When the delegate is human, the two move together; the recent
algorithmic-delegation evidence suggests they can decouple.
\citet{hueholt_trusting_2026} find that subjects delegate a moral decision to an AI
\textit{more} often when its consequences become real, consistent with algorithms
effectively absorbing the principal's internal moral burden, and
\citet{tontrup_strategic_2025} likewise document algorithmic delegation used
strategically as moral cover. Our results speak to the external channel, and there the
algorithm performs poorly as a shield: when third-party punishment is possible,
delegation falls (Result~1), and Player~B punishes the outcome rather than the
delegation decision (Result~2)---so a delegating Player~A would gain no insulation, and
her elicited beliefs suggest she knows it. Read jointly, the evidence suggests that an
algorithm shields the principal's internal moral burden far better than her external
accountability---two channels that canonical human-delegate settings could not
separate, and that algorithmic delegates pull apart. Related work extends this map
along further margins, from the blame absorbed by the programmer behind the algorithm
\citep{chevrier_algorithm_2024} to the compliance asymmetry between human and machine
agents on instructed unethical tasks \citep{kobis_delegation_2025}; a unified design
that varies the relative-performance calibration, the punishment possibility, and the
visibility of the algorithm's properties is the natural next step, which we take up in
Section~\ref{conclusion}.
```

**CURRENT (results.tex:195–196, "Two channels of responsibility-shifting"):**
> Recent work suggests that what the prior literature has called ``the responsibility-shifting motive'' is in fact two distinct sub-motives that tend to co-move when the delegate is human but can decouple when the delegate is an algorithm. \citet{steffel_passing_2016} document that delegation reduces both \textit{felt} responsibility (the principal's own anticipated moral burden) and \textit{anticipated blame} (the principal's anticipated third-party judgement), and that both mediators contribute independently to the propensity to delegate. \citet{hueholt_trusting_2026} test the first channel in a moral-domain delegation paradigm and find that subjects delegate to AI \textit{more} often when the moral consequences of the decision become real (rather than hypothetical), and rate AI's moral capability higher in real-stakes conditions --- consistent with belief adaptation that lets the principal shed her \textit{felt} moral burden through delegation. Our results speak to the second channel: when third-party punishment is possible, delegation to the algorithm \textit{falls} (Result~1), and Player~B punishes by outcome rather than by delegation choice (Result~2). Both are consistent with principals correctly anticipating that the algorithm does not effectively absorb \textit{external} blame. Taken together, this suggests a two-channel reading in which AI is a strong shield against the principal's internal moral burden but a weak shield against the external accountability she faces from third parties --- channels conflated in canonical human-delegate settings but separable when the intermediary is algorithmic.

**CURRENT (results.tex:216, in "Other"):**
> We see scope, then, for the two studies to be parts of a single picture: \citet{feier_hiding_2022} identifies the signal-extraction channel through which delegation can shift third-party blame; we identify a process-ownership channel through which the prospect of accountability can pull the principal toward direct engagement with the decision. The two channels are not mutually exclusive. \citet{chevrier_algorithm_2024}, looking at a third margin (the programr behind the algorithm), and \citet{kobis_delegation_2025}, looking at a fourth (the compliance asymmetry between human and machine agents on instructed unethical tasks), populate further nodes in this expanding map. A unified design that varies the relative-performance calibration, the punishment possibility, and the visibility of the algorithm's compliance properties would be the natural next step. We discuss the implications for future work in Section~\ref{conclusion}.
```

*Mapping:* the two passages are merged; `tontrup_strategic_2025` is added alongside Hueholt (it currently appears only in the literature section); Hueholt's "rate AI's moral capability higher" detail is dropped; the chevrier/kobis "expanding map" is compressed to one sentence; the "single picture" sentence of line 216 is implicit in the merged paragraph rather than restated.

---

# Current passages with no place in the draft

1. **results.tex:63, tail** — "[Comment: complete, once the mechanism paragraphs are worked out.]" — superseded by the new opening.
2. **results.tex:69, last sentence** — "Moreover, it would be reflected in punishment beliefs, which we discuss next." — deliberately cut, per your line-71 comment (the departures story no longer leans on beliefs).
3. **results.tex:73** — "We have already seen that Player B punishment is outcome-based, rather than delegation-based, yet a shirking motive --- which would predict additional punishment for delegation --- could at least rationalize the positive punishment observed in the good outcome--delegated scenario." — cut: the positive punishment after good outcomes is already interpreted in the Result-2 part (footnote citing \citet{coffman_intermediation_2011}). Could return as a footnote to the shirking sentence if you want it kept.
4. **results.tex:103–116** — the commented-out `belief_distributions` paragraph and figure — remain out (the regression table carries the same information).
5. **results.tex:139** — "[Comment: Think more about this potential non-linearity...]" — not addressed in the draft. The May analysis (C6) found no power to distinguish a quadratic from a linear gradient (~60–70 obs per condition); if you want it acknowledged, the natural place is a short footnote on the gradient sentence in unit 14b. Open.
6. **results.tex:96** — "[Comment: Maybe for consistency, include also here the marginal effect at the bottom...]" — a table-generation item (`22_belief_specs.py`), independent of the prose; still open.
7. **results.tex:49 and :59** — comments on cell-level punishment determinants and on hypothetical punishment — Player-B-subsection business, untouched by this draft.
8. **results.tex:7, supervisor comment** (one- vs. two-sided hypothesis framing) — Result-1-subsection business, untouched by this draft.
9. **results.tex:206–210 ("Other": order effects, power)** — not part of the discussion: suggested destinations are a Result-1 robustness footnote (order effects) and the power appendix (power paragraph), after which "Other" can be dissolved.
10. **results.tex:120, first sentence** — "The regression framework also lets us explore which other factors influence the delegation decision." — dropped (transition no longer needed under the new order).
11. **results.tex:189** — "Thus, treatment differences in the propensity to delegate do neither stem from ex-ante differences in performance between both treatments, nor from increased effort..." — absorbed by the unit-13 verdict and the unit-14a opener rather than kept as a separate sentence.
