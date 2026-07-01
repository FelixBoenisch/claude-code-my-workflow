# Draft v2 — subsection "Player B – Punishment behavior"

Reordered to the agreed structure: (1) intro, (2) substantial punishment, (3) bad>good +
good-outcome puzzle as a transition, (4) main result, (5) frequencies/distribution, (6)
conclusion. Ready to drop into `results.tex`.

```latex
\subsection*{Player~B -- Punishment behavior} \label{sec:result2}

We now turn to Player~B's punishment behavior in the \textit{Punishment} condition, where
the punishment decision was real and payoff-relevant.

Player~Bs make active and costly use of the sanction: average punishment is positive in
every one of the four (delegation, outcome) cells of the strategy method
(Figure~\ref{fig:punishment}).

Punishment is far from random, however. Player~Bs punish low-payoff outcomes markedly more
than high-payoff outcomes---a within-subject average difference of about $\pounds 0.21$
($p<0.01$)---which reassures us that the measure reflects a deliberate response to what
happened rather than noise. Yet punishment after a \textit{good} outcome is itself
non-trivial,\footnote{\citet{coffman_intermediation_2011} likewise documents non-trivial
punishment in settings where the decision-maker's action could not have been improved upon.}
which raises a natural question: are Player~Bs reacting not only to the outcome but to the
\textit{delegation choice itself}? If delegating---rather than deciding oneself---were
regarded as blameworthy per se, delegated decisions should be punished differently from
self-made ones, whatever the outcome. We test precisely this.

They are not. Holding the outcome fixed, Player~A is punished no differently for delegating.
After a high payoff, average punishment is $\pounds 0.329$ for delegated versus $\pounds 0.297$
for self-made decisions; after a low payoff, $\pounds 0.482$ versus $\pounds 0.553$. The
low-payoff gap---the cell that H2 concerns---runs in the predicted direction but is small and
statistically insignificant ($\pounds 0.071$; paired $t$-test $p=0.13$, Wilcoxon signed-rank
$p=0.54$). The regression in Table~\ref{tab:reg_punishment} tells the same story: punishment
loads overwhelmingly on the outcome (bad-outcome coefficient $0.256$, $p<0.01$), the main
effect of delegation is essentially zero, and the \textit{Delegated}~$\times$~\textit{Bad
outcome} interaction---the within-subject differential that would capture any insulation---is
only $-0.103$ and borderline significant ($p=0.08$). Because each Player~B is observed in all
four cells, any stable characteristic of the punisher---including her belief about Player~A's
\textit{absolute} performance---is differenced out and cannot, by construction, generate these
within-subject contrasts; consistent with this, that belief is essentially uncorrelated with
chosen punishment in every cell ($|r|\le 0.03$, all $p>0.8$).

\begin{figure}[!htbp]
    \centering
    \caption{Player~B punishment by delegation and outcome scenario}
    \includegraphics[width=0.65\linewidth]{figures/punishment.png}
    \label{fig:punishment}
    \begin{minipage}{0.85\linewidth}
    \footnotesize
    \textit{Note:} For each of the four (delegation, outcome) cells of the strategy method, the
    figure reports the average punishment chosen by Player~B (left $y$-axis, in pounds; error
    bars are standard errors of the mean) and the share of Player~Bs imposing non-zero
    punishment (right $y$-axis, in percent), in the \textit{Punishment} condition (full sample
    $n=80$, passers $n=67$). The full sample is shown at full opacity and the attention-check
    passers are overlaid at lower opacity. Hypothetical punishment in the \textit{No-Punishment}
    condition is reported in Appendix Figure~\ref{fig:punishment_hypothetical}.
    \end{minipage}
\end{figure}

The null is equally clear on the extensive margin and in the distribution of punishment. The
share of Player~Bs imposing \textit{any} punishment is indistinguishable between delegated and
self-made decisions within each outcome (Figure~\ref{fig:punishment}, right axis), and
$45.0\%$ of Player~Bs punish in none of the four scenarios---so the cell averages reflect a
punishing minority rather than light, diffuse sanctioning.\footnote{Among the $44$ Player~Bs
who punish in at least one scenario, sanctions are mostly non-trivial, so the costly option is
used as a substantive penalty rather than a token gesture.} The conclusion is unchanged when we
restrict to subjects who passed the attention check (Table~\ref{tab:reg_punishment},
column~2).\footnote{Restricting to passers leaves the result intact: the low-payoff gap is
$\pounds 0.077$ (paired $t$-test $p=0.15$), and the interaction remains small and insignificant
($-0.078$).}

\medskip
\noindent\textbf{Result~2.} \textit{Player~A cannot avoid punishment by delegating the decision
to the algorithm.}
\medskip

\input{../tables/reg_punishment.tex}

In our setting, then, Player~A cannot shield herself from punishment by delegating to the
algorithm, nor is she punished more for doing so; punishment is determined almost entirely by
the realised outcome. This bears directly on Result~1: a delegation pattern driven by
punishment-avoidance would require Player~B to punish delegated decisions less---which they do
not.
```
