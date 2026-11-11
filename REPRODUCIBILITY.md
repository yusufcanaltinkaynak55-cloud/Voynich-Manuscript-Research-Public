# Reproducibility and release readiness

**Current reproducibility classification:** **PUBLIC DOCUMENTATION ONLY / INDEPENDENT REPRODUCTION NOT YET AVAILABLE.**

This initial public repository contains methodological summaries, a hypothesis registry, and carefully labeled internal experiment outcomes. It contains **no executable reproduction package**, no raw third-party corpus, no complete test manifest, and no proprietary Sherlock implementation.

**Do not claim** that cloning this repository alone reproduces the numerical values in [RESULTS.md](RESULTS.md).

## Minimum evidence bundle for a future independently reproducible result

For each proposed release, provide:

- [ ] A single, frozen question and pre-registered success/failure criterion.
- [ ] Corpus/source identity; download location; reuse rights; immutable revision and cryptographic hashes.
- [ ] Transcription/segmentation conventions, uncertainty handling, and preprocessing documentation.
- [ ] Physical folio (not just random token) train/validation/test manifests.
- [ ] Disclosure of overlap with all previously explored held-out folios.
- [ ] Baselines, null controls, equal search budgets, and candidate-selection procedure.
- [ ] Executable scripts or a **sufficient, inspectable substitute**; versioned dependencies and environment.
- [ ] Fixed seeds where applicable, exact commands, run timestamps, raw metrics, and failure cases.
- [ ] Independent verification: new executor, recorded deviations, and an untouched external test where scientifically necessary.
- [ ] A conclusion limited to the specific outcome measured, with no semantic extrapolation.
- [ ] Security, privacy, copyright, and third-party data redistribution review.

Check boxes are **not** assertions of completion; the default status is unverified.

## Suggested validation sequence

1. **Provenance check:** confirm source licenses, URLs, file versions, hashes, and folio IDs.
2. **Deterministic reproduction:** reproduce numeric outputs with a public or independently inspectable reference pipeline.
3. **Competing mechanisms:** replicate comparisons using appropriate confound controls and matched budgets.
4. **Generalization:** evaluate on truly unseen folios or a separate suitable source witness.
5. **Historical claim gate:** separately verify any asserted reading, sound, or meaning through image and independent lexical evidence.
6. **External audit:** ask independent reviewers to rerun, dispute, and annotate all conclusions.

## Protection of unreleased materials

The private Sherlock implementation, model parameters, experimental keys, unreleased source data, private correspondence, and credentials are **not part of the public bundle**. A future proprietary or controlled-access evaluation may still be scientifically useful, but its access limitations must be disclosed, and it must **not** be described as fully open reproducibility.

This document is a roadmap, not a certification. For current findings and caveats, see [RESULTS.md](RESULTS.md).
