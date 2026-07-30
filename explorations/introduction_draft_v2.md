# Introduction draft, version 2

## Candidate examples for paragraph 1 (pick the ones to list)

1. Medical diagnosis and treatment recommendations (physician relies on a diagnostic system)
2. Consumer credit and lending (banks score loan applicants with statistical models)
3. Hiring (screening software ranks job candidates)
4. Judicial decision support (recidivism risk scores informing bail and sentencing)
5. Financial advice and portfolio management (robo-advisors managing client wealth)
6. Insurance (algorithmic pricing and claims handling)
7. University admissions (algorithmic ranking of applicants)
8. Allocation of public benefits and fraud detection in welfare systems
9. Tax audit selection
10. Content moderation on platforms

The draft below uses examples 1, 2, and 3 as placeholders, marked with brackets.

## Draft (drop-in for introduction.tex)

```latex
\section{Introduction} \label{introduction}

Algorithms increasingly make decisions whose consequences fall on someone other
than the person who deploys them. Physicians rely on diagnostic systems when
treating patients, firms let screening software rank job applicants, financial
advisors draw on algorithmic tools when managing client portfolios, [optional
academic example: and journal editors use algorithms to screen submissions].
In such settings a human
decides whether to hand the decision over to the algorithm, while the outcome
matters to a third party. How others assign responsibility for decisions made
by an algorithm, and how the prospect of being held responsible shapes the
willingness to use algorithms in the first place, are open empirical questions.
This paper addresses both.

The experimental literature on delegation between humans suggests a clear
direction. Delegation shifts responsibility. Principals who delegate an
unpopular decision to an intermediary are punished less for it, feel less
responsible for it, and delegate strategically for precisely this reason
\citep{bartling_shifting_2012, hamman_self-interest_2010,
coffman_intermediation_2011, oexl_shifting_2013}. Recent evidence suggests that
algorithms can take over the intermediary's role. Delegating to an algorithm
increases dishonesty by obscuring intent \citep{kobis_delegation_2025}, is used
to extract surplus while shedding moral responsibility
\citep{tontrup_strategic_2025}, and becomes more attractive when the moral
stakes of the decision are real \citep{hueholt_trusting_2026}.
\citet{feier_hiding_2022} find that decision-makers are held less responsible
for outcomes produced by an algorithm than for outcomes they produced
themselves. Taken together, this work suggests that decision-makers who face
potential sanctions should be drawn to algorithmic delegation, and that
delegation should protect them from punishment.

We examine both questions in a preregistered online experiment with 322
participants. A decision-maker, Player~A, faces a prediction task with monetary
consequences for a matched recipient, Player~B. If her prediction of a person's
body weight from a photograph is accurate, Player~B earns \pounds 5, otherwise
\pounds 1. Player~A's own payoff is unaffected by the prediction. Before the
final prediction, Player~A completes ten incentivized rounds of the same task
and may then either make the consequential prediction herself or delegate it to
an algorithm that is calibrated, at the individual level, to perform exactly as
well as she did in those rounds. Both players know this. Between subjects we
vary whether Player~B can subsequently reduce Player~A's earnings at a small
cost to himself. In the \textit{Punishment} condition, Player~B states a
punishment for every combination of delegation choice and outcome. In the
\textit{No-Punishment} condition, no sanction is possible. The design thus asks,
first, whether the prospect of punishment raises the likelihood that Player~A
delegates to the algorithm and, second, whether delegation lowers the
punishment Player~A receives conditional on the outcome.

Two design features distinguish our experiment from previous work. First, the
algorithm matches each subject's own measured performance, and this is common
knowledge. Beliefs about relative ability are a dominant driver of algorithm
use \citep{logg_algorithm_2019, qin_ai_2025}, and when the algorithm is
calibrated to the subject pool rather than to the individual
\citep[as in][]{feier_hiding_2022}, the delegation choice reveals information
about the decision-maker's confidence in her own ability, so that observers may
sanction perceived overconfidence rather than the decision to delegate itself.
Our calibration removes considerations of relative performance from both sides
of the interaction. Player~A cannot delegate because she believes the algorithm
to be better, and Player~B cannot interpret delegation as a sign of inability.
Second, varying whether punishment is possible identifies whether anticipated
punishment motivates delegation. Prior work on responsibility shifting toward
algorithms observes punishment behavior but does not manipulate its
availability, leaving this motivational question open.

Both answers differ from what the responsibility-shifting literature suggests.
When punishment is possible, 42.5~percent of decision-makers delegate to the
algorithm. When it is not, 59.3~percent do. The prospect of punishment thus
significantly reduces delegation by roughly 17~percentage points, and the
difference is robust to controlling for socio-demographic characteristics as
well as for actual and perceived task performance. Delegation also provides no
protection. Recipients punish bad outcomes more severely than good ones, but
conditional on the outcome, the punishment of delegated and self-made decisions
is statistically indistinguishable. Punishment responds to what happened to the
recipient, not to how the decision was made.

Read together, the two results are puzzling. The prospect of punishment changes
delegation behavior even though no punishment penalty attaches to delegation,
neither in the sanctions recipients impose nor in those decision-makers expect.
Elicited beliefs show that decision-makers overestimate punishment levels
across the board but anticipate no differential between delegated and self-made
decisions. We therefore examine several channels that could produce the
reversal. Sample composition cannot account for it, since randomization is
balanced and the effect survives the corresponding controls. Effort induced by
the prospect of punishment predicts that decision-makers improve on their final
prediction when punishment is possible, whereas improvement concentrates in the
condition without punishment. What changes across conditions is who delegates.
Under the threat of punishment, better performers keep the decision to
themselves, although the individual calibration implies that beliefs about
relative ability cannot be the reason. A preference for producing a good
outcome oneself, or over the uncertainty inherent in the decision, is
consistent with this pattern. Both preferences, however, operate in both
conditions and can explain the treatment difference only if the presence of
accountability activates them, a conjecture our design cannot test. We
therefore present the mechanism as an open question.

Our results contribute to three strands of literature, which
Section~\ref{literature} discusses in detail. To the literature on
responsibility avoidance through delegation, we provide the first test of
whether the prospect of punishment motivates delegation to an algorithm in a
setting with genuine outcome uncertainty and no signal about relative
performance. The motive does not carry over, and the effect runs in the
opposite direction. To the literature on algorithm use, we add the possibility
of punishment as an experimentally manipulated determinant of the decision to
cede a choice to an algorithm, a margin distinct from the more widely studied
willingness to follow algorithmic advice. To the literature on responsibility
attributions for decisions involving algorithms, we contribute a setting in
which the delegation choice carries no information about ability and in which
observers condition sanctions on realized outcomes rather than on algorithm
use.

Our findings also qualify the conclusions of \citet{feier_hiding_2022}, the
study closest to ours. Their decision-makers are held less responsible for
outcomes delegated to an algorithm, whereas ours are not. In their design the
algorithm is calibrated at the session level, so delegation is informative
about self-assessed ability and evaluators have something beyond the outcome to
respond to. Once this channel is closed, the punishment differential
disappears. On the delegation side, their treatments vary the type of delegate
while holding the punishment regime fixed, whereas we hold the delegate fixed
and vary the punishment regime. The two designs therefore answer different
questions, and ours isolates the motivational role of anticipated punishment.

The environment we study resembles the settings in which algorithmic delegation
typically operates, in that the decision involves genuine uncertainty and the
decision-maker has no material stake in the affected party's outcome. Within
the bounds of this setting, our results suggest that regimes holding human
users answerable for algorithmic decisions do more than allocate blame after
the fact. In our data, accountability deterred delegation to an algorithm that
was, by construction, exactly as good as the decision-maker, and it deterred
the better performers most. Whether such deterrence improves or harms outcomes
depends on whether the algorithm is better than its user. The behavioral
response itself, however, runs opposite to the direction the blame-shifting
logic predicts. We note that our evidence comes from a single task on a single
platform with modest stakes and a direct, personal punishment technology.

The remainder of the paper proceeds as follows. Section~\ref{literature}
relates our study to the literature. Section~\ref{design} presents the
experimental design, hypotheses, and identification. Section~\ref{results}
reports the results and examines candidate mechanisms.
Section~\ref{conclusion} concludes.
```
