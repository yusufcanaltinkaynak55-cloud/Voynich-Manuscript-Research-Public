# B17-OPEN-001 | First Completed Public Pairwise-Order Diagnostic

**Executed:** 12 November 2026  
**GitHub Actions run:** [#43185657803](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/actions/runs/43185657803)  
**Tested source commit:** `b2a2ddb39063320c008b88a08bca6c397cd3d15c`  
**Execution outcome:** **SUCCESS**, eight synthetic tests passed, both pinned real transcriptions analyzed, evidence-contract check passed, derived JSON artifact uploaded.  
**Research classification:** **EXPLORATORY / PUBLIC COMPUTATION / PENDING INDEPENDENT REVIEW / NOT A DECIPHERMENT**.

## Task and result

The public B17 reference asks which member of a **pair of different EVA word spellings** came first in a real physical Voynich line. It trains only on other physical folios and evaluates previously seen-in-research test folios. It compares a directed within-line word-pair count model, a deterministic training-word-shuffle control, and a separate prediction from words' visible first/last EVA signs and their learned positions in physical lines.

| Public test statistic | ZL3b | IT2a |
| --- | ---: | ---: |
| Eligible held-out **different-spelling pairs** | **19,695** | **26,323** |
| Directed word-pair orientation, half credit for ties | **0.525362** (52.54%) | **0.525225** (52.52%) |
| Training-line order shuffled, same line membership | 0.499010 (49.90%) | 0.495574 (49.56%) |
| Learned visible first/last-sign position | **0.611627** (61.16%) | **0.603503** (60.35%) |
| Directed pair score minus shuffled control | **+0.026352** (+2.64 pp) | **+0.029651** (+2.97 pp) |
| Chance reference for the specified orientation task | 0.5 | 0.5 |

These are **scores on pairs**, not a percentage of entire lines recovered, words deciphered, correct phonemes, or historical meanings. The public run's additional counts, exclusions, descriptive folio-bootstrap intervals and source/split fingerprints are available in its time-limited Actions JSON artifact. Frozen top-level aggregates are in [expected_metrics.json](expected_metrics.json) and checked by [check_results.py](check_results.py).

### What this result suggests, without over-claiming

- The tested training-pair direction score showed a **small** advantage over a control that randomly shuffles the order of words within each original training line.
- The visible first/last-sign position score showed a **larger** ability to distinguish which of two spellings occurred earlier in a physical manuscript line.
- This does **not** show that a line can be fully reordered, that the manuscript has a non-linguistic mechanism, or that its original language is known. Position effects can reflect copyist conventions, layout and the properties of the EVA transliteration.
- The two transcriptions represent **the same manuscript**, and both test partitions have been explored in previous laboratory studies. Agreement is **not independent historical replication**.

## Relationship to the earlier internal B17 study

The private laboratory's 6 November 2026 B17 experiment used **beam search for whole-line reordering** and compared several natural-language corpora with artificially created line boundaries. The scores reported by that experiment (such as about 0.50–0.51 for a particular transition model and about 0.58–0.59 for its specific line-position model) **are not directly comparable to this public pairwise diagnostic**. Different models, tokenization, sample eligibility and evaluation protocols make numerical subtraction or an implied improvement invalid.

This public run is a **new, narrower, independent public reference program**. It does not redistribute or claim to have rerun the proprietary/private B17 source code.

## Scientific limitations

1. **Already explored folios:** despite physical train/test separation, this is not a newly blind exploration of the manuscript.
2. **Not a full permutation solver:** individual pair decisions can contradict one another. A 61% pair score does not mean 61% of any actual line can be reconstructed.
3. **Common historical source:** ZL3b and IT2a are alternate editorial transcriptions of Beinecke MS 408.
4. **No equal historical-language comparator:** this initial narrow public test deliberately avoids treating artificially line-broken modern texts as matched physical manuscript lines.
5. **Finite simple controls:** shuffling training-line order is not a complete null for lexical, scribal or physical-line positional structure.
6. **Dependent pairs:** many overlapping pairs originate from the same lines and folios. Folio cluster bootstrapping is descriptive, not a substitute for an untouched, preregistered external experiment.
7. **No semantic ground truth:** the semantic decipherment success rate remains **NOT ESTIMABLE**.

## Reproduce

With Python 3.11+ from the repository root:

```bash
python -m unittest discover -s evidence/b17 -p 'test_*.py' -v
python evidence/b17/reference.py --download --out /tmp/b17-public.json
python evidence/b17/check_results.py --actual /tmp/b17-public.json
```

The script downloads only pinned third-party IVTFF sources, confirms cryptographic hashes, and produces derived statistics. Source text, private Sherlock code and model weights are not committed. The check command is **same-code regression**, not outside replication.

**Research decision:** **POSITIVE_LIMITED** for observing modest, method-dependent line-position/direction signals; **INCONCLUSIVE** for identifying any historical writing/cipher mechanism; **NOT ESTIMABLE** for meaning, deciphered words, and full-line restoration.

Read the [protocol and source manifest](README.md), [general scientific methods](../../METHODOLOGY.md) and [rights disclosure](../../SOURCES_AND_RIGHTS.md).
