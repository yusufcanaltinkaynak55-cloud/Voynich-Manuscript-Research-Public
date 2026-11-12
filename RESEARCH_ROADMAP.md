# Research Roadmap and Decision Gates

**Updated:** 12 November 2026  
**Research lead:** Yusuf Can Altınkaynak  
**Status:** Open research agenda, not a claim of peer review, institutional endorsement, or a deciphered Voynich Manuscript.

## Mission and research principle

Investigate competing explanations for the written structure of the Voynich Manuscript (Beinecke MS 408) using transparent, falsifiable computational experiments. The project aims to make methods inspectable, expose negative results, respect original historical sources and third-party rights, and distinguish **observable patterns** from an **independently authenticated historical reading**.

The private Sherlock system is **not** released by this repository. Public experiments are separately implemented reference programs.

## Public research milestones

| Milestone | Deliverable and evidence | Status |
| --- | --- | --- |
| P01. Research record and provenance | English [hypothesis register](HYPOTHESES.md), [methodology](METHODOLOGY.md), [scientific assessment](SHERLOCK_SCIENTIFIC_ASSESSMENT.md) and [CITATION.cff](CITATION.cff) | **PUBLISHED**, not externally validated |
| P02. B09: transformed-spelling collisions | [Protocol](evidence/b09/README.md), [results](evidence/b09/RESULTS.md), public Python test, hash-pinned source input, passing CI | **PUBLIC COMPUTATION PASSED**; outside replication pending |
| P03. B10: original-spelling candidate selection | [Protocol](evidence/b10/README.md), [results](evidence/b10/RESULTS.md), baseline and candidate-coverage safeguards, passing CI | **PUBLIC COMPUTATION PASSED**; outside replication pending |
| P04. B17-OPEN: pairwise word-order diagnostic | [Protocol](evidence/b17/README.md), [results](evidence/b17/RESULTS.md), shuffled-training and position controls, passing CI | **PUBLIC COMPUTATION PASSED**, not equivalent to private full-line B17 |
| P05. Research governance | [Sherlock Model Card](SHERLOCK_MODEL_CARD.md), [CFT-001 overview](CIPHER_FAMILY_COMPARISON.md), contributing and public QA rules | **PUBLISHED / CONTINUOUS IMPROVEMENT** |
| P06. Independent reproduction | New evaluator with separate implementation, reproducible logs and explicit protocol differences | **NOT COMPLETE** |
| P07. Known-key cryptanalytic competence | Safely sourced positive controls with a withheld answer and a separate grader | **NOT ESTABLISHED** |
| P08. Historical meaning/reading gate | Independently verified glyph-to-reading-to-meaning correspondences on previously untouched material | **NOT ESTIMABLE / NOT ESTABLISHED** |
| P09. Versioned archival release | Approved licenses, historical file and source-rights audit, immutable archived snapshot | **WAITING FOR RIGHTS-HOLDER LICENSE DECISION** |

**Critical interpretation:** A successful CI job means its code executed under declared conditions. It does *not* prove a historical cipher, original language, or manuscript reading.

## Next priorities with acceptance criteria

### Priority 0: Make the existing evidence defensible

**A. Outside replication of B09, B10 and B17-OPEN**

*Deliverable:* an independent implementation or independent audit report for each study, with machine/environment record, input hashes, preprocessing decisions, test denominators, results, failures and disagreement analysis.

*Acceptance:* attributable external reviewer and full written replication log, not merely a second execution by the same assistant. The research's two transcriptions must **not** be treated as two historical witnesses.

**B. Stronger negative controls**

*Deliverable:* fixed, fair controls for code-collision ambiguity, folio/layout confounds, word length, repeated word forms, and natural-language comparison.

*Acceptance:* a versioned preregistered protocol, a declared outcome matrix and negative examples, plus execution on data not re-used for model selection.

**C. Public release quality**

*Deliverable:* automated checks for scientific disclaimers, source boundaries and relative references, alongside synthetic unit tests, successful real-data CI and legible research navigation.

*Acceptance:* quality workflow success; none of its automated checks claim to provide scientific peer review.

### Priority 1: Known-answer competence and historical evidence

**D. Safe public reference cryptanalysis benchmark**

Evaluate eligible known-answer historical or synthetic ciphers using a **separately controlled evaluator**, reporting full-key recovery, plaintext recovery, word/character alignment and compute cost as *different* outcomes. Use only material with clear permission to redistribute or fetch. No Sherlock source is needed in the public evaluation pipeline.

*Acceptance:* frozen challenge and clear failure modes; no key or answer leakage; no extrapolation from the known cipher to the unknown Voynich plaintext.

**E. Source-image and transcription uncertainty audit**

Select specific folios with Yale's primary-image references, use multiple independent readers and explicit ambiguities, and compare alternative glyph segmentation. Do not redistribute image assets without rights clearance.

*Acceptance:* an auditable image location → written unit → hypothesis → test chain, including mismatches.

### Priority 2: Carefully bounded historical interpretation

**F. Prospective hypothesis test**

Freeze a candidate, a relevant outside historical anchor, competing mechanisms, acceptance thresholds and a genuinely unused sample *before* inspection.

*Acceptance:* another researcher can independently verify the traceable correspondence and its error rate. **Before this evidence, a percentage of the manuscript “decoded” must not be published.**

## Security and publication constraints

- Never mirror the private Voynich laboratory, Sherlock runtime/model source, training assets, candidate reading keys, private correspondence, secrets, or private third-party material into this repository.
- Public release of **reference implementations** is permitted only after sensitive-information and source-rights review; B09/B10/B17 are narrow research demonstrators, not Sherlock exports.
- Keep experiments separate when their scientific tasks and denominators differ. Do not combine B09 “code collisions,” B10 “eligible spellings selected,” and B17 “pairwise order” into a single reading percentage.
- Do not assert that a statistic is independently replicated merely because ZL3b and IT2a agree.
- Preserve failed tests and superseded interpretations with dates and source links.
- Original repository documentation and scripts currently lack a general reuse license. **Do not infer permission from public GitHub visibility.** Any future CC BY 4.0/MIT grant requires an explicit ownership decision and documented file scope.

## How to participate

Use [CONTRIBUTING.md](CONTRIBUTING.md) for a falsifiable research contribution, [REPRODUCIBILITY.md](REPRODUCIBILITY.md) for evidence requirements and [SOURCES_AND_RIGHTS.md](SOURCES_AND_RIGHTS.md) for attribution and permissions. Reproductions, corrections, stronger baselines and **negative results** are all welcome.

**Related open decisions:** [B09 replication](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/issues/1), [B10 replication](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/issues/2), and [licenses and archival release](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/issues/3).
