# B17-OPEN-001 | Held-out pairwise word-order diagnostic

**Research release:** 12 November 2026  
**Classification:** NEWLY DEFINED PUBLIC REFERENCE TEST / EXPLORATORY / NO MEANING OR TRANSLATION INFERRED

**Core question:** Do trained pairwise word-order preferences and **visible line-position features** predict the relative order of two different EVA spellings within held-out physical Voynich running-text lines better than chance and a deterministic shuffled-training control?

This test is **not** the private B17 experiment's beam-search attempt to reorder *entire lines*, nor does it reproduce the earlier private B17 numerical figures. The previous internal study motivated this narrower, completely transparent protocol. **Do not compare its pairwise diagnostic scores as if they were identical to earlier full-line reordering scores.**

## Data provenance

Same pinned and SHA-256-checked ZL3b and IT2a IVTFF transcriptions as the [B09 public data manifest](../b09/README.md). This is *one manuscript with two editorial transcriptions*, not two independent historical witnesses. The B09 metadata-stratified, physical-folio partition is reused. **Test folios have been explored in earlier laboratory work, so this is not a newly untouched blind holdout**.

Only `P` running-text loci are included. Physical lines are respected. A line containing uncertain or non-EVA tokens is excluded as a whole rather than silently joining the surrounding tokens; lines with fewer than three unambiguous EVA words are excluded. Distinct-spelling pairs only, with repeated identical forms excluded. Exclusions and denominators are reported.

## Public reference protocol

1. **Directed within-line pair model:** on training folios, count every ordered pair of *different* spellings `(a,b)` where `a` is left of `b` within a line. Predict a before b when the training count `c(a,b)` exceeds `c(b,a)`; equal counts receive **half credit**. The documented symmetric alpha=1 smoothing changes confidence, not decision sign.
2. **Position baseline:** train average normalized line position of a word's **first and last visible EVA characters**, shrunk toward the neutral midpoint using a fixed prior of 10 pseudo-observations. Predict a before b if its expected position is earlier. This measures **orthographic and physical-line position**, not grammar or semantics.
3. **Order-destroyed training control:** deterministically shuffle the order of *training-line tokens* (seed 408), preserving line membership, length and token multisets, then refit the directed pair model.
4. **Evaluation:** assess each distinct-spelling `i<j` pair in *original held-out test lines*. Predicted correct order earns one point; incorrect earns zero; ties earn 0.5. `pairwise accuracy = total points / eligible pair count`. Chance reference **0.50**. No parameter search is performed on validation or test folios.
5. **Uncertainty:** 199 deterministic bootstrap resamples of **physical test folios** (seed 1717), reporting a descriptive 95% percentile interval. The test does not control every source of dependence or multiple exploration.
6. **Output:** token/pair/folio counts, model accuracies, coverage, uncertainty, source hashes, split hashes, excluded-line counts, and the differences from the shuffled-training control.

**Interpretation limits:** An accuracy above chance does **not** mean that complete lines can be reconstructed, that the text is readable, or that it contains an identified historical language or a verified cipher. Natural prose also has directional and line-position patterns. A small difference from the shuffled-training control may fail to distinguish language from layout effects. This initial open reference deliberately does **not** assert equivalence with the internal B17 natural-language comparisons, which used artificial comparator line endings.

## Run from the repository root

Python 3.11+ (stdlib only), with internet access for pinned external text retrieval:

```bash
python -m unittest discover -s evidence/b17 -p 'test_*.py' -v
python evidence/b17/reference.py --download --out /tmp/b17-public.json
```

Offline operation with both original source bytes:

```bash
python evidence/b17/reference.py --zl3b /path/to/eva_zl3b.txt --it2a /path/to/IT2a-n.txt --out /tmp/b17-public.json
```

[GitHub Actions](../../.github/workflows/b17-public-reproduction.yml) is configured to run synthetic regression checks and the real-data protocol and to upload **derived JSON, never raw external transcription files**. A CI run must finish successfully before its numerical outcome is cited; no B17-OPEN-001 score is claimed merely by adding this workflow.

## Scientific next steps

- Independent review of transcription filtering, previously explored folios, and line-geometry confounds.
- Prospective frozen validation and more appropriate historical **real-line** comparator texts.
- Re-implementation by a separate researcher using different code.
- A separately versioned, rights-cleared replication of the original private **full-line beam-reordering** B17 experiment if its algorithm and dependencies are approved for release.

**Status:** Structural orientation only; **semantic decipherment accuracy = NOT ESTIMABLE**. Reuse rights and upstream source attribution: [SOURCES_AND_RIGHTS.md](../../SOURCES_AND_RIGHTS.md).
