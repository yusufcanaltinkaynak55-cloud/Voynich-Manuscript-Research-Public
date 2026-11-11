# Glyph Deletion, Orthographic Collisions, and Decipherment Claims
## Scientific synthesis of the B08–B16 Voynich experiments

**Public report:** 11 November 2026  
**Underlying internal research records:** 4–6 November 2026  
**Status:** EXPLORATORY SYNTHESIS; PARTIALLY REPRODUCIBLE; PENDING INDEPENDENT SCIENTIFIC REVIEW  
**Manuscript:** Beinecke Rare Book & Manuscript Library, Yale University, MS 408

> **Central finding:** Removing certain symbols from a Voynich transcription creates many matches to other *written forms*. It has **not** produced independently verified historical word readings, a language identification, or a translation. In fact, much of the apparent coverage arises because the transformation merges numerous different spellings into the same code.

This document is an **English-language, disclosure-safe synthesis** of dated internal experiments, not a new execution of every experiment. One narrow sub-result, the B09 code-collision metric, has been publicly reimplemented and executed in [B09-OPEN-001](evidence/b09/README.md). **Most of B10–B16 cannot yet be independently reproduced from this public repository.** Private source code, training assets, model weights, candidate keys, and unpublished materials are not disclosed.

## 1. Research question

A proposed explanation for regularities in the Voynich Manuscript is that some visible signs are **optional, modifying, or concealing** elements. If so, removing or reinterpreting these signs might expose a smaller and more predictable underlying vocabulary.

This general suggestion is not new in Voynich research, and many variants are possible. The laboratory tested a **specific family of computational predictions** rather than treating the broader theory as established:

1. Do predetermined transformations make unseen written forms collide with known training codes?
2. When multiple original spellings collapse to one code, can the correct spelling be recovered?
3. Are the selected signs uniquely responsible for the observed regularities?
4. Do deletion or glyph-merging transformations make the manuscript more similar to a set of natural-language comparison texts?
5. Can competing explanations, including ordinary orthography and copying/editing processes, account for the observed structure?

**Important terminology:** EVA characters represent an *editorial transliteration convention*. Calling `a/e/i/o/y` “vowel-like” is a shorthand for an experimental character set, **not** an identification of historical vowels or sounds.

## 2. Data, task boundaries, and verification

The internal studies analyzed two IVTFF-style transcriptions, **ZL3b** and **IT2a (Takahashi)**, with physical folios used for train/validation/test separation in specified experiments. They are different transcriptions of **one historical manuscript**, not independent documents.

The B09 public reference evaluator:

- Retrieves immutable, version-pinned transcriptions from upstream sources and rejects incorrect SHA-256 hashes.
- Excludes uncertain written forms and handles explicit word-boundary markers.
- Separates folios, stratifying by recorded manuscript metadata.
- Measures the fraction of **test spellings absent from the training vocabulary** whose *transformed codes* occur in the transformed training vocabulary.
- Compares fixed `aeioy` deletion with fixed `dklrs` deletion and 30 controls that remove the same number of randomly selected character positions per word.

The public [B09 run and exact computational results](evidence/b09/RESULTS.md) are inspectable. Later studies may reuse folios already examined in earlier exploratory experiments. Consequently, their recorded held-out tests should **not** be presented as completely untouched, prospective blind tests.

The eight comparator **texts** used in the internal B15/B16 summaries include three Latin sources, Italian, Ottoman Turkish, two Arabic sources, and Persian. This is **eight texts, not eight independent languages**, and their metrics do not define a universal range for all natural languages.

## 3. Results by experiment family

| Study | Narrow question | Recorded result | Evidential interpretation |
| --- | --- | --- | --- |
| **B08/B09** | Do fixed sign deletions connect unseen spellings to codes observed in training? | Publicly reproduced: `aeioy` code-match rates **75.77% ZL3b / 74.95% IT2a**; fixed `dklrs` controls **61.03% / 61.59%**. | **Positive structural collision observation**; not a reading or recovered historical root. |
| **B09 ambiguity audit** | Does a matching code identify one original written form? | **85.37% / 85.36%** of matched occurrences were ambiguous among multiple training forms; internally reported median **7** forms per matched code. | **Information loss is substantial.** Many-to-one matching inflates apparent coverage. |
| **B10: variant disambiguation** | Can contextual features recover the correct original EVA spelling from a code with multiple candidates? | Under candidate-known conditions, internal top-1 spelling selection was about **53–54%**; a simple frequency baseline was already around **53%**. | Context provided small or inconsistent gains; not 53% of the manuscript read. Some evaluated cases were eligible only because the correct spelling was already among training candidates. |
| **B11-G and B13** | Can nearby signs predict the location/identity of the selected characters? | Two internal implementations reported some spelling-prediction gains, but a different frequent-sign set (`dklrs`) showed comparable context predictability. | Positional regularities are **not unique evidence** of “concealer” signs or historical vowel marks. |
| **B14** | Is local variation across adjacent lines consistent with a copy-modify mechanism? | A modest excess of near variants was reported; limited effects also occurred in comparison text. | **Not diagnostic** of a unique copying algorithm or of the absence of language. |
| **B15** | Does deleting characters move Voynich toward comparison-text statistical signatures? | Among the tested deletions, the internal procedure selected **no deletion** as best. The proposed `aeioy` deletion worsened the selected distance measure. | The tested simple-deletion explanation **was not supported**. The broader method's preregistered status was **METHOD_NOT_DISCRIMINATIVE**, restricting strong inferences. |
| **B16** | Does merging frequently occurring adjacent signs restore natural-language-like statistics? | Some distance improvement on Voynich (**ZL3b 3.61 → 2.88; IT2a 3.45 → 2.84**), but the tested low transition entropy and high near-neighbor density persisted. | **Partial structural fit, not decipherment**; the positive control also missed the experiment's preregistered acceptance threshold. Overall method status: **METHOD_NOT_DISCRIMINATIVE**. |

The internal B10–B16 figures above are **historical report values**, not results newly executed or independently verified while preparing this public synthesis. They should not be cited as established scientific facts without their precise protocol and source materials.

### 3.1 The B09 result: coverage versus ambiguity

In the public B09 run, exact-form out-of-vocabulary test sets contained **875** ZL3b and **966** IT2a token occurrences. After the fixed `aeioy` transformation, roughly three-quarters of those occurrences shared a transformed code with at least one training spelling.

However, the matched code often referred to **several different original spellings**. For approximately **85%** of matched occurrences, the transformation did not uniquely reconstruct the original form.

That means **“a code exists in training” is a much weaker statement than “we can reconstruct a word”**, which is itself a much weaker statement than “we know what the word means.”

The control conditions are also informative: deleting the *other* fixed five-character set matched roughly **61%** of unseen tokens, while randomly deleting the same number of positions yielded medians near **48–49%**. These substantial baseline collision rates show why a raw 75% score is not a standalone decoding statistic.

The public code and run logs provide a concrete, independently rerunnable calculation. This remains **computational repeatability within previously explored data**, not independent external review or a new untouched test.

### 3.2 Why the natural-language comparison is inconclusive beyond its test

The internal B15/B16 work focused on two corpus features:

| Feature | Voynich, selected baseline | Eight comparison texts (not all languages) | Internal B15/B16 observation |
| --- | ---: | ---: | --- |
| Approximate next-character transition entropy (`h2`) | ~**2.20 bits** | **3.10–3.54 bits** | The tested transformations did not restore the comparison envelope. |
| Proportion of word-form types with a near neighbor differing by one unit | ~**88%** | **42–65%** | The tested transformations did not restore the comparison envelope. |

Values depend on corpus selection, preprocessing, and the definition of a “character” or glyph unit. Other natural languages and writing systems may have considerably different distributions; **these eight texts cannot define the theoretical limits of natural language**.

In B16, the positive control based on an artificially encoded Latin sample moved toward natural-language signatures after merging, but it **still did not satisfy the preregistered total-distance acceptance gate**. It would be wrong to declare the entire family of variable-length encodings disproven on that basis.

## 4. Hypothesis decisions, stated narrowly

**Supported as an observation:** under the fixed reported preprocessing and folio partitions, deleting selected EVA characters causes many surface-code matches; distinct original spellings frequently merge.

**Not supported by these particular controls:** the claim that deleting `aeioy` reveals a unique historical root inventory or reliably converts the manuscript into one of the comparison texts; the claim that simple local orthographic regularity uniquely identifies null or filler signs.

**Still open:** more complex multigraph, homophonic, variable-length, language-based, or copy-modify mechanisms. Some related approaches predate this research; see, for example, [Timm and Schinner, *Cryptologia*](https://doi.org/10.1080/01611194.2019.1596999) and work on [Naibbe-style cipher construction](https://doi.org/10.1080/01611194.2025.2566408). Neither source is proof of the manuscript's original process.

**Not evaluable:** accuracy of any supposed Voynich word meanings, phonetic assignments, or translation. There is no independent reference translation on which to compute that accuracy. The correct status is **NOT ESTIMABLE**, not “0% translated” and not “75% decoded.”

## 5. Methodological limitations

1. **Previously explored folios:** later B-series “test” folios may have appeared in earlier exploratory model selection, limiting claims of independent blindness.
2. **Code collisions:** reducing information can mechanically increase apparent dictionary coverage even when no true lexical structure is recovered.
3. **Unequal comparative corpora:** transcriptions, natural-language words, writing systems, and artificial line breaks are not inherently equivalent.
4. **Non-universal controls:** the random deletion null matches the count of removed symbols, not all phonotactic or morphological confounds.
5. **Variable segmentation:** EVA units are convenient editorial representations, not settled historical phonemes.
6. **Calibration limitations:** in B15/B16 the preregistered method-discrimination criterion was not met, even where descriptive contrasts looked informative.
7. **Release gap:** outside B09, complete executable workflows and input manifests for these historical internal measurements are not yet available in this public repository.
8. **No independent semantic ground truth:** therefore there is no evidence chain from an EVA spelling through verified historical sound or meaning to a translated Voynich sentence.

## 6. Next independently testable steps

1. **Publish a second narrowly scoped, rights-cleared package** reproducing either B10's full-form candidate selection or B17's line-order statistics with all baselines and immutable source references.
2. **Measure ambiguity explicitly** in any proposed root/codebook approach: report both coverage and how many original forms map to each transformed code.
3. **Test against stronger controls** including matched natural-language corpora, position- and length-aware deletions, and equal-capacity competing mechanisms.
4. **Use prospective evaluation.** Freeze transformation and scoring rules before applying them to new, genuinely untouched evidence. Declare any overlap with past exploratory folios.
5. **Seek external historical anchors.** Blind image/transcription alignment and independently attested period lexical forms are necessary before a semantic claim can be considered.
6. **Invite independent reruns and criticism.** The [public B09 replication issue](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/issues/1) is open for precisely this purpose.

## 7. Provenance and disclosure

This English synthesis is based on internal research records from early November 2026 covering B08/B09, **B10 variant disambiguation**, B11-G/B13, B14, B15 and B16, and on the publicly reproducible B09-OPEN-001 package. An *unrelated older B-33 series* reused a “B10” experiment number internally; its more optimistic fixed-rule statistics must **not** be conflated with the B10 variant-disambiguation results reported here.

The present document contains **no new decipherment test**, no Sherlock proprietary algorithm, no private source code, no candidate reading key, and no third-party raw transcription. It summarizes internal outcomes with their limitations rather than copying the private laboratory archive. Source statements are dated so that future corrections can supersede them transparently.

**Manuscript and primary catalog:** [Beinecke Library, Yale University, MS 408](https://collections.library.yale.edu/catalog/2002046).  
**Public repeatable subset:** [B09-OPEN-001](evidence/b09/README.md), [measured run](evidence/b09/RESULTS.md).  
**Wider project context:** [Hypothesis registry](HYPOTHESES.md), [methodology](METHODOLOGY.md), [scientific assessment](SHERLOCK_SCIENTIFIC_ASSESSMENT.md), and [rights](SOURCES_AND_RIGHTS.md).

**Final interpretation:** The available measurements help distinguish **surface regularity, recoverable spelling, and historically meaningful reading**. None of these experiments demonstrates the last of those three.
