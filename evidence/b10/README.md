# B10-OPEN-001 | Full written-form reconstruction benchmark

**Public reference release:** 11 November 2026  
**Source:** Previously conducted internal B10 study, 4 November 2026  
**Status:** PUBLICLY REPRODUCED ORTHOGRAPHIC BENCHMARK / INDEPENDENT SCIENTIFIC REVIEW PENDING; **NOT A DECIPHERMENT**

## Scientific question

In [B09](../b09/README.md), removing the fixed EVA-transcription characters `a/e/i/o/y` caused many previously unseen written forms to **collide** with transformed forms in a training lexicon. But the same shortened code often corresponds to several original spellings.

B10 asks the narrower, more demanding question: **If the transformed code is known and multiple complete spellings are possible, can a model select the actually observed written form?** This is **reconstruction of EVA written forms**, not recovery of historical plaintext or meaning.

## Source and privacy

The evaluator is a separate, readable public benchmark implemented using Python's standard library. It imports **only** [the public B09 source hash, parser and folio split utilities](../b09/reference.py). It does **not** import Sherlock, its internal architecture, private experiment scripts, weights, candidate keys, training assets, private correspondence, or historical plaintext.

ZL3b and IT2a are two editorial transcriptions of **the same physical Beinecke MS 408**, not independent manuscripts. The pinned source URLs, immutable commits and SHA-256 digests are documented in [B09](../b09/README.md). No source transcription files are committed to this repo.

## Exact measurement design

- The **same physical folio partition as B09** is reused, grouped by hand / Currier / manuscript-section metadata. It has been explored previously; **this is not a newly blind test**.
- Keep running-text `P` loci; preserve physical lines and uncertain-token exclusions; do not join material across explicit `<->` word boundaries.
- Only the fixed `aeioy` deletion transformation is evaluated in this initial public release; *other transformation variants from the internal series are not reproduced here*.
- Training builds a frequency codebook for each *(metadata group, shortened code)*. Evaluation reports **all held-out test occurrences**, including cases whose code is missing and cases whose correct spelling is absent from the training codebook.
- A restricted **conditional subset** is scored with top-1 accuracy and negative log2 probability (bits/token): it must have **at least two candidate written forms**, and its correct full spelling must already be in the training candidate set. This condition must be disclosed beside any accuracy percentage.
- Compare three explicit baselines: **frequency of observed training spelling**, **position-only** (paragraph/start/middle/end), and **position plus *transformed* left/right neighbour codes**. The target's full word is a grading label, not an input feature; the context cannot see neighbouring full spellings.
- **Fairness correction versus the earlier internal B10:** role-only weights `0.0, 0.2, 0.4, 0.6, 0.8` are all admissible candidates in the contextual model's validation grid. The earlier internal run limited the contextual grid to role weight at most 0.6, which could bias the comparison. This correction is a **declared modified analysis**, not the original preregistered procedure.
- Tune on **ZL3b validation** only; freeze identical weights for the IT2a test. For scoring, apply each transcription's own training counts.
- Report **folio-bootstrap confidence intervals** for a contextual log-loss gain over role-only, and a permutation null that shuffles paired left/right codes *within matching metadata group, target code and position*. Singleton groups cannot be permuted and are disclosed.

**Key limitations:** Using both left and right neighbour codes is a **bidirectional reconstruction exercise**, not a demonstration of left-to-right reading. A many-to-one shortened code does not carry independently verified linguistic meaning. The evaluation subset excludes spellings the codebook cannot generate, and thus **cannot be interpreted as a percentage of the book read**.

## Run locally

Python 3.11+; internet access required only to retrieve source files. From the repository root:

```bash
python -m unittest discover -s evidence/b10 -p 'test_*.py' -v
python evidence/b10/reference.py --download --null-reps 99 --bootstrap-reps 500 --out /tmp/b10-public.json
python evidence/b10/check_results.py --actual /tmp/b10-public.json
```

Offline users can download the exact pinned ZL3b and IT2a inputs, verify their hashes automatically, and run:

```bash
python evidence/b10/reference.py --zl3b /path/to/ZL3b-n.txt --it2a /path/to/IT2a-n.txt --null-reps 99 --bootstrap-reps 500 --out /tmp/b10-public.json
```

[Continuous integration](../../.github/workflows/b10-public-reproduction.yml) executes seven synthetic checks, the real-data reference benchmark, a result-schema check, a fixed-output regression comparison, and stores derived JSON metrics as a workflow artifact. Its [11 November 2026 completed run](RESULTS.md) **passed**. A successful software run is **not a third-party independent scientific replication**.

## Verified public-run results

[Read the full measured public results](RESULTS.md): 4,659 / 4,616 ambiguous eligible test occurrences; frequency-only top-1 53.29% / 52.86%; role-only 53.60% / 53.18%; contextual 53.90% / 53.05%. Neighbour-code contribution was small and the IT2a top-1 classification did not beat role-only. **These are restricted written-form prediction scores, not Voynich reading rates.**

## Internal B10 comparator (different, earlier study)

The 4 November private-laboratory report recorded the following restricted-subset statistics: ZL3b 4,659 ambiguous eligible tokens, baseline frequency top-1 **53.29%**, role-only **53.60%**, context **53.90%**; IT2a 4,616 tokens, frequency **52.86%**, role-only **53.18%**, context **53.05%**.

**Do not copy those values into this public run as its results.** The public evaluator deliberately corrects an earlier unequal search grid, so its contextual estimates may differ. Any discrepancy, including a negative result, must be published as observed. The internal study also examined a second “frame plus shortened code” variant that this initial reference release does **not** reproduce.

## Acceptance and interpretation

A genuinely useful contextual benefit requires superiority on *test* folios that exceeds the position-only baseline and appropriate uncertainty controls; it must also survive comparison with shuffled-neighbour code nulls. If not, conclude **NO ROBUST CONTEXTUAL ADVANTAGE** for this model and setting.

Independent historical word meanings, cipher keys, decoded letters and genuine translation accuracy remain **NOT ESTIMABLE**. See [research methods](../../METHODOLOGY.md), [scientific assessment](../../SHERLOCK_SCIENTIFIC_ASSESSMENT.md), and [rights](../../SOURCES_AND_RIGHTS.md).
