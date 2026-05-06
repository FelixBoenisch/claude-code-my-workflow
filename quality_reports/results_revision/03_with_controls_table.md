# P03 — With-Controls table (redesign)

**Source paragraph:** `manuscript/results.tex` lines 24–41 (the post-figure block: "delegation around 50%" sentence, the `\paragraph{With controls.}` paragraph, and the following Robustness paragraph).
**Status:** Plan, awaiting feedback. **No edits to `results.tex` or `tables/reg_delegation.tex` yet.**
**Last updated:** 2026-05-06.

---

## 1. Context

The current production table at `tables/reg_delegation.tex` (`tab:del_decision_determinants`) has three columns:

- (1) Unconditional: `treat` only — full sample, $N=161$.
- (2) With socio-demographic controls **and** task performance — full sample, $N=159$ (2 missing SES rows dropped).
- (3) Punishment-only with beliefs + performance + SES — restricted to attention-check passers in the Punishment condition, $N=60$.

You're asking for the *With-Controls* paragraph's table to be redesigned with four columns that decompose what (2) currently bundles together (SES vs. performance vs. both), and to keep (1) as the unconditional baseline. Column (3) of the current table — the Punishment-only beliefs spec — is **not** part of this paragraph; it belongs to the Punishment-beliefs paragraph downstream. I flag what to do with it under §5.

The four specs you asked for, all fit on the **full sample** (Logit, HC1 robust SEs):

- (1) Unconditional: `treat`.
- (2) `treat` + SES (age, female, socio_status, went_to_uni, technology_score, leader).
- (3) `treat` + task performance (`overall_score`).
- (4) `treat` + task performance + SES.

---

## 2. The redesigned table — full coefficients (12 specifications)

Code in `explorations/results-revision/explore.py`, P03 block. All specs are Logit, full sample, with HC1 robust SEs. Standard errors in parentheses below each coefficient; two-sided $p$-values in parentheses next to the coefficient.

The 12 specs:

| # | Spec | Beyond `treat` |
|---|---|---|
| (1) | Unconditional | — |
| (2) | + SES | SES vector |
| (3) | + Performance | `overall_score` |
| (4) | Full | `overall_score` + SES |
| (5) | Risk only | `switching_point` |
| (6) | Risk + Perf + SES | `switching_point` + `overall_score` + SES |
| (7) | Order only | `random_order_del` |
| (8) | Order + Perf + SES | `random_order_del` + `overall_score` + SES |
| (9) | Overconf only | `overconfidence` |
| (10) | Overconf + Perf + SES | `overconfidence` + `overall_score` + SES |
| (11) | WA-conf only | `wa_confidence` |
| (12) | WA-conf + Perf + SES | `wa_confidence` + `overall_score` + SES |

SES vector throughout: `age`, `female`, `socio_status`, `went_to_uni`, `technology_score`, `leader`.

**The full table** (wide; render the planning file in a viewer that allows horizontal scroll):

| Variable | (1) Uncond. | (2) +SES | (3) +Perf | (4) Full | (5) Risk only | (6) Risk+Perf+SES | (7) Order only | (8) Order+Perf+SES | (9) Overconf only | (10) Overconf+Perf+SES | (11) WA-conf only | (12) WA-conf+Perf+SES |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `treat` | $+0.677$ ($p=0.034$) | $+0.696$ ($p=0.034$) | $+0.738$ ($p=0.024$) | $+0.757$ ($p=0.023$) | $+0.684$ ($p=0.033$) | $+0.766$ ($p=0.023$) | $+0.695$ ($p=0.031$) | $+0.764$ ($p=0.022$) | $+0.676$ ($p=0.035$) | $+0.771$ ($p=0.022$) | $+0.705$ ($p=0.029$) | $+0.771$ ($p=0.022$) |
|  | $(0.320)$ | $(0.329)$ | $(0.326)$ | $(0.334)$ | $(0.321)$ | $(0.337)$ | $(0.322)$ | $(0.332)$ | $(0.320)$ | $(0.336)$ | $(0.323)$ | $(0.336)$ |
| `overall_score` |  |  | $-0.166$ ($p=0.185$) | $-0.192$ ($p=0.133$) |  | $-0.192$ ($p=0.132$) |  | $-0.185$ ($p=0.144$) |  | $-0.277$ ($p=0.063$) |  | $-0.174$ ($p=0.178$) |
|  |  |  | $(0.125)$ | $(0.128)$ |  | $(0.128)$ |  | $(0.127)$ |  | $(0.149)$ |  | $(0.129)$ |
| `switching_point` |  |  |  |  | $+0.002$ ($p=0.735$) | $+0.002$ ($p=0.787$) |  |  |  |  |  |  |
|  |  |  |  |  | $(0.007)$ | $(0.007)$ |  |  |  |  |  |  |
| `random_order_del` |  |  |  |  |  |  | $+0.317$ ($p=0.326$) | $+0.427$ ($p=0.224$) |  |  |  |  |
|  |  |  |  |  |  |  | $(0.323)$ | $(0.350)$ |  |  |  |  |
| `overconfidence` |  |  |  |  |  |  |  |  | $-0.016$ ($p=0.837$) | $-0.103$ ($p=0.272$) |  |  |
|  |  |  |  |  |  |  |  |  | $(0.075)$ | $(0.094)$ |  |  |
| `wa_confidence` |  |  |  |  |  |  |  |  |  |  | $-0.101$ ($p=0.246$) | $-0.103$ ($p=0.272$) |
|  |  |  |  |  |  |  |  |  |  |  | $(0.087)$ | $(0.094)$ |
| `age` |  | $-0.004$ ($p=0.785$) |  | $-0.004$ ($p=0.800$) |  | $-0.003$ ($p=0.815$) |  | $-0.009$ ($p=0.575$) |  | $-0.003$ ($p=0.857$) |  | $-0.003$ ($p=0.857$) |
|  |  | $(0.015)$ |  | $(0.015)$ |  | $(0.015)$ |  | $(0.015)$ |  | $(0.015)$ |  | $(0.015)$ |
| `female` |  | $+0.279$ ($p=0.447$) |  | $+0.350$ ($p=0.343$) |  | $+0.353$ ($p=0.340$) |  | $+0.409$ ($p=0.271$) |  | $+0.392$ ($p=0.292$) |  | $+0.392$ ($p=0.292$) |
|  |  | $(0.366)$ |  | $(0.369)$ |  | $(0.370)$ |  | $(0.371)$ |  | $(0.373)$ |  | $(0.373)$ |
| `socio_status` |  | $-0.062$ ($p=0.584$) |  | $-0.058$ ($p=0.618$) |  | $-0.061$ ($p=0.598$) |  | $-0.076$ ($p=0.517$) |  | $-0.049$ ($p=0.679$) |  | $-0.049$ ($p=0.679$) |
|  |  | $(0.113)$ |  | $(0.116)$ |  | $(0.117)$ |  | $(0.118)$ |  | $(0.118)$ |  | $(0.118)$ |
| `went_to_uni` |  | $+0.061$ ($p=0.868$) |  | $+0.091$ ($p=0.803$) |  | $+0.091$ ($p=0.803$) |  | $+0.033$ ($p=0.930$) |  | $+0.077$ ($p=0.831$) |  | $+0.077$ ($p=0.831$) |
|  |  | $(0.369)$ |  | $(0.364)$ |  | $(0.364)$ |  | $(0.371)$ |  | $(0.362)$ |  | $(0.362)$ |
| `technology_score` |  | $-0.110$ ($p=0.459$) |  | $-0.078$ ($p=0.613$) |  | $-0.077$ ($p=0.613$) |  | $-0.054$ ($p=0.723$) |  | $-0.072$ ($p=0.634$) |  | $-0.072$ ($p=0.634$) |
|  |  | $(0.149)$ |  | $(0.153)$ |  | $(0.153)$ |  | $(0.153)$ |  | $(0.152)$ |  | $(0.152)$ |
| `leader` |  | $+0.647$ ($p=0.076$) |  | $+0.676$ ($p=0.065$) |  | $+0.678$ ($p=0.065$) |  | $+0.700$ ($p=0.063$) |  | $+0.666$ ($p=0.070$) |  | $+0.666$ ($p=0.070$) |
|  |  | $(0.364)$ |  | $(0.367)$ |  | $(0.368)$ |  | $(0.376)$ |  | $(0.368)$ |  | $(0.368)$ |
| Constant | $-0.302$ ($p=0.181$) | $+0.036$ ($p=0.967$) | $+0.152$ ($p=0.712$) | $+0.402$ ($p=0.665$) | $-0.454$ ($p=0.366$) | $+0.279$ ($p=0.791$) | $-0.463$ ($p=0.093$) | $+0.408$ ($p=0.665$) | $-0.273$ ($p=0.304$) | $+0.729$ ($p=0.463$) | $+0.167$ ($p=0.717$) | $+0.729$ ($p=0.463$) |
|  | $(0.226)$ | $(0.862)$ | $(0.412)$ | $(0.930)$ | $(0.502)$ | $(1.056)$ | $(0.275)$ | $(0.942)$ | $(0.266)$ | $(0.994)$ | $(0.459)$ | $(0.994)$ |
| **N** | $161$ | $159$ | $161$ | $159$ | $161$ | $159$ | $161$ | $159$ | $161$ | $159$ | $161$ | $159$ |
| **Pseudo $R^2$** | $0.020$ | $0.039$ | $0.029$ | $0.049$ | $0.021$ | $0.049$ | $0.025$ | $0.056$ | $0.021$ | $0.055$ | $0.027$ | $0.055$ |
| **AME `treat` (pp)** | $+16.4$ | $+16.5$ | $+17.7$ | $+17.7$ | $+16.6$ | $+17.9$ | $+16.8$ | $+17.7$ | $+16.4$ | $+17.8$ | $+17.0$ | $+17.8$ |

### Reading

- **Headline holds.** The `treat` coefficient is remarkably stable across all 12 specs: $0.68$–$0.77$, $p$-values $0.022$–$0.035$, AME $+16.4$ to $+17.9$ pp. No specification weakens the headline. Two-sided significance at the $5\%$ level survives every robustness check you asked for.
- **Risk preference (`switching_point`) is uninformative.** Coef $+0.002$, $p \approx 0.74$ alone, $p \approx 0.79$ with full controls. Risk-aversion is *not* predictive of delegation in this sample — contrary to Feier et al. (2022), where risk-averse subjects were more likely to delegate. Worth a sentence in the body or appendix.
- **Order (`random_order_del`) is positive but not significant pooled.** Coef $+0.32$ ($p=0.33$) alone, $+0.43$ ($p=0.22$) with full controls — points in the same direction as the within-Punishment order effect documented in the Other section, but pooled the noise washes it out. Including order as a control nudges the `treat` coefficient up slightly ($+0.696 \to +0.764$ vs spec 2 → spec 8) and is the most informative add of the four.
- **Overconfidence does not predict delegation.** Coef $-0.016$ ($p=0.84$) alone; $-0.103$ ($p=0.27$) in spec (10). Confirms what the current Robustness paragraph already says.
- **Spec (10) and Spec (12) are mathematically identical** for `treat`, SES, and the joint confidence/performance fit (note `treat` $= 0.771$, $p=0.022$, AME $+17.8$ pp in both). This is by construction: `overconfidence ≡ wa_confidence − overall_score`, so spec (10) and spec (12) are different parameterisations of the same model. The cells differ only in how the confidence/performance pair gets re-expressed.
- **`overall_score`'s coefficient grows when paired with `overconfidence`** ($-0.277$, $p=0.063$ in spec 10). This is the same identity at work: in spec (10), `overall_score` is identifying the *part of performance not absorbed by overconfidence*, which loads more cleanly. None of this changes the headline.
- **Leader stays robust** at $+0.65$ to $+0.70$, $p \approx 0.06$–$0.08$ across all specs that include SES. Side finding holds.
- **Pseudo $R^2$ ranges from $0.020$ to $0.056$.** Small but normal for this $N$ and outcome.

Two notes:

- **Performance** (`overall_score`): negative, as expected from your heterogeneity narrative — better performers delegate less — but not significant in the full sample ($p=0.133$). The relationship is concentrated in the Punishment condition (production Col 3, restricted: $-0.609$, $p=0.010$). Worth keeping the headline-table coefficient as is, and letting the Punishment-only sub-sample tell the heterogeneity story.
- **Leader** (leadership-experience indicator): $+0.68$, $p=0.065$. Leaders delegate *more*. This is a sub-headline finding the current design doesn't pull out; might or might not be worth a sentence in the body. Flagging.

---

## 2b. Same 12 specs, restricted to attention-check passers (`pass_att2 == 1`)

The canonical analysis sample (per `09_consort.py`) restricts to `pass_att2 == 1`: $N = 131$ ($61$ Punishment, $70$ No-Punishment), or $130$ when SES rows are dropped. This is the sample used in the production Col (3) of the current table.

| Variable | (1) Uncond. | (2) +SES | (3) +Perf | (4) Full | (5) Risk only | (6) Risk+Perf+SES | (7) Order only | (8) Order+Perf+SES | (9) Overconf only | (10) Overconf+Perf+SES | (11) WA-conf only | (12) WA-conf+Perf+SES |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `treat` | $+0.721$ ($p=0.043$) | $+0.756$ ($p=0.040$) | $+0.795$ ($p=0.029$) | $+0.834$ ($p=0.026$) | $+0.727$ ($p=0.042$) | $+0.845$ ($p=0.025$) | $+0.717$ ($p=0.045$) | $+0.813$ ($p=0.031$) | $+0.719$ ($p=0.044$) | $+0.857$ ($p=0.023$) | $+0.753$ ($p=0.037$) | $+0.857$ ($p=0.023$) |
|  | $(0.356)$ | $(0.368)$ | $(0.365)$ | $(0.376)$ | $(0.358)$ | $(0.378)$ | $(0.357)$ | $(0.376)$ | $(0.356)$ | $(0.376)$ | $(0.361)$ | $(0.376)$ |
| `overall_score` |  |  | $-0.210$ ($p=0.129$) | $-0.254$ ($p=0.074$) |  | $-0.255$ ($p=0.072$) |  | $-0.251$ ($p=0.074$) |  | $-0.300$ ($p=0.068$) |  | $-0.238$ ($p=0.099$) |
|  |  |  | $(0.138)$ | $(0.142)$ |  | $(0.142)$ |  | $(0.140)$ |  | $(0.164)$ |  | $(0.144)$ |
| `switching_point` |  |  |  |  | $+0.002$ ($p=0.791$) | $+0.003$ ($p=0.743$) |  |  |  |  |  |  |
|  |  |  |  |  | $(0.008)$ | $(0.008)$ |  |  |  |  |  |  |
| `random_order_del` |  |  |  |  |  |  | $+0.324$ ($p=0.365$) | $+0.458$ ($p=0.243$) |  |  |  |  |
|  |  |  |  |  |  |  | $(0.358)$ | $(0.392)$ |  |  |  |  |
| `overconfidence` |  |  |  |  |  |  |  |  | $+0.026$ ($p=0.769$) | $-0.062$ ($p=0.572$) |  |  |
|  |  |  |  |  |  |  |  |  | $(0.088)$ | $(0.110)$ |  |  |
| `wa_confidence` |  |  |  |  |  |  |  |  |  |  | $-0.081$ ($p=0.427$) | $-0.062$ ($p=0.572$) |
|  |  |  |  |  |  |  |  |  |  |  | $(0.102)$ | $(0.110)$ |
| `age` |  | $+0.001$ ($p=0.937$) |  | $+0.002$ ($p=0.891$) |  | $+0.003$ ($p=0.873$) |  | $-0.003$ ($p=0.852$) |  | $+0.003$ ($p=0.850$) |  | $+0.003$ ($p=0.850$) |
|  |  | $(0.017)$ |  | $(0.017)$ |  | $(0.017)$ |  | $(0.018)$ |  | $(0.017)$ |  | $(0.017)$ |
| `female` |  | $+0.565$ ($p=0.164$) |  | $+0.651$ ($p=0.116$) |  | $+0.644$ ($p=0.120$) |  | $+0.713$ ($p=0.083$) |  | $+0.667$ ($p=0.107$) |  | $+0.667$ ($p=0.107$) |
|  |  | $(0.406)$ |  | $(0.414)$ |  | $(0.414)$ |  | $(0.411)$ |  | $(0.414)$ |  | $(0.414)$ |
| `socio_status` |  | $-0.137$ ($p=0.277$) |  | $-0.134$ ($p=0.304$) |  | $-0.138$ ($p=0.292$) |  | $-0.151$ ($p=0.255$) |  | $-0.128$ ($p=0.330$) |  | $-0.128$ ($p=0.330$) |
|  |  | $(0.126)$ |  | $(0.130)$ |  | $(0.131)$ |  | $(0.133)$ |  | $(0.132)$ |  | $(0.132)$ |
| `went_to_uni` |  | $+0.114$ ($p=0.777$) |  | $+0.184$ ($p=0.646$) |  | $+0.189$ ($p=0.638$) |  | $+0.171$ ($p=0.671$) |  | $+0.148$ ($p=0.710$) |  | $+0.148$ ($p=0.710$) |
|  |  | $(0.403)$ |  | $(0.400)$ |  | $(0.401)$ |  | $(0.403)$ |  | $(0.399)$ |  | $(0.399)$ |
| `technology_score` |  | $-0.004$ ($p=0.980$) |  | $+0.021$ ($p=0.903$) |  | $+0.020$ ($p=0.907$) |  | $+0.052$ ($p=0.767$) |  | $+0.017$ ($p=0.920$) |  | $+0.017$ ($p=0.920$) |
|  |  | $(0.166)$ |  | $(0.174)$ |  | $(0.175)$ |  | $(0.175)$ |  | $(0.173)$ |  | $(0.173)$ |
| `leader` |  | $+0.392$ ($p=0.333$) |  | $+0.413$ ($p=0.316$) |  | $+0.409$ ($p=0.321$) |  | $+0.426$ ($p=0.312$) |  | $+0.415$ ($p=0.316$) |  | $+0.415$ ($p=0.316$) |
|  |  | $(0.405)$ |  | $(0.412)$ |  | $(0.412)$ |  | $(0.421)$ |  | $(0.413)$ |  | $(0.413)$ |
| Constant | $-0.433$ ($p=0.099$) | $-0.252$ ($p=0.795$) | $+0.136$ ($p=0.767$) | $+0.241$ ($p=0.820$) | $-0.572$ ($p=0.329$) | $+0.075$ ($p=0.950$) | $-0.584$ ($p=0.056$) | $+0.237$ ($p=0.826$) | $-0.484$ ($p=0.118$) | $+0.445$ ($p=0.699$) | $-0.053$ ($p=0.921$) | $+0.445$ ($p=0.699$) |
|  | $(0.262)$ | $(0.971)$ | $(0.457)$ | $(1.062)$ | $(0.587)$ | $(1.187)$ | $(0.306)$ | $(1.076)$ | $(0.309)$ | $(1.152)$ | $(0.535)$ | $(1.152)$ |
| **N** | $131$ | $130$ | $131$ | $130$ | $131$ | $130$ | $131$ | $130$ | $131$ | $130$ | $131$ | $130$ |
| **Pseudo $R^2$** | $0.023$ | $0.045$ | $0.036$ | $0.063$ | $0.023$ | $0.064$ | $0.027$ | $0.071$ | $0.023$ | $0.065$ | $0.027$ | $0.065$ |
| **AME `treat` (pp)** | $+17.4$ | $+17.8$ | $+18.9$ | $+19.1$ | $+17.6$ | $+19.3$ | $+17.2$ | $+18.4$ | $+17.4$ | $+19.5$ | $+18.1$ | $+19.5$ |

### Reading — full sample vs attention-check passers

- **Treatment effect strengthens.** `treat` coefficient moves up from the $0.68$–$0.77$ range (full sample) to $0.72$–$0.86$ (passers); AME from $+16$–$18$ pp to $+17$–$20$ pp; significance is preserved everywhere ($p \in [0.022, 0.045]$). The attention-pass restriction *increases* the estimated treatment effect, consistent with attention-failers being noisier rather than systematically different in direction.
- **Performance becomes more visibly negative.** `overall_score` moves from $-0.17$/$-0.19$ ($p \approx 0.13$–$0.18$, full) to $-0.21$/$-0.30$ ($p \approx 0.07$–$0.10$, passers). The pooled performance-delegation relationship is more apparent in the cleaner sample but still doesn't reach $5\%$ — the bulk of the effect remains concentrated within the *Punishment* condition (production Col 3, restricted to passers in Punishment: $-0.609$, $p=0.010$).
- **The `leader` side finding goes away.** $+0.65$/$+0.70$ ($p \approx 0.07$) in the full sample shrinks to $+0.39$/$+0.43$ ($p \approx 0.32$) among passers. The leadership-experience effect appears to be driven by attention-failers — i.e., it's plausibly noise rather than a real channel. Useful diagnostic.
- **`female` reverses direction of borderline-ness.** Coefficient grows from $+0.28$/$+0.35$ ($p \approx 0.34$, full) to $+0.57$/$+0.71$ ($p \approx 0.08$–$0.16$, passers); spec (8) brings it just below $p=0.10$. Tentative pattern that wasn't apparent in the full sample.
- **Risk, order, overconfidence, wa-confidence** behave essentially the same way as in the full sample: small, insignificant.
- **Spec (10) and Spec (12) remain mathematically identical** (re-parameterisation), as in the full sample.
- **Pseudo $R^2$ goes up** from $\le 0.056$ to $\le 0.071$. Cleaner data, more variance explained.

### Sample-restriction trade-off

This is the kind of attention-restriction comparison your [To resolve] item asks for: *"For each analysis, make explicit whether this is with the reduced sample (attention checks) or full sample. Always consider also presenting the robustness check with the other."*

The two samples agree on the headline (treatment effect significant in every spec) but disagree on three side findings:

| Finding | Full sample | Attention passers |
|---|---|---|
| `leader` | Visible ($+0.65$/$+0.70$, $p \approx 0.07$) | **Disappears** ($+0.39$/$+0.43$, $p \approx 0.32$) |
| `female` | Not visible ($+0.28$, $p \approx 0.34$) | **Borderline** ($+0.57$/$+0.71$, $p \approx 0.08$ in spec 8) |
| `overall_score` (pooled) | $p \approx 0.13$–$0.18$ | $p \approx 0.07$–$0.10$ |

Suggests presenting the **passer sample as headline** (cleaner data, in line with the prereg), with the full sample attached as a robustness column or appendix table. (You decide; this is exactly the call your [To resolve] item flags.)

---

## 3. Other covariates we *could* include

Variables present in the cleaned data, with my read on whether each belongs in the headline table:

### Strong candidates (worth considering for the headline or a fifth column)

| Variable | What it is | Why it could go in |
|---|---|---|
| `overconfidence` (= `wa_confidence` − `overall_score`) | Player A's weighted-average belief about own performance, minus actual | The Robustness paragraph (L38) already references it. Putting it directly in the table pre-empts a robustness check and tightens the paragraph. Note: coef on overconfidence is itself near zero ($p\approx 0.27$ per current Robustness); the value is *that the treatment effect survives*. |
| `switching_point` (MPL risk task) | Risk preference proxy | Closes a Feier et al. (2022) comparison: they find risk-averse subjects delegate more. Worth at least one robustness col. |
| `random_order_del` | Order in which the two delegation options were displayed | Order effects are real in the *Punishment* condition (per the Other section, $p=0.07$). Including order as a control in the main spec strengthens the headline by neutralising a known nuisance. Cleanest justification. |

### Medium candidates (could go in, but more naturally elsewhere)

| Variable | Why it's medium |
|---|---|
| `pass_att2` (attention-check passer) | Currently used for *restriction* in Col (3) of the production table. Including as a covariate (instead of restricting) would address your [To resolve] item *"For each analysis, make explicit whether this is with the reduced sample (attention checks) or full sample. Always consider also presenting the robustness check with the other."* I'd run this as a robustness column rather than fold into the headline. |
| `wa_confidence` | Player A's raw weighted-average belief about own performance. Including this *and* `overall_score` essentially identifies the overconfidence-decomposition; you'd be using two correlated measures. Pick one (overconfidence as the residual) — cleaner. |
| `time_taken` | Total time on the experiment. Engagement proxy. Useful as a balance check (per [To resolve] item *"Show that randomization also worked on time taken, etc?"*); less natural as a delegation-decision covariate. Lean against. |

### Don't include

| Variable | Why not |
|---|---|
| `success_last`, `guess_last`, `confidence_last` | Post-treatment. Bad controls. |
| `treat_x_overall_score`, `nodel_del_*_x_treat` | Interaction terms — useful for the heterogeneity paragraph downstream, not the With-Controls headline. |
| `belief_*` / `nodel_del_good`, `nodel_del_bad` | Beliefs about Player B's punishment — relevant only in the Punishment-beliefs paragraph (Col 3 of current table); not in the With-Controls paragraph. |
| `income`, `employ_status`, `student_status`, `education` | Additional SES proxies; would over-control given `socio_status` already in the SES vector. Risk of post-hoc covariate selection. |
| Likert/post-experiment items | Post-treatment, and not all elicited from Player A. |

### Two operational notes

- **The 161 → 159 drop** in cols (2) and (4) is the [To resolve] item on `results.tex` L189. Two subjects have missing SES values. Three options: (i) leave it, with a one-line table footnote; (ii) impute SES with median; (iii) drop those two from *all* columns so $N$ is constant at 159. I'd pick (i) — it's the simplest, the production table already has a note, and the treatment effect is stable.
- **The current production Col (3)** (Punishment-only with beliefs) belongs to the punishment-beliefs paragraph, not this one. Two natural ways to handle it: (A) keep it in the same table, immediately after the new four columns, with a vertical rule separating "Full sample" from "Punishment only" — preserves the current visual; (B) split it off into its own table referenced from the punishment-beliefs paragraph. I'd lean (A) for layout economy, but flagging.

---

## 4. The focused 5-column table — exactly as described in `results.tex` L24

The current paragraph spells out a 5-column layout. Sections 2/2b/3 above remain as background; this is the table that matches the body text verbatim.

**Column map** (revised — Cols 3, 4, 5 each isolate one performance measure, not additive):

| Col | Variables beyond `treat` | Sample |
|---|---|---|
| (1) Unconditional | — | Full ($N=161$) |
| (2) + SES | SES vector | Full ($N=159$) |
| (3) + Actual perf | SES + `overall_score` | Full ($N=159$) |
| (4) + Perceived perf | SES + `wa_confidence` (no `overall_score`) | Full ($N=159$) |
| (5) Passers + Actual | SES + `overall_score`, restricted to `pass_att2 == 1` | Passers ($N=130$) |

SES vector: `age`, `female`, `socio_status`, `went_to_uni`, `technology_score`, `leader`. "Perceived performance" = `wa_confidence` (the weighted-average belief about own performance, over score values 0–10).

**The full table:**

| Variable | (1) Unconditional | (2) + SES | (3) + Actual perf | (4) + Perceived perf | (5) Passers + Actual |
|---|---:|---:|---:|---:|---:|
| `treat` (No-Punishment) | $+0.677$ ($p=0.034$) | $+0.696$ ($p=0.034$) | $+0.757$ ($p=0.023$) | $+0.721$ ($p=0.031$) | $+0.834$ ($p=0.026$) |
|  | $(0.320)$ | $(0.329)$ | $(0.334)$ | $(0.333)$ | $(0.376)$ |
| `overall_score` (actual perf) |  |  | $-0.192$ ($p=0.133$) |  | $-0.254$ ($p=0.074$) |
|  |  |  | $(0.128)$ |  | $(0.142)$ |
| `wa_confidence` (perceived perf) |  |  |  | $-0.118$ ($p=0.209$) |  |
|  |  |  |  | $(0.094)$ |  |
| `age` |  | $-0.004$ ($p=0.785$) | $-0.004$ ($p=0.800$) | $-0.003$ ($p=0.848$) | $+0.002$ ($p=0.891$) |
|  |  | $(0.015)$ | $(0.015)$ | $(0.015)$ | $(0.017)$ |
| `female` |  | $+0.279$ ($p=0.447$) | $+0.350$ ($p=0.343$) | $+0.332$ ($p=0.372$) | $+0.651$ ($p=0.116$) |
|  |  | $(0.366)$ | $(0.369)$ | $(0.372)$ | $(0.414)$ |
| `socio_status` |  | $-0.062$ ($p=0.584$) | $-0.058$ ($p=0.618$) | $-0.051$ ($p=0.661$) | $-0.134$ ($p=0.304$) |
|  |  | $(0.113)$ | $(0.116)$ | $(0.115)$ | $(0.130)$ |
| `went_to_uni` |  | $+0.061$ ($p=0.868$) | $+0.091$ ($p=0.803$) | $+0.047$ ($p=0.898$) | $+0.184$ ($p=0.646$) |
|  |  | $(0.369)$ | $(0.364)$ | $(0.367)$ | $(0.400)$ |
| `technology_score` |  | $-0.110$ ($p=0.459$) | $-0.078$ ($p=0.613$) | $-0.101$ ($p=0.494$) | $+0.021$ ($p=0.903$) |
|  |  | $(0.149)$ | $(0.153)$ | $(0.148)$ | $(0.174)$ |
| `leader` |  | $+0.647$ ($p=0.076$) | $+0.676$ ($p=0.065$) | $+0.641$ ($p=0.080$) | $+0.413$ ($p=0.316$) |
|  |  | $(0.364)$ | $(0.367)$ | $(0.365)$ | $(0.412)$ |
| Constant | $-0.302$ ($p=0.181$) | $+0.036$ ($p=0.967$) | $+0.402$ ($p=0.665$) | $+0.449$ ($p=0.635$) | $+0.241$ ($p=0.820$) |
|  | $(0.226)$ | $(0.862)$ | $(0.930)$ | $(0.945)$ | $(1.062)$ |
| **N** | $161$ | $159$ | $159$ | $159$ | $130$ |
| **Pseudo $R^2$** | $0.020$ | $0.039$ | $0.049$ | $0.047$ | $0.063$ |
| **AME on `treat` (pp)** | $+16.4$ ($p=0.025$) | $+16.5$ ($p=0.026$) | $+17.7$ ($p=0.016$) | $+16.9$ ($p=0.022$) | $+19.1$ ($p=0.017$) |

Logit, HC1 robust SEs in parentheses below each coefficient; two-sided $p$-values inline.

### What the table shows

- **Treatment effect robust across all five specs.** Coefficient $0.68 \to 0.70 \to 0.76 \to 0.72 \to 0.83$; AME $+16$ to $+19$ pp; significance everywhere ($p \in [0.023, 0.034]$). Nothing weakens the headline.
- **Actual performance** (Col 3): $-0.19$, $p=0.13$ in the full sample; (Col 5): $-0.25$, $p=0.074$ on passers. Directionally negative throughout, approaches significance under the attention restriction. Concentrated in *Punishment* (heterogeneity story for the mechanism section).
- **Perceived performance** (Col 4): $-0.12$, $p=0.21$. Bigger than `overall_score` once you don't condition on actual performance, but still not significant. Adding the perceived measure pulls the treatment coefficient down very slightly ($0.76 \to 0.72$), suggesting weak collinearity but no headline change.
- **`leader` consistently $+0.64$ to $+0.68$, $p \approx 0.07$–$0.08$** across all SES-including full-sample columns (2)–(4); fades to $+0.41$, $p=0.32$ on passers (Col 5). Same pattern as before — leadership effect is plausibly an attention-failer artefact.
- **`female` borderline only in the passer column** ($+0.65$, $p=0.116$); not visible in the pooled columns. Tentative.
- **Pseudo $R^2$** rises from $0.02$ to $0.06$. Col (4) ($R^2 = 0.047$) and Col (3) ($R^2 = 0.049$) are essentially tied — actual and perceived performance carry roughly equivalent explanatory power individually.

---

## 5. Reformulating the paragraph — addressing the four embedded comments

### 5.1 Comment "Interpret the Average marginal effect on the treatment"

After the headline coefficients are reported, add one sentence that interprets the AME directly. Suggested wording (updated for the revised column structure):

> "Translating the logit coefficient into an average marginal effect: across the four full-sample specifications, removing the punishment possibility raises the probability of delegation by between $16.4$ and $17.7$ percentage points; the corresponding figure on the attention-check sample is $19.1$ percentage points (Column~5)."

This implements the AME-alongside-coefficient convention discussed earlier and ties cleanly to the abstract's "$17$ percentage-point gap" framing.

### 5.2 Comment "Let's include the full regression table here"

The current production table at `tables/reg_delegation.tex` shows only `treat`, the belief differences, and `overall_score` in the body, with the SES coefficients pushed to the appendix `tables/reg_delegation_full.tex`. To bring the full regression table into the body:

- Update `scripts/python/04_logit_delegation.py` to produce a 5-column main table with **every coefficient** (including SES) shown in-body — i.e., merge the current main + appendix-full structures.
- Drop the appendix-full table or keep it as a sample-size-stable robustness companion.
- Footnote in the main table can simply say "All controls reported."

I'll wire this in once the column structure is locked.

### 5.3 Comment "integrate the following ... overconfidence ... essentially unchanged"

The current body sentence reads:

> "The treatment effect survives several further checks. Controlling for Player A's overconfidence (defined as the weighted-average belief about own performance minus actual performance) leaves the No-Punishment coefficient essentially unchanged."

With the revised column structure (Col 3 = actual perf only; Col 4 = perceived perf only), neither column directly controls for the *overconfidence residual* (`wa_confidence − overall_score`). Two cleanest options:

- **Option A — drop the sentence and adjust the prose** to acknowledge that actual and perceived performance enter as two separate columns rather than as a residual. The robustness message is still in the table: the treatment coefficient barely moves between Col (2) ($0.696$), Col (3) ($0.757$), and Col (4) ($0.721$), so adding either performance measure does not change the headline.
- **Option B — keep an overconfidence sentence**, separately noting (in body or footnote) that constructing the overconfidence residual and including it instead of the two raw measures produces a treatment coefficient of $+0.771$, $p=0.022$ (i.e., the spec from §4 of the wide table; numbers from the prior version of this plan).

If the goal is "show that overconfidence does not break the result", Option A says it implicitly through Cols 3 and 4. If the goal is to engage with overconfidence by name (because the existing literature does), Option B is the way. I'd default to A and keep B in reserve.

### 5.4 Comment "One footnote on order effects without showing a specification in the table"

Suggested footnote, inserted after the headline-coefficient sentence:

> "Including the random-order-of-delegation indicator (which side of the screen the delegation option appeared on) leaves the treatment coefficient essentially unchanged ($+0.43$ on the order indicator with $p=0.22$, treatment coefficient $+0.76$ with $p=0.022$ on the full sample). A more detailed analysis of order effects appears in Section~\ref{sec:other}."

The numbers come from spec (8) of the wide table in §2 above. The footnote keeps the main table to five columns while pre-empting the order-effects question.

### 5.5 The footnote on attention check (current paragraph): keep as-is

> "While the attention check was included on another screen, it may still correlate with who paid attention in deciding to delegate."

This is a clean justification for Col (5). Recommend keeping verbatim.

---

## 6. Suggested rewritten paragraph

Strawman implementing everything above:

> \paragraph{With controls.} Next, we examine the robustness of the observed treatment difference in the delegation decision. Specifically, we assess whether the difference in delegation rates remains when controlling for socio-demographic characteristics and Player~A's task performance. Table~\ref{tab:del_decision_determinants} reports estimates from a Logit model of the delegation decision. Column~(1) reports the unconditional treatment effect. Column~(2) adds a vector of socio-demographic and technology-affinity controls. Columns~(3) and (4) instead add Player~A's actual performance (correct predictions in the first ten rounds) and her perceived performance (the weighted-average belief about own performance), respectively. Column~(5) restricts the sample to subjects who passed the attention check, controlling for actual performance.\footnote{While the attention check was included on another screen, it may still correlate with who paid attention in deciding to delegate.} The treatment effect is robust across all five specifications: the coefficient on the No-Punishment indicator runs from $0.68$ ($p=0.034$, two-sided) in the unconditional specification to $0.83$ ($p=0.026$) in the attention-check sample. Translating these into average marginal effects: removing the punishment possibility raises the probability of delegation by between $16.4$ and $17.7$ percentage points across the four full-sample specifications, and by $19.1$ percentage points on the attention-check sample (Column~5). Neither actual nor perceived performance is significantly associated with delegation in the pooled sample, although actual performance loads negatively and approaches significance under the attention restriction (Column~5: $p=0.074$); we return to the heterogeneity-by-performance pattern in Section~\ref{sec:mechanism}.\footnote{Including a control for the random order in which the two delegation options appeared on the decision screen leaves the treatment coefficient essentially unchanged (treatment coefficient $+0.76$, $p=0.022$ on the full sample, with the order indicator at $+0.43$, $p=0.22$). A more detailed analysis of order effects appears in Section~\ref{sec:other}.}

Net effect:
- Unconditional → SES → SES+actual → SES+perceived progression spelled out.
- AME interpretation in the body.
- Order-effects footnote in place of a spec in the table.
- Overconfidence sentence dropped; covered by Col (4).
- Attention-check footnote kept verbatim.
- Pointer forward to Section~\ref{sec:mechanism} for the performance heterogeneity.

---

## 7. Open questions for you

1. **Confirm the column map** — particularly that "perceived performance" = `wa_confidence` (and not `overconfidence`).
2. **Adopt the rewritten paragraph in §6**, or amend?
3. **AME wording**: do you prefer "between $16.4$ and $17.8$ pp" (a range), or a single representative number ("about $17$ percentage points")?
4. **Order-effects footnote** as drafted in §5.4, or different framing?
5. **Once locked in:** I'll update `scripts/python/04_logit_delegation.py` to produce the redesigned 5-column table (all coefficients shown in-body, AME row included), and rerun. **(No edits yet.)**
