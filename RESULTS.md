# Results and limitations ledger

**Public summary prepared:** 11 November 2026.  
**Source status:** Most items below are summaries of dated **internal** laboratory records. Their underlying private code, raw datasets, fixed environment manifests, and complete logs have **not been published**. **Exceptions:** three narrow public computational tasks now have runnable reference evaluators: B09 transformed-spelling collisions, B10 restricted original-form candidate selection and B17-OPEN pairwise line-order orientation. These are not equivalent metrics. This does **not** independently reproduce other experiments or establish any decipherment.

## Overall conclusion

**No independently verified Voynich reading key, pronunciation system, word meaning, or translation has been established by this project.** The manuscript's semantic decipherment accuracy is **NOT ESTIMABLE** without an independently validated reference. This is different from proving that a model has 0% ability.

## First successful public real-data calculation: B09-OPEN-001

The [B09-OPEN-001 package](evidence/b09/README.md) was run successfully on GitHub Actions on **11 November 2026** using immutable ZL3b/IT2a input versions with checked SHA-256 hashes. Its results match the previous internal B08/B09 aggregate collision measurements:

- ZL3b: **875** unseen-spelling test occurrences, `aeioy` transformation **75.77%**, `dklrs` control **61.03%**, random-position control median **47.54%**.
- IT2a: **966** such occurrences, `aeioy` **74.95%**, `dklrs` **61.59%**, random control median **48.96%**.
- [Actual measured values, code, limits, and run link](evidence/b09/RESULTS.md).

This is **reproduction of a structural many-to-one code-match measurement** on already explored folios. It is **not** an independently verified reading of even one Voynich word. Independent outside replication remains pending.

## Published English research synthesis of the B08–B16 series

The [glyph-obfuscation study](GLYPH_OBFUSCATION_STUDY.md) now documents the **full B08–B16 line of investigation** in English: matching transformed spelling codes, ambiguity, contextual candidate selection, competing glyph controls, natural-language comparisons, glyph merging, null outcomes, and limits of interpretation. **Only the B09 subtest has a verified public computational reproduction package**; the other figures are explicitly labeled as internal reports pending independent replication.

## Second successful public real-data benchmark: B10-OPEN-001

The [B10-OPEN-001 reference benchmark](evidence/b10/README.md) successfully ran on [GitHub Actions on 11 November 2026](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/actions/runs/43069965161), using the **same previously explored folio partition** and pinned ZL3b / IT2a sources.

- ZL3b: **4,659** eligible ambiguous written-form occurrences; frequency top-1 **53.29%**; position-only **53.60%**; context model **53.90%**.
- IT2a: **4,616** such eligible occurrences; frequency **52.86%**; position-only **53.18%**; context **53.05%**.
- The contextual gain in log-loss over position-only was **+0.0043694 bits/token** on ZL3b (folio bootstrap 95% interval **[+0.0006506, +0.0076628]**) and **+0.0013315 bits/token** on IT2a (interval **[−0.0014475, +0.0040950]**). The second interval includes zero. The IT2a contextual top-1 score was lower than position-only.
- [Full public results, denominators, negative findings and limitations](evidence/b10/RESULTS.md).

These figures apply **only** when the correct original EVA spelling is already one of several training candidates under the same shortened code. The benchmark cannot generate unseen spellings and does **not** measure translated words. Test folios were previously examined, and bidirectional neighbour information was used.

## Third successful public real-data diagnostic: B17-OPEN-001

On **12 November 2026**, the [B17-OPEN public pairwise-orientation reference](evidence/b17/README.md) completed a [passing GitHub Actions run](https://github.com/yusufcanaltinkaynak55-cloud/Voynich-Manuscript-Research-Public/actions/runs/43185657803). It analyzed **19,695 / 26,323** different-spelling pairs in held-out ZL3b / IT2a physical P-lines.

- **Directed word-pair orientation:** 0.525362 / 0.525225, with a 0.50 chance reference.
- **Shuffled training-line control:** 0.499010 / 0.495574.
- **Visible first/last-EVA-sign positional model:** 0.611627 / 0.603503.
- **Public decision:** structural direction and line-position signals in this fixed test, **not** deciphered words, a recovered key or a reconstructed line.
- **Essential non-equivalence:** the private **B17** used whole-line beam-search reordering. **B17-OPEN** is a different, narrower reference diagnostic, so its percentages cannot be numerically compared as if the same task had been rerun.

See the [dated B17-OPEN result and limitations](evidence/b17/RESULTS.md). The same manuscript's two transcriptions are not independent external witnesses, and the evaluation folios have appeared in prior research.

## Internal findings: precise claims only

| Internal study / date | Observed or reported internal result | Status and limits |
| --- | --- | --- |
| **B17 / 6 Nov 2026**, word ordering | Tested word-to-word pair-order prediction remained approximately **0.50–0.51**, near the binary chance reference. A separate within-line position comparison produced approximately **0.58–0.59**. | **EXPLORATORY; SPECIFIC WORD-ORDER CLAIM NOT SUPPORTED.** The second measure concerns line position, not a hidden meaning. Natural-text line boundaries in the comparison are artificial. |
| **B18 / 6 Nov 2026**, generative mechanisms | Among **144** tested adapted-language simulation settings and **128** simplified copy-modify settings, **none** met the frozen joint distributional-fit acceptance criterion. | **NOT SUPPORTED for these implementations.** No general theory of constructed language, copying, or ciphering is thereby disproved. One timed-out initial run was subsequently rerun locally; independent end-to-end validation is not documented here. |
| **H045-D follow-ups / 4 Nov 2026**, section-dependent forms | Some internal suffix-prediction differences appeared across sections after conditioning on selected features. A subsequent page-order drift control could reproduce much of the signal. | **EXPLORATORY / CONFOUNDED.** This is not evidence for separate scribal languages or five different keys. |
| **CFT-001 / 9 Nov 2026**, cipher-family comparison | A published Naibbe-style variable-length/homophonic construction exhibited **partial structural resemblance**, but the tested example missed important adjacent-word similarity behavior. Simplified competitor models also failed some criteria. | **EXPLORATORY / INCONCLUSIVE.** The published Naibbe control was added as a clearly documented exploratory extension, not treated as an untouched prospective test. The cipher family of Voynich was not identified. |
| **SHERLOCK-NAIBBE-BLIND-001 / 9 Nov 2026**, known-cipher benchmark | In the internally recorded test, normalized full-string **edit similarity** was **26.9953%** for a restricted one-output-symbol-to-one-letter approach versus **24.6479%** for its frequency baseline, a **2.3474-percentage-point** difference. | **CALIBRATION / NEGATIVE LIMITED RESULT.** This is **not** 27% correctly read letters. The plaintext was **not** recovered, the historical cipher key was **not** recovered, and the one-to-one output assumption cannot express the known cipher's variable-length output. The two reported Python-version runs are not independent scientific replication. |

**Caution regarding source scope:** The *internal-summary table* values reflect archived internal reports reviewed for this initial disclosure. They have not been recomputed in the public repository; any numerical revision must identify its new dataset, version, and run. Percentages from different prediction tasks must not be combined or projected into “number of Voynich words read.”

## Interpretations not established

- The text is Arabic, Persian, Turkish, Latin, Hebrew, or a mixture of these.
- An adapted “borrowed-root” language was used by the manuscript's historical author.
- Any particular EVA glyph has a historically verified sound value.
- There are five independent writing or cipher systems corresponding to proposed scribal hands.
- The manuscript was produced by the Naibbe method or by any other specific cipher family.
- A drawing identifies a nearby Voynich word's meaning.
- Sherlock has deciphered any proportion of the book.

## Known evidence gaps

1. **Publicly released provenance for remaining studies:** exact corpora and permissions, immutable source references, hashes, and preprocessing. B09, B10 and B17-OPEN have scoped source manifests and public reference pipelines.
2. **Executable benchmarks for remaining studies:** frozen scripts, seeds, parameter settings, baseline definitions, and machine-readable results. B09, B10 and B17-OPEN have scoped runnable public implementations.
3. **True external holdout:** folios or independent historical witnesses not repeatedly used in exploratory model selection.
4. **Image-to-text linkage:** reviewed folio/line/glyph coordinates and uncertainty annotations.
5. **Historical validation:** independently sourced, falsifiable glyph-to-reading-to-meaning chains.
6. **Independent assessment:** third-party reproduction and explicit discussion of competing explanations.

These gaps are not a cosmetic issue: they are a barrier to any strong claims of decipherment or reproducibility. The [reproducibility plan](REPRODUCIBILITY.md) lists the minimum conditions for a future evidence release.

## Related scientific reading

- [Yale: Beinecke MS 408](https://beinecke.library.yale.edu/beinecke/collections/beinecke-cipher-voynich-manuscript).
- [Naibbe cipher research article (DOI: 10.1080/01611194.2025.2566408)](https://doi.org/10.1080/01611194.2025.2566408). External work cited for comparison, **not** a project discovery or proof that Voynich uses that cipher.

**This repository does not claim peer review, external validation, or a solved Voynich text.**
