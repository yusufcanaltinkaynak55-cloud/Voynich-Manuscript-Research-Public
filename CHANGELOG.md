# Research Change Log

**A transparent record of changes to the public research project.** This is not a publication-impact metric, scientific discovery log, or certificate of external validation.

## 12 November 2026 | Public research infrastructure update

- Introduced [B17-OPEN-001](evidence/b17/README.md), a **new, narrower public pairwise-order diagnostic**, explicitly distinct from the private B17 full-line-reordering experiment.
  - [First passing GitHub Actions real-data run](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/actions/runs/43185657803).
  - Held-out **19,695 / 26,323** different-spelling pairs on ZL3b / IT2a.
  - Directed word-pair orientation **0.525362 / 0.525225**; shuffled-training control **0.499010 / 0.495574**; visible first/last-EVA-sign position baseline **0.611627 / 0.603503**.
  - Frozen aggregate metrics, independent [regression checker](evidence/b17/check_results.py), source/split hashes and eight synthetic tests. **No translation or complete-line reconstruction claimed.**
- Reorganized the [repository homepage](README.md) around an evidence matrix, visible CI status, reproducible commands, and distinct scientific tasks.
- Introduced [research roadmap](RESEARCH_ROADMAP.md), [security guidance](SECURITY.md), a [machine-readable source manifest](evidence/SOURCE_MANIFEST.json), an [evidence index](evidence/README.md), and [selected academic prior art](REFERENCES.md).
- Introduced [public publication quality CI](.github/workflows/repository-quality.yml) and a Python [release-boundary auditor](scripts/audit_public_repo.py), checking links, expected files, basic disclosure strings, scientific status markers and 22 synthetic tests across B09/B10/B17.
- Added English [independent replication](.github/ISSUE_TEMPLATE/independent-replication.yml) and [scientific correction](.github/ISSUE_TEMPLATE/scientific-correction.yml) issue forms, plus a [research-oriented pull-request template](.github/pull_request_template.md).
- Updated the hypothesis register, scientific assessment, Model Card, findings ledger, methods, provenance and reproducibility documents to avoid stale references to “two public experiments”.
- Opened [B17 independent reproduction review](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/issues/4) and [known-key cipher-recovery challenge design](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/issues/5).

**Transparent correction:** The initial publication QA workflow failed because its test scanner matched its *own* private-repository signature string; the scanner pattern was split across literals, preserving its ability to identify the prohibited sequence in other files. A subsequent quality CI run passed. This was a **release-hygiene tool issue**, not a change to any Voynich metric.

## 11 November 2026 | Initial public results and scientific disclosures

- Published English scientific foundation: hypothesis registry, methodological safeguards, results and limitations, reproducibility guidance, scholarly citation metadata and rights statements.
- Published the [Koçi Bey scientific assessment](SHERLOCK_SCIENTIFIC_ASSESSMENT.md), a safe, English-language adaptation of the internal critical evaluation, **not a historical Koçi Bey document**.
- Published the [B08–B16 glyph-deletion synthesis](GLYPH_OBFUSCATION_STUDY.md) retaining unfavorable null results and the important distinction between apparent code matches and meaning.
- Released the independent public [B09-OPEN-001 reference calculation](evidence/b09/RESULTS.md): 75.77% / 74.95% transformed-code collisions with approximately 85% of matched forms ambiguous. This is **not** a decoded-word fraction.
- Released the public [B10-OPEN-001 candidate-selection benchmark](evidence/b10/RESULTS.md): 53.90% / 53.05% top-1 on a **restricted eligible set** containing only already-represented training candidate spellings. This is **not** manuscript coverage or translation.
- Published the [Sherlock Model Card](SHERLOCK_MODEL_CARD.md) and [CFT-001 cipher-family comparison](CIPHER_FAMILY_COMPARISON.md); explicitly separated internal exploratory measurements from publicly reproduced tasks.
- Opened [B09](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/issues/1) and [B10](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/issues/2) external audit calls and the [license/release readiness](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/issues/3) decision tracker.

**Transparent correction:** The first B10 GitHub Actions run failed on a Python module name collision (`reference.py`); this was fixed by loading the public B09 helper with an explicit distinct module name. Subsequent real-data runs passed. The unsuccessful run remains [visible](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/actions/runs/43069582164).

## Unresolved scientific and rights status

- **No independent verified Voynich key, language, sound system, word meanings or translation.**
- No external scientific replication documented for B09, B10 or B17-OPEN; the two transcriptions are of **one historical manuscript**.
- No general license is yet granted for the original documentation or public reference scripts; public visibility alone does not authorize unrestricted redistribution.
- No stable GitHub release/tag or Zenodo archival snapshot of this public repository has been created as part of the activities described here.

**All future entries should be dated and link to actual Git commits or CI runs.** Corrections must preserve enough history to distinguish changed measurement from changed interpretation.
