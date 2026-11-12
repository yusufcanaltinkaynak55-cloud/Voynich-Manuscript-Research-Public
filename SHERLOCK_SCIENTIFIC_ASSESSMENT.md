# Koçi Bey Report | Public Scientific Assessment of Sherlock

**Document ID:** KBR-001-PUBLIC  
**Underlying internal assessment:** 7 November 2026  
**Public adaptation:** 11 November 2026  
**Prepared for:** Voynich Manuscript Research, an independent research project maintained by Yusuf Can Altınkaynak  
**Document type:** Technical and scientific status assessment, limitations, and research roadmap  
**Evidence status:** **STRATEGIC ASSESSMENT / NOT PEER REVIEWED / NOT A DECIPHERMENT**

> **Naming clarification:** “Koçi Bey Report” is an internal project title inspired by the historical language of critical administrative review. This is **not** a historical document written by Koçi Bey and implies no historical connection, academic endorsement, or institutional affiliation.
>
> **Public-edition boundary:** This is a newly written, non-sensitive summary of the internal assessment, **not a verbatim disclosure of the private report**. No proprietary Sherlock implementation, model weights, unpublished candidate key, credential, private correspondence, or restricted primary-source file is disclosed.

## Executive assessment

The Sherlock research program has developed tools for working with computational transcriptions of the Voynich Manuscript (Beinecke MS 408), measuring recurring written patterns, proposing competing structural mechanisms, and evaluating some predictive and cryptanalytic tasks. These activities are scientifically useful **only when the task and its evaluation metric are clearly specified**.

**The critical conclusion is unchanged: this project does not possess an independently verified Voynich reading key, sound system, word-meaning inventory, or translation.** Its semantic decipherment accuracy is **NOT ESTIMABLE**. This does **not** mean that the manuscript has been demonstrated to be unreadable, or that a model's capability has been measured as zero.

The central challenge is **identifiability**: several distinct writing, language, copying, and cipher mechanisms may reproduce portions of the same observed statistics. An impressive match to a surface pattern does not identify the historical mechanism that produced it.

This assessment therefore prioritizes independent evidence and discriminating tests over rapidly accumulating candidate readings.

## 1. What Sherlock is intended to do

Sherlock is an experimental research program, not a proven Voynich decoder. The private environment includes work in the following areas:

| Research function | What is scientifically measurable | What it does **not** establish |
| --- | --- | --- |
| Transcription analysis | Frequencies, distributions, positional patterns, and differences between editorial transcriptions | Historical glyph sounds or a language identity |
| Pattern prediction | Performance on held-out visible or masked spelling features relative to fixed baselines | Correct translation or a recovered cipher key |
| Candidate mechanism comparison | Which specified simulations or cipher analogues match or miss preregistered statistics | Identification of the manuscript's original author or method |
| Known-answer cipher calibration | Performance on a separately scored example with an actual known answer | Performance on an unknown Voynich plaintext |
| Historical and visual alignment | Whether independently sourced images, transcriptions, and historical lexical witnesses support a frozen prediction | Meaning inferred merely from a drawing's proximity |

**Four distinct tasks must be reported separately:** generating plausible-looking tokens, predicting missing written forms, recovering a known cipher's hidden answer, and deciphering an unknown historical manuscript. Their accuracy figures cannot be combined into one “percentage read.”

The private Sherlock system is **not included in this repository**. The publicly released B09, B10 and B17-OPEN reference evaluators are separate, narrowly scoped computational benchmarks, not the Sherlock private system.

## 2. Evidence currently available and its limitations

### 2.1 Structured transcription coverage

The 7 November internal research inventory described broad coverage across multiple editorial locus categories and exploratory grouping of similar written forms. Such grouping is **heuristic**: a recurring letter sequence is not automatically a linguistic root, suffix, or translated word.

ZL3b and IT2a are alternative **transcriptions of the same physical manuscript**. Agreement between them is useful for measuring transcription sensitivity but is not an independent historical witness or a second manuscript.

The detailed private inventory has not been released as an independently reproducible public package. Therefore this assessment **does not elevate internal inventory counts into independently verified corpus facts**.

### 2.2 Written-form prediction

Internal predictive experiments have reported improvements over specified character-level baselines for particular held-out spelling tasks. Their scientific interpretation remains **limited to those tasks**; these results are not phonetic readings or historical decoding results.

Because the full private Sherlock evaluation implementations and run manifests are not public here, its internal-only findings remain **awaiting independent verification**. Three narrower, non-proprietary benchmark questions, B09, B10 and B17-OPEN, have successful public reference computations. The public [results ledger](RESULTS.md) identifies their exact scope.

### 2.3 An actual public repeatability result: B09

The separately published [B09-OPEN-001 evidence package](evidence/b09/README.md) evaluates collisions between **transformed EVA spelling codes** in training and previously unseen test spellings. Its openly logged [11 November 2026 GitHub Actions run](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/actions/runs/42992577209) passed source hash checks and software tests:

| Measure | ZL3b | IT2a |
| --- | ---: | ---: |
| Exact-form out-of-vocabulary test occurrences | 875 | 966 |
| Collision after removing `aeioy` | 75.77% | 74.95% |
| Collision after removing `dklrs` (fixed control) | 61.03% | 61.59% |
| Median collision with equal-deletion-count randomized positions | 47.54% | 48.96% |
| Fraction of matched occurrences with multiple possible training forms | 85.37% | 85.36% |

**Interpretation:** A selected deterministic transformation can collapse many unfamiliar written forms onto previously observed codes. The very high ambiguity rate is a major caution: **this is not 75% readable vocabulary**. The data do **not** identify those five EVA characters as vowels, padding, a historical writing key, or evidence of Arabic, Persian, Latin, Turkish, or any other language.

The folios were used in earlier private exploration. Public computational reproducibility is therefore **not a new blind discovery**, and independent external scientific verification remains pending. The two transcription versions are not two independent historical sources.

### 2.4 A second public benchmark: B10 spelling reconstruction

The [B10-OPEN-001 public reference experiment](evidence/b10/RESULTS.md) tested the more difficult task of selecting an observed original **EVA spelling** from the competing spellings that collapse to one reduced code. In the initial successful public run, restricted-eligible contextual top-1 accuracy was **53.90%** on ZL3b and **53.05%** on IT2a, compared with position-only **53.60% / 53.18%** and simple codebook frequency **53.29% / 52.86%**. The eligible sets were **4,659 / 4,616** written-form instances whose actual spelling already occurred among training candidates. Previously unseen spellings were **not generatable** by this model.

Contextual log-loss improved slightly in both transcriptions, but **IT2a's folio-bootstrap interval for that small gain included zero** and its contextual top-1 score was below the position-only benchmark. Left and right neighbour codes were used: this is **bidirectional written-form reconstruction, not historical left-to-right decryption**. The benchmark was computationally rerun in GitHub Actions, not independently verified by an outside researcher.

### 2.5 Further public update (12 November 2026): B17-OPEN line orientation

A separate [B17-OPEN public diagnostic](evidence/b17/RESULTS.md) compared directed word-pair orientation with a shuffled-training control and a visible first/last-glyph position baseline. On previously explored held-out folios, pair orientation was approximately **52.54% / 52.52%**, while the visible-edge position diagnostic was **61.16% / 60.35%** on ZL3b / IT2a. These are scores on **word pairs**, not readable tokens or reconstructed full lines. This narrow public calculation is **not** a repetition of the original private B17 beam-search reordering task and does not demonstrate a historical key or meaning.

### 2.6 Competing mechanisms and negative evidence

Several experimental directions in the private research record have encountered limitations that must be retained:

- A simple universal three-consonant-root interpretation and certain fixed language-mapping rules did not pass the specific matched controls used in their tests.
- Some apparent manuscript-section effects in spelling prediction weakened under controls that account for neighbouring pages and layout.
- A tested adapted-language simulation and a simplified copy-modify simulation both failed a jointly specified distributional acceptance criterion. **That is a limitation of those implementations**, not a proof that every adapted language or copying explanation is impossible.
- Published variable-length/homophonic cipher analogues, including Naibbe-type comparisons, remain **hypothesis-generating analogues**, not identified historical keys. Important adjacent-word differences remain unexplained.
- An internal known-cipher Sherlock benchmark did **not** recover the reference plaintext or source key. A small normalized edit-similarity improvement in that test is **not** a decoded-letter fraction and is **not** evidence that Voynich was decoded.

These specific limitations are described further in [RESULTS.md](RESULTS.md) and [HYPOTHESES.md](HYPOTHESES.md). This public document does not claim the private studies have passed independent peer review.

## 3. Six scientific obstacles to a defensible decipherment

### A. Primary glyph evidence and transcription uncertainty

The original manuscript images must be linked to specific folio and line regions. Editorial segmentation, uncertain readings, compound EVA signs, allographic variation, and possible word-boundary ambiguity cannot silently be treated as historically known phonetic units.

**Required evidence:** source-image references, reviewed transcription samples, explicit segmentation alternatives, and documented inter-annotator disagreements.

### B. Competing mechanisms, not one favoured explanation

A single substitution or borrowed-root model should not exclude homophonic, variable-length, polyalphabetic, positional, copy-modify, or linguistic alternatives without testing them. Competing hypotheses must receive comparable training data, candidate budgets, and preregistered stopping rules.

**Required evidence:** at least several clearly specified families compared under the same fixed evaluation criteria and null controls.

### C. Calibrated uncertainty

A model score, a relative compression or predictive-loss gain, and a permutation test result are **not** probabilities that a proposed historical key is correct. Such probabilities require a calibrated, explicitly justified model and suitable independent tests.

**Required evidence:** honest uncertainty estimates, calibration on known-answer problems, and documented failure/overconfidence cases.

### D. Historically appropriate source material

Modern language corpora and much older classical texts are imperfect proxies for the actual language and written practices of a fifteenth-century manuscript. A visually plausible word resemblance is not, by itself, an etymology.

**Required evidence:** dated, source-verified comparators with appropriate linguistic, genre, length, and period controls, including negative examples.

### E. Blind known-key recovery

A credible cryptanalytic system should first demonstrate that it can recover hidden answers in appropriate known-key challenges without accidentally receiving the key, the test plaintext, or equivalent information during development.

**Required evidence:** a frozen solver, an independent challenge preparer and grader, previously unseen messages, and separate measurements of key recovery, plaintext recovery, error, and cost. A successful synthetic trial remains **calibration**, not Voynich decipherment.

### F. Independent historical and visual anchors

Many candidate rules can fit the same surface statistics. To distinguish among them, proposed readings need independent manuscript-image verification, historically attested written forms, competing candidates, and tests on material genuinely withheld from research iteration.

**Required evidence:** a fixed rule that repeatedly survives external checks, including documented mismatches and qualified expert review. Co-occurrence of a picture and a word is not automatically a word-object pairing.

## 4. Three sequential scientific acceptance gates

| Gate | Question | Minimum acceptance principle | Current status |
| --- | --- | --- | --- |
| **A. Cryptanalytic competence** | Can the method recover genuinely withheld answers on relevant known-key examples? | Blind, separately graded recovery under a frozen protocol | **NOT YET ESTABLISHED for the required breadth and reliability** |
| **B. Voynich discrimination** | Can the method outperform serious alternative generating processes on untouched manuscript evidence? | Fair, equal-budget comparisons with transparent negative controls and no test leakage | **NOT YET ESTABLISHED** |
| **C. Historically meaningful reading** | Can one frozen interpretation produce repeatable readings corroborated by independent historical or image evidence? | Independent verification of glyph, reading and meaning correspondences; explicit error accounting | **NOT YET ESTABLISHED / semantic accuracy NOT ESTIMABLE** |

**Passing A and B does not imply C.** The present repository makes no claim that any gate has already been passed.

## 5. Research roadmap and priorities

**Priority 0: Measurement integrity and known-answer calibration.** Freeze a common evaluation vocabulary and source manifest; prevent train/test leakage; compare mechanism families fairly; run withheld-key challenges with independent grading; preserve unsuccessful runs.

**Priority 1: Manuscript-grounded and historical controls.** Audit transcription uncertainty with manuscript images; build period-appropriate source comparisons; report uncertainty and label ambiguity; seek independent replication of public numerical findings.

**Priority 2: Prospective interpretation tests.** Only after the preceding evidence requirements are met, test a *frozen* candidate reading rule against genuinely new material, external historical witnesses and competing candidate explanations. Publish mismatches as well as successes.

Increasing model size or computing power does not, by itself, resolve an identifiability problem: if competing mechanisms produce equivalent observables, the decisive missing ingredient may be **independent evidence**, not more search.

## 6. Public accountability, attribution and reproducibility

1. A merged pull request, successful software test, repeated prompt answer, or generated report **does not constitute scientific validation**.
2. Negative and inconclusive findings remain part of the record. An outcome that could not be scored must not be presented as 0% accuracy.
3. Every numerical claim should identify its dataset, version, tested unit, denominator, metric, baseline, and source run. Retrospective reinterpretations are marked as such.
4. Reuse of previously viewed test folios must be disclosed. The same manuscript represented by two transcriptions must never be counted as two independent historical witnesses.
5. Human-directed research has used AI assistance in drafting, software development and hypothesis exploration. AI participation does not independently authenticate historical conclusions.
6. An external evaluation can be valuable even when proprietary implementation is withheld, provided that access limitations, grading independence, and the resulting reproducibility limits are explicitly reported.

For public reference benchmarks, see [B09](evidence/b09/RESULTS.md) and [B10](evidence/b10/RESULTS.md), plus the [B09 independent replication request](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/issues/1). For the rest of the research, see [METHODOLOGY.md](METHODOLOGY.md), [RESULTS.md](RESULTS.md), and [REPRODUCIBILITY.md](REPRODUCIBILITY.md).

## Final judgment

**Sherlock currently represents an exploratory computational research capability, not a validated historical decipherment.** Its near-term scientific value lies in framing testable alternatives, ruling out overly strong claims, measuring uncertainty, and creating reproducible, independently checkable research procedures.

The next credible milestone is **not a larger claimed reading percentage**. It is a more demanding external test that could fail, and an explicit record of what the result truly establishes.

---

### Provenance, scope and revision note

- **Source:** internal laboratory document KBR-001 (the original Turkish-language *Koçi Bey Report*), dated **7 November 2026**, adapted and condensed for public disclosure on **11 November 2026**.
- **Public evidence update:** includes the B09 and B10 public computational runs completed on 11 November 2026 and the distinct B17-OPEN public pairwise calculation completed on 12 November 2026, which was **not** part of the original 7 November snapshot.
- **Publication level:** public research assessment; **not** an external peer-reviewed article, institutional endorsement, new experiment, or an independent verification certificate.
- **Disclosure boundary:** intentionally omits private repository paths, internal system integration arrangements, implementation-level details, proprietary code, model artifacts, candidate keys, private contacts and any other unreleased research material.
- **Rights:** this repository's original research documents have no blanket reuse license assigned as of this edition; see [SOURCES_AND_RIGHTS.md](SOURCES_AND_RIGHTS.md).
- **Historical manuscript source:** [Beinecke Library, Yale University, MS 408](https://collections.library.yale.edu/catalog/2002046). This project is independent of Yale University.
