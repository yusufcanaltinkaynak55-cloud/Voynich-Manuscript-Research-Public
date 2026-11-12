# Reproducibility and release readiness

**Current reproducibility classification:** **THREE PUBLICLY RUNNABLE, REAL-CORPUS REFERENCE COMPUTATIONS (B09, B10 AND B17-OPEN); INDEPENDENT EXTERNAL SCIENTIFIC REPLICATION PENDING.**

This public repository contains methodological summaries, a hypothesis registry, carefully labeled internal experiment outcomes, and **three narrowly scoped public reference evaluators** for B09 (transformed spelling collisions), B10 (restricted full-spelling candidate selection), and B17-OPEN (pairwise orientation of transcribed word forms in physical lines). Both use version-pinned third-party transcriptions and verify exact SHA-256 hashes. The repository still contains **no private Sherlock implementation, no raw third-party corpus, and no complete evidence bundle for remaining private-laboratory experiments**.

The [B09-OPEN-001](evidence/b09/README.md), [B10-OPEN-001](evidence/b10/README.md) and [B17-OPEN-001](evidence/b17/README.md) packages are runnable with Python 3.11+, an internet connection to fetch pinned sources, and no private credentials. The [B09 run passed](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/actions/runs/42992577209) and the [B10 run passed](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/actions/runs/43069965161). The [B17 run also passed](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/actions/runs/43185657803). The code and derived metrics are open for inspection; this alone is **not an independent scientific review**. **Do not claim** that cloning this repository reproduces the other internal results in [RESULTS.md](RESULTS.md).

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


## Completed B10 reproducibility stage

- **Source and split integrity:** identical B09 folio partitions reused explicitly, with SHA-256-pinned transcription sources.
- **Model fairness:** position-only parameter choices are included in the contextual model's validation grid; all weights are selected using ZL3b validation only.
- **Observed run:** [B10 public computational results](evidence/b10/RESULTS.md) and its [successful CI log](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/actions/runs/43069965161).
- **Regressions:** [expected aggregate results](evidence/b10/expected_metrics.json), [deterministic numerical check](evidence/b10/check_results.py), and seven synthetic tests.
- **Scientific limitation:** selecting among previously seen candidate spellings is **not** historical reading, and IT2a did not show a robust context-over-role top-1 advantage.

```bash
python -m unittest discover -s evidence/b10 -p 'test_*.py' -v
python evidence/b10/reference.py --download --null-reps 99 --bootstrap-reps 500 --out /tmp/b10-public.json
python evidence/b10/check_results.py --actual /tmp/b10-public.json
```

## Completed B17 public pairwise-order diagnostic stage

- **Narrow scope:** predicts the relative order of *two different observed spellings* within physical P lines. It is **not** the private B17 whole-line beam-search experiment and is not manuscript decipherment.
- **Source integrity:** pinned SHA-256-checkable ZL3b and IT2a transcriptions of the same manuscript.
- **Folio partition:** uses previously explored, physical-folio-disjoint test data; **not a fresh external historical witness**.
- **Comparisons:** directed pair counts, shuffled training-line order, learned visible-edge-position baseline, and folio-bootstrap summaries.
- **Public result:** [measured B17-OPEN findings](evidence/b17/RESULTS.md), [source](evidence/b17/reference.py), [frozen expectations](evidence/b17/expected_metrics.json), and [successful CI run](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/actions/runs/43185657803).

```bash
python -m unittest discover -s evidence/b17 -p 'test_*.py' -v
python evidence/b17/reference.py --download --out /tmp/b17-public.json
python evidence/b17/check_results.py --actual /tmp/b17-public.json
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
