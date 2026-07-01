# Extensive-margin probit: P(any punishment)

DV = $1\{\text{punishment} > 0\}$ in a cell, stacked over the four (delegation, outcome) cells (4 obs per Player~B). Probit; SE clustered at the Player~B level, in parentheses. Stars: * p<0.10, ** p<0.05, *** p<0.01.

| Variable | Full sample | Passers |
|---|---|---|
| Delegated | 0.002 (0.077) | -0.042 (0.078) |
| Bad outcome | 0.556*** (0.139) | 0.563*** (0.153) |
| Delegated $\times$ Bad outcome | -0.099 (0.095) | -0.072 (0.103) |
| Player B belief about Player A perf. | -0.083 (0.075) | -0.030 (0.082) |
| Age | -0.006 (0.013) | -0.013 (0.015) |
| Female | 0.115 (0.272) | 0.230 (0.291) |
| Socio-economic status | 0.160 (0.126) | 0.140 (0.129) |
| Went to uni | -0.827*** (0.320) | -0.706** (0.349) |
| Technology score | 0.062 (0.118) | -0.023 (0.131) |
| Leadership position | 0.062 (0.293) | -0.071 (0.321) |
| Constant | -0.382 (0.807) | -0.182 (0.864) |
| **AME of Delegated (pp)** | -1.8 (p=0.462) | -2.9 (p=0.285) |
| **AME of Bad outcome (pp)** | 18.1 (p=0.000) | 19.4 (p=0.000) |
| Observations | 320 | 268 |
| Subjects | 80 | 67 |
| Pseudo R2 | 0.096 | 0.081 |

**Note.** The AME rows are *discrete* average marginal effects on the probability of imposing any punishment, in percentage points: for Delegated, the average change from setting delegated $0\to1$ (with the interaction moved consistently); for Bad outcome, the change from setting bad $0\to1$. They are computed by counterfactual prediction (not naive margins, which mishandle the interaction), with p-values from a 400-rep subject-cluster bootstrap. The probit interaction *coefficient* is not itself the marginal interaction effect (Ai \& Norton 2003); read the AME rows for interpretation.

