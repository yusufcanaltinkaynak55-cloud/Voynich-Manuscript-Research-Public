# Hypothesis registry

**Status date:** 11 November 2026. **All historical-language and decipherment claims below remain unverified.**

This registry is deliberately *falsification-oriented*. Labels apply to **specific testable claims**, not to the worth of a whole research direction. A negative result for one model is not proof that every related model is impossible.

| ID | Hypothesis / claim under examination | Present status | Decisive next evidence |
| --- | --- | --- | --- |
| H01 | The writing encodes an adapted/constructed system combining historically borrowed linguistic material and manuscript-specific orthography. | **NOT YET SCIENTIFICALLY VERIFIED**; one tested simulator did not match preregistered statistics (B18). | Frozen transform producing unseen forms and independently sourced image-to-word-to-meaning correspondences. |
| H02 | Recurring prefix/suffix and line-position patterns reflect an underlying generative process. | **EXPLORATORY** as a structural observation, **NOT YET VERIFIED** as grammar or semantics. | Held-out folio tests against matched shuffles, copy-modify nulls, and alternative segmentation. |
| H03 | A single universal three-consonant root or one specific set of “vowel-like” glyphs reveals the reading key. | **NOT SUPPORTED (strong universal forms)** in internal matched-control experiments. | A unique, stable mapping beating competitive masks and surviving different transcriptions and unseen folios. |
| H04 | Five proposed scribal hands imply five independent language/cipher-generation systems. | **NOT SUPPORTED** as a direct inference in internal conditional tests. | Independent scribal identification and within-section/within-hand predictive separation that survives confound controls. |
| H05 | A fixed Voynich-to-Arabic-root mapping explains unseen tokens better than position-preserving alternatives. | **NOT SUPPORTED** by the tested internal mapping; broader borrowing remains unverified. | Stable, preregistered cross-text mapping with historically attested witnesses and strong null tests. |
| H06 | A single word-to-word ordering rule determines the manuscript's token sequence. | **NOT SUPPORTED** in the original private B17 whole-line test. The separately defined [B17-OPEN](evidence/b17/RESULTS.md) public pairwise diagnostic observes small pair-direction and larger line-position signals; this is **not** evidence of a universal whole-line rule. | Repeated improvement over balanced line-aware baselines in untouched folios and other witnesses. |
| H07 | A homophonic/variable-length cipher family (e.g., published Naibbe-type constructions) is structurally informative. | **EXPLORATORY / INCONCLUSIVE** in CFT-001; tested analogues miss important signatures. | Equal-budget, known-key recovery across unseen historical plaintexts, then independent Voynich-specific discriminating tests. |
| H08 | Local copying/modification generates some lexical regularities. | **OPEN COMPETING EXPLANATION**; tested simplified simulator failed B18 acceptance jointly with H01's simulator. | Competing simulators meeting all preregistered metrics, including adjacent-token behavior and word-length distribution. |
| H09 | Manuscript illustrations anchor specific Voynich words to identified objects and historically attested terms. | **NOT EVALUABLE FOR DECIPHERMENT** with current independent evidence. | Blind object identification, verified transcript-to-image alignment, historical term witnesses, and negative controls. |

## How statuses are assigned

- **EXPLORATORY:** measured in specified internal conditions; external or independent replication remains outstanding.
- **SIMULATION / CALIBRATION:** validated on synthetic or known-key data; does *not* establish historical decoding.
- **NOT SUPPORTED:** a stated prediction failed specified controls; this does not disprove all related theories.
- **NOT EVALUABLE:** required evidence, gold labels, or source material is absent; do not convert this to “0% accuracy.”
- **PENDING INDEPENDENT REVIEW:** no independent end-to-end check has been documented here.
- **NOT YET SCIENTIFICALLY VERIFIED:** an explanation or semantic/phonetic interpretation lacks adequate external confirmation.

The internal experiment labels **B17 (original whole-line study)**, B18 and CFT-001 are provenance identifiers, **not links to fully public reruns of those private analyses**. The separately published [B17-OPEN-001](evidence/b17/README.md) measures a different, narrow pairwise task and must not be conflated with the private B17. See [RESULTS.md](RESULTS.md) and [REPRODUCIBILITY.md](REPRODUCIBILITY.md) for the limits of what is released.

## Conditions for changing a status

An upgrade requires a dated protocol, source provenance, a frozen claim, a fully described evaluation metric, competing baselines, untouched holdouts or new witnesses, failure cases, and (for language/decipherment claims) independently validated mappings or meanings. Editorial confidence, repeated prompts, or a better-looking generated example are insufficient.
