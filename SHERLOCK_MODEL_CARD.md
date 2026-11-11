# Sherlock | Research Model Card (Public Disclosure Edition)

**Version:** 0.1 — 11 November 2026  
**Maintainer:** Yusuf Can Altınkaynak, independent research  
**Category:** Experimental computational text and cryptanalysis research system  
**Scientific status:** **NOT A VERIFIED VOYNICH DECIPHERMENT**  
**Release status:** This card describes a **private research program**; it does **not** release Sherlock source code, checkpoints, training assets, model weights, search configurations or candidate keys.

## Overview

**Sherlock** is the project's umbrella name for a research programme exploring the structure of the Voynich Manuscript (Beinecke MS 408), possible writing and encoding mechanisms, and how to evaluate alternative explanations under controlled conditions.

The system is a **research prototype**, not a historical translation service or an independently validated cryptanalytic product. It combines computational analysis with human-directed hypotheses. Its precise implementation is private.

## Intended scientific uses

- Describe and compare observable written-form distributions and positional regularities in an editorial transcription.
- Test specific, falsifiable predictions about word-shape variation and line structure.
- Compare whether particular generating or encoding mechanisms reproduce declared statistical signatures.
- Evaluate models using known-answer reference ciphers and explicitly separate key recovery from structural similarity.
- Generate hypotheses to be **challenged by independent evidence**, not substitute model output for historical linguistic attestation.

**Not intended for:** reliable manuscript translation, assigning verified phonetic values, reconstructing an unidentified historical language, identifying the manuscript's author, fabricating meanings for visually suggestive tokens, or inferring that apparent resemblance proves shared provenance.

## Data represented in the research programme

- Editorial Voynich transcriptions such as **ZL3b** and **IT2a**, which represent the **same physical manuscript** and may differ in uncertain readings or segmentation.
- Historical and modern language reference corpora and published known-cipher comparators, subject to source-specific rights and suitability review.
- Model evaluation datasets and internal analysis products maintained separately.

Source transcriptions, third-party datasets, original manuscript images, and Sherlock private training data are **not bundled with this public card**. Publicly rerunnable **reference implementations** of narrowly defined tasks are instead placed in [evidence/](evidence/).

## Observed capabilities and evidence hierarchy

| Task | Available public or internal evidence | Assessment |
| --- | --- | --- |
| Parsing and comparing transcriptional word patterns | Public [B09-OPEN-001](evidence/b09/README.md) reference code, source-hash validation, and successful real-data run | **PUBLIC COMPUTATIONAL REPEATABILITY** for **code-collision statistics only** |
| Selecting an original EVA spelling from a shortened code | [B10-OPEN-001](evidence/b10/RESULTS.md): successful real-data public run on restricted candidates with explicit fair-grid and coverage controls | **PUBLIC COMPUTATIONAL REPEATABILITY**, not independently validated decoding |
| Conditional written-form prediction | Internally reported experiments using fixed validation and test groups, with task-specific baselines | **INTERNAL EXPLORATORY EVIDENCE**, not separately reproduced here |
| Known-answer cipher solving | Internally recorded calibration runs, with important failures and model-family constraints | **INSUFFICIENT for general cryptanalytic competence** |
| Recovering an authenticated Voynich key, sounds or meanings | No independently verified key or external semantic ground truth | **NOT ESTABLISHED / NOT ESTIMABLE** |

**Do not conflate the first two rows with decrypting manuscript text.** A word shape that matches a compressed training code is not a known word meaning. For a realistic appraisal of the programme, read the [Koçi Bey scientific assessment](SHERLOCK_SCIENTIFIC_ASSESSMENT.md).

## What does “accuracy” mean here?

The project has used several **mutually incompatible metrics**:

- *Codebook collision rate:* fraction of unseen **spellings** whose simplified spelling shares a training code.
- *Top-1 original-form classification:* fraction of **eligible, training-codebook-representable** targets for which a model selects the exact transcription spelling.
- *Negative log2 probability:* predictive uncertainty measured in bits per evaluated token or character.
- *Edit similarity on a known cipher:* normalized string resemblance, which is **not necessarily character-wise decryption accuracy**.
- *True historical decipherment accuracy:* **NOT ESTIMABLE**, because independent authenticated Voynich plaintext is unavailable.

A higher number for one task must **never** be advertised as the fraction of the Voynich Manuscript that Sherlock has deciphered.

## Evaluation requirements and known failure modes

1. **Folio leakage and prior exploration.** Earlier model searches have examined parts of what subsequent experiments call test folios. A newly claimed blind test requires genuinely fresh evaluation or full disclosure of prior exposure.
2. **Shared historical source.** ZL3b and IT2a assess transcription sensitivity; they are not two independent historical documents.
3. **Many-to-one compression.** Removing characters can increase code collisions while destroying information needed to reconstruct original spellings.
4. **Evaluation-set restrictions.** A classification score conditioned on the correct spelling already being in the training candidate set does **not** measure full manuscript coverage.
5. **Confounds and unbalanced baselines.** Role, manuscript section, text type, page proximity, and the model search budget can produce spurious advantages.
6. **Language chronology.** Modern linguistic corpora and classical sources are not automatically faithful proxies for fifteenth-century orthographic conventions.
7. **Cipher-family mismatch.** A solver constrained to one character per token cannot recover arbitrary multi-character plaintext units from variable-length historical ciphers.
8. **Overconfidence.** A statistical or model probability is not the posterior probability that an interpretation is the authentic reading without suitable model calibration and independent evidence.

## Transparency and release limitations

The code, model architecture, weights, unpublished cryptanalytic candidate keys, special configurations and private source corpora are **not publicly accessible**. A public write-up cannot provide full end-to-end replication of the private Sherlock system. This must be acknowledged wherever internal performance numbers are shown.

The successfully executed public B09 and B10 scripts are **limited experimental reference code**, not Sherlock exports, reverse-engineered components, or proof of model equivalence. Findings remain subject to independent review.

The programme is human-led and uses AI assistance in hypothesis formation, writing and software development. AI-generated statements are treated as hypotheses or drafts until checked against actual sources, execution logs and counterexamples.

## Scientific acceptance gates

- **Gate A: Known-answer competence.** Recover genuinely hidden reference keys/plaintext under separately graded, preregistered conditions.
- **Gate B: Voynich discriminability.** Predict unseen manuscript structures better than matched rival language/cipher/copying mechanisms.
- **Gate C: Historical reading.** Apply one frozen key to independent, verifiable image/lexical anchors and unseen passages, with expert audit and error accounting.

**No gate has been independently certified as passed in this public repository.**

## Collaboration and appropriate citation

External researchers can audit [public experiments](evidence/b09/README.md), review [hypothesis status](HYPOTHESES.md), or contribute stronger controls and documented failure cases under [CONTRIBUTING.md](CONTRIBUTING.md). For attribution to the repository itself, use [CITATION.cff](CITATION.cff). This card is **not** a peer-reviewed model publication, benchmark leaderboard certification, or guarantee of a public API.

**Use restriction notice:** The original documents and reference scripts in this repository do not yet have an explicit general reuse license; see [SOURCES_AND_RIGHTS.md](SOURCES_AND_RIGHTS.md). That does not supersede the licensing of third-party source transcriptions.

*Review this card after any independently verified result or substantial change in the released evidence; do not silently overwrite historical performance claims.*
