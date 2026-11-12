# Selected Literature and Primary Sources

**Last checked:** 12 November 2026  
**Purpose:** Give credit to prior research, distinguish published methods from this project's exploratory experiments, and provide authoritative provenance. This is a **selective bibliography**, not a comprehensive systematic literature review.

## Historical manuscript and transcription provenance

**Beinecke Rare Book & Manuscript Library, Yale University.** *Voynich Manuscript*, MS 408. [Collection record](https://collections.library.yale.edu/catalog/2002046) and [manuscript overview](https://beinecke.library.yale.edu/beinecke/collections/beinecke-cipher-voynich-manuscript).

**Zandbergen, René, and Gabriel Landini.** ZL3b editorial Voynich transcription (IVTFF); exact pinned version and cryptographic hash documented in [SOURCE_MANIFEST.json](evidence/SOURCE_MANIFEST.json).

**Takahashi, Takeshi.** IT2a editorial Voynich transcription; exact pinned version and cryptographic hash documented in [SOURCE_MANIFEST.json](evidence/SOURCE_MANIFEST.json).

*Critical source distinction:* ZL3b and IT2a are two readings of the **same manuscript**, not independent original historical texts. Editorial transliteration is not a confirmed alphabet-to-sound mapping. Upstream rights remain separate from this repository's rights.

## Relevant peer-reviewed prior work

**Greshko, Michael A.** (published online 26 November 2025). “The Naibbe cipher: a substitution cipher that encrypts Latin and Italian as Voynich Manuscript-like ciphertext.” *Cryptologia*. [https://doi.org/10.1080/01611194.2025.2566408](https://doi.org/10.1080/01611194.2025.2566408).

- **Contribution by the cited author:** A hand-executable, verbose homophonic substitution design that generates decipherable Latin/Italian ciphertext sharing several Voynich-like statistical characteristics.
- **Relevant to our work:** Our CFT-001 compares **the author's published cipher sample** with specified Voynich transcription statistics.
- **Does not establish:** That the manuscript was historically encrypted using Naibbe or that Sherlock has recovered a real Voynich key. The Naibbe construction itself is **not a Sherlock invention**.

**Timm, Torsten, and Andreas Schinner.** (2020; online 25 May 2019). “A possible generating algorithm of the Voynich manuscript.” *Cryptologia* 44(1): 1–19. [https://doi.org/10.1080/01611194.2019.1596999](https://doi.org/10.1080/01611194.2019.1596999).

- **Contribution by the cited authors:** A concrete self-citation/copy-modify generating account for several manuscript word-distribution patterns.
- **Relevant to our work:** Copying/editing is a **serious competing mechanism**, not a peripheral null. The public B17 pair-order diagnostic is **not** a replication of their full algorithm.
- **Does not establish:** The historical author's original method or the absence of meaningful language merely because some statistical signatures can be reproduced by copying.

**Matlach, Vladimír; Barbora Anna Janečková; and Daniel Dostál.** (2022). “The Voynich manuscript: Symbol roles revisited.” *PLOS ONE* 17(1): e0260948. [https://doi.org/10.1371/journal.pone.0260948](https://doi.org/10.1371/journal.pone.0260948).

- **Contribution by the cited authors:** Descriptive and statistical analysis of symbol roles, possible compound symbols, and manuscript text structure.
- **Relevant to our work:** Prior art for the importance of **glyph segmentation, symbol-role variability and non-linguistic alternatives**. Our deletion/merging experiments do not originate the general idea that visible signs may have non-trivial units or roles.
- **Does not establish:** One historically authenticated decipherment or a particular sound value for an EVA symbol.

## Other exploratory context

The project also discusses public web hypotheses and potential historical cipher analogies. **Unreviewed essays, preprints and source-code demonstrations must be identified as such**, and cannot be relabelled as independent peer-reviewed verification of our own results.

## Attribution and citation conventions

When publishing a new experiment, distinguish at least four citations:

1. **Primary manuscript** (Yale Beinecke MS 408).
2. **Transcription producer and exact version** (ZL3b / IT2a; source hashes).
3. **Specific prior scholarly method or comparison** (cite its original author, title and DOI).
4. **This repository's actual test** (its stable Git commit, source file, run log and defined metric). Use [CITATION.cff](CITATION.cff) for this repository.

The presence of the citation file **does not make this a peer-reviewed paper** or provide a DOI. A future frozen archival release must decide documentation/code licenses and verify third-party rights first. See [SOURCES_AND_RIGHTS.md](SOURCES_AND_RIGHTS.md).

**Novelty standard:** A method, alphabet idea or cipher family that appears in prior literature must not be presented as invented here. A potential original contribution must be stated narrowly, evaluated under predeclared controls, and supported by independently inspectable evidence.
