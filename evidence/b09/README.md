# B09-OPEN-001 | Reproducible **spelling-collision** test

**Release date:** 11 November 2026  
**Type:** Public reference reimplementation of a previously conducted internal experiment (B08/B09, 4 November 2026)  
**Claim:** Removing a fixed subset of **EVA transcription signs** may make some *unseen spellings* match codes found in the training folios.  
**Not claimed:** A sound system, original plaintext, decipherment, translated word, or a newly untouched blind holdout.

## Exact reproducible question

Does a preselected glyph-deletion transformation `a/e/i/o/y` yield **more collisions** with a training dictionary than deleting a different fixed set `d/k/l/r/s`, or deleting the same number of randomly selected positions per spelling?

A collision means **only** that two visually transcribed spellings reduce to the same string of remaining characters. Many distinct words may share one result. A high collision percentage cannot be read as a translation accuracy percentage.

## Sources: immutable versions, no redistributed corpora

| Input | Attribution | Pinned file | Expected SHA-256 |
| --- | --- | --- | --- |
| ZL3b | René Zandbergen and Gabriel Landini; IVTFF v3b, 13 May 2025 | [Pinned ZL3b](https://raw.githubusercontent.com/Aspect-Research/voynich-autoexploration/31819c914061cc6b63bbf4983e33d643ede52e46/data/transcriptions/eva_zl3b.txt) | `bf5b6d4ac1e3a51b1847a9c388318d609020441ccd56984c901c32b09beccafc` |
| IT2a | Takeshi Takahashi; IVTFF v2a | [Pinned IT2a](https://raw.githubusercontent.com/noah-chelednik/voynich-data/ecd4c8145524d90373535ea3d1617d8190dc8208/data_sources/cache/IT2a-n.txt) | `7f27a8b0feed8f6de0a99900df6bf912dd1d295c38e5f830bac8b41c3f536fb5` |

Attribution and rights: [voynich.nu transliterations](https://www.voynich.nu/transcr.html) and [its CC0 statement](https://www.voynich.nu/roadmap.html#cop). These are *two editorial transcriptions of the same physical manuscript*, not independent historical witnesses. We do **not** copy the full input files into this repository.

## One-command reproduction

Requires Python 3.11+ and internet access for source acquisition. From the repository root:

```bash
python -m unittest discover -s evidence/b09 -p 'test_*.py' -v
python evidence/b09/reference.py --download --trials 30 --out /tmp/b09-public.json
```

Offline users may retrieve the two **exact pinned** source files separately and run:

```bash
python evidence/b09/reference.py --zl3b /path/to/ZL3b-n.txt --it2a /path/to/IT2a-n.txt --trials 30 --out b09-public.json
```

The program refuses incorrect SHA-256 bytes. It writes only derived summary statistics. The GitHub Actions workflow [b09-public-reproduction.yml](../../.github/workflows/b09-public-reproduction.yml) runs both the unit tests and pinned-source real-corpus reproduction, then uploads a JSON artifact. No private access token or private repository checkout is needed.

## Locked implementation choices

1. Keep only **P-locus running text** in IVTFF. Split explicit `<->` as a word boundary. Do not silently fill uncertain/annotated items; accept pure lowercase ASCII EVA spellings only.
2. Match folios by ID across ZL3b and IT2a. Partition **physical folios**, not random tokens, within fixed hand/Currier/section metadata groups. Groups with fewer than 8 eligible folios are train-only.
3. Deterministic folio ordering key: `SHA256("b08o-20261104|" + hand + "/" + currier + "/" + section + "|" + folio)`. Groups with enough folios are split approximately **60% training / 20% validation / 20% test**.
4. For a test spelling to qualify, its exact spelling must **not** occur in the full training vocabulary. This is OOV (out of vocabulary), not a new historical word or a new semantic concept.
5. Count a **hit** when the transformed test spelling exists among transformed training spellings. Denominator: all eligible OOV **token occurrences**, not all unique types. The validation partition is never used as a second test partition.
6. **Fixed alternative** removes `dklrs`; **random null** drops exactly as many positions as the target transformation, deterministically for each spelling and each of 30 preselected trials. This is **not** an all-confounds-matched linguistic baseline.
7. Also report ambiguity: the share of matched test occurrences whose transformed code corresponds to multiple **different** observed training spellings. This quantifies information loss.
8. Numeric rates are rounded to six decimals. Source hashes, folio-group checksums, and token counts are written to the output JSON.

This open code is a **reference implementation**, not copied proprietary Sherlock code or an independent research team's validation. The split and features have been examined in the internal lab before this release. Reproduction of this fixed result **does not** create a new blind test.

## Previously recorded internal comparison (NOT a fresh rerun)

The private laboratory's 4 November 2026 B08/B09 summary reported:

| Measure | ZL3b | IT2a |
| --- | ---: | ---: |
| OOV test token occurrences | 875 | 966 |
| `aeioy` collision rate | 75.77% | 74.95% |
| `dklrs` collision rate | 61.03% | 61.59% |
| Same-deletion-count random median | 47.54% | 48.96% |
| Multiple training-form ambiguity among matched codes | 85.37% | 85.36% |

**These are the archived laboratory comparator values.** The [11 November 2026 public run](RESULTS.md) independently executed the reference script in GitHub Actions and reproduced their main aggregate rates. This is a second computational implementation of an already explored task, **not** an untouched new test or validation by an outside researcher. Any future discrepancy must be reported rather than tuned away. Neither experiment establishes a decipherment.

## Scope and legal limits

The source website publishes transcriptions under CC0 while requesting attribution. The reference script and documentation are original repository content, for which **no general reuse license has yet been granted**. No images, fonts, copyrighted modern editions, credentials, private reports, or Sherlock internals are bundled.

**Verification levels:** software tests, real-data repeatability, external replication, and independent semantic validation are distinct. Here we target the first two only.
