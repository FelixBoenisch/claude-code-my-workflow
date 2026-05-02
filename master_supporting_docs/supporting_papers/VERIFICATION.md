# Bibliography verification — full report

**Date:** 2026-05-02
**Verification methods:**
- Crossref API (`api.crossref.org`) for every entry with a DOI — author, title, journal, year, volume, pages
- Forked `claim-verifier` subagent for entries without DOIs — web search + publisher pages
- Unpaywall API (`api.unpaywall.org`) for open-access PDF discovery + direct download
- Direct fetches from RePEc / author personal pages where Unpaywall returned paywalled

**Total entries:** 48
**Cited in manuscript:** 46 (`trunk_current_2020` and `heaton_social_2023` carried but not currently `\cite`d)

---

## What I found

### Hallucination by me (this session): 1 instance, in markdown reports only
- I wrote "Feier, Powell-Hetschko & Marsden 2022" in [`quality_reports/lit_review_algorithms_responsibility.md`](../../quality_reports/lit_review_algorithms_responsibility.md) and [`quality_reports/peer_review_algorithms_and_responsibility/referee_domain.md`](../../quality_reports/peer_review_algorithms_and_responsibility/referee_domain.md). The actual authors are **Feier, Gogoll, Uhl** — and the bib entry `feier_hiding_2022` had them correctly. I confidently wrote wrong narrative text while the underlying source was correct. **Fixed in both files; the manuscript itself was never affected** because it uses `\citet{feier_hiding_2022}` which renders from the bib.

### Pre-existing problems in the bib (carried over from the original draft, all flagged with `note = {VERIFY}`):

| Entry | Original bib status | What was wrong | Fix applied |
|---|---|---|---|
| `stein_dont_2020` | flagged VERIFY | Title and authors **could not be located** in any indexed database. Likely fabricated by an earlier session. | Title prefixed with `[NOT FOUND]`; strong `note = {VERIFY}` recommending the citation be dropped or replaced. **Cited in [literature.tex](../../manuscript/literature.tex) — needs your decision before submission.** |
| `liu_when_2021` | flagged VERIFY | Severely wrong: nonexistent co-author "Du, Yu" and a title not matching any indexed Bingjie Liu paper. | Replaced with the most likely intended paper (Liu 2021 JCMC, "In AI we trust?"). Carries a `VERIFY` note asking for confirmation. |
| `goldbach_geht_2019` | flagged VERIFY | German title cannot be located. The only documented 2019 paper by these four authors is on route choice, different topic. | Replaced with the route-choice paper (Transportation Research Part F). Carries a `VERIFY` note. |
| `kurtzberg_attribution_2004` | flagged VERIFY | Title doesn't match any 2004 Naquin-Kurtzberg paper. Author order also reversed. | Replaced with the standard Naquin & Kurtzberg 2004 OBHDP paper. Carries a `VERIFY` note. |
| `jauernig_people_2022` | flagged VERIFY | Title was paraphrased, not the actual title. | Title corrected to "People Prefer Moral Discretion to Algorithms..." (Phil & Tech 2022). DOI added. |
| `niszczota_robo-investors_2020` | flagged VERIFY | Title was paraphrased. Wrong journal. | Title corrected to "Robo-investment aversion" (PLoS ONE 2020). DOI added. |
| `shank_attributions_2019` | flagged VERIFY | Title and venue wrong. | Corrected to "When are AI versus human agents faulted for wrongdoing?" (Information, Communication & Society 22(5)). DOI added. |
| `sharan_dont_2020` | flagged VERIFY | Author given names wrong (Neha N. → **Navya Nishith**; Donatella M. → **Daniela Maria**). | Author names corrected. DOI added. |

### Verified clean (or after only adding DOI):

`feier_hiding_2022`, `bartling_shifting_2012`, `coffman_intermediation_2011`, `hamman_self-interest_2010`, `oexl_shifting_2013`, `steffel_passing_2016`, `hill_does_2015`, `dietvorst_algorithm_2015`, `logg_algorithm_2019`, `burton_systematic_2020`, `chugunova_we_2022`, `mahmud_what_2022`, `gogoll_rage_2018`, `kirchkamp_sharing_2019`, `maasland_blame_2022`, `weaver_politics_1986`, `fiorina_legislator_1986`, `berger_watch_2021`, `litterscheidt_financial_2020` (verified despite suspicious-sounding title — the "black box" is the robo-advisor algorithm), `bigman_people_2018`, `dietvorst_people_2020`, `dietvorst_overcoming_2018`, `castelo_task-dependent_2019`, `bogert_humans_2021`, `erat_avoiding_2013` (verified as published JEBO paper, not working paper), `pezzo_pezzo_physician_2006`, `tobia_when_2021`, `chen_otree_2016`, `holt_risk_2002`, `de_quidt_measuring_2018`, `benabou_identity_2011`, `falk_morals_2013`, `newman_eliminating_2020`, `bockstedt_humans_2025`, `ivanova_stenzel_measuring_2024`, `kobis_delegation_2025` (after the prior claim-verifier corrected author list and pages), `chevrier_algorithm_2024` (verified Mathieu Chevrier and Vincent Teixeira, not "Marion / Marina" as I'd initially written; working paper, no DOI).

---

## Open decisions for Felix

These are bib entries where the verifier's correction is a best-guess. Please confirm or override:

1. **`stein_dont_2020`** — currently cited in [literature.tex:21](../../manuscript/literature.tex). The cited paper does not appear to exist. Options:
   - (a) Drop the `\citep{stein_dont_2020}` from the literature section (would leave the surrounding sentence about "complexity of the algorithm" without a supporting reference — could replace with `\citep{castelo_task-dependent_2019}` or similar).
   - (b) Provide the original source (working paper, conference paper, German source) and I'll re-create the bib entry.

2. **`liu_when_2021`** — currently cited in [literature.tex:25](../../manuscript/literature.tex). I replaced the original (nonexistent) entry with the most likely intended paper:
   > Liu, B. (2021). "In AI we trust? Effects of agency locus and transparency on uncertainty reduction in human–AI interaction." *Journal of Computer-Mediated Communication*, 26(6), 384–402.

   Confirm this is the paper you meant.

3. **`goldbach_geht_2019`** — currently cited in [literature.tex:21](../../manuscript/literature.tex). I replaced the German-titled entry (which couldn't be found) with the only indexed 2019 paper by these four authors:
   > Goldbach et al. (2019). "Transferring decisions to an algorithm: A simple route choice experiment." *Transportation Research Part F*, 65, 402–417.

   Different topic from "moral domain" — confirm or supply the German working paper.

4. **`kurtzberg_attribution_2004`** — currently cited in [literature.tex:25](../../manuscript/literature.tex). The original bib title doesn't match any indexed paper. I replaced with the standard:
   > Naquin & Kurtzberg (2004). "Human reactions to technological failure..." *OBHDP*, 93(2), 129–141.

   Note the author order is reversed from your original bib. Confirm.

---

## PDFs in this folder

13 PDFs were retrieved (Unpaywall + direct fetches from author pages and RePEc). For everything else, the DOI is in the bib so you can pull from your university subscription. See [`DOWNLOAD_LOG.md`](DOWNLOAD_LOG.md) for the per-paper status.

### Successfully downloaded (open-access)

| File | Source |
|---|---|
| `feier_hiding_2022.pdf` | Springer (Science and Engineering Ethics) |
| `coffman_intermediation_2011.pdf` | Open-access mirror |
| `berger_watch_2021.pdf` | Springer (BISE) |
| `bogert_humans_2021.pdf` | Nature Scientific Reports |
| `jauernig_people_2022.pdf` | Springer (Philosophy & Technology) |
| `niszczota_robo-investors_2020.pdf` | PLoS ONE |
| `tobia_when_2021.pdf` | Journal of Nuclear Medicine |
| `de_quidt_measuring_2018.pdf` | NBER working paper version |
| `kobis_delegation_2025.pdf` | Nature |
| `maasland_blame_2022.pdf` | Frontiers in Psychology |
| `trunk_current_2020.pdf` | Springer (Business Research) |
| `erat_avoiding_2013.pdf` | Author page (sanjiverat.com) |
| `ivanova_stenzel_measuring_2024.pdf` | TU Berlin RaC working paper version |

### Paywalled (DOI in bib; access via your university subscription)

`bartling_shifting_2012`, `hamman_self-interest_2010`, `oexl_shifting_2013`, `steffel_passing_2016`, `hill_does_2015`, `dietvorst_algorithm_2015`, `logg_algorithm_2019`, `burton_systematic_2020`, `chugunova_we_2022`, `mahmud_what_2022`, `gogoll_rage_2018`, `kirchkamp_sharing_2019`, `litterscheidt_financial_2020`, `sharan_dont_2020`, `bigman_people_2018`, `dietvorst_people_2020`, `dietvorst_overcoming_2018`, `castelo_task-dependent_2019`, `goldbach_geht_2019`, `kurtzberg_attribution_2004`, `pezzo_pezzo_physician_2006`, `liu_when_2021`, `shank_attributions_2019`, `holt_risk_2002`, `benabou_identity_2011`, `falk_morals_2013`, `newman_eliminating_2020`, `bockstedt_humans_2025`.

### Not retrievable in this session

- `stein_dont_2020`: paper doesn't appear to exist (see above).
- `chevrier_algorithm_2024`: GREDEG WP 2024-04. Direct PDF URLs returned errors. Available manually at [https://ideas.repec.org/p/gre/wpaper/2024-04.html](https://ideas.repec.org/p/gre/wpaper/2024-04.html).
- `european_union_ai_act_2024`: legal regulation, no DOI; available at [Official Journal of the EU](https://eur-lex.europa.eu/eli/reg/2024/1689/oj).
- `chen_otree_2016`: Unpaywall returned a DOI redirect that didn't resolve to a PDF. Direct via Elsevier or possibly an author preprint.
- `weaver_politics_1986`, `fiorina_legislator_1986`: 1986 papers, paywalled.

---

## Process improvements going forward

After this incident, two changes I'm now applying:

1. **Always Crossref-verify before writing prose.** When I cite an author by name in narrative text, I cross-check the bib entry every time, not just my memory.
2. **The original bib carried unverified entries from a prior session.** Any new bib additions in this session were Crossref-verified by the `claim-verifier` subagent before merging. This is the standard going forward.

A `verify_bib.py` script lives at [`scripts/python/_outputs/verify_bib.py`](../../scripts/python/_outputs/verify_bib.py) and a `download_papers.py` at [`scripts/python/_outputs/download_papers.py`](../../scripts/python/_outputs/download_papers.py). Both can be re-run after any bib change.
