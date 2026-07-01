# Draft — subsection "Player B – Punishment behavior"

Updated to the level-only 2-column `reg_punishment` table and edited for tone/concision. Ready to drop into `results.tex` (replaces lines 28–59).

```latex
\subsection*{Player~B -- Punishment behavior} \label{sec:result2}

We now turn to Player~B's punishment behavior, beginning with the \textit{Punishment}
condition, in which the punishment decision was real and payoff-relevant.

Punishment is substantial across all four (delegation, outcome) cells of the strategy
method and is governed first and foremost by the realised outcome
(Figure~\ref{fig:punishment}, panel~A): Player~Bs punish low-payoff outcomes more than
high-payoff outcomes, by a within-subject average of roughly $\pounds 0.21$ ($p<0.01$).
Two further features stand out. First, punishment is far from universal---$45.0\%$ of
Player~Bs punish in none of the four scenarios, while the remainder impose the costly
sanction at non-trivial levels.\footnote{Among the $44$ Player~Bs who punish in at least
one scenario, sanctions are mostly non-trivial, so the costly option is used as a
substantive penalty rather than a token gesture.} Second, punishment is appreciable even
after a \textit{good} outcome, suggesting that some Player~Bs sanction the delegation
\textit{choice} itself rather than the outcome alone.\footnote{\citet{coffman_intermediation_2011}
likewise documents non-trivial punishment in settings where the decision-maker's action
could not have been improved upon. Positive punishment after a good outcome therefore need
not reflect noise: Player~Bs may form ex-post views about whether the delegation choice was
appropriate, independent of the realised outcome.}

\begin{figure}[!htbp]
    \centering
    \caption{Player~B punishment by delegation and outcome scenario}
    \includegraphics[width=0.95\linewidth]{figures/punishment.png}
    \label{fig:punishment}
    \begin{minipage}{0.95\linewidth}
    \footnotesize
    \textit{Note:} Both panels report, for each of the four (delegation, outcome) cells of
    the strategy method, the average punishment chosen by Player~B (left $y$-axis, in
    pounds; error bars are standard errors of the mean) and the share of Player~Bs choosing
    non-zero punishment (right $y$-axis, in percent). In each panel, the full sample is
    shown at full opacity and the attention-check passers are overlaid at lower opacity.
    Panel~A reports actual punishment in the \textit{Punishment} condition (full sample
    $n=80$, passers $n=67$). Panel~B reports hypothetical punishment in the
    \textit{No-Punishment} condition (full sample $n=81$, passers $n=68$), where Player~Bs
    answered the same questions but could not impose punishment in practice.
    \end{minipage}
\end{figure}

The question central to H2 is whether, holding the outcome fixed, Player~A is punished
differently when she delegates. She is not. After a high payoff, average punishment is
$\pounds 0.329$ for delegated versus $\pounds 0.297$ for self-made decisions; after a low
payoff, $\pounds 0.482$ versus $\pounds 0.553$. The low-payoff gap---the cell that H2
concerns---runs in the predicted direction but is small and statistically insignificant
($\pounds 0.071$; paired $t$-test $p=0.13$, Wilcoxon signed-rank $p=0.54$). The regression
in Table~\ref{tab:reg_punishment} delivers the same verdict: punishment is overwhelmingly a
function of the outcome (bad-outcome coefficient $0.256$, $p<0.01$), the main effect of
delegation is essentially zero, and the \textit{Delegated}~$\times$~\textit{Bad outcome}
interaction---the within-subject differential that would capture any insulation---is only
$-0.103$ and borderline significant ($p=0.08$).

Because each Player~B is observed in all four cells, any stable characteristic of the
punisher---including her belief about Player~A's \textit{absolute} performance---is
differenced out and cannot, by construction, generate these within-subject contrasts.
Consistent with this, Player~B's belief about Player~A's score is essentially uncorrelated
with chosen punishment in every cell ($|r|\le 0.03$, all $p>0.8$).

The same null appears on the extensive margin: the share of Player~Bs imposing any
punishment is indistinguishable between delegated and self-made decisions
(Figure~\ref{fig:punishment}, panel~A, right axis), and the conclusion is unchanged when we
restrict to subjects who passed the attention check (Table~\ref{tab:reg_punishment},
column~2).\footnote{Restricting to attention-check passers leaves the result intact: the
low-payoff gap is $\pounds 0.077$ (paired $t$-test $p=0.15$), and the interaction remains
small and insignificant ($-0.078$; Table~\ref{tab:reg_punishment}, column~2).} Player~B
thus punishes delegated decisions neither substantially less harshly nor substantially less
often.

\medskip
\noindent\textbf{Result~2.} \textit{Player~A cannot avoid punishment by delegating the
decision to the algorithm.}
\medskip

\input{../tables/reg_punishment.tex}

In our setting, then, Player~A cannot shield herself from punishment by delegating to the
algorithm, nor is she punished more for doing so; punishment is determined almost entirely
by the realised outcome. This bears directly on Result~1: a delegation pattern driven by
punishment-avoidance would require Player~B to punish delegated decisions less---which they
do not.
```
