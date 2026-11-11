# Methodology and scientific safeguards

**Version:** Initial public protocol summary, 11 November 2026. This is a description of research practice and planned public verification, **not** a claim that the private implementation has been independently audited.

## 1. Research questions

We separate four tasks that must never share an undifferentiated “accuracy” percentage:

1. **Transcription and structural measurement:** What patterns occur in glyph strings, tokens, lines, sections, and positions?
2. **Prediction and generation:** Can a model predict hidden glyphs or reproduce specific distributional statistics?
3. **Known-key cryptanalysis:** Can a solver recover a withheld key or plaintext on a cipher with a verifiable answer?
4. **Historical Voynich decipherment:** Can a fixed interpretation recover independently checkable text, meanings, or a key from manuscript evidence?

Success at (1), (2), or (3) does **not** imply success at (4).

## 2. Data and provenance

- **Primary object:** Beinecke MS 408. The underlying images and catalog information are controlled by Yale and should be consulted at their source.
- **Transcription witnesses:** Work has considered IVTFF-based ZL3b and Takahashi/IT-style renderings. These are **alternative transcriptions of the same historical document**, not independent manuscripts.
- Record transcription identifier, version, line conventions, uncertainty markers, section/folio references, input hashes, and exclusion rules.
- Avoid silently converting **EVA transcription units** into historical sounds or letters; segmentation and glyph ambiguity are model choices.
- Respect the licensing, attribution, and redistribution terms of each external corpus. Raw transcriptions or third-party historical editions are **not** redistributed in this initial release.

## 3. Evaluation design

1. State the **narrow, falsifiable claim** and pre-register decision criteria before the final test where possible.
2. Split by **physical folio** rather than randomly mixing highly related words across train and test. Track repeated folio reuse across studies.
3. Fit model selection on training/validation data. Lock hyperparameters and transforms before touching test data.
4. Compare **matched baselines**: frequency, n-gram, length, word/line-position shuffles, copy-modify, and alternative segmentations as relevant.
5. Use equal candidate budgets and identical data access for competing mechanisms; document any exceptions.
6. Examine stability across transcriptions, manuscript sections, and plausible scribal or copying confounders.
7. Report the metric's numerator, denominator, decision threshold, confidence/uncertainty where justified, and all failure cases.
8. Preserve negative results, timeouts, missing inputs, and post-hoc analyses with explicit labels.

**Leakage warning:** Reusing the same withheld folios in multiple exploratory experiments can make subsequent “blind” results less convincing even when each script uses a train/test split. A genuinely new test set or independent historical witness is needed for stronger claims.

## 4. Historical and semantic verification

A proposed word reading must be traceable through the following chain:

**original image region → independently checked glyph transcription → frozen glyph/sound or cipher rule → source-backed historical lexical candidate → blind competing-candidate evaluation.**

Drawing proximity alone does not establish meaning. Shared spelling fragments alone do not establish Arabic, Persian, Latin, Turkish, Hebrew, or any other source language. A historical analogy is not an attestation of the manuscript's author or cipher.

## 5. Evidence grading

| Evidence | Appropriate interpretation |
| --- | --- |
| Descriptive frequency and positional effects | Structural observation |
| Stronger held-out glyph prediction | Predictive improvement for the defined task |
| Synthetic cipher or known-key recovery | Calibration/benchmark under its exact conditions |
| Similarity to a known cipher family | Analogy or hypothesis-generating evidence |
| Independently verified reading and translation | Potential decipherment evidence, subject to critical review |
| No reliable answer key | **NOT EVALUABLE / NOT ESTIMABLE** for semantic accuracy |

An independent reimplementation must use the published data manifest, hashes, protocol, outputs, and scripts. **Most internal experiments do not yet have those complete materials in this public repository.** Two narrowly scoped, publicly runnable exceptions are [B09-OPEN-001](evidence/b09/README.md), which tests transformed-code collisions, and [B10-OPEN-001](evidence/b10/RESULTS.md), which tests restricted full-spelling candidate selection. Neither estimates word meanings or a deciphered manuscript. See [REPRODUCIBILITY.md](REPRODUCIBILITY.md).

## 6. Authorship, AI use, and corrections

This is human-directed research with AI-assisted analysis and software development. AI-generated hypotheses, code, text, and interpretations receive no automatic authority: they must pass the same source checks, controls, and independent verification. Material corrections should retain dates, the original claim, the new evidence, and a reason for the revision.
