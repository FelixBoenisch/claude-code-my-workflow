# Attention-check robustness comparison
Each analysis below is run twice:
- **Full sample** — no attention-check exclusion.
- **Attention-pass** — `pass_att2 == 1` (Player A excluded on belief-elicitation screen; Player B excluded on punishment-elicitation screen).


## Sample sizes

| Metric | Full sample | Attention-pass | Δ |
|---|---:|---:|---:|
| N Player A total | 159 | 129 | -30 |
|   Punishment | 80 | 61 | -19 |
|   No-Punishment | 79 | 68 | -11 |
| N Player B total | 161 | 135 | -26 |
|   Punishment | 80 | 67 | -13 |
|   No-Punishment | 81 | 68 | -13 |

## Balance — Player A

| Metric | Full sample | Attention-pass | Δ |
|---|---:|---:|---:|
| age mean Pun | 39.026 | 38.35 | -0.676 |
| age mean No-Pun | 37.886 | 36.588 | -1.298 |
| age p (treat balance) | 0.5571 | 0.3992 | -0.1579 |
| female mean Pun | 0.487 | 0.517 | +0.03 |
| female mean No-Pun | 0.506 | 0.5 | -0.006 |
| female p (treat balance) | 0.936 | 0.9912 | +0.0552 |
| socio_status mean Pun | 5.179 | 5.1 | -0.079 |
| socio_status mean No-Pun | 5.329 | 5.265 | -0.064 |
| socio_status p (treat balance) | 0.5424 | 0.5469 | +0.0045 |
| went_to_uni mean Pun | 0.575 | 0.541 | -0.034 |
| went_to_uni mean No-Pun | 0.557 | 0.618 | +0.061 |
| went_to_uni p (treat balance) | 0.9446 | 0.4824 | -0.4622 |
| technology_score mean Pun | 2.087 | 2.082 | -0.005 |
| technology_score mean No-Pun | 2.266 | 2.294 | +0.028 |
| technology_score p (treat balance) | 0.3664 | 0.3226 | -0.0438 |
| leader mean Pun | 0.362 | 0.328 | -0.034 |
| leader mean No-Pun | 0.329 | 0.324 | -0.005 |
| leader p (treat balance) | 0.7827 | 1 | +0.2173 |

## Balance — Player B

| Metric | Full sample | Attention-pass | Δ |
|---|---:|---:|---:|
| age mean Pun | 37.087 | 36.209 | -0.878 |
| age mean No-Pun | 42.356 | 42 | -0.356 |
| age p (treat balance) | 0.0107 | 0.0105 | -0.0002 |
| female mean Pun | 0.588 | 0.597 | +0.009 |
| female mean No-Pun | 0.493 | 0.468 | -0.025 |
| female p (treat balance) | 0.3136 | 0.1956 | -0.118 |
| socio_status mean Pun | 5.425 | 5.403 | -0.022 |
| socio_status mean No-Pun | 5.11 | 5.177 | +0.067 |
| socio_status p (treat balance) | 0.2045 | 0.4049 | +0.2004 |
| went_to_uni mean Pun | 0.688 | 0.701 | +0.013 |
| went_to_uni mean No-Pun | 0.481 | 0.515 | +0.034 |
| went_to_uni p (treat balance) | 0.0127 | 0.0408 | +0.0281 |
| technology_score mean Pun | 1.363 | 1.284 | -0.079 |
| technology_score mean No-Pun | 1.333 | 1.353 | +0.02 |
| technology_score p (treat balance) | 0.8687 | 0.7199 | -0.1488 |
| leader mean Pun | 0.287 | 0.269 | -0.018 |
| leader mean No-Pun | 0.321 | 0.309 | -0.012 |
| leader p (treat balance) | 0.7715 | 0.7452 | -0.0263 |

## H1 — delegation rate by condition

| Metric | Full sample | Attention-pass | Δ |
|---|---:|---:|---:|
| delegation rate Punishment % | 42.5 | 39.3 | -3.2 |
| delegation rate No-Pun % | 60.8 | 58.8 | -2 |
| gap (pp) | 18.3 | 19.5 | +1.2 |
| N Punishment | 80 | 61 | -19 |
| N No-Punishment | 79 | 68 | -11 |
| p (Pearson chi²) | 0.0212 | 0.0272 | +0.006 |
| p (Fisher exact) | 0.0264 | 0.0345 | +0.0081 |

## Logit Col 1 (treat only, full sample)

| Metric | Full sample | Attention-pass | Δ |
|---|---:|---:|---:|
| N | 159 | 129 | -30 |
| treat coef | 0.7395 | 0.7895 | +0.05 |
| treat SE | 0.3229 | 0.3597 | +0.0368 |
| treat p | 0.022 | 0.0282 | +0.0062 |
| Pseudo R² | 0.0242 | 0.0275 | +0.0033 |

## Logit Col 2 (treat + score + controls, full sample)

| Metric | Full sample | Attention-pass | Δ |
|---|---:|---:|---:|
| N | 157 | 128 | -29 |
| treat coef | 0.864 | 0.9537 | +0.0897 |
| treat SE | 0.3412 | 0.3855 | +0.0443 |
| treat p | 0.0113 | 0.0134 | +0.0021 |
| Pseudo R² | 0.0594 | 0.0769 | +0.0175 |

## Logit Col 3 (Punishment-only, belief differences + score + controls)

| Metric | Full sample | Attention-pass | Δ |
|---|---:|---:|---:|
| N | 78 | 60 | -18 |
| bel diff (good) coef | 0.8115 | 1.579 | +0.7675 |
| bel diff (good) p | 0.1248 | 0.0332 | -0.0916 |
| bel diff (bad) coef | -0.2768 | 0.9369 | +1.2137 |
| bel diff (bad) p | 0.5794 | 0.2123 | -0.3671 |
| overall_score coef | -0.3948 | -0.6094 | -0.2146 |
| overall_score p | 0.0327 | 0.0098 | -0.0229 |
| Pseudo R² | 0.1137 | 0.2465 | +0.1328 |

## H2 — Player B punishment cells, paired tests

| Metric | Full sample | Attention-pass | Δ |
|---|---:|---:|---:|
| N Player B (Punishment cond.) | 80 | 67 | -13 |
| punish_del_good £ | 0.3294 | 0.3112 | -0.0182 |
| punish_nodel_good £ | 0.2975 | 0.3104 | +0.0129 |
| punish_del_bad £ | 0.4819 | 0.494 | +0.0121 |
| punish_nodel_bad £ | 0.5531 | 0.5709 | +0.0178 |
| diff bad (nodel-del) £ | 0.0713 | 0.0769 | +0.0056 |
| diff good (nodel-del) £ | -0.0319 | -0.0007 | +0.0312 |
| paired-t p (bad) | 0.1308 | 0.1526 | +0.0218 |
| Wilcoxon p (bad) | 0.5437 | 0.5333 | -0.0104 |
| paired-t p (good) | 0.5347 | 0.9887 | +0.454 |
| Wilcoxon p (good) | 0.2714 | 0.5935 | +0.3221 |
| MDE bad (£, 80% power) | 0.1307 | 0.1487 | +0.018 |
| MDE good (£, 80% power) | 0.1431 | 0.1476 | +0.0045 |
| never punishes (n) | 36 | 28 | -8 |
| never punishes (%) | 45 | 41.8 | -3.2 |

## Punishment regression — pooled OLS, clustered SE

| Metric | Full sample | Attention-pass | Δ |
|---|---:|---:|---:|
| N (subject-by-cell) | 320 | 268 | -52 |
| delegated coef | 0.0319 | 0.0007 | -0.0312 |
| delegated p | 0.5388 | 0.9889 | +0.4501 |
| bad_outcome coef | 0.2556 | 0.2604 | +0.0048 |
| bad_outcome p | 0.0003 | 0.001 | +0.0007 |
| interaction coef | -0.1031 | -0.0776 | +0.0255 |
| interaction p | 0.0761 | 0.1371 | +0.061 |
| adj R² | 0.0774 | 0.0341 | -0.0433 |

## Performance × delegation correlation (Punishment cond. only)

| Metric | Full sample | Attention-pass | Δ |
|---|---:|---:|---:|
| N | 80 | 61 | -19 |
| Pearson r | -0.189 | -0.224 | -0.035 |
| p | 0.0925 | 0.0826 | -0.0099 |

## Mechanism / effort — non-delegators

| Metric | Full sample | Attention-pass | Δ |
|---|---:|---:|---:|
| n non-delegators Punishment | 46 | 37 | -9 |
| n non-delegators No-Pun | 31 | 28 | -3 |
| success rate Punishment % | 21.7 | 21.6 | -0.1 |
| success rate No-Pun % | 48.4 | 50 | +1.6 |
| p (success rate diff) | 0.0187 | 0.02 | +0.0013 |
| mean overall_score Pun | 2.98 | 3 | +0.02 |
| mean overall_score No-Pun | 3.29 | 3.32 | +0.03 |
| p (score diff) | 0.3162 | 0.3489 | +0.0327 |

## Hypothetical delegation (No-Pun within-subject)

| Metric | Full sample | Attention-pass | Δ |
|---|---:|---:|---:|
| n pairs | 79 | 68 | -11 |
| actual delegation % | 60.8 | 58.8 | -2 |
| hypothetical delegation % | 51.9 | 51.5 | -0.4 |
| n switched: would-stop | 12 | 10 | -2 |
| n switched: would-start | 5 | 5 | ≈0 |
| McNemar p | 0.0896 | 0.1967 | +0.1071 |

## Order effects (random_order_del)

| Metric | Full sample | Attention-pass | Δ |
|---|---:|---:|---:|
| treat × order coef | -1.1468 | -1.0761 | +0.0707 |
| treat × order p | 0.0796 | 0.1394 | +0.0598 |
| p (order in Punishment) | 0.0704 | 0.1166 | +0.0462 |
| p (order in No-Pun) | 0.4941 | 0.6222 | +0.1281 |

## Belief distributions — delegators vs non-delegators (Punishment cond.)

| Metric | Full sample | Attention-pass | Δ |
|---|---:|---:|---:|
| belief_del_good delegators £ | 0.757 | 0.679 | -0.078 |
| belief_del_good non-delegators £ | 0.523 | 0.439 | -0.084 |
| belief_del_good diff (del-nodel) | 0.235 | 0.24 | +0.005 |
| belief_del_good t-test p | 0.1309 | 0.1939 | +0.063 |
| belief_del_good n delegators | 34 | 24 | -10 |
| belief_del_good n non-delegators | 46 | 37 | -9 |
| belief_nodel_good delegators £ | 0.812 | 0.821 | +0.009 |
| belief_nodel_good non-delegators £ | 0.451 | 0.319 | -0.132 |
| belief_nodel_good diff (del-nodel) | 0.361 | 0.502 | +0.141 |
| belief_nodel_good t-test p | 0.0159 | 0.0064 | -0.0095 |
| belief_nodel_good n delegators | 34 | 24 | -10 |
| belief_nodel_good n non-delegators | 46 | 37 | -9 |
| belief_del_bad delegators £ | 0.89 | 0.842 | -0.048 |
| belief_del_bad non-delegators £ | 0.947 | 0.997 | +0.05 |
| belief_del_bad diff (del-nodel) | -0.057 | -0.156 | -0.099 |
| belief_del_bad t-test p | 0.6594 | 0.3179 | -0.3415 |
| belief_del_bad n delegators | 34 | 24 | -10 |
| belief_del_bad n non-delegators | 46 | 37 | -9 |
| belief_nodel_bad delegators £ | 0.95 | 0.963 | +0.013 |
| belief_nodel_bad non-delegators £ | 1.001 | 1.031 | +0.03 |
| belief_nodel_bad diff (del-nodel) | -0.051 | -0.069 | -0.018 |
| belief_nodel_bad t-test p | 0.7019 | 0.6672 | -0.0347 |
| belief_nodel_bad n delegators | 34 | 24 | -10 |
| belief_nodel_bad n non-delegators | 46 | 37 | -9 |

## Player B beliefs about Player A performance

| Metric | Full sample | Attention-pass | Δ |
|---|---:|---:|---:|
| true score mean (Player A) | 2.956 | 2.946 | -0.01 |
| Player A wa_confidence mean | 4.77 | 4.903 | +0.133 |
| Player B wa_difficulty mean | 4.324 | 4.198 | -0.126 |
| A overestimation (pts) | 1.814 | 1.957 | +0.143 |
| B overestimation (pts) | 1.368 | 1.252 | -0.116 |

## Player B Likert × punishment correlations

| Metric | Full sample | Attention-pass | Δ |
|---|---:|---:|---:|
| responsibility n | 53 | 44 | -9 |
| responsibility mean | 1.981 | 2.023 | +0.042 |
| responsibility × nodel_del_bad r | 0.254 | 0.242 | -0.012 |
| responsibility × nodel_del_bad p | 0.066 | 0.1138 | +0.0478 |
| responsibility × nodel_del_good r | 0.206 | 0.363 | +0.157 |
| responsibility × nodel_del_good p | 0.1382 | 0.0154 | -0.1228 |
| trust n | 53 | 44 | -9 |
| trust mean | 3.642 | 3.636 | -0.006 |
| trust × nodel_del_bad r | 0.108 | 0.13 | +0.022 |
| trust × nodel_del_bad p | 0.4423 | 0.3992 | -0.0431 |
| trust × nodel_del_good r | 0.144 | 0.061 | -0.083 |
| trust × nodel_del_good p | 0.3039 | 0.6935 | +0.3896 |
| perception n | 53 | 44 | -9 |
| perception mean | 2.83 | 2.818 | -0.012 |
| perception × nodel_del_bad r | 0.05 | 0.089 | +0.039 |
| perception × nodel_del_bad p | 0.7207 | 0.5647 | -0.156 |
| perception × nodel_del_good r | -0.087 | -0.235 | -0.148 |
| perception × nodel_del_good p | 0.5342 | 0.1248 | -0.4094 |
