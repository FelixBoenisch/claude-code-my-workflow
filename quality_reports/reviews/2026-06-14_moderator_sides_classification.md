---
title: Classifying the algorithm-aversion corpus into the "algorithm / task / control" sides
date: 2026-06-14
scope: supports literature.tex lines 33–37 (the three-side moderator split). No manuscript text changed.
method: read the curated per-paper summaries (verified against the PDFs) for every algorithm-use / algorithm-aversion paper in master_supporting_docs/supporting_papers/, plus the review/meta papers (Burton 2020, Qin 2025, Sunstein 2024) to bound the taxonomy. Direction of each effect checked against the paper's own result.
---

# Which corpus papers fit "algorithm side / task side / control side"

Lines 33–37 currently read:

> **algorithm side**: aversion stronger when the algorithm cannot be observed to learn (Berger) and when reasoning is opaque (Litterscheidt, Sharan)
> **task side**: aversion rises with irreducible uncertainty (Dietvorst 2020), perceived subjectivity (Castelo), loss framing (Bockstedt); reliance rises with difficulty (Bogert)
> **control side**: people use imperfect algorithms more when they can modify the output (Dietvorst 2018)

Below: the papers that fit **well**, the ones currently cited that **do not** fit (with the reason), and corpus papers that belong to a **different bucket** (so you don't force-fit them). "Direction" matters here — some of these are *appreciation* (use rises) rather than *aversion* (use falls), and one current citation has the sign backwards.

---

## ALGORITHM SIDE — properties of the algorithm itself

| Paper | Specific moderator | Direction | Fit | In bib? |
|---|---|---|---|---|
| `berger_watch_2021` | algorithm not seen to learn / improve | aversion ↑ (offset when learning shown) | **Strong** — keep | cited |
| `liu_when_2021` | machine-*learned* (opaque) rules vs human-made rules; transparency works only if meaningful | distrust ↑ for opaque ML; transparency ↓ it contingently | **Strong — add.** This is the real "opacity" citation; currently mis-shelved in ¶25 (responsibility strand) | cited (¶25) |
| `dietvorst_algorithm_2015` | confidence collapses after seeing the algorithm err | aversion ↑ | **Strong** — it is itself an algorithm-behaviour moderator, not just the seminal anchor; could be cited here too | cited (¶28) |
| `kormylo_till_2025` | algorithms can't "betray" — trust-violation depresses human-advisor uptake but not algorithmic | aversion ↑ for humans, not algorithms | **Strong** (algorithm-specific property) — already in my earlier S-6 proposal | cited |

**Do NOT keep on the algorithm side (current miscites):**
- `litterscheidt_financial_2020` — cited at line 33 for "opaque reasoning." The paper is about **financial education raising robo-advisor delegation**; its transparency finding is that *informationally meaningful* education increases use, not that opacity drives aversion. Supports the opposite framing at best, and via a different manipulation. **Remove from the opacity clause.**
- `sharan_dont_2020` — also cited at line 33 for "opaque reasoning." The paper actually finds **algorithm *appreciation*** (AI preferred to human advice) and that **personality / locus of control** moderate trust. It is a *person-side* moderator, not an algorithm-opacity result. **Remove from the opacity clause** (relocate — see "different bucket" below).
- `stein_dont_2020` — still in the old line-30 mega-sentence for "complexity." Flagged `[NOT FOUND]` / possibly fabricated in the bib. **Drop entirely.** (If you want the complexity moderator, it is real in the literature — but needs a verified source; none is in the folder.)

→ Suggested algorithm-side citation set after cleanup: **Berger (learning) · Liu (opacity/ML rules) · Kormylo (betrayal asymmetry)**, optionally Dietvorst 2015 (post-error aversion).

---

## TASK SIDE — properties of the task / decision

| Paper | Specific moderator | Direction | Fit | In bib? |
|---|---|---|---|---|
| `dietvorst_people_2020` | irreducible outcome uncertainty (diminishing sensitivity to error) | aversion ↑ | **Strong** — keep | cited |
| `castelo_task-dependent_2019` | perceived subjectivity of the task (vs objective) | aversion ↑ for subjective | **Strong** — keep | cited |
| `bogert_humans_2021` | task difficulty | **reliance ↑** (appreciation, not aversion) | **Strong** — keep, but it is an *appreciation* result; line 35 already phrases it as "reliance increases," which is correct. Do **not** lump it under "subjectivity" as the old line 30 did | cited |
| `bockstedt_humans_2025` | gain-vs-loss framing | **delegation ↑ under loss framing** (aversion *reverses*) | **Strong fit, but the SIGN IS WRONG in line 35.** Line 35 says "aversion rises with loss framing"; the paper finds loss framing *increases* AI delegation. Fix the direction. PDF not in folder — summary is abstract-based, so verify against the published paper before relying on it | cited |

**Borderline / better placed elsewhere:**
- `niszczota_robo-investors_2020` — aversion to robo-investing, **amplified by moral content** of the portfolio. This is a *moral-domain* result; it fits the task side only if you treat "moral content" as a task property. It reads more naturally in strand 3 (moral domain), where it is currently cited (¶21). Keep there; don't double-count on the task side.

→ Suggested task-side citation set: **Dietvorst 2020 (uncertainty) · Castelo (subjectivity) · Bogert (difficulty → reliance)**, plus Bockstedt **with corrected direction** (loss framing → more delegation).

---

## CONTROL SIDE — the decision-maker's retained agency

| Paper | Specific moderator | Direction | Fit | In bib? |
|---|---|---|---|---|
| `dietvorst_overcoming_2018` | even *token* ability to modify the algorithm's output | use ↑ sharply | **Strong** — keep; this is the cleanest control-side result | cited |
| `ivanova_stenzel_measuring_2024` | willingness to *cede control* (menu-based elicitation) | heterogeneous | **Strong conceptually**, but this is the anchor of the separate "ceding decision control" paragraph I proposed (S-6b). Decide whether it lives on the control side here or in that paragraph — don't cite it in both | cited (¶39, commented) |
| `ivanova_stenzel_delegating_2025` | under-delegation to *both* AI and human = general preference for **decision autonomy** | autonomy preference ↓ delegation | **Strong conceptually**, same overlap caveat | in bib, unused |

Note: the control side is the best-attested category in the *review* literature — it is Burton's "decision autonomy" theme and Sunstein's "desire for agency/control" mechanism (see below). So a control-side clause is well-founded even though only Dietvorst 2018 sits cleanly inside it among the *primary* papers; the Ivanova-Stenzel pair extends it but overlaps with the full-delegation sub-strand.

→ Suggested control-side citation: **Dietvorst 2018 (modifiability)**; optionally fold in the autonomy-preference point (Ivanova-Stenzel) if you are *not* giving it a separate paragraph.

---

## Corpus papers that do NOT fit any of the three sides (don't force them in)

These are real moderators or findings, but they belong to a **decision-maker / person side** or to another strand. Flagging so they are not swept into the three-side sentence:

| Paper | What it actually is | Where it belongs |
|---|---|---|
| `sharan_dont_2020` | personality (Big Five) + locus of control moderate trust; finds AI *appreciation* | **person side** — individual differences, not algorithm/task/control |
| `goldbach_geht_2019` | extraversion predicts delegation; delegation only ~10% in a non-moral route-choice task | **person side** (and a low-delegation data point) |
| `logg_algorithm_2019` | the *appreciation* anchor; appreciation wanes vs one's *own* judgement and **for experts** | the contrast that opens the strand; the "experts rely less" part is **person side** |
| `newman_eliminating_2020` | algorithmic HR decisions seen as less *procedurally fair* (reductionism) | **strand 3** (perceptions/fairness), an outcome, not a use-moderator |
| `niszczota_robo-investors_2020` | robo-aversion amplified by moral content | **strand 3** (moral domain) |
| `dargnies_aversion_2026` | three findings: transparency-about-internals **null** (algorithm side), **gender-profiling** driver (domain), manager **overconfidence** lowers delegation / feedback raises it (person side) | **spans buckets** — cite selectively: the transparency-null can sit on the algorithm side, the overconfidence result is person side. Don't cite it as a single "side" |

**Structural implication.** The three "sides" cleanly cover algorithm / task / control, but two recurring moderator families fall outside them: (i) a **decision-maker / person side** (expertise, personality, locus of control, overconfidence — Logg, Sharan, Goldbach, Dargnies), and (ii) an **expectations / asymmetric-forgiveness** family (Dietvorst 2015's core: people forgive algorithmic error less). Because line 28–35 is a "for example" list rather than an exhaustive taxonomy, you have two clean options:
1. **Keep three sides**, relocate the person-side papers (Sharan, Goldbach) out of the moderator sentence, and let Logg stay as the appreciation anchor. (Simplest; my recommendation.)
2. **Add a short fourth clause** ("and on the decision-maker side, with expertise and overconfidence — \citealp{logg_algorithm_2019,dargnies_aversion_2026}") if you want the person-side represented.

---

## Cross-check against the review/meta papers (these bound the taxonomy)

The three-side split is consistent with how the surveys in your own bib organize the field — which is reassuring, and worth a one-clause signpost:

- **Burton, Stein & Jensen (2020)** — five themes: *expectations & expertise · decision autonomy (= control side) · incentivization · cognitive compatibility · divergent rationalities*. "Decision autonomy" = your control side; "cognitive compatibility/divergent rationalities" ≈ algorithm side.
- **Sunstein & Gaffe (2024)** — five mechanisms: *agency/control (= control side) · moral/emotional reaction (≈ moral-content task side) · belief in unique human knowledge · ignorance/opacity (= algorithm side) · asymmetric forgiveness (= algorithm-behaviour side)*.
- **Qin et al. (2025)** meta-analysis — **capability × personalization-need** framework: "capability" maps to algorithm-side + task-difficulty; "personalization need" maps to task-side (subjective/moral tasks). 442 effect sizes; appreciation in the high-capability/low-personalization quadrant only.

None of these surface an additional *primary* moderator paper in your folder beyond those classified above; they mainly confirm the buckets and add the person-side and expectations families that sit outside the three sides.

---

## One-line summary of recommended changes to lines 33–37 (for when you do edit)

1. **Algorithm side:** Berger + Liu + Kormylo (drop Litterscheidt and Sharan — both miscited for opacity; drop stein_dont_2020 from line 30).
2. **Task side:** Dietvorst 2020 + Castelo + Bogert, and **fix Bockstedt's direction** (loss framing → *more* delegation, not more aversion).
3. **Control side:** Dietvorst 2018; optionally the Ivanova-Stenzel autonomy point (but don't double-cite it with the full-delegation paragraph).
4. **Relocate** Sharan/Goldbach (person side), keep Niszczota/Newman in strand 3.
5. **Delete the duplicate** old mega-sentence at line 30 (lines 33–37 supersede it).
