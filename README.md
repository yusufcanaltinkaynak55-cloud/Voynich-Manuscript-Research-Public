# Voynich Manuscript Research

**An independent, evidence-led investigation of the Voynich Manuscript (Yale Beinecke MS 408)**

[![Research publication quality](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/actions/workflows/repository-quality.yml/badge.svg)](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/actions/workflows/repository-quality.yml)
[![B09 reproducibility](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/actions/workflows/b09-public-reproduction.yml/badge.svg)](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/actions/workflows/b09-public-reproduction.yml)
[![B10 reproducibility](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/actions/workflows/b10-public-reproduction.yml/badge.svg)](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/actions/workflows/b10-public-reproduction.yml)
[![B17 diagnostic](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/actions/workflows/b17-public-reproduction.yml/badge.svg)](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/actions/workflows/b17-public-reproduction.yml)

**Maintainer:** Yusuf Can Altınkaynak  
**Research scope:** Computational analysis, historical cipher comparison, testable writing-system hypotheses, and scientific reproducibility  
**Public record:** Established November 2026; documentation updated **12 November 2026**  
**Decipherment status:** **No independently verified key, sound system, word meaning, or translation.**

> **Scientific boundary:** This project is **not** announcing a solution to the Voynich Manuscript. It measures specific observable patterns in editorial transcriptions. Successful statistical prediction, software CI, and matching codes are **not equivalent to reading the historical text**.

## At a glance

The project separates *observation*, *prediction*, *cipher calibration* and *historical meaning*. A narrow positive result is published with its denominators, failed controls, corpus limitations and a reproducible computational procedure where available.

| Public study | Precisely measured task | Reported results on ZL3b / IT2a | Evidence status |
| --- | --- | --- | --- |
| **[B09](evidence/b09/README.md)** | Does deleting a fixed set of EVA transcription characters cause unseen *spellings* to match transformed training codes? | **75.77% / 74.95%** code collisions; about **85%** of matches are ambiguous among several original spellings | [Reproducible public computation](evidence/b09/RESULTS.md); external scientific audit pending |
| **[B10](evidence/b10/README.md)** | Can a model choose the correct original *EVA spelling* from multiple already-seen training candidates? | **53.90% / 53.05%** contextual top-1 on **4,659 / 4,616 eligible examples**, compared with a strong frequency/position baseline | [Reproducible public computation](evidence/b10/RESULTS.md); right-context use and selection bias disclosed |
| **[B17-OPEN](evidence/b17/README.md)** | Can models predict which of two different word spellings appeared first in a physical manuscript line? | **52.54% / 52.52%** directed word-pair accuracy; **61.16% / 60.35%** visible edge-position diagnostic | [Reproducible public computation](evidence/b17/RESULTS.md); **not** the original private whole-line B17 |

All three experiments use version-pinned **ZL3b and IT2a transcriptions of the same manuscript**. These are **not two independent historical witnesses**. Previously explored folios were reused in the tests; the work does **not** establish a newly blind historical decipherment. Results across the three tasks must **never be combined as a fraction of the book decoded**. Historical semantic accuracy remains **NOT ESTIMABLE**.

The publicly released reference scripts were written separately from the **private Sherlock** research environment. None of the scripts is a distribution of Sherlock code, model checkpoints, candidate keys or proprietary training assets.

## Where to begin

| Publication | What it contains |
| --- | --- |
| **[Research roadmap](RESEARCH_ROADMAP.md)** | Delivered stages, unmet scientific acceptance gates, independently auditable next steps |
| **[Evidence index](evidence/README.md)** | All three public real-data experiments, versions, software and reviewer status |
| **[Selected literature](REFERENCES.md)** | Confirmed prior academic work, primary source attributions and novelty limits |
| **[Change log](CHANGELOG.md)** | Dated public research updates, corrections, earlier failed CI runs, and outstanding scientific limitations |
| **[Sherlock Model Card](SHERLOCK_MODEL_CARD.md)** | Intended uses, supported measurements, methodological limitations and disclosure boundaries |
| **[Koçi Bey scientific assessment](SHERLOCK_SCIENTIFIC_ASSESSMENT.md)** | Critical programme review, six principal obstacles and three acceptance gates |
| **[Hypothesis register](HYPOTHESES.md)** | Competing, falsifiable claims and their current evidential status |
| **[Glyph-deletion study](GLYPH_OBFUSCATION_STUDY.md)** | B08–B16 structural experiments and negative controls, distinguishing code collisions from reading |
| **[Cipher-family comparison](CIPHER_FAMILY_COMPARISON.md)** | CFT-001 exploratory comparison with prior published cipher and copy-modify models |
| **[Methodology](METHODOLOGY.md)** and **[results ledger](RESULTS.md)** | Evaluation principles, scientific status labels, limitations and dated findings |
| **[Reproducibility](REPRODUCIBILITY.md)** | Required source manifests, data separation, run evidence and independent validation standards |

### Reproduce the three scoped public computations

Python 3.11+ and an internet connection are sufficient to retrieve the exact pinned upstream transcriptions and run the reference implementations. No private repository credentials are required.

```bash
# First, verify the public code and repository integrity:
python scripts/audit_public_repo.py
python -m unittest discover -s evidence/b09 -p 'test_*.py' -v
python -m unittest discover -s evidence/b10 -p 'test_*.py' -v
python -m unittest discover -s evidence/b17 -p 'test_*.py' -v

# Then run real-source computations and compare frozen summary metrics:
python evidence/b09/reference.py --download --trials 30 --out /tmp/b09-result.json
python evidence/b09/check_results.py --actual /tmp/b09-result.json

python evidence/b10/reference.py --download --null-reps 99 --bootstrap-reps 500 --out /tmp/b10-result.json
python evidence/b10/check_results.py --actual /tmp/b10-result.json

python evidence/b17/reference.py --download --out /tmp/b17-result.json
python evidence/b17/check_results.py --actual /tmp/b17-result.json
```

**Execution evidence:** [B09 passing Actions run](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/actions/runs/42993276261), [B10 passing Actions run](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/actions/runs/43070522482), [B17 passing Actions run](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/actions/runs/43185657803). The live badges above reflect **software-workflow status, not peer review or decipherment**.

## Scholarly standards and release policy

- **Independent validation is not yet complete.** Publicly runnable code and repeat runs are computational evidence, not an external referee's finding. See [reproducibility requirements](REPRODUCIBILITY.md).
- **Negative results remain visible.** Failed tests, competing models and alternative interpretations are recorded rather than discarded.
- **Comparative research is credited.** The project does not claim authorship of historical cipher systems or earlier Voynich models; see [selected academic literature](REFERENCES.md) and [CFT-001](CIPHER_FAMILY_COMPARISON.md).
- **Upstream text and image rights are respected.** Third-party transcriptions are fetched from pinned sources rather than redistributed. See [source manifest](evidence/SOURCE_MANIFEST.json) and [sources and rights](SOURCES_AND_RIGHTS.md).
- **No private technology disclosure.** The proprietary Sherlock research system, unpublished code, model weights, candidate keys, private correspondence and secrets are not part of this public repository. See [responsible disclosure guidance](SECURITY.md).
- **English-only public research communication.** Original personal names, historical titles and primary-source terms remain properly attributed.

## Contribute, cite and follow the work

Critical assessments, independent reimplementations, corrections and negative findings are welcome. Start with [CONTRIBUTING.md](CONTRIBUTING.md) and the [roadmap](RESEARCH_ROADMAP.md). See [CITATION.cff](CITATION.cff) to cite this *living GitHub research record*, not a peer-reviewed decipherment paper.

The manuscript is held by [Yale's Beinecke Rare Book & Manuscript Library, MS 408](https://beinecke.library.yale.edu/beinecke/collections/beinecke-cipher-voynich-manuscript). This independent project is **not affiliated with or endorsed by Yale University**.

**Rights:** No general reuse license for the project's original documents and public reference scripts has yet been granted. **Public visibility does not equal an open-source or Creative Commons license.** See [SOURCES_AND_RIGHTS.md](SOURCES_AND_RIGHTS.md) and the [release-readiness decision](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/issues/3).
