# Introduction draft, version 3

Reconciles v2 with the current introduction.tex and the live literature, design, and results sections, then revised against introduction conventions of Experimental Economics, JEEA, and the Economic Journal (six published intros analyzed; see notes at the end).

Open decision carried over: the academic example ("journal editors use algorithms to screen submissions") is omitted here for a clean three-example opening; it can be appended to the first sentence pair if preferred.

## Draft (drop-in for introduction.tex)

```latex
\section{Introduction} \label{introduction}

Algorithms increasingly make decisions whose consequences fall on someone other
than the person who deploys them. Physicians rely on diagnostic systems when
treating patients, firms let screening software rank job applicants, and
financial advisors draw on algorithmic tools when managing client portfolios.
In such settings a human decides whether to put the algorithm in charge, while
a third party bears the consequences. Two questions follow naturally. Does
delegating a decision to an algorithm change the responsibility that others
assign to the human who delegated it? And does the prospect of being held
responsible change the willingness to delegate in the first place? This paper
provides experimental evidence on both.

The experimental literature on delegation between humans points in a clear
direction. Delegation shifts responsibility. Principals who delegate an
unpopular decision to a human intermediary are punished less for it, feel less
responsible for it, and delegate strategically for precisely this reason
\citep{bartling_shifting_2012, hamman_self-interest_2010,
coffman_intermediation_2011, oexl_shifting_2013}. Recent evidence suggests
that algorithms can take over the intermediary's role. Delegation to an
algorithm increases dishonesty by obscuring intent \citep{kobis_delegation_2025},
is used to extract surplus while shedding moral responsibility
\citep{tontrup_strategic_2025}, becomes more attractive when the moral stakes
of the decision are real \citep{hueholt_trusting_2026}, and shields
decision-makers from being held responsible for bad outcomes
\citep{feier_hiding_2022}. On this reading, decision-makers who face potential
punishment should be drawn to the algorithm, and delegation should protect
them when outcomes turn out badly.

Testing these predictions cleanly imposes two requirements on the experimental
environment. First, the delegation decision must carry no information about
ability. Beliefs about relative performance are a dominant driver of algorithm
use \citep{logg_algorithm_2019, qin_ai_2025}, and when the algorithm is
calibrated to the subject pool rather than to the individual, as in
\citet{feier_hiding_2022}, choosing it reveals the decision-maker's confidence
in her own ability, so that observers may sanction perceived overconfidence
rather than the act of delegating. Second, the availability of punishment must
itself be varied. Existing work on responsibility shifting toward algorithms
observes how third parties punish but does not manipulate whether punishment
is possible, so the motivational claim that decision-makers delegate in order
to avoid punishment has remained untested.

Our preregistered online experiment with 322 participants meets both
requirements.\footnote{The experiment was preregistered at
AsPredicted~\#133980, available at
\href{https://aspredicted.org/hs9az8.pdf}{\nolinkurl{aspredicted.org/hs9az8.pdf}}.}
A decision-maker, Player~A, faces a prediction task with monetary consequences
for a matched recipient, Player~B. If her estimate of a person's body weight
from a photograph is accurate, Player~B earns \pounds 5, otherwise \pounds 1.
Player~A's own payoff is unaffected by the prediction. Before the final
prediction, Player~A completes ten incentivized rounds of the same task and
may then either make the consequential prediction herself or delegate it to an
algorithm that succeeds with exactly the accuracy she achieved in those
rounds. This individual calibration is common knowledge, so neither player can
read anything about ability into the delegation choice. Between subjects we
vary whether Player~B can reduce Player~A's earnings at a small cost to
himself. In the \textit{Punishment} condition, Player~B states a punishment
for every combination of delegation choice and outcome. In the
\textit{No-Punishment} condition, no sanction is possible.

Both predictions fail, the first with reversed sign. When punishment is
possible, 42.5~percent of decision-makers delegate to the algorithm. When it
is not, 59.3~percent do. The prospect of punishment thus significantly reduces
delegation by roughly 17~percentage points, and the difference is robust to
controlling for socio-demographic characteristics and for actual and perceived
task performance. Delegation also offers no protection. Recipients punish bad
outcomes more severely than good ones, but conditional on the outcome, the
punishment of delegated and self-made decisions is statistically
indistinguishable. Punishment responds to what happened to the recipient, not
to how the decision was made, and decision-makers anticipate this correctly.
Their elicited beliefs overstate how much they will be punished in every
scenario but embody no penalty for delegation as such.

Read together, the two results are puzzling. The possibility of punishment
moves the delegation decision even though no punishment attaches to
delegation, neither in realized sanctions nor in beliefs. We examine several
candidate explanations. Sample composition is ruled out by randomization and
by the robustness of the effect to controls. Effort provides no
reconciliation either. If the threat of punishment led decision-makers to
keep the decision in order to outperform the algorithm, improvement on the
final prediction should concentrate in the \textit{Punishment} condition,
whereas it concentrates where punishment is impossible. What does change
across conditions is who delegates. Under the threat of punishment, better
performers keep the decision to themselves, a pattern that cannot reflect
beliefs about relative ability, which our calibration removes. A preference
for producing a good outcome oneself, or an aversion to delegating decisions
whose outcomes are most uncertain, is consistent with this pattern. Either
preference, however, operates in both conditions and can generate the
treatment difference only if accountability itself activates it. Our design
cannot separate these readings, and we leave the mechanism as an open
question.

The paper contributes to three literatures, which Section~\ref{literature}
reviews in detail. To the literature on responsibility avoidance through
delegation, we provide the first direct test of whether the prospect of
punishment motivates delegation to an algorithm, and we find that it
discourages delegation instead. To the literature on algorithm use, we add
the possibility of punishment as an experimentally manipulated determinant of
ceding a decision to an algorithm, a margin distinct from the more widely
studied willingness to follow algorithmic advice. To the literature on
responsibility attributions for decisions involving algorithms, we show that
once delegation is uninformative about ability, third parties sanction
realized outcomes rather than the use of the algorithm.

The last result qualifies the findings of \citet{feier_hiding_2022}, the study
closest to ours, in which decision-makers are held less responsible for
outcomes delegated to an algorithm than for outcomes of their own actions.
Under their session-level calibration, delegation is informative about
self-assessed ability, so evaluators have something other than the outcome to
respond to. Closing this channel removes the punishment differential.
Moreover, their treatments vary the type of delegate under a fixed punishment
regime, whereas we hold the delegate fixed and vary the punishment regime.
The two designs therefore answer complementary questions, and ours isolates
the motivational role of anticipated punishment.

The environment we study, a prediction under genuine uncertainty made by a
decision-maker with no material stake in the affected party's outcome,
resembles the settings in which algorithmic delegation typically operates in
practice. Within its bounds, our results suggest that holding human users
answerable for algorithmic decisions does more than allocate blame after the
fact. Accountability deterred delegation to an algorithm that was, by
construction, exactly as good as its user, and it deterred the better
performers most. Whether such deterrence is desirable depends on whether the
algorithm outperforms its user. The direction of the behavioral response,
however, is the opposite of what the blame-shifting logic predicts.

The remainder of the paper is organized as follows. Section~\ref{literature}
relates the study to the literature. Section~\ref{design} presents the
experimental design and hypotheses. Section~\ref{results} reports the results
and examines candidate mechanisms. Section~\ref{conclusion} concludes.
```

## What changed relative to v2 and the current introduction.tex

1. Conflicts resolved toward the live sections and prior feedback. Two design features only (individual calibration, punishment variation), framed as identification requirements rather than a Feier comparison. No p-values or marginal effects. The mechanism paragraph matches the results section's open-question stance and treats process ownership and uncertainty aversion as parallel candidates. Result 2 wording ("the punishment of delegated and self-made decisions is statistically indistinguishable") is robust to re-framing Result 2 from Player B's perspective.
2. From the current introduction.tex, two elements were kept. The two-research-question framing in the opening paragraph, and the preregistration footnote (AsPredicted #133980), which also restores information lost when the appendix preregistration section was deleted.

## Revisions made after reading published introductions (EE, JEEA, EJ)

1. Added an explicit identification-requirements paragraph before the design summary (the Bauer et al. EJ 2023 and Oexl and Grossman EE 2013 pattern for punishment experiments).
2. Results preview quantified with percentages and percentage points only, mirroring the order of the results section. None of the six published intros contains p-values or test statistics.
3. Contribution kept as a single woven paragraph deferring detail to the separate literature section, following Ziegler, Romagnoli and Offerman (JEEA 2024), the corpus paper whose paper structure (separate related-literature section) matches ours; the closest-paper differentiation gets its own short paragraph, as in Oexl and Grossman.
4. Roadmap paragraph retained (standard at EE and JEEA; droppable only for EJ).
5. No numbered hypotheses in the intro; the roadmap notes they appear in the design section (none of the six intros numbers hypotheses).
6. Length approximately 1,150 words, at the Experimental Economics norm (about 1,000 to 1,300) and comfortably under the JEEA norm (about 1,900 to 2,000), consistent with "very concise."
