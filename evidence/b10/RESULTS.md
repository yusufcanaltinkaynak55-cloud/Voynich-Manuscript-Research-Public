# B10-OPEN-001 | First Completed Public Run

**Measured on:** 11 November 2026  
**Run:** [GitHub Actions #43069965161](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/actions/runs/43069965161)  
**Source code commit of successful run:** [`44777018af7cf80f1fa1f9da07049015f7a0b59b`](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/commit/44777018af7cf80f1fa1f9da07049015f7a0b59b)  
**Result:** GitHub Actions **SUCCESS**. Seven synthetic unit tests passed, both exact-source hashes were checked, real-corpus evaluation completed, the output disclosure contract passed, and derived machine-readable JSON was uploaded as a time-limited workflow artifact.  
**Scientific status:** **PUBLIC COMPUTATIONAL REPRODUCTION OF RESTRICTED SPELLING RECONSTRUCTION, NOT INDEPENDENT DECIPHERMENT**.

## What did the benchmark actually predict?

For a held-out Voynich transcription event, the model was given:

- A shortened written-form **EVA code** obtained by deleting `a/e/i/o/y`.
- Metadata group and physical **line-position role**.
- Optionally, the **shortened codes** of the immediately preceding and following accepted words.

The model then assigned probabilities to **complete EVA spellings previously seen in training with that same code**. The actual target spelling was used **only to grade the prediction**.

An individual test event was *eligible for a top-1 score* only if the correct full spelling was already in that training codebook **and** at least two different training spellings shared the same code. This is a **restricted candidate-selection task**, not generation of novel words, translation of Voynich, or decipherment of a source language.

## Observed real-data results

| Measurement | ZL3b | IT2a |
| --- | ---: | ---: |
| All test written-form occurrences | **6,164** | **6,266** |
| No training candidate for the transformed code | 445 | 497 |
| Code exists, but correct full spelling was unseen | 989 | 1,073 |
| One candidate only (not ambiguous) | 71 | 80 |
| **Ambiguous and eligible occurrences** | **4,659** | **4,616** |
| Simple frequency, top-1 | **53.29%** | **52.86%** |
| Position-only, top-1 | **53.60%** | **53.18%** |
| Position + neighbour codes, top-1 | **53.90%** | **53.05%** |
| Frequency negative log2 probability (bits/token; lower is better) | 1.9427479 | 1.9778085 |
| Position-only bits/token | 1.8990116 | 1.9284097 |
| Position + neighbour codes bits/token | **1.8946422** | **1.9270781** |
| Context gain over position (bits/token) | **+0.0043694** | +0.0013315 |
| Folio-bootstrap 95% interval for context gain | **[+0.0006506, +0.0076628]** | **[−0.0014475, +0.0040950]** |
| Within-group neighbour-code permutation, empirical p | 0.01 | 0.01 |

All rows except the initial coverage counts describe **only 4,659 / 4,616 ambiguous, eligible occurrences**. These rates are **not** percentages of translated or deciphered manuscript words. The estimated Voynich semantic reading accuracy remains **NOT ESTIMABLE**.

## What did the fairer model-selection grid change?

The public benchmark allows the contextual model to choose *every position-only candidate* evaluated by the role baseline; this fixes an unequal-candidate-grid limitation identified in the earlier private B10 protocol.

For this first public run, the resulting measured top-1 and loss metrics coincided with the corresponding internal-report values to their published precision. **Equal numerical outcomes do not prove that the original search-space imbalance was harmless in other conditions.** The revised analysis is transparently identified as a **post-hoc fairness correction**, not passed off as an unchanged preregistered test.

The model weights are tuned using **ZL3b validation only** and reused on IT2a, with each transcription evaluated on its own training counts. Both transcription versions describe the **same physical MS 408**, so agreement is *not* independent historical confirmation.

## Interpretation of the weak context signal

- Relative to the simple frequency baseline, including the line role helps predict the *written form* of an already representable code.
- Adding immediate neighbour codes improved the mean probabilistic loss slightly on ZL3b and IT2a, but **ZL3b is the only source for which the folio-bootstrap interval for this particular gain excluded zero**.
- On IT2a, adding neighbours **reduced exact top-1 accuracy** from 53.18% to 53.05%, despite the small log-loss gain. This distinction matters: top-1 classification and probability scoring are not equivalent metrics.
- A permutation comparison found lower actual loss than shuffled neighbour pairs under the *stated, limited* group-conditioned null (empirical p=0.01 in each transcription). However, its null distribution leaves singleton groups unchanged and does not control every manuscript confound. This result and the IT2a bootstrap uncertainty should both be reported.
- The test uses **right-hand as well as left-hand context**, so it is inherently **bidirectional reconstruction**. It cannot establish a left-to-right historical reading procedure.

**Overall judgment:** Some conditional orthographic regularity was measured. A broad, transcription-independent, historically meaningful advantage from neighbour information **has not been established**. The output cannot justify a claim that Sherlock has read a fraction of the Voynich Manuscript.

## Public verification path

From the repository root, with Python 3.11+ and a connection to pinned public sources:

```bash
python -m unittest discover -s evidence/b10 -p 'test_*.py' -v
python evidence/b10/reference.py --download --null-reps 99 --bootstrap-reps 500 --out /tmp/b10-public.json
python evidence/b10/check_results.py --actual /tmp/b10-public.json
```

The [public reference code](reference.py) uses only the [B09 public source/hash and folio split helpers](../b09/reference.py), the Python standard library, and public external transcriptions; it does **not** use Sherlock proprietary software.

- Frozen output values: [expected_metrics.json](expected_metrics.json).
- Numerical regression checker: [check_results.py](check_results.py).
- Synthetic tests: [test_reference.py](test_reference.py).
- Source and task protocol: [README.md](README.md).
- Real run and execution logs: [GitHub Actions #43069965161](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/actions/runs/43069965161).

The first CI attempt failed at module-import resolution, before the real corpus was evaluated. [Its failed execution remains visible](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/actions/runs/43069582164). The name collision was corrected; the subsequent run completed successfully. No model adjustment was made based on that failed preflight.

## Limitations and next evidence gate

The code and fixed inputs enable **public computational reproducibility**. However:

1. The test folios were explored by previous laboratory work; this is **not** a newly untouched blind experiment.
2. The matching and scoring set excludes many spellings that the training codebook could not reconstruct. Full-book coverage is not demonstrated.
3. The prior internal B10 had a second positional-frame variant not reproduced in this narrowly scoped release.
4. The role- and neighbour-conditioned models may exploit scribal, text-section, layout, or page-related statistical effects that are **not** a historical cipher key.
5. No independent outside research team has yet audited this public result.
6. No independently authenticated Voynich plaintext, lexical meanings, or phonetic reading has been recovered.

The appropriate next scientific step is an **independent rerun / independent implementation and fair baseline audit**, followed by truly prospective material. Please document both positive and negative results.

**Status:** `REPRODUCED_PUBLIC_COMPUTATION`, `PENDING_INDEPENDENT_SCIENTIFIC_REVIEW`, `SEMANTIC_DECIPHERMENT_NOT_ESTIMABLE`.
