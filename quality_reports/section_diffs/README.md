# Section diffs — old draft vs current manuscript

A section-by-section comparison between the original working-draft manuscript
(`old_paper/` outside the project root, used as the snapshot before any edits
were made in this session) and the current manuscript at
[`manuscript/`](../../manuscript/).

The comparison is asymmetric: the **old draft is a working document** with
bullet outlines, ChatGPT-marked paragraphs (`\textcolor{red}`), reference
quotations from other papers (`\textcolor{blue}`), unrealized hypotheses,
TODO notes, and alternative phrasings of the same idea. The **current
manuscript is a polished draft** at submission shape. So most of the
"changes" are about (i) selecting one phrasing from many candidates,
(ii) dropping reference quotations into proper paraphrase or citation, and
(iii) cutting bullet outlines that were planning notes rather than prose.

For each section, the comparison file documents:

1. **Overview** — what the section did then vs now
2. **What changed in the prose** — substantive shifts in framing or content
3. **Dropped items** — every concrete idea, note, quote, TODO, or planned
   analysis that was present in the old draft and is **not** in the current
   manuscript. **This is the load-bearing list** — what to revisit if you
   want to bring something back.

## Index

| File | Section | Old (lines) | New (lines) |
|---|---|---:|---:|
| [01_main_and_abstract.md](01_main_and_abstract.md) | `main.tex` (preamble + abstract) | 131 | 102 |
| [02_introduction.md](02_introduction.md) | `introduction.tex` | 209 | 17 |
| [03_literature.md](03_literature.md) | `literature.tex` | 343 | 37 |
| [04_design.md](04_design.md) | `design.tex` | 104 | 78 |
| [05_results.md](05_results.md) | `results.tex` | 327 | 104 |
| [06_conclusion.md](06_conclusion.md) | `conclusion.tex` | 28 | 21 |
| [07_appendix.md](07_appendix.md) | `appendix.tex` | 97 | 151 |

Line counts are misleading: the new manuscript uses one paragraph per long
line; the old draft uses wrapped lines with many short fragments. Word counts
would be a fairer measure but the reduction is real (the old draft contained
a large amount of notes and quoted material that is not in the new prose).

## How to use

When you want to revisit a dropped item, open the relevant file's "Dropped
items" section. Items are grouped by category (planned analysis, alternative
framing, quoted reference material, design-question note, future-work hint).
Each item carries a short note on **why** it was dropped where I can infer it
(usually: "post-hoc reframing in line with peer review", "merged into a
broader paragraph", or "outside the manuscript's tightened scope").

## Caveat

I have not preserved every single word that was deleted; that would
duplicate the diff. Instead, I focus on **distinct ideas, claims, quotes,
and planned analyses**. If you want a true line-by-line diff, run
`diff -u old_paper/<section>.tex paper/manuscript/<section>.tex` in a terminal.
