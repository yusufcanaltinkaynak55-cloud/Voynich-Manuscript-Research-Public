# Voynich Manuscript Research | Public Research Record

**Independent, exploratory research on the Voynich Manuscript (Beinecke MS 408)**

**Maintainer:** Yusuf Can Altınkaynak  
**Public record initiated:** 11 November 2026  
**Status:** Research in progress; **no independently verified decipherment, reading key, phonetic mapping, or word translation**.

This repository presents a carefully scoped public record of computational and historical hypotheses about the Voynich Manuscript. The objective is to test how the manuscript's writing behaves and to compare competing language, script, and cipher mechanisms without treating resemblance or a machine-learning score as a translation.

The public repository is **not** a mirror of the private research environment. It does not contain the proprietary Sherlock research implementation, model weights, unpublished candidate keys, private correspondence, credentials, or third-party raw corpora and manuscript images. Some summarized results originate in internal experiment records and **cannot yet be reproduced from this public release**. Exceptions are the narrowly defined **B09 spelling-collision calculation** and **B10 full-spelling candidate-selection benchmark**, for which separately scoped public reference programs and successful GitHub Actions runs are now available. This is computational repeatability, **not independent semantic verification**.

## Public evidence packages and scientific assessments

The repository now includes two **separate reference benchmark implementations**. B09 has successfully reproduced its structural aggregate statistics; [B10](evidence/b10/RESULTS.md) has also successfully run its more demanding, restricted full-spelling candidate-selection task with a fairer model-selection grid. In the B10 public test, contextual top-1 classification improved slightly over position-only on ZL3b but not IT2a. The [B09 completed run](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/actions/runs/42992577209) and [B10 completed run](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/actions/runs/43069965161) provide public execution evidence. Such runs are **not** outside scientific replication, verified translation, or proof of a historical key.

The [Sherlock Model Card](SHERLOCK_MODEL_CARD.md) discloses the private system's intended research uses and limitations without opening proprietary code. The [cipher-family comparison](CIPHER_FAMILY_COMPARISON.md) summarizes exploratory internal CFT-001 measurements and prior academic work; that entire experiment is **not** independently reproducible from this public repository.

## First publicly runnable real-data evidence package

**[B09-OPEN-001: unseen-spelling code collisions](evidence/b09/README.md)** is a small, transparent Python-standard-library test on version-pinned ZL3b and IT2a transcriptions. Both inputs are independently downloaded and hash-checked; a folio-partitioned OOV test compares deletion of `aeioy` against deletion of `dklrs` and 30 matched-deletion-count randomized controls. This explicitly tests **spelling collisions, not decipherment**.

- [Measured public-run results](evidence/b09/RESULTS.md): 875 / 966 OOV test occurrences; 75.77% / 74.95% `aeioy` collisions, versus the specified controls.
- [Reproduction script](evidence/b09/reference.py), [regression tests](evidence/b09/test_reference.py), [frozen expected outputs](evidence/b09/expected_metrics.json).
- [Successful public GitHub Actions run](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/actions/runs/42992577209).

The code is a **reference reimplementation**, not the private Sherlock software. These are previously explored holdouts, **not a newly blind discovery**. A third-party research team has **not yet** independently replicated or reviewed the findings.

## Read the research

| Document | Purpose |
| --- | --- |
| [HYPOTHESES.md](HYPOTHESES.md) | Competing hypotheses, limitations, and falsification criteria |
| [GLYPH_OBFUSCATION_STUDY.md](GLYPH_OBFUSCATION_STUDY.md) | English-language scientific synthesis of B08–B16: glyph deletion, collisions, controls, and negative results |
| [evidence/b10/README.md](evidence/b10/README.md) | Successfully run public B10 full-form selection benchmark, with fair baseline grid and measured results |
| [SHERLOCK_MODEL_CARD.md](SHERLOCK_MODEL_CARD.md) | Public Sherlock capabilities, limitations, research boundaries, and evaluation requirements |
| [CIPHER_FAMILY_COMPARISON.md](CIPHER_FAMILY_COMPARISON.md) | CFT-001 structural cipher and copy-modify comparison; external comparators and negative evidence |
| [SHERLOCK_SCIENTIFIC_ASSESSMENT.md](SHERLOCK_SCIENTIFIC_ASSESSMENT.md) | Public Koçi Bey (KBR-001) scientific assessment: Sherlock's capabilities, limitations, evidence gates and roadmap |
| [evidence/b09/README.md](evidence/b09/README.md) | First public real-data reproduction package and verified run |
| [METHODOLOGY.md](METHODOLOGY.md) | Research design, controls, leakage risks, and evidence standards |
| [RESULTS.md](RESULTS.md) | Dated exploratory findings, negative results, and what they **do not** establish |
| [REPRODUCIBILITY.md](REPRODUCIBILITY.md) | Current reproducibility gap and an auditable release checklist |
| [SOURCES_AND_RIGHTS.md](SOURCES_AND_RIGHTS.md) | Primary sources, transcription provenance, third-party rights, and licensing status |
| [CITATION.cff](CITATION.cff) | How to cite this **repository** (not a peer-reviewed publication) |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to submit falsifiable, sourced research contributions |

## Research directions

- Position-sensitive patterns in glyph sequences, words, lines, and manuscript sections.
- Alternative interpretations of apparent stems, suffixes, scribal variation, and transliteration.
- A **constructed or adapted writing/language system** hypothesis involving historical borrowing; this is **unverified**.
- Comparison of cipher families, including substitution, homophony, variable-length encoding, and copy-modify processes.
- Calibrating methods on *known* ciphers, while keeping success on those ciphers separate from success on Voynich.

The name **Sherlock** denotes a private experimental research system for candidate generation, controlled comparisons, and evaluation. Its presence in research descriptions is **not** evidence that the manuscript has been deciphered. No source code, architecture, keys, training data, or model checkpoints for Sherlock are published here.

## Evidence rules

1. **Observation is not interpretation.** A recurring pattern does not prove a sound, word, language, or meaning.
2. **Internal replication is not independent validation.** Two transcriptions of MS 408 are not two independent manuscripts.
3. **Known-key or synthetic-cipher benchmarks are calibrations.** They cannot be reported as Voynich decoding accuracy.
4. **Negative outcomes are retained.** Failure of a *specific implementation* does not refute every version of a hypothesis.
5. **No translation percentage without an independently verified truth set.** Current semantic decipherment accuracy is **not estimable**, not “0%.”

Statuses used here: **EXPLORATORY**, **SIMULATION / CALIBRATION**, **NOT SUPPORTED (specific test)**, **NOT EVALUABLE**, **PENDING INDEPENDENT REVIEW**, and **NOT YET SCIENTIFICALLY VERIFIED**.

## Primary manuscript and external materials

The manuscript is held by the **Beinecke Rare Book & Manuscript Library, Yale University**, as MS 408. Yale provides digital images and a general description:

- [Yale Library: The Beinecke Cipher (Voynich) Manuscript](https://beinecke.library.yale.edu/beinecke/collections/beinecke-cipher-voynich-manuscript)
- [Sources, provenance, and rights](SOURCES_AND_RIGHTS.md)

This project is independent. It is **not affiliated with, endorsed by, or a decipherment announcement from Yale University**.

## Language of this public repository

**English is the publication language** for all public-facing reports, repository documentation, code comments, workflow descriptions, issue discussions, and contribution proposals. Names of people and historical report titles (e.g., **Koçi Bey**) are preserved as proper nouns; any substantial non-English quotation must include an English rendering. This convention does not change the private laboratory's language or source-document originals.

## Participation and citation

See [CONTRIBUTING.md](CONTRIBUTING.md) for evidence-based contributions and [CITATION.cff](CITATION.cff) for attribution. This repository is a living, non-peer-reviewed research record. The presence of a public link or a citation file does not constitute external verification.

**Licensing notice:** A reuse license has **not yet been selected** for these original documents. Do not assume that public visibility grants permission for unrestricted reuse; see [SOURCES_AND_RIGHTS.md](SOURCES_AND_RIGHTS.md) for details.
