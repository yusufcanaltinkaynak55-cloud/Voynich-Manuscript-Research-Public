# Security and responsible disclosure

This repository is a **public research record**, not a mirror of the private Sherlock system.

## Do not disclose

- API keys, passwords, authentication tokens, secrets, or private access material.
- Private Sherlock source code, model checkpoints, proprietary tuning/search configurations, unpublished candidate reading keys, or private experimental assets.
- Private correspondence, personal information, unreleased institutional records or third-party copyrighted images/texts without authorization.
- Any material from a private repository that the rights holder has not explicitly cleared for public distribution.

## Reporting a security concern

Please **do not post secrets, exploitable vulnerabilities, private code snippets, or leaked credentials in public GitHub Issues or pull requests**.

If GitHub's private vulnerability reporting is enabled for this repository, use that private mechanism. Otherwise contact the maintainer through a privately agreed channel, without attaching sensitive data to a public issue. Public issues may be used for non-sensitive scientific corrections.

## Supported scope

The public B09, B10 and B17 reference scripts fetch fixed public transcription URLs and verify SHA-256 hashes. No private tokens should be needed. Avoid changing these source URLs to unreviewed, mutable or unsafe origins.

A successful source-code scan or CI test is **not** proof that no sensitive content exists in the current working tree, public Git history or past artifacts. Sensitive-data incidents require a separate incident response, potentially including key revocation and history review.

**Release hygiene:** Keep third-party source bytes and raw manuscript images out of this repository unless attribution, scope and redistribution rights have been reviewed. Read [SOURCES_AND_RIGHTS.md](SOURCES_AND_RIGHTS.md).
