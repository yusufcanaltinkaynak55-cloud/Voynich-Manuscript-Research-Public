# Results and limitations ledger

**Public summary prepared:** 11 November 2026.  
**Source status:** Summaries of dated **internal** laboratory records. The underlying private code, raw datasets, fixed environment manifests, and complete logs have **not been published in this repository**. The entries below are therefore **not independently reproducible from this public record**.

## Overall conclusion

**No independently verified Voynich reading key, pronunciation system, word meaning, or translation has been established by this project.** The manuscript's semantic decipherment accuracy is **NOT ESTIMABLE** without an independently validated reference. This is different from proving that a model has 0% ability.

## Internal findings: precise claims only

| Internal study / date | Observed or reported internal result | Status and limits |
| --- | --- | --- |
| **B17 / 6 Nov 2026**, word ordering | Tested word-to-word pair-order prediction remained approximately **0.50–0.51**, near the binary chance reference. A separate within-line position comparison produced approximately **0.58–0.59**. | **EXPLORATORY; SPECIFIC WORD-ORDER CLAIM NOT SUPPORTED.** The second measure concerns line position, not a hidden meaning. Natural-text line boundaries in the comparison are artificial. |
| **B18 / 6 Nov 2026**, generative mechanisms | Among **144** tested adapted-language simulation settings and **128** simplified copy-modify settings, **none** met the frozen joint distributional-fit acceptance criterion. | **NOT SUPPORTED for these implementations.** No general theory of constructed language, copying, or ciphering is thereby disproved. One timed-out initial run was subsequently rerun locally; independent end-to-end validation is not documented here. |
| **H045-D follow-ups / 4 Nov 2026**, section-dependent forms | Some internal suffix-prediction differences appeared across sections after conditioning on selected features. A subsequent page-order drift control could reproduce much of the signal. | **EXPLORATORY / CONFOUNDED.** This is not evidence for separate scribal languages or five different keys. |
| **CFT-001 / 9 Nov 2026**, cipher-family comparison | A published Naibbe-style variable-length/homophonic construction exhibited **partial structural resemblance**, but the tested example missed important adjacent-word similarity behavior. Simplified competitor models also failed some criteria. | **EXPLORATORY / INCONCLUSIVE.** The published Naibbe control was added as a clearly documented exploratory extension, not treated as an untouched prospective test. The cipher family of Voynich was not identified. |
| **SHERLOCK-NAIBBE-BLIND-001 / 9 Nov 2026**, known-cipher benchmark | In the internally recorded test, normalized full-string **edit similarity** was **26.9953%** for a restricted one-output-symbol-to-one-letter approach versus **24.6479%** for its frequency baseline, a **2.3474-percentage-point** difference. | **CALIBRATION / NEGATIVE LIMITED RESULT.** This is **not** 27% correctly read letters. The plaintext was **not** recovered, the historical cipher key was **not** recovered, and the one-to-one output assumption cannot express the known cipher's variable-length output. The two reported Python-version runs are not independent scientific replication. |

**Caution regarding source scope:** These values reflect archived internal reports reviewed for this initial disclosure. They have not been recomputed in the public repository; any numerical revision must identify its new dataset, version, and run. Percentages from different prediction tasks must not be combined or projected into “number of Voynich words read.”

## Interpretations not established

- The text is Arabic, Persian, Turkish, Latin, Hebrew, or a mixture of these.
- An adapted “borrowed-root” language was used by the manuscript's historical author.
- Any particular EVA glyph has a historically verified sound value.
- There are five independent writing or cipher systems corresponding to proposed scribal hands.
- The manuscript was produced by the Naibbe method or by any other specific cipher family.
- A drawing identifies a nearby Voynich word's meaning.
- Sherlock has deciphered any proportion of the book.

## Known evidence gaps

1. **Publicly released provenance:** exact corpora and permissions, immutable source references, hashes, and preprocessing.
2. **Executable benchmark:** frozen scripts, seeds, parameter settings, baseline definitions, and machine-readable results.
3. **True external holdout:** folios or independent historical witnesses not repeatedly used in exploratory model selection.
4. **Image-to-text linkage:** reviewed folio/line/glyph coordinates and uncertainty annotations.
5. **Historical validation:** independently sourced, falsifiable glyph-to-reading-to-meaning chains.
6. **Independent assessment:** third-party reproduction and explicit discussion of competing explanations.

These gaps are not a cosmetic issue: they are a barrier to any strong claims of decipherment or reproducibility. The [reproducibility plan](REPRODUCIBILITY.md) lists the minimum conditions for a future evidence release.

## Related scientific reading

- [Yale: Beinecke MS 408](https://beinecke.library.yale.edu/beinecke/collections/beinecke-cipher-voynich-manuscript).
- [Naibbe cipher research article (DOI: 10.1080/01611194.2025.2566408)](https://doi.org/10.1080/01611194.2025.2566408). External work cited for comparison, **not** a project discovery or proof that Voynich uses that cipher.

**This repository does not claim peer review, external validation, or a solved Voynich text.**
