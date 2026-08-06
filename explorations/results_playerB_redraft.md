# Redraft: subsection "Player B -- Punishment behavior" (results.tex, lines 33-64)

Scope. The subsection from `\subsection*{Player~B -- Punishment behavior}` up to the start of "Mechanisms". The Mechanisms section is untouched. Result 2 is kept verbatim (wording settled with the supervisor comments, package E). The redraft follows the writing guide (active voice, present tense for findings, topic sentences, one idea per sentence, no colons or dash asides in prose, economic magnitudes) and the established terminology (delegation decision, the final prediction, delegated/self-made as the cell register).

## Critical review of the current draft

1. **Redundant double negative in the opening paragraph.** The paragraph makes the "punishment is not random" point twice, first as "carries real informational content rather than being random" and then as "need not reflect noise either". The redraft states the outcome sensitivity once, then uses the good-outcome levels as a separate, second argument.

2. **Missing test statistics.** The £0.20 outcome difference is called significant but carries no test in the text (it is paired *t*, p < 0.001; now also in the manifest as `fig_pun_outcome_diff_paired_p` = 0.00075). The good-outcome comparison (£0.33 vs £0.30) has no test either (paired *t*, p = 0.53, manifest key `fig_pun_good_pair_paired_p`). The redraft adds both.

3. **A logic slip in the good-outcome argument.** The draft explains positive punishment after good outcomes by "views about the appropriateness of delegation". That argument covers only the delegated cells. Self-made decisions with good outcomes attract the same £0.30, and views about delegation cannot explain punishing someone for *not* delegating. The redraft broadens the argument to views about how the final prediction should have been made, which covers both cells and still matches the Coffman footnote.

4. **Colon and dash constructions.** "tells the same story: Punishment loads..." uses a colon, and "-- the differential that would capture any insulation... --" is a dash aside. Both are rewritten as separate sentences per the house rules.

5. **Precision and a sentence fragment.** "£0.071" is more precise than every other pound figure in the section (redraft uses £0.07), and "After a bad outcome, £0.48 versus £0.55." is a fragment (redraft makes it a full sentence).

6. **Register mismatch with the figure.** The text says "self-made decisions" while the figure ticks and note say "Self-decided". I kept "self-made" in the prose, which is the established cell register. If you prefer full alignment, changing the figure ticks to "Self-made" is a one-line edit in `20_punishment_figure.py`; alternatively the prose switches to "self-decided" throughout this subsection.

7. **Connective pile-up.** The last two paragraphs open consecutive sentences with "Thus", "Thus", "Therefore". The redraft varies the connectives and merges the two closing claims into one paragraph with a clearer link to Result 1.

8. **The figure note misdescribes the whiskers.** The current note says only "Whiskers are $\pm 1$ standard error of the share." After adding whiskers to the gold bars, the green whiskers (standard error of the *mean* punishment) are no longer described, and the sentence attaches the share definition to all whiskers. The note below fixes this. It also adds a key for the "+£0.20***" arrow annotation, which currently has stars with no definition in the note; if you would rather keep the note minimal, at least the whisker sentence needs the fix.

9. **The `\hl` question on the diff-in-diff table.** My recommendation is to keep Table `tab:reg_punishment` in the main text. Result 2 is a null claim, and the interaction coefficient (−0.103, p = 0.08) is the only regression evidence behind it; a skeptical referee will want the full specification next to the claim rather than in the appendix. If space becomes binding at the polish stage, moving it to the appendix and citing the interaction in the text is a defensible fallback.

10. **"only weakly significant".** The guide discourages intensifiers that steer interpretation ("only"). The convention footnote already defines "weakly significant", so the label can stand alone. The redraft drops "only"; restore it if you want the emphasis.

## Redrafted LaTeX

```latex
\subsection*{Player~B -- Punishment behavior} \label{sec:result2}

We now turn to Player~B's punishment behavior in the \textit{Punishment} condition, in which punishment was payoff-relevant. Punishment is substantial in all four (delegation, outcome) scenarios of the strategy method, with average deductions between $\pounds 0.30$ and $\pounds 0.55$ (Figure~\ref{fig:punishment}). Punishment responds strongly to the outcome. Player~Bs punish bad outcomes more than good outcomes, by $\pounds 0.20$ on average (paired $t$-test, $p<0.001$), so measured punishment carries informational content. The substantial punishment after \textit{good} outcomes need not reflect noise either. Player~Bs can hold views about how the final prediction should have been made, independently of the realized outcome, and can punish accordingly.\footnote{For example, \citet{coffman_intermediation_2011} likewise documents non-trivial punishment in settings where the decision-maker's action could not have been improved upon.}

%% [figure environment unchanged; suggested revised note below]

Holding the outcome fixed, Player~B punishes delegated and self-made decisions alike. After a good outcome, average punishment is $\pounds 0.33$ for delegated and $\pounds 0.30$ for self-made decisions (paired $t$-test, $p=0.53$). After a bad outcome, the ordering reverses, with $\pounds 0.48$ for delegated against $\pounds 0.55$ for self-made decisions. The punishment gap for bad outcomes thus runs in the direction predicted by H2 but is small and statistically insignificant ($\pounds 0.07$; paired $t$-test $p=0.13$; Wilcoxon signed-rank $p=0.54$).

\medskip
\noindent\textbf{Result~2.} \textit{Conditional on a low-payoff outcome, Player~B does not punish delegated decisions significantly less than self-made ones.}
\medskip

Regression analysis in Table~\ref{tab:reg_punishment} confirms this pattern. Punishment loads overwhelmingly on the outcome, with a bad-outcome coefficient of $0.256$ ($p<0.01$), while the effect of delegation after good outcomes is essentially zero. The \textit{Delegated}~$\times$~\textit{Bad outcome} interaction measures the differential that would capture any insulation from punishment after bad outcomes. It amounts to $-0.103$ and is weakly significant ($p=0.08$).\footnote{In the regression, because punishment for the different scenarios is elicited within-subject, any stable characteristic of Player~B is differenced out and cannot, by construction, confound the within-subject comparison. Thus, the control variables merely capture the between-subject association with Player~B's \textit{average} punishment level. We find no striking relationship between Player~B's average punishment level and either their socio-demographic characteristics or their beliefs about Player~A's \textit{absolute} performance.} The conclusion is unchanged when we restrict the sample to subjects who passed the attention check, which was included on the punishment elicitation screen (Table~\ref{tab:reg_punishment}, Column~(2)).

\input{../tables/reg_punishment.tex}

The same pattern holds on the extensive margin.\footnote{The corresponding regression results can be found in Appendix Table~\ref{tab:reg_punishment_extensive}.} For each outcome, the share of Player~Bs imposing \textit{any} punishment is indistinguishable between delegated and self-made decisions (Figure~\ref{fig:punishment}, right axis). Punishment is also far from universal. Nearly half of Player~Bs ($45.0\%$) impose no punishment in any of the four scenarios. Within each scenario, average punishment therefore reflects a punishing minority rather than light, diffuse sanctioning.

In sum, Player~B punishes delegated decisions neither less harshly nor less frequently than self-made ones. In our setting, Player~A can therefore not escape punishment by delegating the final prediction to the algorithm, but she also pays no punishment premium for doing so. Punishment responds almost entirely to the realized outcome. This finding disciplines the interpretation of Result~1. A drop in delegation motivated by punishment avoidance would require delegation to affect punishment, and in Player~B's observed behavior it does not.
```

## Suggested revised figure note

Keeps the shortened structure of the current note and fixes the whisker description; the arrow key sentence is optional.

```latex
\textit{Note:} For each scenario (delegation, outcome), the green bars report the average punishment chosen by Player~B (left $y$-axis, in pounds) and the gold bars the share of Player~Bs imposing non-zero punishment (right $y$-axis, in percent), in the \textit{Punishment} condition. Whiskers are $\pm 1$ standard error of the mean for the green bars and of the share for the gold bars. The brackets mark the within-outcome comparisons of average punishment between delegated and self-made decisions (paired $t$-tests, $p=0.53$ for good and $p=0.13$ for bad outcomes). The dashed lines mark the mean of average punishment within each outcome group, and the arrow reports their difference (paired $t$-test; $^{***}\,p<0.01$). The subsample of attention-check passers is shown in Appendix Figure~\ref{fig:punishment_passers}. Hypothetical punishment in the \textit{No-Punishment} condition is reported in Appendix Figure~\ref{fig:punishment_hypothetical}.
```

## Change log (draft vs redraft)

- Opening paragraph restructured. Outcome sensitivity stated once with its test; good-outcome argument broadened from "appropriateness of delegation" to "how the final prediction should have been made" (covers the self-made cells).
- Added p-values for the £0.20 difference (p < 0.001) and the good-outcome pair (p = 0.53).
- "£0.071" rounded to £0.07; the bad-outcome fragment made a full sentence.
- Regression paragraph split. Colon and dash-aside constructions removed; "only" dropped before "weakly significant"; "column~2" capitalized to match the Column~(1)--(5) style used earlier in the section.
- Extensive-margin paragraph reworded ("with 45.0\% of Player~Bs punishing in none of the four scenarios" replaced by two short sentences).
- Closing paragraph merges the two "Thus/Therefore" paragraphs, varies connectives, and restates the link to Result~1 as a one-step argument.
- The commented-out hypothetical-punishment line and the `\hl` diff-in-diff comment are omitted from the redraft; the `\hl` question is answered in point 9 above (recommendation to keep the table).
```
