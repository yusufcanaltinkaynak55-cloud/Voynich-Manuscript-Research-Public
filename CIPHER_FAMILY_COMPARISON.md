# CFT-001 | Structural Comparisons With Cryptographic and Non-Cryptographic Mechanisms

**Public synthesis:** 11 November 2026  
**Internal study:** CFT-001, 9 November 2026  
**Classification:** **EXPLORATORY / COMPARATOR ANALYSIS / NOT INDEPENDENTLY REPRODUCED HERE**  
**Decipherment established?** **No.** A Voynich plaintext, reading key, language identity and historical enciphering method are **not known from these tests**.

## Summary

One question motivating the programme is whether Voynich word and glyph distributions resemble the *outcomes of particular historical cipher families* rather than a particular natural-language corpus.

A private exploratory comparison included several simple, artificially implemented mechanisms and a genuine published **Naibbe-style verbose homophonic** ciphertext. Some global statistics of the published Naibbe example were relatively close to the Voynich transcriptions, but an important **adjacent similar-word** statistic had the **opposite sign**. This is a useful counterexample to a facile equation of structural similarity with historical identification.

The **Naibbe comparison is not an original invention of this research programme**: the cipher construction and its published examples are prior work, attributable to their creator. Nor is a combination of cipher and scribal/line effects demonstrably novel. An analogous workshop-cipher proposal has circulated separately; that source was not treated as an externally verified Voynich solution.

This is an English, safely summarized version of the private assessment; it does **not** reveal unpublished Sherlock code, keys, research strategies or raw third-party material.

## Prior work and competing ideas

| Proposed mechanism | Why it is relevant | Status under CFT-001 |
| --- | --- | --- |
| **Verbose homophonic / variable-length cipher, including published Naibbe constructions** | A plaintext unit may have multiple ciphertext renderings and ciphertext groups may span multiple symbols | **PARTIAL STRUCTURAL ANALOGUE**, not a recovered key |
| **Ordinary monoalphabetic substitution** | Preserves many vocabulary-shape invariants under one-to-one replacement | **THE TOY IMPLEMENTATION DID NOT FIT**; not a universal historical exclusion |
| **Simple repeating polyalphabetic substitution** | Could disperse repeated letters and change entropy | **THE TESTED PERIODIC TOY DID NOT FIT** |
| **Simple homophony or null insertion** | Changes surface frequencies without preserving a one-to-one character mapping | **THE TESTED TOYS DID NOT FIT ALL SIGNATURES** |
| **Copy-modify / self-citation mechanisms** | Can produce local near-duplicate forms without assuming an underlying decipherable message | **SERIOUS COMPETING GENERATOR**; tested simplified version was insufficient |
| **Whole-line/whole-book transposition, book ciphers, steganography, complex nomenclators** | Broader cipher families with distinct invariants | **NOT ADEQUATELY TESTED** in this specific comparison |
| **An adapted or constructed writing system** | Could combine linguistic morphology with specialized orthography | **OPEN HYPOTHESIS**, not verified history |

### External research that must be credited

- **Michael Greshko, Naibbe-style cipher study**, *Cryptologia*: [DOI 10.1080/01611194.2025.2566408](https://doi.org/10.1080/01611194.2025.2566408). The published scheme and examples belong to the cited work, not to Sherlock.
- **Timm and Schinner**, copy and self-citation theory, *Cryptologia*: [DOI 10.1080/01611194.2019.1596999](https://doi.org/10.1080/01611194.2019.1596999).
- **Matlach and colleagues**, analysis of Voynich text structure: [PLOS ONE 2022, DOI 10.1371/journal.pone.0260948](https://doi.org/10.1371/journal.pone.0260948).
- **Workshop cipher / Naibbe-related proposal**: [voynich.site exploratory write-up](https://voynich.site/en/findings/workshop-cipher/). It is **not** represented here as peer-reviewed confirmation.

Research into historical ciphers and artificial writing systems long predates the present study. Historical plausibility does not determine authorship or the existence of a hidden plaintext.

## CFT-001 design, as documented internally

- The reference set contained **ZL3b** and **IT2a**, two transcriptions of the *same* Voynich manuscript.
- Comparator materials included two nineteenth-century English works, a published Naibbe ciphertext sample, and **eight synthetic toy mechanisms** under internally specified pre-processing.
- The internal comparison used the first **20,000 eligible token occurrences** of each corpus and a common line-length geometry. Natural source line endings were not preserved in that geometry, introducing an important confound.
- Among the measured properties were conditional symbol entropy, vocabulary size and length, near-neighbor word-form density, first-versus-internal symbol differences, and local adjacency of identical or one-substitution-neighbor words.
- A fixed randomization seed and **19 within-line shuffles** were used for the adjacency baseline. These are not enough for fine-grained significance claims.
- The published Naibbe example was introduced in a documented **exploratory extension after the original toy-model protocol**. Therefore that comparison must **not** be advertised as a fully prospective blind confirmation.

**Reproduction status:** The original scripts, all fixed source corpora and the full machine-readable evaluation package have **not** been released into this public repository. The numbers below are **internally recorded archival values**, not newly run or externally audited data.

## Selected internal measurements

| Metric on 20,000 token occurrences | Voynich ZL3b | Voynich IT2a | Published Naibbe sample |
| --- | ---: | ---: | ---: |
| Conditional next-symbol entropy (bits, `h2`) | **2.221** | **2.252** | **2.170** |
| Distinct written forms | 4,335 | 4,631 | 4,331 |
| Mean token length in defined units | 4.291 | 4.365 | 4.792 |
| Fraction of forms with a same-length one-substitution neighbor | **82.45%** | **81.67%** | **95.80%** |
| Observed fraction of adjacent identical or one-substitution-related forms | 0.03718 | 0.03559 | 0.00911 |
| Matched within-line shuffle reference for adjacent similarity | 0.03404 | 0.03216 | 0.01120 |
| **Relative excess of adjacent similar forms** | **+9.23%** | **+10.67%** | **−18.67%** |

**Positive but limited observation:** Selected global entropy and vocabulary-shape measures were relatively close.

**Negative observation:** The adjacency effect differed in sign, and other measures such as word length and near-neighbor density did not match. This particular published cipher sample **does not reproduce the full measured Voynich signature**. Because its original message, segmentation and content differ from the manuscript, the mismatch **does not disprove the broader cipher family**.

## What these data cannot tell us

- The probability that Voynich was produced by Naibbe, another historical cipher family, or a copy-modify process.
- The manuscript's actual language, historical author, plaintext or cipher key.
- The genuineness or semantic content of a particular apparent glyph cluster.
- Whether every family member would show the same mismatches as a single sample or toy implementation.
- Whether a model that fits the measured statistics can recover a withheld key on a novel cipher.

**Structural resemblance is not cryptanalytic identification.** Different mechanisms can create similar measurements. The physical manuscript and source history must supply independent evidence.

## Next falsifiable public milestone

A new study should **pre-register** the comparators and numerical acceptance criteria before a fresh data split or previously untested corpus is examined. At minimum:

1. Include published known-key variable-length ciphers, copy-modify models, and frequency/position-matched nulls, **with source rights checked**.
2. Use identical text budgets, clearly specified tokenization and geometries, and stronger uncertainty estimation than 19 shuffles.
3. Measure both global properties **and** the adjacency effect so a model cannot succeed by fitting one metric while silently failing another.
4. In addition to structural resemblance, test **recovery of genuinely withheld plaintext and keys** on separate known-answer material.
5. State up front whether the result is **structural calibration** or **historical reading**; do not switch interpretations after seeing the answer.
6. Preserve negative and failed outcomes, audit previous holdout exposure, and invite independent replication.

A release of CFT-002 source code and machine-readable derived outputs would strengthen auditability, but is **not claimed to have occurred in this document**.

## Literature and novelty provenance

See the [selected and source-checked bibliography](REFERENCES.md) for complete author names, titles and original DOI links for Greshko's Naibbe construction, Timm and Schinner's self-citation model, and Matlach, Janečková and Dostál's symbol-role study. These are **existing contributions by other researchers**, not methods first invented by Sherlock.

## Related public project materials

- [Scientific status and research gates](SHERLOCK_SCIENTIFIC_ASSESSMENT.md).
- [Sherlock Model Card](SHERLOCK_MODEL_CARD.md).
- [Hypothesis registry](HYPOTHESES.md).
- [Glyph-deletion and collision controls](GLYPH_OBFUSCATION_STUDY.md).
- [First open B09 benchmark](evidence/b09/README.md).
- [Reproducibility standards](REPRODUCIBILITY.md).

**Rights:** No raw manuscript images, third-party cipher text, source transcriptions or unreleased private model assets are copied into this report. Please consult [SOURCES_AND_RIGHTS.md](SOURCES_AND_RIGHTS.md) before reusing original documents or code.
