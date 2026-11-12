# Public Evidence Index

**Updated:** 12 November 2026  
**Scope:** Three narrowly specified, real-data computational reference studies. **No historical Voynich decipherment is claimed.**

| Study | Measured unit | Public script and tests | First passing real-data run | Independent external audit |
| --- | --- | --- | --- | --- |
| [B09-OPEN-001](b09/README.md) | Previously unseen EVA **spelling-code collisions** after a fixed deletion | [Source](b09/reference.py), [tests](b09/test_reference.py), [results](b09/RESULTS.md) | [11 Nov 2026](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/actions/runs/42992577209) | **Pending** |
| [B10-OPEN-001](b10/README.md) | Selecting an exact EVA spelling among **already represented candidate forms** | [Source](b10/reference.py), [tests](b10/test_reference.py), [results](b10/RESULTS.md) | [11 Nov 2026](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/actions/runs/43069965161) | **Pending** |
| [B17-OPEN-001](b17/README.md) | Direction of **different-spelling pairs** in real physical lines | [Source](b17/reference.py), [tests](b17/test_reference.py), [results](b17/RESULTS.md) | [12 Nov 2026](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/actions/runs/43185657803) | **Pending** |

**Crucial distinction:** B09, B10 and B17 measure **different tasks, populations and denominators**. Their scores cannot be averaged, compared as like-for-like decoder accuracy, or extrapolated to a “percentage of Voynich words read.” B17-OPEN is a new pairwise diagnostic, **not** a reproduction of the internal full-line beam-search experiment.

All transcriptions are source-pinned and cryptographically verified using the [source manifest](SOURCE_MANIFEST.json), and independently checked in the individual evaluators. ZL3b and IT2a represent the **same manuscript**, and folios have previously appeared in exploratory work. Public CI repeatability is **not** scientific peer review or newly blind historical evidence.

## Quick audit

From the repository root, with Python 3.11+:

```bash
python scripts/audit_public_repo.py
python -m unittest discover -s evidence/b09 -p 'test_*.py' -v
python -m unittest discover -s evidence/b10 -p 'test_*.py' -v
python -m unittest discover -s evidence/b17 -p 'test_*.py' -v
```

For actual real-transcription runs and their machine-readable outputs, follow each study's README. No private Sherlock source, weights, candidate keys, credentials or unlicensed raw text are supplied here.

Use the [project's reproduction protocol](../REPRODUCIBILITY.md), [scientific methods](../METHODOLOGY.md), and [rights notice](../SOURCES_AND_RIGHTS.md) when interpreting the results.
