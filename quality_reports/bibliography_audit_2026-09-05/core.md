# Bibliography audit — core assignment

As of 2026-09-05. Proposal only; bibliography and manuscript files were not edited.

Coverage: 30 entries, 18 currently cited. All 30 are already recorded as published journal/proceedings papers and their publication status is confirmed; no working-paper-to-journal conversion is needed in this assignment. One factual correction (uncited), four optional enrichments.

Verification compared author identity/order and spelling, full title, journal/proceedings, final year, volume, issue when applicable, page range/article number, DOI, entry type, and existing month/ISSN where present. Publisher-deposited DOI metadata was fetched individually for 29 entries; the remaining Fiorina entry was verified on OUP. Raw evidence: `core_crossref.json`. Earlier online years were distinguished from final issue years. Bibliographic title capitalization, valid TeX accents, DOI capitalization, and article-number storage in `pages` are not treated as factual errors. Local Zotero file links, historical access dates, abstract text and research-claim annotations are outside metadata verification.

## Planned changes for review

| Entry | Cited? | Planned change | Priority |
|---|---|---|---|
| `bartling_shifting_2012` | Yes | `author`: Bartling, B. and Fischbacher, U. → Bartling, Bj{\"o}rn and Fischbacher, Urs. Optional consistency only: expand correct initials using published PDF. No author identity/order error. | Optional |
| `heaton_social_2023` | No | `articleno`: missing → 11. Optional ACM proceedings locator completion; existing 1–11 page range is correct. Use only a field supported by bibliography style. | Optional |
| `fiorina_legislator_1986` | Yes | `doi`: missing → 10.1093/oxfordjournals.jleo.a036905. Optional missing persistent identifier, verified on OUP article page. | Optional |
| `litterscheidt_financial_2020` | No | `author`: Litterscheidt, Roman and Streich, David J. → Litterscheidt, Rouven and Streich, David J.. Necessary correction: first author’s given name is Rouven, not Roman. | Correction |
| `bogert_humans_2021` | No | `number`: missing → 1. Optional issue completion from publisher-deposited Crossref; Nature recommended citation uses volume and article number without issue. | Optional |

No automatic title/key substitutions are proposed. The existing Goldbach annotation about the intended source should remain pending author clarification. For Heaton, Edinburgh is the verified conference venue; New York is ACM’s publisher location. Changing the address convention would be optional and is not included among the proposed field changes.

## Individual verification ledger

### `feier_hiding_2022` — cited

Till Feier; Jan Gogoll; Matthias Uhl (2022). Hiding Behind Machines: Artificial Agents May Help to Evade Punishment. Science and Engineering Ethics, 28(2): Article 19. DOI: 10.1007/s11948-022-00372-7.

Published 4 April 2022; 19 is the article number, not a single-page citation. Issue 2 confirmed in publisher-deposited Crossref metadata.

Outcome: **verified_no_change**.

Evidence: [Springer article and citation metadata](https://link.springer.com/article/10.1007/s11948-022-00372-7); [Publisher-deposited Crossref metadata (retrieved 2026-09-05)](https://api.crossref.org/works/10.1007/s11948-022-00372-7).

### `bartling_shifting_2012` — cited

B. Bartling; U. Fischbacher (2012). Shifting the Blame: On Delegation and Responsibility. The Review of Economic Studies, 79(1): 67–87. DOI: 10.1093/restud/rdr023.

Online 8 August 2011; final issue January 2012. Keep year 2012. Publisher metadata uses initials; published PDF supplies full given names.

Outcome: **verified_optional_enrichment**.

- Optional consistency only: expand correct initials using published PDF. No author identity/order error. `author`: `Bartling, B. and Fischbacher, U.` → `Bartling, Bj{\"o}rn and Fischbacher, Urs`.

Evidence: [Published article in institutional archive](https://doc.rero.ch/record/290015/files/rdr023.pdf); [Author institutional publication list](https://www.econ.uzh.ch/en/people/faculty/bartling/research.html); [Publisher-deposited Crossref metadata (retrieved 2026-09-05)](https://api.crossref.org/works/10.1093/restud/rdr023).

### `coffman_intermediation_2011` — cited

Lucas C Coffman (2011). Intermediation Reduces Punishment (and Reward). American Economic Journal: Microeconomics, 3(4): 77–106. DOI: 10.1257/mic.3.4.77.

November 2011 issue. The missing period after middle initial C is typographic normalization only.

Outcome: **verified_no_change**.

Evidence: [American Economic Association article](https://www.aeaweb.org/articles?id=10.1257/mic.3.4.77); [Publisher-deposited Crossref metadata (retrieved 2026-09-05)](https://api.crossref.org/works/10.1257/mic.3.4.77).

### `hamman_self-interest_2010` — cited

John R Hamman; George Loewenstein; Roberto A Weber (2010). Self-Interest through Delegation: An Additional Rationale for the Principal-Agent Relationship. American Economic Review, 100(4): 1826–1846. DOI: 10.1257/aer.100.4.1826.

September 2010 issue. Publisher abbreviates final page as 46; 1826–1846 is the same correct range. Periods after middle initials are optional typography.

Outcome: **verified_no_change**.

Evidence: [American Economic Association article](https://www.aeaweb.org/articles?id=10.1257/aer.100.4.1826); [Publisher-deposited Crossref metadata (retrieved 2026-09-05)](https://api.crossref.org/works/10.1257/aer.100.4.1826).

### `oexl_shifting_2013` — cited

Regine Oexl; Zachary J. Grossman (2013). Shifting the blame to a powerless intermediary. Experimental Economics, 16(3): 306–312. DOI: 10.1007/s10683-012-9335-7.

Original Springer page: online 26 July 2012, issue September 2013. Keep 2013. Crossref online date 14 March 2025 is inconsistent with original publication history and should not replace the original date; it appears associated with later platform hosting.

Outcome: **verified_no_change**.

Evidence: [Original Springer article and issue date](https://link.springer.com/article/10.1007/s10683-012-9335-7); [Publisher-deposited Crossref metadata (retrieved 2026-09-05)](https://api.crossref.org/works/10.1007/s10683-012-9335-7).

### `steffel_passing_2016` — cited

Mary Steffel; Elanor F. Williams; Jaclyn Perrmann-Graham (2016). Passing the buck: Delegating choices to others to avoid responsibility and blame. Organizational Behavior and Human Decision Processes, 135: 32–44. DOI: 10.1016/j.obhdp.2016.04.006.

July 2016 volume; no issue number in Elsevier/Crossref citation metadata.

Outcome: **verified_no_change**.

Evidence: [Elsevier article metadata](https://www.sciencedirect.com/science/article/pii/S0749597815300108); [Publisher-deposited Crossref metadata (retrieved 2026-09-05)](https://api.crossref.org/works/10.1016/j.obhdp.2016.04.006).

### `hill_does_2015` — cited

Adam Hill (2015). Does Delegation Undermine Accountability? Experimental Evidence on the Relationship Between Blame Shifting and Control. Journal of Empirical Legal Studies, 12(2): 311–339. DOI: 10.1111/jels.12074.

Online 28 April 2015; June 2015 issue. Both subtitle and all core citation fields confirmed.

Outcome: **verified_no_change**.

Evidence: [Wiley article metadata](https://onlinelibrary.wiley.com/doi/10.1111/jels.12074); [Publisher-deposited Crossref metadata (retrieved 2026-09-05)](https://api.crossref.org/works/10.1111/jels.12074).

### `dietvorst_algorithm_2015` — cited

Berkeley J. Dietvorst; Joseph P. Simmons; Cade Massey (2015). Algorithm aversion: People erroneously avoid algorithms after seeing them err. Journal of Experimental Psychology: General, 144(1): 114–126. DOI: 10.1037/xge0000033.

Final 2015 volume 144(1), 114–126 confirmed in APA-deposited Crossref metadata. Institutional early manuscript shows provisional 2014/143/000 metadata, which must not replace final publication details. APA article page blocked direct retrieval.

Outcome: **verified_no_change**.

Evidence: [Author institutional manuscript](https://repository.upenn.edu/server/api/core/bitstreams/4d24c079-228b-47bd-ba8c-166eeddee8de/content); [Publisher-deposited Crossref metadata (retrieved 2026-09-05)](https://api.crossref.org/works/10.1037/xge0000033).

Limitations: Core fields verified from publisher-deposited DOI metadata; direct publisher article retrieval unavailable. This is metadata verification, not an assessment of research claims.

### `logg_algorithm_2019` — cited

Jennifer M. Logg; Julia A. Minson; Don A. Moore (2019). Algorithm appreciation: People prefer algorithmic to human judgment. Organizational Behavior and Human Decision Processes, 151: 90–103. DOI: 10.1016/j.obhdp.2018.12.005.

Available online 5 February 2019; March 2019 volume. DOI contains 2018 but citation year 2019 is correct.

Outcome: **verified_no_change**.

Evidence: [Published article, author-hosted copy](https://coral-beige-dbda.squarespace.com/s/Algorithm-Appreciation-People-prefer-algorithmic-to-human-judgment.pdf); [Publisher-deposited Crossref metadata (retrieved 2026-09-05)](https://api.crossref.org/works/10.1016/j.obhdp.2018.12.005).

### `burton_systematic_2020` — cited

Jason W. Burton; Mari‐Klara Stein; Tina Blegind Jensen (2020). A systematic review of algorithm aversion in augmented decision making. Journal of Behavioral Decision Making, 33(2): 220–239. DOI: 10.1002/bdm.2155.

Online 23 October 2019; April 2020 issue. Keep year 2020. Mari‐Klara uses a valid Unicode hyphen in the file; this is not a corrupted author name.

Outcome: **verified_no_change**.

Evidence: [Wiley article metadata and publication dates](https://onlinelibrary.wiley.com/doi/10.1002/bdm.2155); [Publisher-deposited Crossref metadata (retrieved 2026-09-05)](https://api.crossref.org/works/10.1002/bdm.2155).

### `chugunova_we_2022` — cited

Marina Chugunova; Daniela Sele (2022). We and It: An interdisciplinary review of the experimental evidence on how humans interact with machines. Journal of Behavioral and Experimental Economics, 99: Article 101897. DOI: 10.1016/j.socec.2022.101897.

Earlier working paper exists, but entry already cites final journal article: August 2022, volume 99, article 101897. Final title/authors/DOI/locator independently confirmed in Elsevier-deposited Crossref metadata; direct Elsevier page blocked.

Outcome: **verified_no_change**.

Evidence: [ETH record documenting earlier working paper and link to later version](https://www.research-collection.ethz.ch/handle/20.500.11850/442053?locale-attribute=en); [Publisher-deposited Crossref metadata (retrieved 2026-09-05)](https://api.crossref.org/works/10.1016/j.socec.2022.101897).

Limitations: Core fields verified from publisher-deposited DOI metadata; direct publisher article retrieval unavailable. This is metadata verification, not an assessment of research claims.

### `mahmud_what_2022` — cited

Hasan Mahmud; A.K.M. Najmul Islam; Syed Ishtiaque Ahmed; Kari Smolander (2022). What influences algorithmic decision-making? A systematic literature review on algorithm aversion. Technological Forecasting and Social Change, 175: Article 121390. DOI: 10.1016/j.techfore.2021.121390.

February 2022 volume. DOI/copyright contain 2021, but final citation year 2022 is correct. Article number 121390.

Outcome: **verified_no_change**.

Evidence: [Elsevier article](https://doi.org/10.1016/j.techfore.2021.121390); [Author dissertation containing published article](https://lutpub.lut.fi/bitstream/handle/10024/168356/Hasan%20Mahmud_A4.pdf?isAllowed=y&sequence=1); [Publisher-deposited Crossref metadata (retrieved 2026-09-05)](https://api.crossref.org/works/10.1016/j.techfore.2021.121390).

### `trunk_current_2020` — uncited

Anna Trunk; Hendrik Birkel; Evi Hartmann (2020). On the current state of combining human and artificial intelligence for strategic organizational decision making. Business Research, 13(3): 875–919. DOI: 10.1007/s40685-020-00133-x.

Online 20 November 2020; November 2020 issue 3. Core fields and ISSNs match.

Outcome: **verified_no_change**.

Evidence: [Springer article metadata](https://link.springer.com/article/10.1007/s40685-020-00133-x); [Publisher-deposited Crossref metadata (retrieved 2026-09-05)](https://api.crossref.org/works/10.1007/s40685-020-00133-x).

### `gogoll_rage_2018` — cited

Jan Gogoll; Matthias Uhl (2018). Rage against the machine: Automation in the moral domain. Journal of Behavioral and Experimental Economics, 74: 97–103. DOI: 10.1016/j.socec.2018.04.003.

June 2018 volume; core fields verified from Elsevier-deposited Crossref and the published article reproduced in the author dissertation.

Outcome: **verified_no_change**.

Evidence: [Author dissertation containing published article](https://mediatum.ub.tum.de/doc/1449095/document.pdf); [Publisher-deposited Crossref metadata (retrieved 2026-09-05)](https://api.crossref.org/works/10.1016/j.socec.2018.04.003).

### `kirchkamp_sharing_2019` — uncited

Oliver Kirchkamp; Christina Strobel (2019). Sharing responsibility with a machine. Journal of Behavioral and Experimental Economics, 80: 25–33. DOI: 10.1016/j.socec.2019.02.010.

Accepted February 2019 according to author; final June 2019 publication already correctly recorded, 80:25–33.

Outcome: **verified_no_change**.

Evidence: [Author publication list](https://www.kirchkamp.de/); [Author article status page](https://www.kirchkamp.de/research/shareMachine.html); [Publisher-deposited Crossref metadata (retrieved 2026-09-05)](https://api.crossref.org/works/10.1016/j.socec.2019.02.010).

### `maasland_blame_2022` — uncited

Christian Maasland; Kristina S. Weißmüller (2022). Blame the Machine? Insights From an Experiment on Algorithm Aversion and Blame Avoidance in Computer-Aided Human Resource Management. Frontiers in Psychology, 13: Article 779028. DOI: 10.3389/fpsyg.2022.779028.

Published 25 May 2022. 779028 is an article number; authors, title, volume and DOI match.

Outcome: **verified_no_change**.

Evidence: [Frontiers published article](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.779028/full); [Publisher-deposited Crossref metadata (retrieved 2026-09-05)](https://api.crossref.org/works/10.3389/fpsyg.2022.779028).

### `heaton_social_2023` — uncited

Dan Heaton; Jérémie Clos; Elena Nichele; Joel E. Fischer (2023). The Social Impact of Decision-Making Algorithms: Reviewing the Influence of Agency, Responsibility and Accountability on Trust and Blame. Proceedings of the First International Symposium on Trustworthy Autonomous Systems, ACM, Article 11, pp. 1–11. DOI: 10.1145/3597512.3599706.

Published proceedings paper, 11 July 2023; ACM Article No. 11, pages 1–11. ISBN 9798400707346 and Edinburgh conference venue confirmed for these proceedings. Crossref distinguishes publisher location New York, NY, USA from event location Edinburgh United Kingdom. Existing address is the true conference venue; publisher-address normalization is optional.

Outcome: **verified_optional_enrichment**.

- Optional ACM proceedings locator completion; existing 1–11 page range is correct. Use only a field supported by bibliography style. `articleno`: `missing` → `11`.

Evidence: [ACM article metadata](https://doi.org/10.1145/3597512.3599706); [Author institutional publication record](https://highlights.cdt.horizon.ac.uk/students/psxdh7-1); [Institutional record for same proceedings ISBN and venue](https://research.aber.ac.uk/en/publications/a-practical-taxonomy-of-tas-related-usecase-scenarios/); [Publisher-deposited Crossref metadata (retrieved 2026-09-05)](https://api.crossref.org/works/10.1145/3597512.3599706).

### `weaver_politics_1986` — cited

R. Kent Weaver (1986). The Politics of Blame Avoidance. Journal of Public Policy, 6(4): 371–398. DOI: 10.1017/s0143814x00004219.

Original issue October–December 1986 (Crossref print month October). Later online hosting date 28 November 2008 must not replace 1986. All core fields verified in CUP-deposited Crossref metadata; direct publisher page blocked.

Outcome: **verified_no_change**.

Evidence: [Publisher-deposited Crossref metadata (retrieved 2026-09-05)](https://api.crossref.org/works/10.1017/s0143814x00004219).

Limitations: Core fields verified from publisher-deposited DOI metadata; direct publisher article retrieval unavailable. This is metadata verification, not an assessment of research claims.

### `fiorina_legislator_1986` — cited

Morris P. Fiorina (1986). Legislator Uncertainty, Legislative Control, and the Delegation of Legislative Power. The Journal of Law, Economics, and Organization, 2(1): 33–51. DOI: 10.1093/oxfordjournals.jleo.a036905.

OUP confirms spring 1986, 2(1), 33–51, full author and title. Journal ampersand versus “and” is an accepted name/style variation; no correction needed.

Outcome: **verified_optional_enrichment**.

- Optional missing persistent identifier, verified on OUP article page. `doi`: `missing` → `10.1093/oxfordjournals.jleo.a036905`.

Evidence: [Oxford University Press article metadata](https://academic.oup.com/jleo/article-abstract/2/1/33/873292).

### `berger_watch_2021` — uncited

Benedikt Berger; Martin Adam; Alexander Rühr; Alexander Benlian (2021). Watch Me Improve—Algorithm Aversion and Demonstrating the Ability to Learn. Business & Information Systems Engineering, 63(1): 55–68. DOI: 10.1007/s12599-020-00678-5.

Online 4 December 2020; February 2021 issue. Keep 2021. Existing TeX umlaut in Rühr and em-dash title separator correctly represent publisher spelling.

Outcome: **verified_no_change**.

Evidence: [Springer article and issue date](https://link.springer.com/article/10.1007/s12599-020-00678-5); [Publisher-deposited Crossref metadata (retrieved 2026-09-05)](https://api.crossref.org/works/10.1007/s12599-020-00678-5).

### `litterscheidt_financial_2020` — uncited

Rouven Litterscheidt; David J. Streich (2020). Financial education and digital asset management: What's in the black box?. Journal of Behavioral and Experimental Economics, 87: Article 101573. DOI: 10.1016/j.socec.2020.101573.

August 2020 volume 87, article 101573. First author is Rouven, not Roman; verified independently by Elsevier page, publisher-deposited Crossref metadata and authors replication data. Other core fields match.

Outcome: **correction_required**.

- Necessary correction: first author’s given name is Rouven, not Roman. `author`: `Litterscheidt, Roman and Streich, David J.` → `Litterscheidt, Rouven and Streich, David J.`.

Evidence: [Elsevier published article metadata](https://www.sciencedirect.com/science/article/abs/pii/S2214804319304367); [Authors original replication data](https://data.mendeley.com/datasets/zhbzv9jtww/1); [Publisher-deposited Crossref metadata (retrieved 2026-09-05)](https://api.crossref.org/works/10.1016/j.socec.2020.101573).

### `sharan_dont_2020` — uncited

Navya Nishith Sharan; Daniela Maria Romano (2020). The effects of personality and locus of control on trust in humans versus artificial intelligence. Heliyon, 6(8): Article e04572. DOI: 10.1016/j.heliyon.2020.e04572.

Published 28 August 2020; 6(8), e04572. Both full author names and order match NLM/Elsevier metadata. Citation key does not need to match the final title.

Outcome: **verified_no_change**.

Evidence: [NLM PubMed article record](https://pubmed.ncbi.nlm.nih.gov/32923706/); [Publisher-deposited Crossref metadata (retrieved 2026-09-05)](https://api.crossref.org/works/10.1016/j.heliyon.2020.e04572).

### `bigman_people_2018` — cited

Yochanan E. Bigman; Kurt Gray (2018). People are averse to machines making moral decisions. Cognition, 181: 21–34. DOI: 10.1016/j.cognition.2018.08.003.

Final December 2018 volume 181, 21–34, confirmed by Elsevier-deposited metadata and author institutional record.

Outcome: **verified_no_change**.

Evidence: [Author institutional research record](https://cris.iucc.ac.il/en/publications/people-are-averse-to-machines-making-moral-decisions/); [Publisher-deposited Crossref metadata (retrieved 2026-09-05)](https://api.crossref.org/works/10.1016/j.cognition.2018.08.003).

### `jauernig_people_2022` — cited

Johanna Jauernig; Matthias Uhl; Gari Walkowitz (2022). People Prefer Moral Discretion to Algorithms: Algorithm Aversion Beyond Intransparency. Philosophy & Technology, 35(1): Article 2. DOI: 10.1007/s13347-021-00495-y.

Published online 26 January 2022; March 2022 issue 1. The DOI includes 2021 but citation year 2022 is correct. 2 is the article number.

Outcome: **verified_no_change**.

Evidence: [Springer article metadata](https://link.springer.com/article/10.1007/s13347-021-00495-y); [Publisher-deposited Crossref metadata (retrieved 2026-09-05)](https://api.crossref.org/works/10.1007/s13347-021-00495-y).

### `dietvorst_people_2020` — cited

Berkeley J. Dietvorst; Soaham Bharti (2020). People Reject Algorithms in Uncertain Decision Domains Because They Have Diminishing Sensitivity to Forecasting Error. Psychological Science, 31(10): 1302–1314. DOI: 10.1177/0956797620948841.

Online 11 September 2020; October 2020 issue. Full title, authors and order, 31(10), 1302–1314 and DOI match SAGE.

Outcome: **verified_no_change**.

Evidence: [SAGE article metadata](https://journals.sagepub.com/doi/10.1177/0956797620948841); [Publisher-deposited Crossref metadata (retrieved 2026-09-05)](https://api.crossref.org/works/10.1177/0956797620948841).

### `dietvorst_overcoming_2018` — uncited

Berkeley J. Dietvorst; Joseph P. Simmons; Cade Massey (2018). Overcoming Algorithm Aversion: People Will Use Imperfect Algorithms If They Can (Even Slightly) Modify Them. Management Science, 64(3): 1155–1170. DOI: 10.1287/mnsc.2016.2643.

Online in Articles in Advance 4 November 2016; final March 2018 issue 64(3), 1155–1170. Keep 2018.

Outcome: **verified_no_change**.

Evidence: [Published article on author university website](https://faculty.wharton.upenn.edu/wp-content/uploads/2016/08/Dietvorst-Simmons-Massey-2018.pdf); [Publisher-deposited Crossref metadata (retrieved 2026-09-05)](https://api.crossref.org/works/10.1287/mnsc.2016.2643).

### `castelo_task-dependent_2019` — uncited

Noah Castelo; Maarten W. Bos; Donald R. Lehmann (2019). Task-Dependent Algorithm Aversion. Journal of Marketing Research, 56(5): 809–825. DOI: 10.1177/0022243719851788.

Online 15 July 2019; October 2019 issue. All core fields verified in SAGE-deposited Crossref metadata; direct SAGE retrieval blocked.

Outcome: **verified_no_change**.

Evidence: [Publisher-deposited Crossref metadata (retrieved 2026-09-05)](https://api.crossref.org/works/10.1177/0022243719851788).

Limitations: Core fields verified from publisher-deposited DOI metadata; direct publisher article retrieval unavailable. This is metadata verification, not an assessment of research claims.

### `bogert_humans_2021` — uncited

Eric Bogert; Aaron Schecter; Richard T. Watson (2021). Humans rely more on algorithms than social influence as a task becomes more difficult. Scientific Reports, 11(1): Article 8028. DOI: 10.1038/s41598-021-87480-9.

Published 13 April 2021. Article 8028, not page 8028. Crossref supplies issue 1, although Nature recommended citation omits issue; adding it is optional.

Outcome: **verified_optional_enrichment**.

- Optional issue completion from publisher-deposited Crossref; Nature recommended citation uses volume and article number without issue. `number`: `missing` → `1`.

Evidence: [Nature published article metadata](https://www.nature.com/articles/s41598-021-87480-9); [Publisher-deposited Crossref metadata (retrieved 2026-09-05)](https://api.crossref.org/works/10.1038/s41598-021-87480-9).

### `goldbach_geht_2019` — uncited

Carina Goldbach; Deniz Kayar; Thomas Pitz; Jörn Sickmann (2019). Transferring decisions to an algorithm: A simple route choice experiment. Transportation Research Part F: Traffic Psychology and Behaviour, 65: 402–417. DOI: 10.1016/j.trf.2019.08.011.

Elsevier-deposited Crossref metadata verifies the current English title, all four authors, year, volume, page range and DOI. The existing annotation records a separate unresolved question about whether this paper was the author’s intended source for an earlier German title; bibliographic identity is verified but author intent cannot be inferred. Preserve that intent question until resolved.

Outcome: **verified_no_change**.

Evidence: [Publisher-deposited Crossref metadata (retrieved 2026-09-05)](https://api.crossref.org/works/10.1016/j.trf.2019.08.011).

Limitations: Core fields verified from publisher-deposited DOI metadata; direct publisher article retrieval unavailable. This is metadata verification, not an assessment of research claims. Intended-source question in existing annote remains unresolved; no bibliography replacement or annotation removal proposed.

### `niszczota_robo-investors_2020` — uncited

Paweł Niszczota; Dániel Kaszás (2020). Robo-investment aversion. PLOS ONE, 15(9): e0239277. DOI: 10.1371/journal.pone.0239277.

Published 17 September 2020. Authors Paweł Niszczota and Dániel Kaszás, 15(9), e0239277 and DOI match. PLoS ONE versus PLOS ONE is capitalization only.

Outcome: **verified_no_change**.

Evidence: [PLOS published article and citation](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0239277); [Publisher-deposited Crossref metadata (retrieved 2026-09-05)](https://api.crossref.org/works/10.1371/journal.pone.0239277).
