# fig:realized_vs_anticipated — house-style update for review

Applies the five agreed changes (2026-08-10) to the realized-vs-anticipated figure. Not yet in production; `21_realized_vs_anticipated.py` is unchanged until sign-off.

1. Outcome grouping and ordering exactly as in fig:punishment. Same x-positions, tick labels Delegated / Self-decided, second label row Good outcome / Bad outcome, same label-row spacing.
2. Realized punishment recolored from magenta #B65D81 to the moss green #5b7553 of fig:punishment, so Player B's actual punishment wears one color across all figures. Anticipated punishment keeps mint #5DB692, matching the hypothetical appendix figure. Magenta retires to the accent role.
3. Values printed at the base of every bar, white bold.
4. Whiskers capsize 3 and linewidth 1.1, y-axis label "Average punishment (£)", figure size matched to fig:punishment (6.8 x 4.2).
5. No brackets or difference arrows. The overestimation gap and the within-outcome flatness of beliefs carry the message unaided.

## Full sample (body figure)

![new full sample](figs/realized_vs_anticipated_new.png)

## Attention-check passers (appendix figure)

![new passers](figs/realized_vs_anticipated_new_passers.png)

## Current production version, for comparison

![current](../manuscript/figures/realized_vs_anticipated.png)

## Round 2 (2026-08-10) — matched scale, moss at 70% opacity, beliefs in magenta

Per feedback: (a) the y-scale now matches fig:punishment in pounds per inch — the figure keeps the same width (6.8 in) and grows in height by the ylim ratio (1.15/0.8), so a £0.33 moss bar is as tall here as there; (b) the realized-punishment bars are the same moss green at 70% opacity; (c) the anticipated-punishment bars are magenta #B65D81.

Scale caveat for the manuscript: equal pixel scale only survives printing if both figures are included at the same width. fig:punishment uses `width=0.75\linewidth` while fig:realized_vs_anticipated currently uses `0.85\linewidth`, so the include width would need to change to `0.75\linewidth` as well (the figure then also becomes taller on the page, ~44% taller than fig:punishment).

Color caveat: with beliefs in magenta here, the anticipated-punishment bars in the hypothetical appendix figure (currently mint #5DB692, from the same elicitation) would want the same magenta for consistency, and mint would leave the palette.

![v2 full sample](figs/realized_vs_anticipated_v2.png)

![v2 passers](figs/realized_vs_anticipated_v2_passers.png)

## Round 3 (2026-08-10) — full-opacity moss

As Round 2 (matched scale, magenta beliefs) but the realized-punishment bars back at full moss, identical to fig:punishment.

![v3 full sample](figs/realized_vs_anticipated_v3.png)

![v3 passers](figs/realized_vs_anticipated_v3_passers.png)

## Round 4 (2026-08-10) — belief-color candidates alongside moss #5b7553

Four alternatives to magenta for Player A's anticipated punishment; realized punishment stays full moss. Passers variants exist for each (`_passers` suffix).

### Rust #A45A52

![rust](figs/realized_vs_anticipated_v4_rust.png)

### Terracotta #B0713F

![terracotta](figs/realized_vs_anticipated_v4_terracotta.png)

### Plum #6d597a

![plum](figs/realized_vs_anticipated_v4_plum.png)

### Slate #5B7080

![slate](figs/realized_vs_anticipated_v4_slate.png)

## Round 5 (2026-08-10) — brightness ladders for rust and terracotta

Four steps each, lightened from the Round 4 base in even increments (+6% to +24% lightness). Realized punishment stays full moss #5b7553.

### Rust ladder (base #A45A52)

**b1 — #ac6159**

![rust b1](figs/rva_rust_b1.png)

**b2 — #b16a63**

![rust b2](figs/rva_rust_b2.png)

**b3 — #b6746d**

![rust b3](figs/rva_rust_b3.png)

**b4 — #bb7d76**

![rust b4](figs/rva_rust_b4.png)

### Terracotta ladder (base #B0713F)

**b1 — #bb7843**

![terracotta b1](figs/rva_terracotta_b1.png)

**b2 — #bf7f4d**

![terracotta b2](figs/rva_terracotta_b2.png)

**b3 — #c38757**

![terracotta b3](figs/rva_terracotta_b3.png)

**b4 — #c78e62**

![terracotta b4](figs/rva_terracotta_b4.png)

## Round 6 (2026-08-10) — terracotta b1 adopted, bar order swapped

Belief color terracotta b1 (#bb7843); within each scenario the moss realized-punishment bar comes first and the terracotta anticipated bar second. Legend order follows. (An intermediate render of this round used rust b1 by mistake; the images below are terracotta b1.)

![v5 full sample](figs/realized_vs_anticipated_v5.png)

![v5 passers](figs/realized_vs_anticipated_v5_passers.png)

## Adopted: Round 6 (2026-08-10)

Implemented in `21_realized_vs_anticipated.py` (both outputs regenerated; manifest keys unchanged). Note of fig:realized_vs_anticipated updated in results.tex (grouping, colors, in-bar values); both include widths set to `0.75\linewidth` so the pounds-per-inch scale match with fig:punishment holds on the page. The y-axis maximum is 1.15 in both variants. Resolved 2026-08-10: the hypothetical appendix figure's anticipated-punishment bars switched from mint #5DB692 to terracotta #bb7843, so anticipated punishment wears one color everywhere; mint has left the palette. Final color system: moss green #5b7553 = Player B punishment, terracotta #bb7843 = Player A anticipated punishment, gold #C4A54F = share punishing, blue pair #3b6ea8/#8aacd1 = conditions, magenta #9c3a6a = accent (difference arrows).
