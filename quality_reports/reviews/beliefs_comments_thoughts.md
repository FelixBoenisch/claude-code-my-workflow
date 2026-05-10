---
title: "Thoughts and analyses for results.tex inline comments (lines 69–88)"
author: "Claude (review pass)"
date: "2026-05-10 (revised)"
scope: "manuscript/results.tex, lines 69–88 (Punishment-beliefs section)"
---

# Overview

Lines 69–88 of [results.tex](../../manuscript/results.tex#L69-L88) now span
two paragraphs: a new candidate-channel framing (line 69) and the
**Punishment beliefs** paragraph itself (line 71+), followed by a clean
caveats paragraph (line 73) and the `belief_distributions` figure.

**State as of latest revision:**

- **NEW** comment on line 69 about the prior-literature claim (Comment A
  below).
- **RESOLVED** in the new caveat paragraph at line 73: old Comments 2
  (noisy measure), 3 (between-subject), and 8 (pool treatments). Brief
  status notes are kept below for the record; the analyses remain in
  this file under "Resolved comments — analyses kept for the record".
- **DRAFTED** in
  [`beliefs_section_updated.tex`](beliefs_section_updated.tex) (a
  drop-in replacement for lines 69–88): old Comments 1, 4, 5, 6, 7.
  Companion artifacts:
  - [`scripts/python/21_realized_vs_anticipated.py`](../../scripts/python/21_realized_vs_anticipated.py)
    → `figures/realized_vs_anticipated.png` (new figure for Comment 1).
  - [`scripts/python/22_belief_specs.py`](../../scripts/python/22_belief_specs.py)
    → `tables/reg_belief_specs.tex` with label `tab:reg_belief_specs`
    (new 5-column table for Comments 4 + 6; existing
    `tab:del_decision_determinants` left unchanged).
  Sections below describe each comment for the record.

All numerical results come from [`beliefs_comments_analysis.py`](beliefs_comments_analysis.py)
on `data/clean/delegator_cleaned.parquet` and
`data/clean/evaluator_cleaned.parquet`.

> **Sample sizes used throughout (Punishment, treat=0):**
> Player A full = 80, passers = 61.  Player B full = 80, passers = 67.

---

## Comment A (line 69, NEW): "check that this is indeed the case" — prior-literature claim

**Context.** Line 69 of the new candidate-channel paragraph cites
\citet{gogoll_rage_2018, niszczota_robo-investors_2020, jauernig_people_2022}
in support of "observers view delegating moral decisions to algorithms
relatively critically." The comment asks to verify the citation actually
supports this thrust.

**Thoughts (prior, not freshly verified).** I have not fetched and re-read
the three papers in this session, so the following is my standing
recollection — flag for verification:

- **Gogoll & Uhl (2018), "Rage against the machine: Automation in the
  moral domain", JBEE.** Directly on-point: tests how third-party
  observers evaluate delegation of moral decisions to algorithms vs.
  humans, and finds critical reactions toward algorithm delegation.
  Likely supports the cited claim.
- **Niszczota & Kaszás (2020), "Robo-investment aversion."** Aversion to
  algorithmic investment management; the moral angle is around
  sin-stocks / ESG-relevant investing. Tangentially supports the claim
  via the broader algorithm-aversion-in-value-laden-decisions
  literature, but the framing is investing rather than the
  third-party-blame angle our paper uses.
- **Jauernig, Uhl & Walkowitz (2022).** I recall this as fitting the
  "people prefer human discretion to algorithms in moral domains"
  literature, but I'd want to confirm the exact thrust before relying
  on it as the headline citation.

**Verification approach (suggested, not yet run).** Run
[`/verify-claims`](../../.claude/skills/verify-claims) on the relevant
sentence, or manually fetch the three abstracts and confirm they support
the "delegating moral decisions to algorithms is viewed critically"
phrasing. Of the three, Gogoll & Uhl is the most directly on-point;
the other two may need a softer hedge in the prose ("e.g., on related
algorithm-aversion-in-value-domains, see ...") or replacement with a
closer citation (e.g., Bigman & Gray 2018, *Cognition*, "People are
averse to machines making moral decisions").

**Recommendation.** Either run a quick lit-verification pass before
finalising, or downgrade Niszczota and Jauernig to "see also" cites
behind a stronger lead citation (Gogoll & Uhl, or Bigman & Gray if
appropriate to add).

---

## Comment 1 (line 77): "Make a figure that compares realized with anticipated punishment in each scenario"

**Thoughts.** The current `Figure~\ref{fig:punishment}` ([20_punishment_figure.py](../../scripts/python/20_punishment_figure.py))
no longer overlays Player A beliefs on Player B punishment — that overlay was
moved out and is now missing. The text on line 77 still asserts the belief
overlap ("hollow bars") that no longer exists in the figure. So this comment is
correct: the cross-reference is stale.

The right fix is a small companion figure (e.g.
`figures/realized_vs_anticipated.png`) with one bar pair per cell:
- realized (Player B, punishment condition) average punishment, and
- anticipated (Player A, same condition) average punishment.
SE bars on both, ideally a passers/full overlay analogous to the rest of the
figure system.

I have not generated the PNG (writing to `figures/` should go through a
numbered script under `scripts/python/`). The numbers needed for it are:

### Realized vs anticipated punishment (Punishment condition)

**Full sample (n_B = 80, n_A = 80):**

| Cell        | Realized (B) | Anticipated (A) | Belief gap | t (Welch) | p     |
|-------------|-------------:|----------------:|-----------:|----------:|------:|
| Del + Good  | 0.329        | 0.622           | +0.293     | +2.92     | 0.004 |
| Del + Bad   | 0.482        | 0.923           | +0.441     | +4.37     | 0.000 |
| Self + Good | 0.297        | 0.604           | +0.307     | +3.14     | 0.002 |
| Self + Bad  | 0.553        | 0.979           | +0.426     | +4.07     | 0.000 |

**Passers only (n_B = 67, n_A = 61):**

| Cell        | Realized (B) | Anticipated (A) | Belief gap | t (Welch) | p     |
|-------------|-------------:|----------------:|-----------:|----------:|------:|
| Del + Good  | 0.311        | 0.534           | +0.222     | +2.05     | 0.043 |
| Del + Bad   | 0.494        | 0.936           | +0.442     | +3.89     | 0.000 |
| Self + Good | 0.310        | 0.516           | +0.206     | +1.89     | 0.061 |
| Self + Bad  | 0.571        | 1.004           | +0.433     | +3.71     | 0.000 |

Player As **systematically overestimate** punishment in every cell, by
£0.20–£0.44, all rejecting equality at p < 0.05 in the full sample (and
≤ 0.06 even in the smaller passers sample). The "hollow-bar" claim in the
prose is therefore correct in spirit — the data still support
overestimation — but the figure that backs it up needs to be remade.

**Recommendation:** add a numbered script (e.g. `21_realized_vs_anticipated.py`)
producing `figures/realized_vs_anticipated.png`, mirroring the bar-system style
of the existing punishment figure, and update the cross-reference on line 77.

---

## Comment 2 (formerly line 79): "Introduce beliefs as an incredibly noisy measure" — RESOLVED

**Status.** Folded into the new caveat paragraph at
[results.tex:73](../../manuscript/results.tex#L73). All four sources of
noise the comment listed (unincentivised, hedging, hypotheticality
gradient across treatments, reverse causality) are now in the prose.
Detailed analysis (delegators-vs-non belief comparison, both treatments)
is preserved at the end of this file under
"Resolved comments — analyses kept for the record".

---

## Comment 3 (formerly line 81, first): "Expand belief analysis to between-subject setting" — RESOLVED

**Status.** No longer relevant to the paragraph as it now stands — the
caveat paragraph at [results.tex:73](../../manuscript/results.tex#L73)
explicitly justifies the within-Punishment restriction on *structural*
grounds (the punishment-anticipation channel is operative only when
punishment is possible). A between-subject calibration check on belief
levels is informative as a sanity check on belief-elicitation
comparability but is no longer being used as a mechanism test.
Numerical tables retained at the end of this file under "Resolved
comments — analyses kept for the record" should the author want to use
them as a footnote/appendix robustness check.

---

## Comment 4 (line 81, second): "Check whether `tab:del_decision_determinants` is the relevant reference"

**Thoughts.** **The reference is wrong.** I traced the LaTeX label to its
generator:

- `tab:del_decision_determinants` is generated by
  [`04_logit_delegation.py:90-102`](../../scripts/python/04_logit_delegation.py#L90-L102),
  written to `tables/reg_delegation.tex`. Its Column (3) is the *main*
  delegation-controls regression with regressors `treat + SES + overall_score`
  — **no belief differences**. That's the table cited correctly on line 24
  (the "With controls" paragraph) and line 133.
- The belief-difference regression cited in line 81 is in the separate
  `tab:reg_delegation_beliefs`, generated at
  [`04_logit_delegation.py:158-170`](../../scripts/python/04_logit_delegation.py#L158-L170)
  and written to `tables/reg_delegation_beliefs.tex`.

So the prose should reference `tab:reg_delegation_beliefs` (and, separately,
`reg_delegation_beliefs.tex` is currently not `\input{}`-ed anywhere in the
manuscript — `grep -n "reg_delegation_beliefs" manuscript/`** returns zero
matches in `.tex` source).

**Recommended fix:**

1. Update `04_logit_delegation.py` so the belief table has three columns
   (the comment specifies: beliefs only / +controls / +controls passers),
   and re-export it.
2. Add `\input{tables/reg_delegation_beliefs.tex}` near line 81.
3. Replace `\ref{tab:del_decision_determinants}` on line 81 with
   `\ref{tab:reg_delegation_beliefs}`.

I ran the three-spec regression so the table content is ready. Coefficients
on belief differences (encoding: positive ⇒ subject expects more punishment
for self-decided than for delegated, conditional on outcome):

### Three specs — Logit of delegation on belief differences (Punishment only)

| Spec                                                        |   N | pseudo-R² | bel_diff_bad (b, p) | bel_diff_good (b, p) |
|-------------------------------------------------------------|----:|----------:|---------------------|----------------------|
| (1) Beliefs only — full Punishment                          |  80 | 0.013     | +0.005, p=0.991     | +0.561, p=0.247      |
| (2) Beliefs + controls — full Punishment                    |  78 | 0.114     | -0.277, p=0.579     | +0.812, p=0.125      |
| (3) Beliefs + controls — passers only ← **paper's coeffs**  |  60 | 0.246     | +0.937, p=0.212     | +1.579, p=0.033      |

Controls = `overall_score, age, female, socio_status, went_to_uni,
technology_score, leader`.

The good-outcome coefficient survives only in Spec (3) (the most-restricted
sample). It is *not* significant under any less-restrictive spec, which is
worth flagging in the prose.

---

## Comment 5 (line 81, third): "Potentially update" coefficient values

**Thoughts.** The numbers in the current text — bel_diff_good = 1.58
(p=0.033), bel_diff_bad = 0.94 (p=0.21) — match Spec (3) above
(passers + controls) **exactly to the displayed precision**. So no numeric
update is needed for that specification. What needs to change is the
surrounding text once Comment 4's spec broadening is implemented (Specs 1
and 2 weaken the result).

---

## Comment 6 (line 81, fourth): "Weight the differences by P(success), or take the average"

**Thoughts.** Conceptually this is the right move: A's belief about the
total expected punishment penalty for switching from delegation to
self-decision is

```
ΔE[punishment] = P(good) · (belief_nodel_good - belief_del_good)
               + P(bad)  · (belief_nodel_bad  - belief_del_bad)
               = P(good) · bel_diff_good + (1 - P(good)) · bel_diff_bad
```

That is exactly what the punishment-anticipation channel posits should
matter for the delegation choice. Using a *single* weighted regressor
also resolves the two-regressors interpretation worry (Comment 7).

**Implementation choice for P(success).** I used
`p_success = wa_confidence / 10` — Player A's elicited weighted-average
score over the 0–10 distribution, normalised to a probability. The mean
in the Punishment sample is 0.47 (sd 0.19), close to the empirical
good-outcome rate, which is a reasonable sanity check.

### Single-regressor specifications

| Sample          | Regressor                  | Controls | N  | b      | SE    | p      |
|-----------------|----------------------------|----------|---:|-------:|------:|-------:|
| Full Punishment | weighted by P(good)        | none     | 80 | +0.791 | 0.690 | 0.252  |
| Full Punishment | weighted by P(good)        | yes      | 78 | +0.954 | 0.742 | 0.199  |
| Full Punishment | simple average             | none     | 80 | +0.553 | 0.656 | 0.399  |
| Full Punishment | simple average             | yes      | 78 | +0.629 | 0.744 | 0.398  |
| Passers only    | weighted by P(good)        | none     | 61 | +2.122 | 0.988 | **0.032** |
| Passers only    | weighted by P(good)        | yes      | 60 | +3.329 | 1.532 | **0.030** |
| Passers only    | simple average             | none     | 61 | +1.815 | 0.934 | 0.052  |
| Passers only    | simple average             | yes      | 60 | +2.708 | 1.286 | **0.035** |

**Reading.** Both transformations carry the same qualitative message — and
the weighted version is a *cleaner* effect than the two-regressor
specification: in the passers sample, a one-pound increase in expected
punishment for non-delegation (over delegation) raises the log-odds of
delegation by ~3.3 (p=0.030, with controls). Significance still depends on
the attention-passers restriction.

**Recommendation.** Add the weighted-difference specification as the
preferred single-regressor alternative; show the simple-average version as a
robustness column.

---

## Comment 7 (line 81, fifth): "Is it even reasonable to include the two differences as regressors?"

**Thoughts.** Three issues to think about:

1. **Multicollinearity.** Empirically, no:
   `corr(bel_diff_good, bel_diff_bad) = 0.035` in full Punishment,
   `-0.101` in passers. Implied VIF ≈ 1.0. So the two coefficients are not
   fighting each other.
2. **Interpretation.** The two coefficients answer
   *partial* questions: holding constant the asymmetry-in-bad-outcomes,
   how does delegation respond to asymmetry-in-good-outcomes? That is a
   sensible decomposition only if you believe A's decision rule
   actually treats the two outcome-conditional asymmetries as
   *separate inputs* (rather than weighted into a single
   ΔE[punishment]). Under expected-utility A, only the weighted sum
   matters, and including both is over-parameterised.
3. **Power.** With N≈60 and a 10-regressor specification, two collinear-but
   -not-statistically-collinear regressors burn a degree of freedom you
   can't really afford.

**Net view.** The two-regressor table is fine *as a descriptive
decomposition*, but the structural quantity that maps cleanly onto the
punishment-anticipation channel is the single weighted difference (Comment
6). I would lead with the weighted version and demote the two-regressor
spec to a secondary column.

---

## Comment 8 (formerly line 85): "Devise an analysis using beliefs from BOTH treatments" — RESOLVED

**Status.** The new caveat paragraph at
[results.tex:73](../../manuscript/results.tex#L73) settles this: the
within-Punishment restriction is justified on structural grounds — the
punishment-anticipation channel is operative only when punishment is
possible, so beliefs about a counterfactual that cannot materialise do
not enter Player~A's decision rule in the No-Punishment arm. Pooling
the two conditions is therefore a category error rather than a missing
analysis. The pooled-treatment regressions I ran (Spec A/B/C with
`bel_diff × treat` interactions) are preserved at the end of this file
under "Resolved comments — analyses kept for the record" but should
**not** be read as a mechanism test.

---

# Summary punch list (current state, ordered by impact)

**Active items (still to address):**

1. **Cross-reference fix (Comment 4)** — `tab:del_decision_determinants` →
   `tab:reg_delegation_beliefs`; ensure
   `\input{tables/reg_delegation_beliefs.tex}` is added near
   [results.tex:77](../../manuscript/results.tex#L77). Update
   `04_logit_delegation.py` so the belief table has three columns
   (beliefs only / +controls / passers).
2. **Weighted-difference specification (Comment 6)** — cleaner mapping to
   theory than the two-regressor decomposition; cleaner result in
   passers (b ≈ 3.3, p = 0.030).
3. **Realized-vs-anticipated companion figure (Comment 1)** — text on
   [results.tex:75](../../manuscript/results.tex#L75) still references
   "hollow bars" that no longer exist in `figures/punishment.png`.
4. **Two-regressors clarification (Comment 7)** — keep the two-regressor
   table as descriptive only; the structural quantity is the single
   weighted difference.
5. **Coefficient update (Comment 5)** — no change needed for the cited
   numbers (1.58 / 0.94 / p=0.033 / p=0.21) under the current
   passers-with-controls specification, but the paragraph should
   acknowledge that the result weakens substantially under broader specs
   (Spec 1: p=0.247; Spec 2: p=0.125 — see Comment 4 table).
6. **Prior-literature check (Comment A, NEW)** — verify that
   gogoll_rage_2018 / niszczota_robo-investors_2020 / jauernig_people_2022
   actually support "observers view delegating moral decisions to
   algorithms relatively critically" (line 69). Gogoll & Uhl is on-point;
   the other two may need hedging or replacement.

**Resolved items (folded into the new caveat paragraph at
[results.tex:73](../../manuscript/results.tex#L73)):**

- Comment 2 (noisy measure caveats): all four sources of noise now in
  prose.
- Comment 3 (between-subject analysis): no longer required as a
  mechanism test; the caveat paragraph justifies the within-Punishment
  restriction structurally.
- Comment 8 (pool both treatments): rejected as a category error;
  caveat paragraph makes the case explicitly.

---

# Resolved comments — analyses kept for the record

The numerical work for Comments 2, 3, and 8 is preserved here in case
it's needed for footnotes, robustness appendix, or a future revision.

## §R2 — Belief level by delegation choice (was Comment 2 follow-up)

**Punishment (treat=0), passers (n=61):**

| Variable          | deleg=1 | deleg=0 | diff   | t     | p     |
|-------------------|--------:|--------:|-------:|------:|------:|
| belief_del_good   | 0.679   | 0.439   | +0.240 | +1.32 | 0.194 |
| belief_del_bad    | 0.842   | 0.997   | -0.156 | -1.01 | 0.318 |
| belief_nodel_good | 0.821   | 0.319   | +0.502 | +2.91 | 0.006 |
| belief_nodel_bad  | 0.963   | 1.031   | -0.069 | -0.43 | 0.667 |
| nodel_del_good    | 0.142   | -0.120  | +0.262 | +1.89 | 0.066 |
| nodel_del_bad     | 0.121   | 0.034   | +0.087 | +0.69 | 0.494 |

**No-Punishment (treat=1, hypothetical), passers (n=70):**

| Variable          | deleg=1 | deleg=0 | diff   | t     | p     |
|-------------------|--------:|--------:|-------:|------:|------:|
| belief_del_good   | 0.419   | 0.608   | -0.190 | -1.14 | 0.259 |
| belief_del_bad    | 1.057   | 0.813   | +0.244 | +1.44 | 0.154 |
| belief_nodel_good | 0.353   | 0.340   | +0.013 | +0.09 | 0.931 |
| belief_nodel_bad  | 0.911   | 0.890   | +0.021 | +0.14 | 0.890 |
| nodel_del_good    | -0.066  | -0.268  | +0.202 | +1.59 | 0.117 |
| nodel_del_bad     | -0.146  | 0.077   | -0.223 | -1.28 | 0.206 |

**Reading.** The delegators-vs-non pattern that motivates the §77
paragraph survives only in Punishment; in No-Punishment it's noisier and
partially reversed (`nodel_del_bad` flips sign), consistent with the
"all four scenarios are hypothetical" point now in the caveat paragraph.

## §R3 — Between-subject belief levels by treatment (was Comment 3)

**Full sample:**

| Variable          | Punish | NoPun  | diff   | t     | p     |
|-------------------|-------:|-------:|-------:|------:|------:|
| belief_del_good   | 0.622  | 0.515  | +0.108 | +1.04 | 0.299 |
| belief_del_bad    | 0.923  | 0.893  | +0.030 | +0.30 | 0.768 |
| belief_nodel_good | 0.604  | 0.398  | +0.206 | +2.10 | 0.038 |
| belief_nodel_bad  | 0.979  | 0.871  | +0.108 | +1.15 | 0.250 |
| nodel_del_good    | -0.018 | -0.117 | +0.099 | +1.25 | 0.212 |
| nodel_del_bad     | +0.057 | -0.022 | +0.078 | +0.85 | 0.398 |

**Passers only:**

| Variable          | Punish | NoPun  | diff   | t     | p     |
|-------------------|-------:|-------:|-------:|------:|------:|
| belief_del_good   | 0.534  | 0.500  | +0.034 | +0.29 | 0.771 |
| belief_del_bad    | 0.936  | 0.953  | -0.017 | -0.15 | 0.883 |
| belief_nodel_good | 0.516  | 0.347  | +0.169 | +1.57 | 0.119 |
| belief_nodel_bad  | 1.004  | 0.902  | +0.102 | +0.96 | 0.341 |
| nodel_del_good    | -0.017 | -0.153 | +0.136 | +1.53 | 0.129 |
| nodel_del_bad     | +0.068 | -0.051 | +0.119 | +1.14 | 0.258 |

**Use.** Useful as a footnote/appendix calibration check on
belief-elicitation comparability across arms; not a mechanism test.
The two `nodel_del_*` belief differences are statistically
indistinguishable across treatments, supporting the "channel is
availability, not belief variation" framing of the caveat paragraph.

## §R8 — Pooled-treatment regressions (was Comment 8)

Encoding: `pun = 1` for Punishment; `bel_diff_avg = 0.5 ·
(bel_diff_good + bel_diff_bad)`. Controls: `overall_score, age, female,
socio_status, went_to_uni, technology_score, leader`.

| Spec |                                       | N    | pR²   | pun (b, p)        | bel_diff_avg (b, p) | bel_avg × pun (b, p) |
|-----:|---------------------------------------|-----:|------:|-------------------|---------------------|----------------------|
| A    | Pooled, avg diff × treat              | 159  | 0.054 | -0.796, p=0.019   | +0.309, p=0.614     | +0.348, p=0.700      |
| B    | Pooled, both diffs × treat            | 159  | 0.080 | -0.888, p=0.011   | (see analysis 7)    | (see analysis 7)     |
| C    | Spec A, passers only                  | 130  | 0.090 | -0.930, p=0.018   | -0.252, p=0.719     | +2.326, p=0.047      |

**Use.** Not a mechanism test — see the discussion in the caveat
paragraph and the resolved-Comment-8 stub above. The significant
interaction in Spec C is mechanically expected once you accept that
beliefs only enter the decision rule in the Punishment arm.
