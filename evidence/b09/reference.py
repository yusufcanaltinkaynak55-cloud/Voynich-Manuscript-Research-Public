#!/usr/bin/env python3
"""B09-OPEN-001: transparent reference reproduction of a structural test.

This is a standalone implementation of a documented B09 test, not the private
Sherlock solver and not a decipherment. Python >=3.11; standard library only.
No third-party text is committed by this program.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from hashlib import sha256
import json
from pathlib import Path
import re
from statistics import median
from tempfile import TemporaryDirectory
from urllib.request import Request, urlopen

SOURCES = {
    "ZL3b": {
        "url": "https://raw.githubusercontent.com/Aspect-Research/voynich-autoexploration/"
               "31819c914061cc6b63bbf4983e33d643ede52e46/"
               "data/transcriptions/eva_zl3b.txt",
        "sha256": "bf5b6d4ac1e3a51b1847a9c388318d609020441ccd56984c901c32b09beccafc",
        "credit": "René Zandbergen and Gabriel Landini (ZL3b)",
    },
    "IT2a": {
        "url": "https://raw.githubusercontent.com/noah-chelednik/voynich-data/"
               "ecd4c8145524d90373535ea3d1617d8190dc8208/"
               "data_sources/cache/IT2a-n.txt",
        "sha256": "7f27a8b0feed8f6de0a99900df6bf912dd1d295c38e5f830bac8b41c3f536fb5",
        "credit": "Takeshi Takahashi (IT2a)",
    },
}
VOWEL_LIKE_EVA = frozenset("aeioy")  # not a claim about phonetics
CONTROL_EVA = frozenset("dklrs")
HEADER = re.compile(r"^<(f\d+[rv]\d*)>\s*(.*)$")
LOCUS = re.compile(r"^<(f\d+[rv]\d*)\.[^,>]+,([^>]+)>\s*(.*)$")
BODY_LOCUS = re.compile(r"(?:^|[,;])\s*[@+*=]?P")
EDITOR_COMMENT = re.compile(r"<![^>]*>")
UNCERTAIN = re.compile(r"\{[^}]*\}|\[[^]]*\]")
REMAINING_TAG = re.compile(r"<[^>]*>")
PURE_EVA = re.compile(r"[a-z]+")


def checked_bytes(raw: bytes, expected: str) -> bytes:
    observed = sha256(raw).hexdigest()
    if observed != expected:
        raise ValueError(f"SHA-256 mismatch: expected {expected}, got {observed}")
    return raw


def download(name: str) -> bytes:
    # Request exact, version-pinned files; refuse changed data.
    source = SOURCES[name]
    request = Request(source["url"], headers={"User-Agent": "Voynich-B09-Open/1.0"})
    with urlopen(request, timeout=45) as resp:
        raw = resp.read()
    return checked_bytes(raw, source["sha256"])


def parse_ivtff(raw: bytes) -> dict:
    """Keep P-locus ASCII EVA, exclude uncertain glyph slots.

    Literal <-> is a word break, never concatenated. P-locus position is
    retained while uncertain slots are skipped, not repaired. This is a
    transliteration analysis, not a transcription of manuscript images.
    """
    pages = {}
    current = None
    for row in raw.decode("utf-8-sig").splitlines():
        header = HEADER.match(row)
        if header:
            current = header.group(1)
            meta = header.group(2)
            def tag(label):
                found = re.search(r"\$" + label + r"=([^\s>]+)", meta)
                return found.group(1) if found else "?"
            pages[current] = {
                "stratum": (tag("H"), tag("L"), tag("I")),
                "p_lines": 0,
                "words": [],
            }
            continue
        locus = LOCUS.match(row)
        if not locus or current is None:
            continue
        folio, locus_type, body = locus.groups()
        if folio != current or not BODY_LOCUS.search(locus_type):
            continue
        pages[current]["p_lines"] += 1
        body = body.replace("<->", ".")
        body = EDITOR_COMMENT.sub(" ", body)
        body = body.split("!")[0]
        body = UNCERTAIN.sub("?", body)
        body = REMAINING_TAG.sub("", body)
        for word in re.split(r"[.,\s=]+", body):
            if PURE_EVA.fullmatch(word or ""):
                pages[current]["words"].append(word)
    if len(pages) < 150:
        raise ValueError("Not enough folios parsed; check IVTFF version/format")
    return pages


def fixed_split(left: dict, right: dict) -> dict:
    """Re-create B08/B09's disclosed metadata-stratified folio partition.

    DO NOT call this a newly untouched holdout: these same folios were used
    in previous laboratory analysis.
    """
    strata = defaultdict(list)
    common = sorted(set(left) & set(right))
    if len(common) < 190:
        raise ValueError("Insufficient paired transcription folios")
    for folio in common:
        if left[folio]["stratum"] != right[folio]["stratum"]:
            raise ValueError(f"Metadata mismatch in {folio}")
        if min(left[folio]["p_lines"], right[folio]["p_lines"]) < 3:
            continue
        strata[left[folio]["stratum"]].append(folio)
    result = {"train": [], "validation": [], "test": []}
    for group, members in sorted(strata.items()):
        ordered = sorted(members, key=lambda f: sha256(
            ("b08o-20261104|" + "/".join(group) + "|" + f).encode()
        ).hexdigest())
        n = len(ordered)
        if n < 8:
            result["train"].extend(ordered)
            continue
        train_end = max(2, round(0.60 * n))
        valid_end = train_end + max(1, round(0.20 * n))
        if valid_end >= n:
            train_end, valid_end = n - 2, n - 1
        result["train"].extend(ordered[:train_end])
        result["validation"].extend(ordered[train_end:valid_end])
        result["test"].extend(ordered[valid_end:])
    assert not (set(result["train"]) & set(result["test"]))
    assert not (set(result["validation"]) & set(result["test"]))
    assert not (set(result["train"]) & set(result["validation"]))
    if not result["test"]:
        raise ValueError("No held-out folios")
    return result


def words_for(pages: dict, ids: list[str]) -> list[str]:
    return [word for folio in ids for word in pages[folio]["words"]]


def skeleton(word: str, excluded: frozenset) -> str:
    return "".join(c for c in word if c not in excluded) or "∅"


def randomized_skeleton(word: str, trial: int) -> str:
    """Drop the same NUMBER of positions as the aeioy rule in this word."""
    positions = list(range(len(word)))
    count = sum(c in VOWEL_LIKE_EVA for c in word)
    state = int.from_bytes(
        sha256(f"b09-null|{trial}|{word}".encode()).digest()[:4], "big")
    for i in range(len(positions) - 1, 0, -1):
        state = (1664525 * state + 1013904223) & 0xffffffff
        j = state % (i + 1)
        positions[i], positions[j] = positions[j], positions[i]
    removed = set(positions[:count])
    return "".join(ch for i, ch in enumerate(word) if i not in removed) or "∅"


def score(train: list[str], oov: list[str], key_fn) -> dict:
    codebook = defaultdict(set)
    for form in train:
        codebook[key_fn(form)].add(form)
    matched = [len(codebook[key_fn(w)]) for w in oov if key_fn(w) in codebook]
    return {
        "oov_test_tokens": len(oov),
        "matched_oov_tokens": len(matched),
        "matched_oov_rate": round(len(matched) / len(oov), 6) if oov else None,
        "ambiguous_matched_token_fraction": (
            round(sum(n > 1 for n in matched) / len(matched), 6)
            if matched else None),
        "median_train_forms_per_matched_code": median(matched) if matched else None,
    }


def evaluate(pages: dict, split: dict, null_trials: int = 30) -> dict:
    train = words_for(pages, split["train"])
    test = words_for(pages, split["test"])
    known = set(train)
    oov = [w for w in test if w not in known]
    if len(oov) < 100:
        raise ValueError("Too few OOV test tokens to evaluate")
    vowel = score(train, oov, lambda w: skeleton(w, VOWEL_LIKE_EVA))
    control = score(train, oov, lambda w: skeleton(w, CONTROL_EVA))
    nulls = [
        score(train, oov, lambda w, k=k: randomized_skeleton(w, k))[
            "matched_oov_rate"]
        for k in range(1, null_trials + 1)
    ]
    return {
        "train_tokens": len(train),
        "test_tokens": len(test),
        "test_folios": len(split["test"]),
        "oov_test_tokens": len(oov),
        "remove_aeioy": vowel,
        "remove_dklrs_control": control,
        "random_same_deletion_count_null": {
            "trials": null_trials,
            "minimum": min(nulls),
            "median": round(median(nulls), 6),
            "maximum": max(nulls),
        },
        "not_a_reading_or_translation": True,
    }


def run(zl: bytes, it: bytes, null_trials: int = 30) -> dict:
    zl = checked_bytes(zl, SOURCES["ZL3b"]["sha256"])
    it = checked_bytes(it, SOURCES["IT2a"]["sha256"])
    left, right = parse_ivtff(zl), parse_ivtff(it)
    split = fixed_split(left, right)
    return {
        "experiment": "B09-OPEN-001",
        "created_utc_date": "2026-11-11",
        "research_task": "Held-out unseen-spelling collisions after fixed glyph deletion",
        "source_sha256": {k: v["sha256"] for k, v in SOURCES.items()},
        "source_urls": {k: v["url"] for k, v in SOURCES.items()},
        "split_folios": {k: len(v) for k, v in split.items()},
        "shared_folio_ids_sha256": {k: sha256(
            ("\n".join(sorted(v)) + "\n").encode()).hexdigest()
            for k, v in split.items()},
        "same_historical_manuscript": True,
        "previously_explored_holdout": True,
        "semantic_accuracy": "NOT_ESTIMABLE",
        "interpretation": "code-collision coverage, NOT decipherment",
        "results": {
            "ZL3b": evaluate(left, split, null_trials),
            "IT2a": evaluate(right, split, null_trials),
        },
    }


def main() -> None:
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--download", action="store_true", help="Fetch immutable external sources")
    cli.add_argument("--zl3b", type=Path, help="Existing ZL3b source file")
    cli.add_argument("--it2a", type=Path, help="Existing IT2a source file")
    cli.add_argument("--trials", type=int, default=30)
    cli.add_argument("--out", type=Path, required=True)
    args = cli.parse_args()
    if args.trials < 1 or args.trials > 100:
        cli.error("--trials must be between 1 and 100")
    if args.download == bool(args.zl3b or args.it2a):
        cli.error("Choose --download OR both --zl3b and --it2a")
    if not args.download and not (args.zl3b and args.it2a):
        cli.error("Both local source paths are required")
    if args.download:
        zl, it = download("ZL3b"), download("IT2a")
    else:
        zl, it = args.zl3b.read_bytes(), args.it2a.read_bytes()
    outcome = run(zl, it, args.trials)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(outcome, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    for source in ("ZL3b", "IT2a"):
        z = outcome["results"][source]
        print(f"{source}: OOV {z['oov_test_tokens']}; "
              f"aeioy {z['remove_aeioy']['matched_oov_rate']:.6f}; "
              f"dklrs {z['remove_dklrs_control']['matched_oov_rate']:.6f}; "
              f"random median {z['random_same_deletion_count_null']['median']:.6f}; "
              "semantics NOT_ESTIMABLE")
    print(f"Derived summary saved: {args.out}; no corpus bytes saved.")


if __name__ == "__main__":
    main()
