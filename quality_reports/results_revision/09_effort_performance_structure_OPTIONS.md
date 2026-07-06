---
title: "Structuring the performance/effort arguments in the Discussion subsection"
date: "2026-07-05"
scope: "The blocks currently ordered: Anticipated punishment → Effort → Selection on performance & process ownership"
status: "Decision document — sketches all orderings, their logical dependencies, required stitches, and a recommendation"
---

# 1. The problem, stated precisely

The effort dispatch compares performance *improvements* (rounds 1–10 error vs. final-prediction error) across conditions. That comparison is valid only if the rounds 1–10 baseline is comparable across conditions — same incentives, same (expected) effort. The current draft order presents the effort block **before** any discussion of baseline performance, so the argument leans on an unstated premise. That is a real gap in the draft as ordered.

Two facts can close it, and the stronger one is currently used **nowhere** in the manuscript's discussion:

- **F1 (by design).** During the first ten rounds, subjects had not yet learned of Player B, the delegation option, or the punishment possibility, and faced identical private incentives (£4/£2) in both conditions. Baseline effort therefore *cannot* differ by treatment, up to sampling noise. (Design section, Player A procedure.)
- **F2 (empirically).** Rounds 1–10 scores are balanced across conditions (2.93/10 on average, indistinguishable; `fig:performance`), as is overconfidence.

F1 is the airtight card — it converts "the baselines happen to look similar" into "the baselines could not have differed." Whichever structure is chosen, F1 should be stated once, explicitly.

A useful reframing that any option can use: the ten rounds are the *treatment-blind* baseline (same private stakes, no knowledge of the manipulation), while the final prediction is the *treatment-exposed* round (no private stakes; punishment stakes only in one arm). The improvement measure is exactly the within-subject contrast between the two, so its cross-arm difference isolates the effect of the punishment prospect on effort — up to selection into non-delegation, which is what the subgroup balance (3.12 vs. 2.98, p=0.66) and the endogeneity footnote handle.

# 2. Inventory of performance/effort facts and who needs them

| # | Fact | Needed by |
|---|------|-----------|
| F1 | Treatment revealed only after round 10 → baseline treatment-blind by design | Effort (baseline validity); Artifact check |
| F2 | Rounds 1–10 scores + confidence balanced across conditions | Effort; Artifact check; precondition for interpreting the gradient |
| F3 | Treatment effect robust to performance/confidence controls (Table 1, (3)–(4)) | Artifact check |
| F4 | Within-*Punishment* gradient: better performers delegate less; none in *No-Punishment* | Selection/ownership |
| F5 | Delegator composition: 2.47 vs. 3.06 (p=0.039); extra *No-Punishment* delegators from mid/upper | Selection/ownership |
| F6 | Actual performance discriminates delegators/non-delegators, perceived does not (2.38/3.00 vs. 4.69/4.71) | Selection/ownership |
| F7 | Improvement (rounds 1–10 → final) among non-delegators: *No-Punishment* improves, *Punishment* does not; same image | Effort |
| F8 | Non-delegator outcomes 45.5% vs. 21.7%; subgroup ex-ante balance 3.12 vs. 2.98 (p=0.66) | Effort |
| F9 | Punishment beliefs uncorrelated with performance; no good/bad asymmetry difference (appendix) | Selection/ownership (not belief-mediated) |
| F10 | EU benchmark: individual-level, common-knowledge calibration → no gradient predicted | Selection/ownership (the interpretive lever) |

**The two structural dependencies that create the ordering problem:**

- **D1.** Effort needs F1/F2 (baseline comparability) → performance foundations must precede the effort block *in some form*.
- **D2.** The EU-benchmark step (F10) presumes the two options are perceived as equivalent; the effort channel (believing one can beat one's own record) is precisely the escape from that equivalence → the gradient *interpretation* is cleanest after effort is dispatched.

D1 pulls performance material before effort; D2 pulls effort before the gradient *interpretation*. Any structure must satisfy both or pay for the violation with a forward hedge.

# 3. The options

### Option 1 — as drafted: Anticipation → Effort → [Balance → Gradient → Ownership]

**Chain:** instrumental channels first (anticipation, then effort), then the preference account as survivor.

- Satisfies D2; violates D1 as written (Felix's point).
- **Fix within this option:** open the effort block's evidence paragraph with F1+F2 in two sentences, e.g.:
  > "Two features make this a clean test. The punishment manipulation was revealed only after the ten rounds, so baseline performance is unaffected by treatment by design — and it is balanced empirically ($2.93$ correct predictions on average in both conditions; Figure~\ref{fig:performance}). The final prediction, by contrast, is made with the manipulation in full view."
  The selection block's opener then *references* rather than restates balance ("Result~1 is, as noted, no artifact of sample composition...").
- Pros: minimal change from the draft; survivor stays adjacent to Taking stock; D2 satisfied without any hedge.
- Cons: the balance facts debut inside the effort block, where they read as serving effort only; the "what Result 1 is *not*" framing weakens slightly.

### Option 1b — dedicated foundation block: Anticipation → **Baseline comparability** (short) → Effort → [Gradient → Ownership]

**Chain:** after anticipation is dispatched, a 3–4 sentence block establishes F1+F2+F3 once, explicitly serving *everything* that follows; then effort; then selection/ownership.

- Sketch of the foundation block:
  > "\paragraph{A preliminary: performance across conditions.} The remaining candidates all involve Player~A's task performance, so we first establish what it can and cannot explain. The punishment manipulation was revealed only after the first ten rounds, so baseline performance is unaffected by treatment by design, and it is balanced empirically ($2.93$ correct out of ten in both conditions; Figure~\ref{fig:performance}), as is Player~A's confidence in her own performance. Result~1 is therefore not an artifact of sample composition---consistent with the treatment effect surviving performance and confidence controls (Table~\ref{tab:del_decision_determinants}, Columns~(3)--(4)). What performance *can* do is shape behavior within conditions, and the next two candidates use it in exactly that way."
- Satisfies D1 (foundations precede effort) and D2 (effort precedes gradient interpretation).
- Pros: F1/F2 stated once, serving both downstream blocks; the artifact concern is dispatched early (referee comfort); both later blocks start clean.
- Cons: one more block header; the anticipation→effort adjacency breaks (mild — the link is one footnote); the "balanced across, yet selected within" springboard is split across blocks, though the gradient block can still echo it in one clause ("Performance is balanced *across* conditions; what differs is who delegates *within* them.").

### Option 2 — performance first, effort last: Anticipation → [Balance → Gradient → Ownership] → Effort

**Chain:** all performance material (artifact check, gradient, composition, ownership interpretation) before effort.

- Satisfies D1 trivially; violates D2 — the EU-benchmark step runs while the beat-my-own-record escape is still open.
- **Required stitch:** a forward hedge inside the ownership block, e.g. "...unless Player~As believe they can outperform their own record through effort, a possibility we test — and reject — below." (A verdict-promising forward reference; the kind of dangling flank the current order avoids.)
- Pros: performance is fully developed before the effort block ever touches it; the effort block's selection caveat lands on prepared ground (the reader already knows delegation is performance-selected in *Punishment*).
- Cons: the constructive account is interrupted by its own caveat; the empirical part of the section ends on a dispatched channel, so Taking stock must reach back over the effort block to the survivor; two blocks now forward-reference each other.

### Option 3 — evidence first, interpretation after effort: Anticipation → Balance → **Gradient & composition (descriptive)** → Effort → **Ownership (interpretation)**

**Chain:** establish the performance *facts* (balance; gradient; delegator composition) as descriptive findings; then test effort — which, once the gradient is on the table, is motivated twice over (it is a candidate explanation for Result 1 *and* a rational explanation for the gradient); then interpret what survives (EU benchmark → not belief-mediated → not perceived ability → process ownership).

- Satisfies D1 (balance and the descriptive facts precede effort) *and* D2 (interpretation follows the effort dispatch). No forward hedge needed anywhere.
- The effort block gains a motivation sentence: "The gradient itself suggests a rational version of this story: if better performers believe they can beat their own record, both the gradient and Result~1 could reflect effort rather than preference." Killing effort then does double duty, and the ownership block opens with "With effort ruled out, the gradient must reflect something else."
- Pros: the most logically integrated order — every block's premise is on the table before it is used, and every dispatch pays off twice; survivor still lands last, adjacent to Taking stock.
- Cons: the most rewriting relative to the current text; the reader carries the uninterpreted gradient across the effort block (about two paragraphs — tolerable, and the effort block explicitly holds the thread); the selection block splits into two headers or one long one.

### Option 4 — status quo of the manuscript (for completeness): Beliefs → Gradient → Ownership → Uncertainty → Balance → Effort

- Violates D2 (ownership interpreted before effort is closed) *and* stages balance after the gradient interpretation (the May review's F8 objection). Both later blocks lean on facts established after them. Not recommended; listed only as the baseline being replaced.

# 4. Comparison at a glance

| | D1 (baseline before effort) | D2 (effort before gradient interpretation) | Forward hedges needed | Rewriting effort | Survivor adjacent to Taking stock |
|---|---|---|---|---|---|
| 1 (as drafted + fix) | via in-block stitch | yes | none | small | yes |
| 1b (foundation block) | yes, cleanly | yes | none | small–medium | yes |
| 2 (performance first) | yes | **no** | one (ownership → effort) | medium | no |
| 3 (evidence → effort → interpretation) | yes | yes | none | largest | yes |
| 4 (status quo) | no | no | — | — | no |

# 5. Recommendation

**Option 1b** as the default: it fixes the gap at its root (one foundation block stating F1+F2+F3, serving everything downstream), keeps both dependencies satisfied without hedges, and costs only a short new block plus two adjusted openers. **Option 3** is the better structure in the abstract — every argument's premises precede it and the effort dispatch is motivated twice — and is worth choosing if you are rewriting these blocks from scratch anyway (which, mid-rewrite, you partly are). Option 2 is workable but pays for performance-first with a dangling verdict-promise inside the constructive block, which is the kind of flank the restructure was meant to eliminate.

Independent of the choice: **state F1 explicitly, once.** "The punishment manipulation was revealed only after the ten rounds" is the strongest sentence available for this whole part of the paper and currently appears nowhere in the discussion. It upgrades the baseline from "balanced" to "could not have differed," and it is also the cleanest justification for calling the ten rounds a baseline at all.
