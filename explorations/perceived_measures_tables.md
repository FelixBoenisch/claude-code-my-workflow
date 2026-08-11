# Table 1 and Table 3 variants with mean, median, and mode of perceived performance

Code: `explorations/perceived_measures_tables.py` (run from `scripts/python`). Production scripts, `tables/reg_delegation.tex`, and `tables/reg_belief_specs.tex` are untouched.

Construction. From the elicited probability distribution over own scores (`confidence0`--`confidence10`, normalized): **mean** = probability-weighted average (identical to the production `wa_confidence`), **median** = smallest score at which the cumulative subjective probability reaches one half, **mode** = score with the highest assigned probability (equals the existing `highest_confidence`). Correlations with the mean: median 0.97, mode 0.83.

All regressions are Probit with robust (HC1) standard errors, as in production.

## Table 1 analog (tab:del_decision_determinants), Column (4)

Column (4) is the only column in which perceived performance enters. Full sample, delegation on the Punishment indicator, socio-demographic controls, and the respective measure.

| Measure | Punishment coef. (p) | AME of Punishment | Measure coef. (p) | N | Pseudo R² |
|---|---|---|---|---|---|
| Mean (= production) | $-0.448$ ($0.029$) | $-17.2$ pp ($p=0.026$) | $-0.072$ ($0.203$) | 159 | 0.047 |
| Median | $-0.443$ ($0.030$) | $-17.0$ pp ($p=0.027$) | $-0.051$ ($0.288$) | 159 | 0.044 |
| Mode | $-0.437$ ($0.032$) | $-16.9$ pp ($p=0.029$) | $-0.014$ ($0.676$) | 159 | 0.040 |

The treatment effect is unchanged to the first decimal of the AME, and no perceived-performance measure approaches significance.

## Table 3 analog (tab:reg_belief_specs), perceived measure replacing actual performance

As in the earlier exercise, the respective perceived measure replaces `overall_score` in the control set. Column (1) has no controls and is unaffected. Belief-measure AMEs are in percentage points per £0.10, as in the production table.

### Mean (= wa_confidence)

| Spec | Belief measure (p) | AME per £0.10 | Measure coef. (p) | N |
|---|---|---|---|---|
| (2) full + controls | $+0.416$ ($0.367$) | $+1.50$ pp ($0.360$) | $-0.080$ ($0.369$) | 78 |
| (3) passers + controls | $+1.329$ ($0.039$) | $+4.16$ pp ($0.024$) | $-0.032$ ($0.776$) | 60 |
| (4) weighted, passers | $+1.742$ ($0.021$) | $+5.30$ pp ($0.009$) | $-0.060$ ($0.579$) | 60 |
| (5) decomposition, passers | good $+0.696$ ($0.083$), bad $+0.607$ ($0.094$) | — | $-0.032$ ($0.776$) | 60 |

### Median

| Spec | Belief measure (p) | AME per £0.10 | Measure coef. (p) | N |
|---|---|---|---|---|
| (2) full + controls | $+0.349$ ($0.441$) | $+1.27$ pp ($0.437$) | $-0.018$ ($0.816$) | 78 |
| (3) passers + controls | $+1.317$ ($0.036$) | $+4.11$ pp ($0.023$) | $+0.029$ ($0.749$) | 60 |
| (4) weighted, passers | $+1.681$ ($0.023$) | $+5.13$ pp ($0.011$) | $+0.012$ ($0.895$) | 60 |
| (5) decomposition, passers | good $+0.693$ ($0.075$), bad $+0.595$ ($0.101$) | — | $+0.030$ ($0.741$) | 60 |

### Mode

| Spec | Belief measure (p) | AME per £0.10 | Measure coef. (p) | N |
|---|---|---|---|---|
| (2) full + controls | $+0.299$ ($0.499$) | $+1.09$ pp ($0.496$) | $+0.026$ ($0.615$) | 78 |
| (3) passers + controls | $+1.335$ ($0.032$) | $+4.13$ pp ($0.019$) | $+0.058$ ($0.364$) | 60 |
| (4) weighted, passers | $+1.666$ ($0.022$) | $+5.04$ pp ($0.011$) | $+0.046$ ($0.467$) | 60 |
| (5) decomposition, passers | good $+0.719$ ($0.063$), bad $+0.573$ ($0.111$) | — | $+0.060$ ($0.346$) | 60 |

## Reading

1. **Table 1: nothing moves.** The Punishment AME stays at $-17$ pp ($p \le 0.029$) under all three measures, and no measure is significant (mode is the weakest, $p=0.68$).
2. **Table 3: the belief-measure result is measure-invariant.** The passers coefficient sits at $+1.32$ to $+1.34$ ($p=0.032$--$0.039$) and the weighted variant at $+1.67$ to $+1.74$ ($p=0.021$--$0.023$) regardless of which perceived-performance statistic serves as the control. The perceived measure itself is never significant in any specification (all $p \ge 0.35$); its sign even flips between mean (negative) and median/mode (positive) among passers, which is what noise around zero looks like.
3. **Note on comparability:** in these Table 3 variants the belief-measure AMEs (e.g., $+4.16$ pp per £0.10 in (3)) differ slightly from the production values ($+4.7$ pp) because production controls for actual performance, which is itself predictive; the belief coefficient is robust to that difference too.

If any of this goes into the paper, the natural form is the one-sentence robustness footnote proposed earlier (all $p \ge 0.36$ across mean, median, mode, P($\ge 5$), and the subjective standard deviation), backed by promoting `perceived_measures_tables.py` to a numbered script with manifest keys.
