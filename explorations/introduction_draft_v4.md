# Introduction draft, version 4

Revises v3 using the writing guide (explorations/intro_writing_guide.md) and two corrections. Controlling for relative performance is presented as a design feature that does identifying work, not a requirement for testing. The contribution states what the paper delivers, not which literatures it belongs to.

## Draft (drop-in for introduction.tex)

```latex
\section{Introduction} \label{introduction}

P1: Algorithms increasingly make decisions whose consequences fall on someone other
than the person who deploys them. Physicians rely on diagnostic systems when
treating patients, firms let screening software rank job applicants, and
financial advisors draw on algorithmic tools when managing client portfolios.
In each case a human decides whether to put the algorithm in charge, while a
third party bears the consequences. Two questions follow. Does delegating a
decision to an algorithm change the responsibility that others assign to the
person who delegated it? And does the prospect of being held responsible
change the willingness to delegate in the first place? This paper provides
experimental evidence on both.

P2: For delegation between humans, the experimental literature points in a clear
direction. Delegation shifts responsibility. Principals who delegate an
unpopular decision to a human intermediary are punished less for it, feel less
responsible for it, and delegate strategically for precisely this reason
\citep{bartling_shifting_2012, hamman_self-interest_2010,
coffman_intermediation_2011, oexl_shifting_2013}. Recent evidence suggests
that algorithms can inherit the intermediary's role. Delegation to an
algorithm increases dishonesty by obscuring intent
\citep{kobis_delegation_2025}, is used to extract surplus while shedding moral
responsibility \citep{tontrup_strategic_2025}, becomes more attractive when
the moral stakes of the decision are real \citep{hueholt_trusting_2026}, and
shields decision-makers from being held responsible for bad outcomes
\citep{feier_hiding_2022}. On this reading, decision-makers who face potential
punishment should be drawn to the algorithm, and delegation should protect
them when outcomes turn out badly. Yet no existing design varies whether
punishment is possible, so the first prediction, that anticipated punishment
motivates delegation to an algorithm, has not been tested directly.

P3: We test both predictions in a preregistered online experiment with 322
participants, detailed in Section~\ref{design}.\footnote{The experiment was
preregistered at AsPredicted~\#133980, available at
\href{https://aspredicted.org/hs9az8.pdf}{\nolinkurl{aspredicted.org/hs9az8.pdf}}.}
A decision-maker, Player~A, faces a prediction task with monetary consequences
for a matched recipient, Player~B. If her estimate of a person's body weight
from a photograph is accurate, Player~B earns \pounds 5, otherwise \pounds 1.
Player~A's own payoff is unaffected by the prediction. Before the final
prediction, Player~A completes ten incentivized rounds of the same task and
may then either make the consequential prediction herself or delegate it to an
algorithm that succeeds with exactly the accuracy she achieved in those
rounds. Between subjects we vary whether Player~B can reduce Player~A's
earnings at a small cost to himself. In the \textit{Punishment} condition,
Player~B states a punishment for every combination of delegation choice and
outcome. In the \textit{No-Punishment} condition, no sanction is possible.

P4: Two features of this design do the identifying work. First, comparing
delegation across the two conditions turns the motivational question into a
treatment comparison. Everything except the possibility of punishment is held
fixed, so any difference in delegation is attributable to its prospect.
Second, the algorithm is calibrated to each decision-maker individually, and
this is common knowledge between the players. Delegation therefore reveals
nothing about ability. This matters because beliefs about relative performance
are a dominant driver of algorithm use \citep{logg_algorithm_2019,
qin_ai_2025}, and because in pool-calibrated designs, as in
\citet{feier_hiding_2022}, observers may sanction the overconfidence that a
decision not to delegate reveals rather than the decision itself. In our
setting, neither the delegation choice nor the punishment response can be
contaminated by inferences about ability.

P5: Both predictions fail, the first with reversed sign. When punishment is
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

P6: Read together, the two results are puzzling. The possibility of punishment
moves the delegation decision even though no punishment attaches to
delegation, neither in realized sanctions nor in beliefs. We examine several
candidate explanations. Sample composition is ruled out by randomization and
by the robustness of the treatment effect to controls. Effort provides no
reconciliation either. If the threat of punishment led decision-makers to keep
the decision in order to outperform the algorithm, improvement on the final
prediction should concentrate in the \textit{Punishment} condition, whereas it
concentrates where punishment is impossible. What does change across
conditions is who delegates. Under the threat of punishment, better performers
keep the decision to themselves, a pattern that cannot reflect beliefs about
relative ability, which our calibration removes. A preference for producing a
good outcome oneself, or an aversion to delegating decisions whose outcomes
are most uncertain, is consistent with this pattern. Either preference,
however, operates in both conditions and can generate the treatment difference
only if accountability itself activates it. Our design cannot separate these
readings, and we leave the mechanism as an open question.

P7: Our contribution is twofold. First, we provide the first direct test of
whether anticipated punishment motivates delegation to an algorithm, the
motive the responsibility-avoidance literature identifies for human
intermediaries, and we find that it operates with the opposite sign.
Accountability disciplines algorithm use rather than fueling it, and it does
so selectively among the decision-makers most likely to succeed. Second, we
document how third parties assign responsibility for algorithmic delegation
when the delegation choice is uninformative about ability. Punishment then
tracks realized outcomes, and the insulation that delegation appeared to offer
in earlier designs disappears.

P8: Our design most closely resembles \citet{feier_hiding_2022}, who find that
decision-makers are held less responsible for outcomes delegated to an
algorithm than for outcomes of their own actions. Under their session-level
calibration, delegation is informative about self-assessed ability, so
evaluators have something other than the outcome to respond to. Closing this
channel removes the punishment differential. Their treatments vary the type of
delegate under a fixed punishment regime, whereas we hold the delegate fixed
and vary the punishment regime. The two studies thus answer complementary
questions, and ours isolates the motivational role of anticipated punishment.
Section~\ref{literature} positions the paper in the related literature more
broadly.

P9: The environment we study, a prediction under genuine uncertainty made by a
decision-maker with no material stake in the affected party's outcome,
resembles the settings in which algorithmic delegation typically operates in
practice. Within its bounds, our results suggest that holding human users
answerable for algorithmic decisions does more than allocate blame after the
fact. Accountability deterred delegation to an algorithm that was, by
construction, exactly as good as its user, and it deterred the better
performers most. Whether such deterrence is desirable depends on whether the
algorithm outperforms its user. The direction of the behavioral response,
however, is the opposite of what the blame-shifting logic predicts.

P10: The remainder of the paper is organized as follows. Section~\ref{literature}
relates the study to the literature. Section~\ref{design} presents the
experimental design and hypotheses. Section~\ref{results} reports the results
and examines candidate mechanisms. Section~\ref{conclusion} concludes.
```

## Changes from v3, keyed to the writing guide

1. Gap sentence added at the end of paragraph two ("Yet no existing design varies whether punishment is possible..."), the one-sentence specific-gap move (guide, section 2). This replaces the v3 "requirements" paragraph as the motivation for the design.
2. The identification paragraph is reframed from "testing imposes two requirements" to "two features of this design do the identifying work," and moved after the design summary so the reader knows the design before hearing what it identifies (guide, sections 4 and 5). The calibration is now a feature with a stated payoff, not a requirement.
3. Contribution rewritten as a twofold statement of what the paper delivers, with action verbs and no framing around literatures (guide, section 9). The deferral to the literature section is one unobtrusive trailing sentence at the end of the Feier paragraph, the Ziegler device (guide, section 12).
4. The Feier paragraph now opens with the corpus differentiation-sentence shape, "Our design most closely resembles..." (guide, section 8).
5. Design paragraph gains the inline section pointer "detailed in Section~\ref{design}" (guide, section 5, the Oexl move).
6. Results sentences carry the comparison inside the sentence, percentages only (guide, section 6); unchanged from v3 apart from polish.
7. One emphasis structure only ("Both predictions fail, the first with reversed sign"), consistent with the corpus's one-signpost norm (guide, section 6).
