#!/usr/bin/env python3
"""Review public repository structure, Markdown references, and release boundaries.

This is an automated DOCUMENTATION/SECURITY HYGIENE gate. It cannot prove
scientific validity, detect every secret, or audit all previous Git history.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md", "METHODOLOGY.md", "RESULTS.md", "REPRODUCIBILITY.md",
    "SOURCES_AND_RIGHTS.md", "CONTRIBUTING.md", "CITATION.cff",
    "SHERLOCK_MODEL_CARD.md", "SHERLOCK_SCIENTIFIC_ASSESSMENT.md",
    "GLYPH_OBFUSCATION_STUDY.md", "CIPHER_FAMILY_COMPARISON.md",
    "RESEARCH_ROADMAP.md",
    "evidence/b09/reference.py", "evidence/b09/RESULTS.md",
    "evidence/b10/reference.py", "evidence/b10/RESULTS.md",
    "evidence/b17/reference.py", "evidence/b17/RESULTS.md",
)
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)\s]+)(?:\s+[^)]*)?\)")
DANGEROUS = [
    ("Private repository identifier", re.compile("Voynik" + "-El-" + "Yazmalar-", re.I)),
    ("GitHub classic access token", re.compile(r"\bghp_[A-Za-z0-9]{36,}\b")),
    ("GitHub fine-grained token", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{30,}\b")),
    ("OpenAI-style key", re.compile(r"\bsk-proj-[A-Za-z0-9_-]{20,}\b")),
    ("PEM private key header", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
]
EXCLUDE_DIRS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".venv"}


def tracked_public_files(root: Path):
    """Scan only code/doc formats in working tree, including newly added files."""
    allowed = {".md", ".py", ".yml", ".yaml", ".cff", ".json", ".toml", ".txt"}
    for file in sorted(root.rglob("*")):
        if any(x in EXCLUDE_DIRS for x in file.relative_to(root).parts):
            continue
        if not file.is_file() or file.suffix not in allowed:
            continue
        if file.stat().st_size > 2_000_000:
            raise ValueError(f"Oversized public source requiring manual review: {file}")
        yield file


def audit(root: Path) -> list[str]:
    failures = []
    for needed in REQUIRED:
        if not (root / needed).is_file():
            failures.append(f"Required public evidence/doc missing: {needed}")
    for path in tracked_public_files(root):
        rel = path.relative_to(root).as_posix()
        try:
            source = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            failures.append(f"{rel}: non-UTF-8 document")
            continue
        for description, pattern in DANGEROUS:
            if pattern.search(source):
                failures.append(f"{rel}: possible prohibited disclosure: {description}")
        if path.suffix != ".md":
            continue
        for index, line in enumerate(source.splitlines(), start=1):
            # URLs, image binaries and fragments are not local path references.
            for match in LINK.finditer(line):
                target = unquote(match.group(1)).split("#", 1)[0].split("?",1)[0]
                if not target or re.match(r"(?i)^(?:[a-z][a-z0-9+.-]*:|//)", target):
                    continue
                resolved = (path.parent / target).resolve()
                if not resolved.is_relative_to(root.resolve()):
                    failures.append(f"{rel}:{index}: local link escapes repository: {target}")
                elif not resolved.exists():
                    failures.append(f"{rel}:{index}: broken relative link: {target}")
    # Critical scientific disclosure, but not a substitute for reading the text.
    for experiment in ("b09", "b10", "b17"):
        report = root / "evidence" / experiment / "RESULTS.md"
        if report.is_file():
            contents = report.read_text(encoding="utf-8")
            if "NOT ESTIMABLE" not in contents and "NOT_ESTIMABLE" not in contents:
                failures.append(f"evidence/{experiment}/RESULTS.md: missing semantic limit")
    return failures


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--root", type=Path, default=ROOT)
    args = p.parse_args()
    errors = audit(args.root)
    if errors:
        for error in errors:
            print("ERROR:", error)
        print(f"FAIL: {len(errors)} publication hygiene issue(s)")
        sys.exit(1)
    print("PASS: required evidence, relative links, basic sensitive strings and semantic limitations")
    print("Reminder: this does not certify historical or scientific validity.")


if __name__ == "__main__":
    main()
