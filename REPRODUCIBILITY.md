# Reproducibility and release readiness

**Current reproducibility classification:** **ONE PUBLICLY RUNNABLE, REAL-CORPUS COMPUTATIONAL REPRODUCTION (B09-OPEN-001); INDEPENDENT EXTERNAL SCIENTIFIC REPLICATION PENDING.**

This public repository contains methodological summaries, a hypothesis registry, carefully labeled internal experiment outcomes, and **one self-contained reference evaluator** for a precisely defined part of the B09 study. The evaluator fetches third-party transcriptions from immutable upstream versions and verifies their hashes. The repository still contains **no private Sherlock implementation, no raw third-party corpus, and no complete evidence bundle for the other internal experiments**.

The [B09-OPEN-001 reproduction package](evidence/b09/README.md) is **runnable** with Python 3.11+, an internet connection to fetch pinned sources, and no private credentials. Its [first public run passed](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/actions/runs/42992577209). The code and derived metrics are open for inspection; this alone is **not an independent scientific review**. **Do not claim** that cloning this repository reproduces the other internal results in [RESULTS.md](RESULTS.md).

## Completed B09 reproducibility stage

- **Source integrity:** version-pinned ZL3b/IT2a transcriptions and hard-coded SHA-256 validation.
- **Evaluation disclosure:** deterministic folio-stratified split, held-out OOV definition, competing fixed masks, and 30 equal-deletion-count null trials.
- **Public execution:** GitHub Actions unit tests and real-corpus computation completed successfully on 11 November 2026.
- **Durable baseline:** [measured results](evidence/b09/RESULTS.md) and [machine-readable aggregate expectations](evidence/b09/expected_metrics.json).
- **Remaining:** outside reproduction, independent data/segmentation audit, truly new holdout, and historical reading/meaning validation.

```bash
python -m unittest discover -s evidence/b09 -p 'test_*.py' -v
python evidence/b09/reference.py --download --trials 30 --out /tmp/b09-public.json
python evidence/b09/check_results.py --actual /tmp/b09-public.json
```


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
