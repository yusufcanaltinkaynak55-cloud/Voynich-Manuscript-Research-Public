# B09-OPEN-001 | First completed public run

**Completed:** 11 November 2026  
**Run:** [GitHub Actions #42992577209](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/actions/runs/42992577209)  
**Source commit:** [`c969120ebbdfc9e236c55a0a1aed517fd1ffaa20`](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/commit/c969120ebbdfc9e236c55a0a1aed517fd1ffaa20)  
**Workflow conclusion:** **success**. Seven synthetic unit tests passed; pinned ZL3b and IT2a source hashes passed; the output contract was checked; the complete derived JSON was uploaded as a workflow artifact (retention-limited).

## Actual public-run results (not merely predictions)

| Metric | ZL3b | IT2a |
| --- | ---: | ---: |
| Held-out exact-form OOV token occurrences | **875** | **966** |
| Deleting `aeioy`: training-code collision rate | **0.757714** (75.77%) | **0.749482** (74.95%) |
| Deleting `dklrs`: control collision rate | 0.610286 (61.03%) | 0.615942 (61.59%) |
| Equal-deletion-count random-position control: 30-trial median | 0.475429 (47.54%) | 0.489648 (48.96%) |
| Observed difference: `aeioy` minus `dklrs` | **0.147428** (+14.74 pp) | **0.133540** (+13.35 pp) |
| Matched instances whose code maps to multiple training spellings | **0.853695** (85.37%) | **0.853591** (85.36%) |

**Interpretation:** On this **previously explored, folio-partitioned** dataset, a fixed five-character deletion transformation produces more transformed **spelling collisions** than these two controls. It does not demonstrate that those five signs represent vowels, nulls, diacritics, or a historical decipherment key.

**Why the result is not a translation:** Many distinct training spellings collapse to the same shortened code; the apparent coverage is many-to-one. Neither translation correctness nor historical linguistic identity has a verified gold standard. **Voynich semantic decoding accuracy: NOT ESTIMABLE.**

## Verification provenance

- The original closed-laboratory B08/B09 test from 4 November 2026 reported collision rates rounded to 75.77% / 74.95% and OOV counts 875 / 966. This **public reference implementation** reproduced those principal values under the exact pinned transcriptions and partition key.
- Fixed negative controls (`dklrs` and same-deletion-count random deletion) were also computed in the same public run, not adopted from a private report.
- The public artifact contains further machine-readable derived counts and split fingerprints; no raw manuscript transcription or Sherlock code was committed.
- An independent outside researcher **has not yet been documented as rerunning or auditing this study**. Both transcriptions derive from the same physical MS 408, so agreement is sensitivity to editing/transcription, not replication on a different historical witness.
- This experiment reuses known holdout folios and is not a new blind discovery. Multiple-tested transformation choices and corpus-specific structure remain plausible confounds.
- The random-position deletion baseline preserves the number of removed characters per spelling but does **not** match linguistic phonotactics; it is a limited null, not a decisive natural-language comparison.

## How to verify

```bash
python -m unittest discover -s evidence/b09 -p 'test_*.py' -v
python evidence/b09/reference.py --download --trials 30 --out /tmp/b09-public.json
python evidence/b09/check_results.py --actual /tmp/b09-public.json
```

Source hashes and protocols are in [README.md](README.md). The durable expectation values, transcribed from the first public Actions run logs, are in [expected_metrics.json](expected_metrics.json). This verification is **deterministic regression**, not external scientific validation.

**Reproducibility status:** open reference evaluator plus exact third-party source hashes and a successful public workflow; **independent external replication remains pending**.
