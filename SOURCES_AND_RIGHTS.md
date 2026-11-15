# Primary sources, attribution, and rights

**Prepared:** 11 November 2026.

## Primary object

The subject of this research is the Voynich Manuscript, **Beinecke MS 408**, held by Yale University's Beinecke Rare Book & Manuscript Library.

- Official Yale overview and digitization access: https://beinecke.library.yale.edu/beinecke/collections/beinecke-cipher-voynich-manuscript
- Recommended identification for the manuscript: **Beinecke Rare Book & Manuscript Library, Yale University, MS 408**.

The manuscript is not owned by this repository, and the researcher does not claim authorship of the historical manuscript. This independent project has no institutional affiliation or endorsement from Yale.

## Transcriptions and historical comparators

Internal exploratory work has referred to **ZL3b** and **IT2a/Takahashi** transcription traditions and to external historical language/cipher examples.

- Different electronic transcriptions of MS 408 are **not independent historical witnesses**.
- A transcription convention such as EVA is not itself proof of the language or sound values of the original writing.
- Any future distribution of transcription data must carry the upstream credit, source/version reference, and relevant terms of use.
- Any future reproduction of Yale images, facsimiles, third-party editions, cipher samples, or derived data must undergo source-specific permission and rights review.

**No raw third-party transcriptions, manuscript images, historical-edition texts, published cipher datasets, or proprietary Sherlock research code are included in this public repository.** The [B09](evidence/b09/README.md), [B10](evidence/b10/README.md) and [B17-OPEN](evidence/b17/README.md) reference evaluators are separate public experiment scripts, not proprietary Sherlock components. They retrieve source transcriptions transiently from pinned upstream URLs and verify exact SHA-256 hashes.

## Source-specific clarification for the first public computation

ZL3b (René Zandbergen and Gabriel Landini) and IT2a (Takeshi Takahashi) are credited individually in the [B09-OPEN-001 manifest](evidence/b09/README.md). The full computational [source manifest](evidence/SOURCE_MANIFEST.json) records pinned URLs, commits, hashes and attribution. The originating [voynich.nu rights statement](https://www.voynich.nu/roadmap.html) makes its listed transcription material available under **CC0**, with acknowledgement requested. That **source-material status does not automatically license the original scripts or documentation in this repository**; these remain without a chosen reuse license.

## Prior work and related literature

- Yale's MS 408 description and image access (above).
- [Naibbe cipher study, DOI 10.1080/01611194.2025.2566408](https://doi.org/10.1080/01611194.2025.2566408), an **external published comparator**. Related cipher constructions and comparisons predate this repository; this research does not claim their invention.
- Other papers, historical source editions, corpus authors, or digitization providers must be acknowledged **per specific future experiment**, not absorbed into a blanket ownership claim.

## Rights in the public research documents and reference code

**Licensing decision recorded: 15 November 2026.** The repository uses two separately scoped public licenses:

- **Original author-created research prose, original diagrams and explanatory Markdown documents:** [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). Reuse and adaptation, including commercial uses, require appropriate attribution, a license link and disclosure of changes.
- **Original public reference Python scripts and original GitHub Actions workflow code:** [MIT License](LICENSE-CODE). Copies or substantial portions of the code must retain the copyright and license notice.

The authoritative [file-level licensing map](LICENSE.md) identifies included paths and exclusions. **No blanket license is granted to copied third-party content**, including MS 408 facsimile images, externally authored transcriptions, prior published scholarly work, third-party datasets, software dependencies, or materials fetched by the reference scripts. Original works and outputs whose rights cannot be established remain outside the licenses until reviewed.

The independent private Sherlock laboratory, candidate keys, checkpoints, unpublished systems (including ALFA), and private communications are not part of this public licensing grant. Publishing these limited reference implementations does **not** open-source the private research environment.

The licenses do not imply endorsement by Yale, an independently confirmed decipherment, or peer review.

## Citation and provenance principles

- Cite **the original historical manuscript holder**, **the transcriber/dataset provider**, and **the author's actual analysis** separately.
- Do not cite this repository as proof that a decipherment is correct.
- For the repository itself, use [CITATION.cff](CITATION.cff).
- If a paper or Zenodo deposit is cited, check its **exact title, author list, DOI, and version** before inserting that reference; do not silently treat an unrelated DOI as the DOI of this repository.
