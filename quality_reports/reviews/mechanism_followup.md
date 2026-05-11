---
title: "Follow-up: mechanism-section concrete rewrites + new appendix/main figures"
date: "2026-05-11"
scope: "results.tex lines 119–173"
---

# What I produced in this round

**New scripts (SSOT-compliant):**
- [`scripts/python/23_beliefs_vs_performance.py`](../../scripts/python/23_beliefs_vs_performance.py)
  → `figures/beliefs_vs_performance.png` — six-panel appendix figure (C5b).
- [`scripts/python/24_performance_by_delegation.py`](../../scripts/python/24_performance_by_delegation.py)
  → `figures/performance_by_delegation.png` — main-text figure splitting
  performance distribution by delegation status (C7).

**Untouched:** `results.tex` (per instruction); the existing
`07_performance.py` and `figures/performance.png` (C7 lives under a new
name as you asked).

All LaTeX snippets below are paste-ready. Insertion points are referenced
to the current numbering of [results.tex](../../manuscript/results.tex).

---

## C2 — Feier et al. contrast (revised after your correction)

**Your correction.** In Feier et al., the algorithm's population performance
distribution is matched to the humans' population distribution, so an
individual human in the upper part of the distribution rationally thinks
she is better than the algorithm in expectation; a low performer
rationally thinks she is worse. That generates an EU-rational
performance→delegation gradient. In our design, each individual
Player~A has been informed she and her algorithm perform equally well at
the *individual* level, so EU predicts \emph{no} performance gradient
at all — the gradient we observe in \textit{Punishment} therefore cannot
be a rational response to an expected-utility comparison.

**Suggested insertion** (place as a footnote on the last sentence of
[results.tex:120](../../manuscript/results.tex#L120), or as a one-sentence
addition between the heterogeneity paragraph and the process-ownership
paragraph at line 124):

```latex
This contrasts with the setting of \citet{feier_hiding_2022}, in which the
algorithm's performance distribution is matched to the human distribution
at the \textit{population} level: a high-performing subject who recognises
her position in that distribution rationally believes she outperforms the
algorithm in expectation and a low-performing one rationally believes the
reverse, producing an expected-utility-rational performance-to-delegation
gradient. In our design, performance is equalised at the \textit{individual}
level and is common knowledge, so expected utility predicts no gradient at
all; the pattern documented here in the \textit{Punishment} condition is
therefore informative about preferences rather than about beliefs over
relative ability.
```

---

## C3 — Specific rewrite for lines 124–126

The current line-124 paragraph is good (it implements the third-party-stake
framing). Line 126 is now redundant with line 124's first sentence
("Player~As who have a higher chance of producing the high payoff …
prefer to bring about that good outcome themselves"). I'd replace line 126
with the version below, which keeps the "this is process ownership, not
blame avoidance" disambiguation and adds an empirical lever: blame
avoidance would predict the *opposite* heterogeneity gradient (loading on
worse performers, who are more likely to produce a bad outcome).

**Suggested replacement for [results.tex:126](../../manuscript/results.tex#L126):**

```latex
The operative motive is the desire to be the proximate cause of a
\textit{good} outcome --- not the avoidance of being the proximate cause
of a bad one. A blame-avoidance variant would also predict less delegation
in the \textit{Punishment} arm, but its heterogeneity gradient should run
in the opposite direction: it would load most strongly on
\textit{worse}-performing Player~As, whose conditional probability of
producing a bad outcome for Player~B is higher. The data show the opposite
gradient.
```

This keeps the figure placement (between the two paragraphs) intact and
gives the reader a discriminating prediction that distinguishes process
ownership from a generic blame story.

---

## C5a / C5b — rigorous treatment for the appendix

### Numerical results (for an appendix table or a single sentence in the body)

**C5a (within-subject test that the delegation penalty for the good
outcome exceeds that for the bad outcome).** Define
$\Delta^{\text{good}} = \text{belief\_del\_good} - \text{belief\_nodel\_good}$
and similarly for the bad outcome. We test
$H_0: \Delta^{\text{good}} - \Delta^{\text{bad}} = 0$ by a one-sample
paired $t$-test on the difference of differences:

| Sample                    |  $\bar{\Delta}^{\text{good}}$ |  $\bar{\Delta}^{\text{bad}}$ |  diff-of-diff |  $t$  |   $p$  |
|---------------------------|------------------------------:|-----------------------------:|--------------:|------:|-------:|
| Punishment, full (n=80)   | +0.018                        | −0.057                       | +0.075        | +0.99 | 0.325  |
| Punishment, passers (n=61)| +0.017                        | −0.068                       | +0.085        | +0.89 | 0.376  |

So Player~A does *not* expect a relatively larger punishment penalty for
delegation in the good-outcome state than in the bad-outcome state.

**C5b (belief independence from task performance).** Pearson correlations
of each belief variable with `overall_score` in the
*Punishment / passers* sample (n=61):

| Variable             | Pearson $r$ |  $p$   |
|----------------------|------------:|-------:|
| belief\_del\_good    | $-0.208$    | 0.107  |
| belief\_nodel\_good  | $-0.117$    | 0.369  |
| belief\_del\_bad     | $+0.048$    | 0.713  |
| belief\_nodel\_bad   | $-0.079$    | 0.543  |
| nodel\_del\_good     | $+0.117$    | 0.367  |
| nodel\_del\_bad      | $-0.153$    | 0.239  |

None significant; the closest to a relationship is
`belief_del_good` ($r = -0.21$, $p=0.11$). Crucially, the two
*belief differences* — the regressors that actually enter
`tab:reg_belief_specs` — are both null
($r=+0.12$, $p=0.37$; $r=-0.15$, $p=0.24$).

### Suggested appendix subsection (paste-ready)

```latex
\subsection{Punishment beliefs and task performance}
\label{appendix:beliefs_vs_performance}

In the main text we claim that Player~A's punishment beliefs do not vary
systematically with her own task performance, and that Player~As do not
expect a relatively larger punishment penalty for delegation in
good-outcome states than in bad-outcome states. This appendix documents
the supporting analyses, restricted to the \textit{Punishment} condition
and attention-check passers ($n=61$) for consistency with the main
within-subject regression.

\paragraph{Difference-of-differences in the expected delegation penalty.}
Define the expected punishment penalty for delegation in each outcome as
$\Delta^{\text{good}} \equiv \beta^{\text{del,high}} - \beta^{\text{self,high}}$
and analogously $\Delta^{\text{bad}}$. A within-subject paired $t$-test
of $H_0: \Delta^{\text{good}} = \Delta^{\text{bad}}$ yields
$\bar\Delta^{\text{good}}-\bar\Delta^{\text{bad}} = +0.075$
($t=+0.99$, $p=0.325$) on the full Punishment sample and
$+0.085$ ($t=+0.89$, $p=0.376$) on the passers. We cannot reject
equality of the two delegation penalties.

\paragraph{Independence of beliefs from task performance.}
Figure~\ref{fig:beliefs_vs_performance} plots each of the four
cell-level punishment beliefs and the two outcome-conditional belief
differences against Player~A's task performance in the first ten
rounds. Pearson correlations are reported in each panel; all six are
small ($|r| \leq 0.21$) and statistically insignificant at conventional
levels. In particular, the two belief differences that enter the
regression in Table~\ref{tab:reg_belief_specs} are uncorrelated with
task performance ($r=+0.12$, $p=0.37$ for the good-outcome difference;
$r=-0.15$, $p=0.24$ for the bad-outcome difference). The within-subject
correlation between beliefs and delegation reported in the main text
therefore cannot be attributed to a shared dependence on task
performance.

\begin{figure}[!htbp]
    \centering
    \caption{Player~A punishment beliefs are independent of task performance}
    \includegraphics[width=\linewidth]{figures/beliefs_vs_performance.png}
    \label{fig:beliefs_vs_performance}
    \begin{minipage}{0.95\linewidth}
    \footnotesize
    \textit{Note:} Each panel plots one belief variable against
    Player~A's score in the first ten rounds, restricted to the
    \textit{Punishment} condition and attention-check passers ($n=61$).
    Points are jittered horizontally for legibility. Lines are OLS fits;
    annotations report Pearson $r$ and its two-sided $p$-value. Top row:
    good-outcome beliefs (delegation, self, and the difference
    \textit{self}~$-$~\textit{delegation}). Bottom row: low-outcome beliefs.
    \end{minipage}
\end{figure}
```

Footnote text to drop into the main body (e.g., on the relevant clause at
[results.tex:139](../../manuscript/results.tex#L139)):

```latex
\footnote{See Appendix~\ref{appendix:beliefs_vs_performance} for the
supporting numerical and graphical evidence: a within-subject test that
$\Delta^{\text{good}}=\Delta^{\text{bad}}$ ($p=0.376$ in the passers
sample), and all six correlations between Player~A's punishment beliefs
and her task performance ($|r|\leq 0.21$, none significant at
conventional levels).}
```

---

## C7 — Performance and confidence by treatment × delegation

The figure now mirrors the layout of `figures/performance.png` (top
bars-plus-KDE panel + boxplot strips below) and adds the
delegation-status split within each treatment. Two columns, one per
treatment; within each column, the actual-performance histogram is
shown in blue (delegators dark, non-delegators light) and the
weighted-average performance belief is overlaid as a KDE in magenta
(delegators solid, non-delegators dashed). Four boxplot strips below
each panel report the same four series, in the order
\textit{Perf., del.} / \textit{Perf., non-del.} / \textit{Conf., del.} /
\textit{Conf., non-del.}

Two facts the figure makes visible at a glance:

1. **In Punishment, actual performance discriminates between delegators
   and non-delegators (mean 2.38 vs.\ 3.00) but perceived performance
   essentially does not (mean 4.69 vs.\ 4.71).** Delegators in Punishment
   are not subjects who *believe* they are worse than the algorithm; they
   are subjects who *are* worse, even though their confidence does not
   reflect it. This is consistent with the process-ownership story (the
   gradient is in the objective probability of producing a good outcome,
   not in self-assessed ability).
2. **In No-Punishment, actual performance does not discriminate (means
   2.98 vs.\ 3.13) and perceived performance is mildly higher among
   non-delegators (5.33 vs.\ 4.85).** No gradient is required to
   rationalise the higher delegation share — the channel that operates
   in Punishment is off.

**Suggested figure environment** (replaces the existing comment at
[results.tex:158](../../manuscript/results.tex#L158); could sit right
after the performance-balance paragraph at line 145 or alongside the
delegator-performance footnote at line 164):

```latex
\begin{figure}[!htbp]
    \centering
    \caption{Performance and confidence distributions by treatment and delegation choice}
    \includegraphics[width=0.98\linewidth]{figures/performance_by_delegation.png}
    \label{fig:performance_by_delegation}
    \begin{minipage}{0.95\linewidth}
    \footnotesize
    \textit{Note:} Restricted to attention-check passers. Within each
    treatment, the top panel shows the share of Player~As at each
    first-ten-rounds score, separately for those who delegated (dark
    blue) and those who did not (light blue), with the weighted-average
    performance belief overlaid as a KDE (delegators solid magenta,
    non-delegators dashed pink). Boxplot strips below the top panel
    report the same four series. In the \textit{Punishment} condition,
    actual performance discriminates between delegators and
    non-delegators (means $2.38$ vs.\ $3.00$) while perceived performance
    does not (means $4.69$ vs.\ $4.71$). In the \textit{No-Punishment}
    condition, neither actual nor perceived performance discriminates
    (actual: $2.98$ vs.\ $3.13$; perceived: $4.85$ vs.\ $5.33$). The
    additional delegators in \textit{No-Punishment} therefore come
    disproportionately from the middle and upper portion of the actual
    performance distribution.
    \end{minipage}
\end{figure}
```

The figure caption already states the punch line; the footnote at
[results.tex:164](../../manuscript/results.tex#L164) can stay verbatim or
be lightened to a forward reference (e.g., "see
Figure~\ref{fig:performance_by_delegation} for the corresponding
distributions").

---

## C9 — Conclusion paragraph (M1–M4 in your order, no experimenter demand)

**Suggested replacement for [results.tex:170](../../manuscript/results.tex#L170):**

```latex
In sum, we considered four candidate mechanisms behind Result~1.
M1 (anticipated differential punishment) is inconsistent with
Player~A's elicited beliefs: she does not expect a relatively larger
punishment penalty for delegation in the good-outcome state than in
the bad-outcome state (Section~\ref{sec:beliefs};
Appendix~\ref{appendix:beliefs_vs_performance}). M2 (ex-ante differences
in task performance between conditions) is inconsistent with the
balance documented in Figure~\ref{fig:performance}: average
performance over rounds~1--10 is statistically indistinguishable
across treatments. M3 (extra effort to outperform the algorithm under
the threat of punishment) is inconsistent with the round-11 effort
data, which run in the opposite direction: it is in the
\textit{No-Punishment} condition, not in the \textit{Punishment}
condition, that non-delegators improve from rounds 1--10 to the
final prediction. M4 (process ownership of the outcome) is the only
candidate the data support: the negative performance--delegation
gradient in \textit{Punishment} and the absence of any comparable
gradient in \textit{No-Punishment} (Figure~\ref{fig:performance_delegation_scatter},
Figure~\ref{fig:performance_by_delegation}) jointly indicate that
Player~As who are likely to deliver the high payoff to Player~B
prefer to do so personally, but only when Player~B's payoff is at
meaningful third-party stake. We are explicit that the supporting
evidence consists of a single heterogeneity pattern in a 60-subject
sub-sample and a comparison of delegator success rates; the pattern is
the most consistent reading of the data we have, but not a confirmed
mechanism. A direct test would require a treatment that varies process
ownership while holding the punishment possibility fixed --- for
example, an arm in which the algorithm is presented as Player~A's own
``tool'' rather than as a separate agent.
```

If you'd rather drop the limitations sentences at the end and have a
shorter "In sum", keep up through "...meaningful third-party stake." —
the punch line of the section is the M1-M3-ruled-out / M4-survives
verdict, and the limitations can live in the Conclusion section instead.
