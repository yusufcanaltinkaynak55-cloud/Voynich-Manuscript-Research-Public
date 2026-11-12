# Yusuf Can Altınkaynak

**Independent Interdisciplinary Researcher**  
*Computational cryptanalysis · AI-assisted linguistic analysis · Semantic modeling · Digital humanities*

[GitHub](https://github.com/yusufcanaltinkaynak55-cloud) · [ORCID: 0009-0007-5670-9122](https://orcid.org/0009-0007-5670-9122) · [LinkedIn](https://www.linkedin.com/in/yusufaltinkaynak)

## Research identity

I develop and examine experimental computational methods for studying linguistic structure, uncertain historical writing systems, semantic representation, and the limits of AI-assisted inference. My work focuses on **testable hypotheses, explicit baselines, reproducible experiments, methodological criticism, and careful separation of patterns from verified meaning**.

I work as an **independent researcher**, not as a representative of Yale University or any other research institution. The research described in this repository is not a university-endorsed project, peer-reviewed decipherment, or a claim to a formal academic research position.

## Current public research: Voynich Manuscript (MS 408)

I maintain the [Voynich Manuscript Research public repository](README.md), an English-language research record on the historical manuscript held by Yale's Beinecke Rare Book & Manuscript Library.

Its current open, automatically executed benchmark series examines **three different questions**:

| Study | Question | Exact result type |
| --- | --- | --- |
| [B09-OPEN-001](evidence/b09/RESULTS.md) | When EVA signs are deleted, how often do previously unseen spellings collide with transformed training forms? | **Orthographic code matches**, with strong many-to-one ambiguity |
| [B10-OPEN-001](evidence/b10/RESULTS.md) | Among multiple **previously observed** spellings sharing a transformed code, can a simple model select the original form? | **Restricted written-form classification**, not full vocabulary coverage |
| [B17-OPEN-001](evidence/b17/RESULTS.md) | How accurately can models predict which of two different transcribed words occurred earlier in a physical line? | **Pairwise relative-order statistics**, not restored full lines |

These experiments provide **public computational repeatability**, with independent outside scientific replication still pending. ZL3b and IT2a are editorial transcriptions of **the same historical manuscript**. None of these metrics is a percentage of the text deciphered. **No authenticated Voynich plaintext, verified word meanings, original reading key or translation has been recovered by this research programme.**

The broader experimental system referred to as **Sherlock** remains private. Its source code, model artifacts, candidate keys, and proprietary configurations are not disclosed. The public benchmark code was implemented separately and must not be misrepresented as an open release of Sherlock.

## Additional research directions

**ALFA / ALFA-Q (experimental semantic analysis).** An exploratory research and software-design programme investigating semantic structure, coherence, signal/noise distinctions, and explainable evaluation. These are **development topics**, not independently validated products or formal scientific discoveries. Private or unpublished materials are not exposed by the Voynich public repository.

Other interests include **computational linguistics, knowledge representation, historically grounded cryptanalysis, human–AI evaluation, and reproducible research workflows**.

## Research practice

- State exactly what a metric measures, including sample eligibility and denominators.
- Compare rival explanations under explicit and proportionate controls.
- Publish negative and inconclusive findings instead of silently filtering them out.
- Distinguish a model's statistical success from source-authenticated historical meaning.
- Give credit to prior researchers, primary manuscript holders, and original transcription producers.
- Invite outside critique and independent reimplementation.

## Collaboration

Contributions in experimental cryptanalysis, historical linguistics, manuscript studies, uncertainty-aware transcription, and scientific software testing are welcome. The most useful starting points are the [research roadmap](RESEARCH_ROADMAP.md), [evidence index](evidence/README.md), [selected references](REFERENCES.md), and [contribution policy](CONTRIBUTING.md).

### Citation and attribution

Please cite the specific dataset producers and prior literature alongside the relevant benchmark code and versioned GitHub record. [CITATION.cff](CITATION.cff) includes the repository's author attribution and research identifier. The project currently has **no blanket reuse license** for its original prose or public reference scripts; see [SOURCES_AND_RIGHTS.md](SOURCES_AND_RIGHTS.md).

*Profile updated: 12 November 2026. This is an author description, not an independent evaluation of scholarly competence or an academic credential.*
