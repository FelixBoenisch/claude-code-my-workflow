# Introduction draft — Algorithms and Responsibility

## Structure (rationale)

Target: top general-interest / top experimental field journal. The intro follows the standard arc, compressed into ~2.5 pages:

1. **Hook + question** (¶1–2): real-world stakes → the behavioral question (does accountability push people toward or away from algorithms?) → the sharp prediction inherited from the human-delegation literature.
2. **Design** (¶3–4): what we do in one paragraph; then the three identification-relevant design features (individual-level calibration, role separation, No-Punishment arm) — each tied to the confound it removes.
3. **Findings** (¶5–6): Result 1 (the reversal, with magnitudes), Result 2 (no insulation; beliefs consistent with it). Findings before mechanisms, numbers up front.
4. **Mechanism triage** (¶7): what the data rule out, what pattern remains, candid statement that the remaining candidates cannot be separated by this design.
5. **Contribution** (¶8–9): placement in the three strands (mirroring the literature section) + explicit differentiation from Feier et al., including the reconciliation.
6. **Relevance + scope** (¶10): policy reading with explicit caveats.
7. **Roadmap** (¶11).

Conventions respected: no mechanism is declared "the" explanation (process ownership presented as one candidate); H2 null reported as a null with power caveat; all numbers match `results.tex`.

## Draft (drop-in for introduction.tex)

```latex
\section{Introduction} \label{introduction}

Algorithms increasingly make decisions whose consequences fall on someone other
than the person who deploys them. A physician follows a diagnostic system's
assessment of a patient, a loan officer relies on a credit-scoring model, a
manager lets screening software rank applicants. In each case a human decides
whether to put the algorithm in charge, the algorithm's output determines a
third party's outcome, and --- increasingly by regulation and organizational
practice --- the human remains accountable for the result. This combination
raises a basic behavioral question: does being held accountable make people
more willing, or less willing, to hand a decision over to an algorithm?

A long-standing experimental literature on delegation between humans delivers a
sharp prediction. Delegation shifts responsibility. Principals who delegate an
unpopular decision to an intermediary are punished less for it, feel less
responsible for it, and delegate strategically for precisely this reason
\citep{bartling_shifting_2012, hamman_self-interest_2010,
coffman_intermediation_2011, oexl_shifting_2013}. A recent strand suggests that
algorithms can inherit the intermediary's role: delegating to an AI increases
dishonesty by obscuring intent \citep{kobis_delegation_2025}, is used to
extract surplus while shedding moral responsibility \citep{tontrup_strategic_2025},
and is chosen more often precisely when moral stakes become real
\citep{hueholt_trusting_2026}. In the study closest to ours,
\citet{feier_hiding_2022} find that principals are held less responsible for
outcomes produced by an algorithm they chose than for outcomes they produced
themselves. On this reading, accountability should push decisions toward
algorithms: when punishment looms, ``the algorithm did it'' is a shield worth
buying.

We test this prediction directly. In a preregistered online experiment
($N=322$; $161$ in each role), a decision-maker (Player~A) faces a prediction
task with real consequences for a matched recipient (Player~B): if her
prediction of a person's body weight from a photograph is accurate, Player~B
earns \pounds 5, otherwise \pounds 1. Player~A's own payoff is unaffected.
Before the final prediction, Player~A completes ten incentivized rounds of the
same task and may then either make the consequential prediction herself or
delegate it to an algorithm that is calibrated, at the individual level, to
perform exactly as well as she did --- a fact known to both players. Between
subjects we vary a single feature: in the \textit{Punishment} condition,
Player~B can subsequently reduce Player~A's earnings at a cost to himself,
conditional on both the delegation choice and the realized outcome (elicited
via the strategy method); in the \textit{No-Punishment} condition, no sanction
is possible.

Three design features carry the identification. First, calibrating the
algorithm to each subject's own measured performance --- and making this common
knowledge --- removes beliefs about relative ability, otherwise a dominant
driver of algorithm use \citep{logg_algorithm_2019, qin_ai_2025}, from both
sides of the market: Player~A cannot delegate because she thinks the algorithm
is better, and Player~B cannot read delegation as a confession of inability. In
\citet{feier_hiding_2022}, whose algorithm is calibrated at the session level,
delegation carries exactly this signal, and evaluators may sanction perceived
overconfidence rather than responsibility-taking. Second, delegators and
evaluators are disjoint subject pools, so punishment is not contaminated by the
evaluator's own delegation experience. Third, and unlike prior work on
algorithmic responsibility-shifting, the \textit{No-Punishment} arm lets us
identify whether the \emph{prospect} of punishment itself motivates delegation
--- the motivational claim at the heart of the responsibility-avoidance
literature --- rather than only how observers respond to it.

Our first finding reverses the prediction. When punishment is possible,
$42.5\%$ of decision-makers delegate to the algorithm; when it is not,
$59.3\%$ do (two-sided $p=0.033$). The prospect of punishment thus
\emph{reduces} delegation by roughly $17$~percentage points, an effect that is
robust to controlling for socio-demographics and for actual and perceived task
performance (average marginal effects between $16.5$ and $19.2$~percentage
points). Far from reaching for the algorithmic shield, decision-makers respond
to accountability by keeping the decision in their own hands.

Our second finding helps explain why the shield is not worth reaching for ---
and deepens the puzzle. Recipients punish outcomes, not delegation: conditional
on a bad outcome, average punishment of delegated and self-made decisions is
statistically indistinguishable (\pounds 0.482 versus \pounds 0.553; the
differential that would capture insulation from punishment is marginal at
best), and the same holds after good outcomes. Decision-makers' elicited
beliefs anticipate this correctly: while they overestimate punishment levels in
every scenario, they expect no punishment penalty (or discount) for delegating
as such, conditional on the outcome. Anticipated differential punishment
therefore cannot account for the treatment difference in delegation --- the
prospect of punishment changes behavior even though neither actual nor
expected punishment attaches to the delegation choice itself.

What does account for it? We can rule out several candidates. The reversal is
not a composition artifact: randomization is balanced on observables,
performance, and confidence, and the effect survives the corresponding
controls. It is not punishment-induced effort: if accountability spurred
decision-makers to try to outperform their algorithm, improvement on the final
prediction should concentrate in the \textit{Punishment} condition, whereas it
concentrates where punishment is impossible. What the data do show is a shift
in \emph{who} delegates: under the threat of punishment, it is the
better-performing decision-makers who keep the decision for themselves
(delegators score $2.47$ of ten versus $3.06$ in the \textit{No-Punishment}
condition), a pattern that cannot reflect beliefs about relative ability, which
our calibration neutralizes by construction. Preferences over being the
proximate cause of a good outcome (``process ownership'') and preferences over
the uncertainty inherent in the decision are both consistent with this
pattern, but both are treatment-independent on their face and can explain the
reversal only if activated by accountability itself --- a conjecture our
design, in which punishment and accountability coincide by construction,
cannot test. We present the mechanism as an open question and the heterogeneity
evidence as exploratory.

Our results contribute to three literatures, which Section~\ref{literature}
reviews in detail. First, to the literature on responsibility avoidance
through delegation \citep{bartling_shifting_2012, hamman_self-interest_2010,
coffman_intermediation_2011, oexl_shifting_2013, steffel_passing_2016}, we
provide what is, to our knowledge, the first clean test of whether the
prospect of punishment motivates delegation to an \emph{algorithm} in a
setting with genuine outcome uncertainty and no relative-performance signal.
The answer is no --- the motive not only fails to extend, it reverses.
Second, to the literature on algorithm use \citep{dietvorst_algorithm_2015,
logg_algorithm_2019, irlenbusch_human_2026}, we add accountability as a
treatment-manipulated moderator of the delegation margin --- distinct from
advice-taking --- and show that it suppresses algorithm use selectively among
abler decision-makers, complementing survey-based evidence that the propensity
to shift blame predicts delegation to algorithms in financial decisions
\citep{holzmeister_delegation_2023}. Third, to the literature on
responsibility attributions for algorithm-assisted decisions
\citep{gogoll_rage_2018, bigman_people_2018, feier_hiding_2022,
chevrier_algorithm_2024}, we contribute an outcome-based benchmark: once the
delegation decision carries no information about ability, third parties
condition sanctions on realized outcomes rather than on the use of the
algorithm.

The contrast with \citet{feier_hiding_2022} is instructive rather than
contradictory. Their decision-makers are held less responsible for
algorithm-delegated outcomes; ours are not. But in their session-level
calibration, delegation is informative about the principal's self-assessed
ability, so third parties have something beyond the outcome to sanction. Our
individual-level calibration closes that channel, and the punishment
differential disappears with it --- consistent with a signal-extraction
reading of their result. On the delegation side, their design holds the
punishment regime fixed and varies the delegate; ours holds the delegate fixed
and varies the punishment regime. The two designs thus answer different
questions, and ours isolates the motivational margin their setup leaves open.

The setting we study --- a prediction under genuine uncertainty, made by a
decision-maker with no material stake in the affected party's outcome --- is
deliberately the environment in which real-world algorithmic delegation
typically operates, from diagnosis to forecasting to screening. Within the
bounds of this setting, the results carry a cautionary implication for
accountability-based governance of algorithmic decision-making. Frameworks
that hold human users answerable for algorithm-mediated outcomes are usually
conceived as allocating responsibility after the fact. Our evidence suggests
they also shape adoption before the fact: accountability deterred delegation
to an algorithm that was, by construction, exactly as good as the human ---
and deterred it most among the more able decision-makers. Whether this
discipline is desirable depends on whether the algorithm is in fact better or
worse than its user; our point is that the behavioral response exists and runs
opposite to what the blame-shifting logic predicts. At the same time, we are
explicit about scope: the evidence comes from one task, one platform, and
modest stakes, and the punishment technology we study is direct and personal
rather than institutional.

The remainder of the paper proceeds as follows. Section~\ref{literature}
relates our study to the literature. Section~\ref{design} presents the
experimental design, hypotheses, and identification. Section~\ref{results}
reports the results and examines candidate mechanisms.
Section~\ref{conclusion} concludes.
```
