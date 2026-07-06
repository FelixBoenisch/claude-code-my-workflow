---
title: "DRAFT v2 (polished): 'Discussion of results' subsection (full LaTeX)"
date: "2026-07-02"
scope: "Replacement draft for manuscript/results.tex \\subsection{Discussion of results} (lines 61–204) + absorbs the Feier material from \\subsection{Other}"
status: "DRAFT for Felix's review — no manuscript files edited"
basis: "v1 restructured per comments of 2026-07-02; v2 is a full sentence-level polish pass. Effort paragraph now reflects the resolved design fact: delegators do NOT make the final prediction."
---

Reading guide: the LaTeX below is self-contained and paste-ready except for the few
`% [...]` comments, which mark (i) items to verify against the analysis scripts before
pasting and (ii) the two sentences you may want to cut (the orienting sentence in the
opening; the good-outcome sentence in Taking stock). Notes on remaining decisions and
knock-on fixes follow at the end.

---

# The draft

```latex
\subsection{Discussion of results} \label{sec:mechanism}

Result~1 does not merely fail to support \textit{Hypothesis~1}: the effect is
statistically significant in the opposite direction. The possibility of punishment
discourages, rather than encourages, delegation to the algorithm. Read together with
Result~2, this is puzzling. The prospect of punishment changes Player~A's delegation
decision, even though the punishment Player~B actually imposes attaches to outcomes,
not to delegation---conditional on the outcome, we detect no penalty for delegating. In
this subsection, we first ask why the responsibility-shifting motive underlying
\textit{Hypothesis~1} may have had little force in our setting; we then turn to
explanations that could actively reverse its prediction.
% [Optional: the last sentence is the only "roadmap" element --- cut it if you prefer
% no preview at all.]

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

This reasoning, however, explains at most a null result: if shifting responsibility
onto the algorithm is worth little here, delegation should simply differ little across
conditions. It cannot explain why punishment pushes delegation \textit{down}. Some
force must actively discourage delegation when punishment is
possible.\footnote{Recent evidence that algorithmic delegates can serve as moral cover
\citep[e.g.,][]{tontrup_strategic_2025, hueholt_trusting_2026} sharpens the puzzle; we
return to it at the end of this section.}

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

This implication gives the belief data a precise role. The algorithm reproduces
Player~A's own success probability, and both players know it, so the outcome lottery
faced by Player~B is the same whether or not Player~A delegates. Punishment that
responds only to the outcome therefore burdens both options equally and cannot tilt the
choice between them. What can tilt the choice is an asymmetry: expected punishment
attached to the delegation decision itself, conditional on the outcome. This is the
quantity the elicited beliefs measure.\footnote{The equivalence of the two options
presumes that Player~A does not expect to beat her own record through extra effort on
the final prediction; we take up this possibility below.}

\paragraph{Punishment beliefs.} \label{sec:beliefs} After the delegation decision but
before learning the outcome, we elicited Player~A's beliefs about Player~B's punishment
in each of the four \textit{(delegation, outcome)} scenarios.

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

Two patterns emerge (Figure~\ref{fig:realized_vs_anticipated}). First, Player~As
substantially \textit{overestimate} punishment: average anticipated punishment exceeds
average realized punishment in every scenario. By the argument above, however, an error
that concerns both options alike cannot tilt the choice between them; what matters is
the asymmetry. Second, the asymmetry is absent: Player~As expect essentially the same
punishment for delegated and self-made decisions, conditional on the outcome, correctly
anticipating the pattern in Player~B's actual behavior (Result~2).\footnote{The
expected punishment penalty for delegation is small and statistically indistinguishable
from zero in both outcome states, and a within-subject test finds no asymmetry between
the two ($p=0.376$ among passers); see Appendix~\ref{appendix:beliefs_vs_performance}.
% [VERIFY: the appendix currently documents the diff-of-diffs test and the
% belief--performance correlations; the cell-level tests that each penalty is itself
% indistinguishable from zero should be added there (the May analysis confirms both are
% small and insignificant).]
} The same holds across conditions: hypothetical beliefs elicited in the
\textit{No-Punishment} condition closely track those in the \textit{Punishment}
condition (Figure~\ref{fig:realized_vs_anticipated}, blue bars). The manipulation
appears to have changed whether punishment could materialise, not what subjects
expected it to look like; a cross-condition difference in beliefs about the punishment
schedule is therefore unlikely to drive the delegation gap.
% [D2: the last two sentences are the repurposed role of the blue bars. If you later
% drop the blue bars, delete both.]

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

The estimated relationship is weak in the full sample but sharpens among attentive
subjects. In Columns~(1)--(2) the belief coefficient is positive but far from
significant ($p>0.39$): in the unrestricted \textit{Punishment} sample, expected
differential punishment does not predict delegation. Among attention-check passers,
subjects who expect a one-pound larger punishment penalty for deciding themselves are
markedly more likely to delegate (simple average: $2.71$, $p=0.035$; weighted average:
$3.33$, $p=0.030$). In the decomposition, the good-outcome belief difference carries
the relationship ($1.58$, $p=0.033$), while the bad-outcome difference is positive but
noisier ($0.94$, $p=0.21$).

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

What differs across conditions is \textit{who} delegates. Within the
\textit{Punishment} condition, better-performing Player~As are less likely to delegate:
the correlation between the first-ten-rounds score and delegation is negative (Pearson
$r=-0.19$, $p=0.092$ among passers; Figure~\ref{fig:performance_delegation_scatter}), a
pattern also visible in the pooled delegation regression, where performance loads
negatively and approaches significance under the attention restriction
(Table~\ref{tab:del_decision_determinants}, $p=0.068$).\footnote{A similar relationship
holds for \textit{perceived} performance: Player~A's weighted-average belief about her
own performance enters with a small negative coefficient but is never statistically
significant (e.g., $b=-0.07$ in the passers-with-controls specification).
% [VERIFY: exact coefficient and p-value against 04_logit_delegation.py.]
} In the \textit{No-Punishment} condition there is no comparable gradient. The
composition of delegators shifts accordingly: Player~As who delegated in the
\textit{Punishment} condition scored on average $2.47$ out of ten in the first ten
rounds, compared with $3.06$ for delegators in the \textit{No-Punishment} condition
(two-sided $p=0.039$; $2.38$ vs.\ $2.98$, $p=0.080$, among passers). The additional
delegation in the \textit{No-Punishment} condition thus comes disproportionately from
the middle and upper part of the performance distribution---precisely the subjects who,
when punishment is on the table, keep the decision for themselves.

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

The reading that remains is a preference over \textit{process}. Player~As who have a
good chance of producing the high payoff prefer to bring it about themselves rather
than through the algorithm: they attach value to being the one who acts, beyond the
consequences of acting. We refer to this as \textit{process ownership} of the outcome.
% [CITATION TODO: anchor the preceding sentence in the decision-rights/control
% literature after verification --- candidates: Bartling, Fehr and Herz (2014,
% Econometrica, intrinsic value of decision rights); Owens, Grossman and Fackler (2014,
% AEJ:Micro, control premium); neither is in ProjectAlgorithm.bib yet. Fallback:
% "consistent with the broader psychological-ownership literature, in which the
% intensity of caring tracks the size of the stake." steffel_passing_2016 is
% deliberately NOT used here (their asymmetry runs blame > credit); it appears in the
% two-channel paragraph below, where it fits.]
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
% [D6: optional closing sentence --- flagged as suggestive; cut if it overreaches.]

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

---

# Notes

### What the polish pass changed (v1 → v2)

- **One-step-per-sentence discipline throughout.** Every paragraph now runs claim → evidence → verdict, and redundant restatements were cut (e.g., the opening previously stated the puzzle twice; the level-overestimation logic previously appeared in both the anticipation and beliefs paragraphs in full).
- **Opening:** four sentences — reversal, its meaning, the joint puzzle with Result 2, orientation. Nothing else.
- **Departures:** the dictator-game contrast is now a strict parallel (three ingredients there, their removal here), and the causal chain "intent obscured → punishment motive loses bite → intermediary loses value" is one sentence instead of three.
- **Anticipation:** the "only the asymmetry can tilt the choice" argument is now stated once, cleanly, before the data; the effort caveat moved to a footnote so the argument is uninterrupted; "all three variants carry the same testable implication" replaces the vaguer "behavioral signature."
- **Beliefs:** the two-patterns paragraph now uses the asymmetry logic instead of re-deriving it; the blue-bars point is two sentences with a clear inference ("changed whether punishment could materialise, not what subjects expected it to look like").
- **Effort:** rewritten around the resolved design fact — delegators make no final prediction, so effort is observable exactly for the group the story concerns; the story's prediction is stated before the test ("non-delegators should improve specifically in the *Punishment* condition").
- **Selection block:** the artifact check, gradient, composition fact, Feier/EU contrast, two belief checks, and interpretation now each occupy one paragraph with a single job; the process-ownership paragraph separates the preference (one sentence) from when it binds (arm-specificity) from what it does not require (belief asymmetry).
- **Feier paragraph:** the two tensions are named first, then resolved in order; the signal-extraction claim is explicitly narrowed in the footnote per your earlier comment.

### Resolved: the effort/design question

Delegators do not make the final prediction. Two knock-on fixes outside this subsection, for the later sync pass:

1. **`conclusion.tex` (Limitations)** currently asserts the opposite ("Player A also makes the final prediction whether or not she ultimately decides to delegate, which equates the time cost of the two options...") — this sentence is factually wrong and must be removed or replaced. Note its replacement may want to acknowledge the implication that delegation *saves* effort/time, which makes the shirking variant in the anticipation block concrete.
2. **`design.tex`** never states explicitly that the prediction screen is skipped under delegation (only the appendix timeline note does). Agreed fix: insert at the end of the paragraph ending "...costless delegation is standard in the literature~\citep{bartling_shifting_2012,coffman_intermediation_2011,feier_hiding_2022}." (immediately before "We then asked Player~A to report her beliefs..."):
   > "If Player~A chose to make the prediction herself, she entered her final prediction on the next screen; if she delegated, this screen was skipped and she made no further prediction."

   (Variant with "---together with a statement of her confidence in it---" if the confidence elicitation should be documented in the body.)

### Items flagged inline (`% [...]`)

1. **VERIFY — cell-level belief tests** for the footnote in the beliefs paragraph (add to Appendix `beliefs_vs_performance`).
2. **VERIFY — perceived-performance footnote** coefficient/p against `04_logit_delegation.py` (−0.07 vs. −0.06, p≈0.75).
3. **CITATION TODO — process-ownership anchor** (Bartling–Fehr–Herz 2014 / Owens et al. 2014, to verify and add to bib; Steffel reserved for the two-channel paragraph).
4. **Optional cuts:** orienting sentence in the opening; good-outcome sentence in Taking stock (D6).

### Polish-pass items for the later sync (unchanged from v1)

- Spelling is mixed BE/AE in the manuscript; the draft inherits the mix ("unincentivised", "materialise" vs. "behavior", "rationalization") — harmonize once, manuscript-wide.
- Once pasted, the M1–M4 labels disappear from the body; intro, conclusion, and the appendix preregistration table still use (mutually inconsistent) M-labels and need a sync pass.
- The bad-cell punishment p-value discrepancy (0.13 in `results.tex` vs. 0.153 in appendix/conclusion — likely full vs. passers) is avoided in this draft but should be made sample-explicit where it appears.
- "Other" subsection: after this draft absorbs the Feier material, order effects → Result-1 robustness footnote, power → appendix, then "Other" can be dissolved.
