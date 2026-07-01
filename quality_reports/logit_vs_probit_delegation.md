# Delegation determinants: Logit (current) vs Probit

Dependent variable: delegation (1 = delegated to algorithm). HC1 robust standard errors in parentheses. Stars: * p<0.10, ** p<0.05, *** p<0.01 (two-sided). Columns (1)-(4) full sample; (5) attention-check passers. Two subjects drop in (2)-(4) for missing demographics.

## Table A — Logit (current `tab:del_decision_determinants`)

| Variable | (1) | (2) | (3) | (4) | (5) |
|---|---|---|---|---|---|
| No-Punishment indicator | 0.677** (0.320) | 0.696** (0.329) | 0.757** (0.334) | 0.721** (0.333) | 0.834** (0.376) |
| Task performance |  |  | -0.192 (0.128) |  | -0.254* (0.142) |
| Perceived performance |  |  |  | -0.118 (0.094) |  |
| Age |  | -0.004 (0.015) | -0.004 (0.015) | -0.003 (0.015) | 0.002 (0.017) |
| Female |  | 0.279 (0.366) | 0.350 (0.369) | 0.332 (0.372) | 0.651 (0.414) |
| Socio-economic status |  | -0.062 (0.113) | -0.058 (0.116) | -0.051 (0.115) | -0.134 (0.130) |
| Went to uni |  | 0.061 (0.369) | 0.091 (0.364) | 0.047 (0.367) | 0.184 (0.400) |
| Technology score |  | -0.110 (0.149) | -0.078 (0.153) | -0.101 (0.148) | 0.021 (0.174) |
| Leadership position |  | 0.647* (0.364) | 0.676* (0.367) | 0.641* (0.365) | 0.413 (0.412) |
| Constant | -0.302 (0.226) | 0.036 (0.862) | 0.402 (0.930) | 0.449 (0.945) | 0.241 (1.062) |
| **AME of No-Punishment (pp)** | 16.4** (p=0.025) | 16.5** (p=0.026) | 17.7** (p=0.016) | 16.9** (p=0.022) | 19.1** (p=0.017) |
| N | 161 | 159 | 159 | 159 | 130 |
| Pseudo R2 | 0.020 | 0.039 | 0.049 | 0.047 | 0.063 |

## Table B — Probit (same specifications)

| Variable | (1) | (2) | (3) | (4) | (5) |
|---|---|---|---|---|---|
| No-Punishment indicator | 0.423** (0.199) | 0.435** (0.204) | 0.472** (0.206) | 0.448** (0.205) | 0.517** (0.230) |
| Task performance |  |  | -0.119 (0.079) |  | -0.158* (0.086) |
| Perceived performance |  |  |  | -0.072 (0.056) |  |
| Age |  | -0.002 (0.009) | -0.002 (0.009) | -0.002 (0.009) | 0.002 (0.010) |
| Female |  | 0.175 (0.227) | 0.222 (0.228) | 0.212 (0.229) | 0.407 (0.254) |
| Socio-economic status |  | -0.038 (0.071) | -0.035 (0.072) | -0.031 (0.071) | -0.082 (0.079) |
| Went to uni |  | 0.036 (0.227) | 0.059 (0.225) | 0.025 (0.227) | 0.124 (0.247) |
| Technology score |  | -0.069 (0.092) | -0.048 (0.095) | -0.062 (0.092) | 0.014 (0.107) |
| Leadership position |  | 0.404* (0.225) | 0.422* (0.226) | 0.399* (0.225) | 0.253 (0.253) |
| Constant | -0.189 (0.141) | 0.018 (0.537) | 0.242 (0.570) | 0.268 (0.580) | 0.134 (0.645) |
| **AME of No-Punishment (pp)** | 16.5** (p=0.026) | 16.6** (p=0.026) | 17.8** (p=0.016) | 17.0** (p=0.022) | 19.2** (p=0.017) |
| N | 161 | 159 | 159 | 159 | 130 |
| Pseudo R2 | 0.020 | 0.039 | 0.049 | 0.047 | 0.064 |

## Note

Raw coefficients are not directly comparable across the two (logit coefficients are ~1.6-1.8x probit), but the average marginal effects (AME rows) and significance are nearly identical, so the substantive conclusion is unchanged.

