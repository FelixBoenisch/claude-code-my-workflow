# `main.tex` and abstract — old vs new

## Overview

The old `main.tex` is the LaTeX shell + abstract + a `\todo` block with the
author's writing timeline. The new `main.tex` keeps the same shell with
small, deliberate updates and a substantially expanded abstract.

## What changed in the prose

### Preamble
- **Author footnote** added: WZB email, "Acknowledgements to be added at submission" (was just "WZB Berlin Social Science Center").
- **Bibliography style** changed: `\bibliographystyle{chicago}` → `\bibliographystyle{aer}` (AEA submission target).
- **Input encoding** changed: `[latin9]{inputenc}` → `[utf8]{inputenc}` (resolves the Marí-Klara character bug in the Burton et al. bib entry).

### Abstract
- **Old (1 paragraph, ~150 words)**: high-level framing — "necessitating a thorough understanding of how decisions involving algorithms are perceived and made". Reports two findings: no difference in punishment between delegated/non-delegated; punishment possibility reduces delegation. Closes with "the ability to use algorithms as a means to shift responsibility is limited, in turn slowing down algorithmic uptake."
- **New (1 paragraph, ~250 words)**: leads with the responsibility-avoidance literature framing; specifies $N=322$ split (161+161); names the design innovation (algorithm calibrated at the individual level); reports the H1 reversal as **"contrary to the preregistered prediction"** with the 17pp gap and two-sided $p=0.049$; reports H2 as **"we cannot reject equal punishment"** with explicit underpowered-against-moderate-effects caveat; presents process ownership as **the candidate hypothesis "most consistent with the data, while flagging that the supporting evidence is exploratory and the design cannot rule out experimenter demand"**; closes with the AI Act / regulatory framing bounded by "Within the bounds of the setting we study".

## Dropped items

### Working notes / housekeeping

- **`\todo[inline]` block with the writing timeline** (lines 90–102 of old `main.tex`). A 5-row table mapping calendar weeks (Jan 2–Feb 1, 2026) to writing milestones. Useful if you want to recreate the original writing schedule for a new draft cycle.
- **`\textcolor{red}{chatGPT}` and `\textcolor{blue}{Feier et al}` color-key markers** at lines 105–106. These flagged whose ideas/text fragments were chatGPT-generated vs Feier-quoted in the rest of the draft.
- **`\printinunitsof{pt}\prntlen{\textwidth}` and `\printinunitsof{pt}\prntlen{\textheight}`** at lines 87–88. Layout-debugging artefacts.

### Abstract framing options not retained

- **"Algorithms are becoming ubiquitous in decision-making, necessitating a thorough understanding of how decisions involving algorithms are perceived and made."** — the punchy opening of the old abstract. The new abstract leads instead with the responsibility-avoidance-literature frame.
- **"slowing down algorithmic uptake"** — the explicit closing claim that limited blame-shifting slows adoption. Tightened in the new abstract to the more bounded "may discipline algorithmic adoption rather than merely allocate post-hoc responsibility".

### JEL classification + keywords

- **Old:** `JEL Classification: asdf` and `Keywords: asdf` (literal placeholders).
- **New:** `JEL: C91, D81, D91, O33`; `Keywords: algorithms; delegation; responsibility; punishment; experiment`.

(Not really "dropped" — completed.)

## Why the changes (where I can infer)

- The author footnote, AEA bibstyle, and abstract reframe came from the `--peer AER` review's editor + methods-referee feedback (especially: bound the policy framing, hedge mechanism, switch to AEA style).
- The utf8 encoding change came from a hard compile error (latin9 cannot render the `Marí-Klara` character in the Burton et al. bib entry).
- The `\todo` writing timeline was for the author's own planning and naturally drops out of a polished draft.
