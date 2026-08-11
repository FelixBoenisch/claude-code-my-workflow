# Redraft: "Anticipated differential punishment" block (results.tex, lines 75-125)

Two versions. **Version A** (2026-08-08) keeps the original order (caveats before the evidence) and only compresses. **Version B** (2026-08-10, below) additionally reorders per the follow-up discussion: elicitation → aggregate null → margin evidence → reservations last, so the block closes on the limited weight of the belief measure, which the signaling paragraph later relies on. The suggested table note at the bottom applies to both versions.

Goal. Keep the block directed at the mechanism question. The mechanism test is the *average* belief difference (zero, so anticipation cannot explain Result 1) and it is settled by the figure paragraph. The regression material stays, but in a supporting role: the five-column walkthrough moves into the table note (which the writing guide wants self-contained anyway), and the estimates paragraph shrinks to the headline number. All five columns stay in the table, as agreed.

One discovery supporting the compression. The current footnote to the regression paragraph ("The two underlying belief measures compare expected punishment...") duplicates a sentence the generated table note already contains almost verbatim ("Belief differences are within-subject (no delegation) − (delegation)..."). The walkthrough was documenting the table twice.

## What moves where

| Current | Redraft |
|---|---|
| ¶ "The most natural candidate..." (line 75) | Unchanged |
| ¶ Elicitation + caveats (line 80) | Unchanged |
| ¶ Two patterns + figure (line 82) | Unchanged (this is the mechanism verdict) |
| ¶ Five-column walkthrough (line 95) | Compressed to four sentences; details to the table note |
| Footnote: belief-difference construction | Deleted (already in the table note) |
| Footnote: orthogonality of the two differences | Moved to the table note |
| "(the statistic that enters an expected-utility calculation)" | Dropped |
| ¶ Estimates (line 102) | Compressed; Column (5) numbers to a footnote |
| `\hl` at line 104 (fold in performance/socio-demographics) | Recommend deleting per earlier discussion; performance has its own paragraph below |
| ¶ "Taken together..." (line 121) + Result 3 | Unchanged |

## Version A — redrafted LaTeX (original order, compressed)

```latex
\paragraph{Anticipated differential punishment.} The most natural candidate is anticipation of differential punishment. Player~A may expect a delegated decision to be punished more harshly than a self-made one, and delegate less in response. Such an expectation would, for example, be consistent with evidence that observers view the delegation of morally consequential decisions to machines relatively critically \citep[e.g.,][]{gogoll_rage_2018, bigman_people_2018, jauernig_people_2022, bonnefon_moral_2024}.

After the delegation decision but before learning the outcome, we elicited Player~A's beliefs about Player~B's punishment in each of the four (delegation, outcome) scenarios. We interpret the belief measure with caution for several reasons. First, the elicitation was unincentivized and took place after the delegation decision, so reports may reflect post-hoc rationalization rather than the beliefs that drove the choice. Second, hypotheticality may introduce additional noise as only two of the four scenarios could still materialize after Player~A's delegation decision in the \textit{Punishment} condition, and all four were purely hypothetical in the \textit{No-Punishment} condition. Anticipated punishment can affect behavior only where punishment is possible. We therefore focus in the analysis of punishment beliefs on the \textit{Punishment} condition.

Two patterns emerge (Figure~\ref{fig:realized_vs_anticipated}). First, Player~As, on average, substantially overestimate punishment in every scenario. Second, Player~As expect essentially the same punishment for delegated and self-made decisions, conditional on the outcome, correctly anticipating the pattern in Player~B's actual punishment behavior (Result~2).\footnote{The expected punishment penalty for delegation is small and statistically indistinguishable from zero in both outcome states, and a within-subject test finds no asymmetry between the two.} Thus, measured beliefs provide no support for a punishment anticipation mechanism for Result~1.\footnote{The same holds for the fully hypothetical beliefs elicited in the \textit{No-Punishment} condition, which closely track those in the \textit{Punishment} condition (Appendix Figure~\ref{fig:punishment_hypothetical}). Thus, the manipulation appears not to have changed what subjects expected punishment to look like.}

%% [figure environment unchanged]

Punishment beliefs nevertheless carry within-subject information. Table~\ref{tab:reg_belief_specs} reports Probit regressions of the delegation decision on Player~A's belief difference in expected punishment (\textit{no delegation}~$-$~\textit{delegation}), so that higher values correspond to a larger expected punishment penalty for deciding herself. All specifications are restricted to the \textit{Punishment} condition. Columns~(1)--(3) use the simple average of the two outcome-conditional belief differences, Column~(4) a weighted average using Player~A's elicited outcome probabilities, and Column~(5) enters the two differences separately. The table note provides the details of each specification.

%% [table input unchanged]

Expected differential punishment does not predict delegation in the full sample (Columns~(1)--(2)). Among subjects who passed the attention check on the belief-elicitation screen, the relationship sharpens. A $\pounds 0.10$ larger expected punishment penalty for deciding herself is associated with a $4.7$~percentage-point higher probability of delegation (Column~(3), $p=0.011$), and with $5.5$~percentage points under the weighted specification (Column~(4), $p=0.006$).\footnote{In the decomposition of Column~(5), the good-outcome belief difference carries the relationship ($2.7$~percentage points per $\pounds 0.10$, $p=0.010$), while the bad-outcome difference is positive but noisier ($1.7$~percentage points, $p=0.165$). The two differences are nearly orthogonal in this sample (Pearson correlation $-0.10$ among passers), so we read Column~(5) as a descriptive decomposition rather than as two competing regressors.}

Taken together, the belief evidence is mixed. The measure itself is not pure noise. Within the \textit{Punishment} condition, subjects whose beliefs embody a larger penalty for deciding themselves are more likely to delegate, so the delegation choice responds to belief asymmetries where they exist. But a margin whose average is zero provides no aggregate push. For anticipation of punishment to generate a $17$~percentage-point delegation gap between treatments, Player~As would need to expect systematically harsher punishment for delegated decisions. They do not and neither would such an expectation have been correct, as Player~B's realized punishment exhibits no delegation penalty either (Result~2). Anticipated differential punishment is thus a dimension along which subjects differ, but it cannot explain the treatment difference in delegation.

\medskip
\noindent\textbf{Result~3.} \textit{On average, Player~A expects no punishment penalty for delegation, mirroring Player~B's actual punishment behavior. Within the Punishment condition, however, Player~As who expect a larger penalty for deciding themselves are more likely to delegate.}
\medskip
```

## Version B — redrafted LaTeX (reordered, caveats last)

Order: motive → elicitation (with the Punishment-condition focus moved up, since the reader needs it before any results) → aggregate null + figure → margin evidence → reservations → synthesis → Result 3. The reservations paragraph now qualifies both findings symmetrically (the aggregate null and the within-subject correlation) and frames the limitation by scope. Levels and averages are most exposed to the elicitation problems, relative within-subject comparisons less so. The synthesis keeps the Result 2 safety net prominent, so the rejection of the anticipation mechanism does not rest on the belief measure alone.

```latex
\paragraph{Anticipated differential punishment.} The most natural candidate is anticipation of differential punishment. Player~A may expect a delegated decision to be punished more harshly than a self-made one, and delegate less in response. Such an expectation would, for example, be consistent with evidence that observers view the delegation of morally consequential decisions to machines relatively critically \citep[e.g.,][]{gogoll_rage_2018, bigman_people_2018, jauernig_people_2022, bonnefon_moral_2024}.

After the delegation decision but before learning the outcome, we elicited Player~A's beliefs about Player~B's punishment in each of the four (delegation, outcome) scenarios. Anticipated punishment can affect behavior only where punishment is possible. We therefore focus in the analysis of punishment beliefs on the \textit{Punishment} condition.

Two patterns emerge (Figure~\ref{fig:realized_vs_anticipated}). First, Player~As, on average, substantially overestimate punishment in every scenario. Second, Player~As expect essentially the same punishment for delegated and self-made decisions, conditional on the outcome, correctly anticipating the pattern in Player~B's actual punishment behavior (Result~2).\footnote{The expected punishment penalty for delegation is small and statistically indistinguishable from zero in both outcome states, and a within-subject test finds no asymmetry between the two.} Thus, measured beliefs provide no support for a punishment anticipation mechanism for Result~1.\footnote{The same holds for the fully hypothetical beliefs elicited in the \textit{No-Punishment} condition, which closely track those in the \textit{Punishment} condition (Appendix Figure~\ref{fig:punishment_hypothetical}). Thus, the manipulation appears not to have changed what subjects expected punishment to look like.}

%% [figure environment unchanged]

The belief measure nevertheless carries within-subject information. Table~\ref{tab:reg_belief_specs} reports Probit regressions of the delegation decision on Player~A's belief difference in expected punishment (\textit{no delegation}~$-$~\textit{delegation}), so that higher values correspond to a larger expected punishment penalty for deciding herself. All specifications are restricted to the \textit{Punishment} condition. Columns~(1)--(3) use the simple average of the two outcome-conditional belief differences, Column~(4) a weighted average using Player~A's elicited outcome probabilities, and Column~(5) enters the two differences separately. The table note provides the details of each specification.

%% [table input unchanged]

Expected differential punishment does not predict delegation in the full sample (Columns~(1)--(2)). Among subjects who passed the attention check on the belief-elicitation screen, the relationship sharpens. A $\pounds 0.10$ larger expected punishment penalty for deciding herself is associated with a $4.7$~percentage-point higher probability of delegation (Column~(3), $p=0.011$), and with $5.5$~percentage points under the weighted specification (Column~(4), $p=0.006$).\footnote{In the decomposition of Column~(5), the good-outcome belief difference carries the relationship ($2.7$~percentage points per $\pounds 0.10$, $p=0.010$), while the bad-outcome difference is positive but noisier ($1.7$~percentage points, $p=0.165$). The two differences are nearly orthogonal in this sample (Pearson correlation $-0.10$ among passers), so we read Column~(5) as a descriptive decomposition rather than as two competing regressors.}

The belief measure has limitations. The elicitation was unincentivized, took place after the delegation decision, and was partly hypothetical, as only two of the four scenarios could still materialize after Player~A's delegation decision in the \textit{Punishment} condition and all four were purely hypothetical in the \textit{No-Punishment} condition. The lack of incentives and the hypothetical scenarios weigh most heavily on the level and the average of reported beliefs. The timing weighs on the within-subject relationship, which may partly capture subjects justifying a choice already made rather than beliefs shaping that choice. We therefore give the belief evidence limited weight in either direction. In particular, we do not treat the absence of an average belief difference as ruling out that punishment-related concerns weigh on the delegation decision.

Taken together, the belief evidence does not support anticipated differential punishment as the mechanism behind Result~1. For anticipation of punishment to generate a $17$~percentage-point delegation gap between conditions, Player~As would need to expect systematically harsher punishment for delegated decisions. The measured beliefs show no such expectation, and such an expectation would not have been correct, as Player~B's realized punishment exhibits no delegation penalty either (Result~2). What the belief evidence does show is heterogeneity. Within the \textit{Punishment} condition, Player~As whose beliefs embody a larger penalty for deciding themselves are more likely to delegate. Anticipated punishment is thus a dimension along which subjects differ, but it provides no aggregate push toward less delegation under punishment.

\medskip
\noindent\textbf{Result~3.} \textit{On average, Player~A expects no punishment penalty for delegation, mirroring Player~B's actual punishment behavior. Within the Punishment condition, however, Player~As who expect a larger penalty for deciding themselves are more likely to delegate.}
\medskip
```

### Version B change log (relative to Version A)

- The caveats leave the elicitation paragraph, which shrinks to procedure plus the Punishment-condition focus.
- A new reservations paragraph sits after the regression evidence and before the synthesis. Revised 2026-08-10 per feedback: it opens with the facts of the elicitation rather than an interpretive stance ("we interpret with caution in both directions" felt defensive without stated reasons), maps each problem to what it contaminates (no incentives and hypotheticality hit levels and averages; post-decision timing hits the within-subject relationship), and only then concludes with the weight assignment. The closing sentence remains the hook for the signaling paragraph.
- The synthesis was rewritten (2026-08-10): the old version walked backwards through the block (re-arguing "not pure noise" right after the reservations qualified it) and closed with an unscoped "cannot explain the treatment difference". The new version leads with the verdict, rests it on the two legs that survive the caveats (measured beliefs show no penalty; a correct expectation of one was impossible given Result~2), then states the heterogeneity finding, and closes scoped ("no aggregate push toward less delegation under punishment").
- "nevertheless" in the regression paragraph now contrasts with the aggregate null rather than with the caveats.
- Everything else (motive paragraph, figure, table, compressions, footnotes) is identical to Version A.

## Suggested revised table note

Per the single-source rule this goes into `scripts/python/22_belief_specs.py` (the `note` variable, lines 120-131), then the script is re-run. The additions are the column descriptions and the orthogonality remark; the construction and AME sentences are already there.

```python
note = (
    "Probit regressions of Player~A's delegation decision, restricted to the "
    "\\textit{Punishment} condition. Robust (HC1) standard errors in parentheses. "
    "Significance: $^{*}\\,p<0.10$; $^{**}\\,p<0.05$; $^{***}\\,p<0.01$ (two-sided). "
    "Belief differences are within-subject \\textit{(no delegation)}~$-$~\\textit{(delegation)} "
    "in expected punishment, so positive coefficients indicate that subjects who expect "
    "to be punished more harshly for not delegating (relative to delegating) are more "
    "likely to delegate. "
    "Columns~(1)--(3) use the simple average of the two outcome-conditional belief "
    "differences, without controls, with controls, and with controls on the subsample of "
    "attention-check passers, respectively. Column~(4) replaces the simple average with a "
    "weighted average, using Player~A's elicited probability of the high payoff as the "
    "weight. Column~(5) enters the good-outcome and the bad-outcome difference separately; "
    "the two are nearly orthogonal (Pearson correlation $-0.10$ among passers), so "
    "Column~(5) serves as a descriptive decomposition. "
    "The \\textit{AME} rows report the average marginal effect of the belief measure "
    "entered in the respective column on the probability of delegation, in percentage "
    "points per \\pounds 0.10 increase in the corresponding belief difference."
)
```

## Change log (draft vs redraft)

- The first three paragraphs and the figure are untouched. The mechanism verdict stays where it is and now stands out more because less follows it.
- The walkthrough paragraph shrinks from ~180 to ~80 words. Its two footnotes disappear from the text; the construction footnote was redundant with the existing table note, the orthogonality footnote moves into the note next to the Column~(5) description it qualifies.
- The estimates paragraph shrinks to full-sample null, passers headline (4.7 pp), and weighted variant (5.5 pp); the Column~(5) numbers move to a footnote.
- The parenthetical "(the statistic that enters an expected-utility calculation)" is dropped.
- The synthesis paragraph and Result~3 are unchanged.
- Block length falls by roughly a third; no number, column, or claim is removed from the paper, only relocated between text, footnotes, and the table note.
```
