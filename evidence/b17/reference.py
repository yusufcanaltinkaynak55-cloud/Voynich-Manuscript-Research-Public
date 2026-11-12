#!/usr/bin/env python3
"""B17-OPEN-001: public, falsifiable *pair orientation* diagnostic.

This is a newly specified, narrow reference experiment, not the private
B17 beam-reordering implementation and not a Voynich decipherment.
It uses only public B09 source integrity and folio splitting utilities.
Python >=3.11, standard library only. No corpus files are committed.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import random
import re

_b09_file = Path(__file__).resolve().parents[1] / "b09" / "reference.py"
_spec = importlib.util.spec_from_file_location("b09_for_b17_open", _b09_file)
if _spec is None or _spec.loader is None:
    raise ImportError("Missing public B09 source parsing reference")
b09 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b09)

ALPHA = 1.0
EDGE_PRIOR = 10.0
SEED_TRAIN_SHUFFLE = 408
SEED_BOOTSTRAP = 1717
N_BOOTSTRAP = 199
MIN_WORDS = 3


def parse_lines(raw: bytes) -> tuple[dict[str, list[list[str]]], dict]:
    """Keep physically delimited running-text P lines, exclude uncertain lines.

    A line is excluded in full if its parsing is ambiguous. No word labels,
    plaintext or externally claimed phonemes are inferred from EVA.
    """
    reference = b09.parse_ivtff(raw)  # requires physically plausible IVTFF
    result = defaultdict(list)
    discarded = Counter()
    current = None
    for row in raw.decode("utf-8-sig").splitlines():
        header = b09.HEADER.match(row)
        if header:
            current = header.group(1)
            continue
        locus = b09.LOCUS.match(row)
        if not locus or current not in reference:
            continue
        folio, location, body = locus.groups()
        if folio != current or not b09.BODY_LOCUS.search(location):
            continue
        body = body.replace("<->", ".")
        body = b09.EDITOR_COMMENT.sub(" ", body)
        body = body.split("!")[0]
        body = b09.UNCERTAIN.sub("?", body)
        body = b09.REMAINING_TAG.sub("", body)
        tokens = [w for w in re.split(r"[.,\s=]+", body) if w]
        if any(not b09.PURE_EVA.fullmatch(w) for w in tokens):
            discarded["uncertain_or_non_eva_line"] += 1
            continue
        if len(tokens) < MIN_WORDS:
            discarded["short_line"] += 1
            continue
        result[folio].append(tokens)
    return dict(result), dict(discarded)


def get_lines(by_folio: dict, ids: list[str]) -> list[tuple[str, list[str]]]:
    return [(folio, line) for folio in ids
            for line in by_folio.get(folio, [])]


class PairModel:
    """Directed word co-occurrence within an original physical line."""
    def __init__(self, lines: list[tuple[str, list[str]]]):
        self.ordered = Counter()
        for _, words in lines:
            for i, a in enumerate(words):
                for b in words[i + 1:]:
                    if a != b:
                        self.ordered[a, b] += 1

    def direction(self, a: str, b: str) -> tuple[int, bool]:
        """+1: a before b, -1: b before a, 0: inconclusive tie."""
        if a == b:
            return 0, False
        forward = self.ordered[a, b]
        backward = self.ordered[b, a]
        if forward == backward:
            return 0, (forward + backward) > 0
        # Symmetric Dirichlet smoothing alpha cancels in a binary decision.
        probability = (forward + ALPHA) / (forward + backward + 2 * ALPHA)
        return (1 if probability > .5 else -1), True


class EdgePositionModel:
    """Predict orientation from a word's visible first/last EVA signs."""
    def __init__(self, lines: list[tuple[str, list[str]]]):
        self.counts = defaultdict(lambda: [0.0, 0])
        for _, words in lines:
            for i, w in enumerate(words):
                key = (w[0], w[-1])
                self.counts[key][0] += i / (len(words) - 1)
                self.counts[key][1] += 1

    def estimate(self, word: str) -> tuple[float, bool]:
        x, n = self.counts[(word[0], word[-1])]
        return (x + EDGE_PRIOR * 0.5) / (n + EDGE_PRIOR), n > 0

    def direction(self, a: str, b: str) -> tuple[int, bool]:
        av, covered_a = self.estimate(a)
        bv, covered_b = self.estimate(b)
        return (1 if av < bv else -1 if av > bv else 0), covered_a and covered_b


def shuffled_training(lines: list[tuple[str, list[str]]]) -> list[tuple[str, list[str]]]:
    rng = random.Random(SEED_TRAIN_SHUFFLE)
    out = []
    for folio, words in lines:
        new = list(words)
        rng.shuffle(new)
        out.append((folio, new))
    return out


def count_pairs(lines: list[tuple[str, list[str]]], model) -> dict:
    """Pair denominator excludes identical-spelling ties; other ties score 0.5.

    All pairs come from real held-out P lines. Pairwise orientation is NOT
    equivalent to decoding a complete sentence or reordering an entire line.
    """
    groups = defaultdict(lambda: [0, 0, 0, 0])
    line_count = 0
    for folio, words in lines:
        line_count += 1
        slot = groups[folio]
        for i, a in enumerate(words):
            for b in words[i+1:]:
                if a == b:
                    slot[3] += 1
                    continue
                direction, covered = model.direction(a, b)
                slot[0] += 2 if direction == 1 else 1 if direction == 0 else 0
                slot[1] += 1
                slot[2] += int(covered)
    total = sum(v[1] for v in groups.values())
    if total < 100:
        raise ValueError("Not enough eligible test pairs")
    hit2 = sum(v[0] for v in groups.values())
    matched = sum(v[2] for v in groups.values())
    excluded = sum(v[3] for v in groups.values())
    # Folio cluster bootstrap; does NOT create new historical witnesses.
    ids = sorted(groups)
    rng = random.Random(SEED_BOOTSTRAP)
    estimates = []
    for _ in range(N_BOOTSTRAP):
        sample = [groups[ids[rng.randrange(len(ids))]] for __ in ids]
        numerator = sum(v[0] for v in sample)
        denom = sum(v[1] for v in sample)
        estimates.append(numerator / (2 * denom))
    estimates.sort()
    return {
        "n_lines": line_count,
        "n_folios": len(groups),
        "n_distinct_spelling_pairs": total,
        "n_identical_spelling_pairs_excluded": excluded,
        "pairwise_orientation_accuracy_with_half_credit_ties": round(hit2/(2*total), 6),
        "training_signal_coverage": round(matched / total, 6),
        "folio_bootstrap95": [round(estimates[int(.025*N_BOOTSTRAP)],6),
                              round(estimates[min(N_BOOTSTRAP-1,int(.975*N_BOOTSTRAP))],6)],
        "pairwise_null_chance": 0.5,
    }


def compare_transcription(name: str, by_folio: dict, split: dict,
                          discarded: dict) -> dict:
    train = get_lines(by_folio, split["train"])
    test = get_lines(by_folio, split["test"])
    if not train or not test:
        raise ValueError("Insufficient physically disjoint running-text lines")
    lexical = PairModel(train)
    shuffled = PairModel(shuffled_training(train))
    edge = EdgePositionModel(train)
    result = {
        "train_lines": len(train),
        "test_lines": len(test),
        "discarded_running_text_lines": discarded,
        "word_pair_direction": count_pairs(test, lexical),
        "shuffled_training_null": count_pairs(test, shuffled),
        "edge_position_only": count_pairs(test, edge),
    }
    result["observed_minus_shuffled_pair_accuracy"] = round(
        result["word_pair_direction"]["pairwise_orientation_accuracy_with_half_credit_ties"]
        - result["shuffled_training_null"]["pairwise_orientation_accuracy_with_half_credit_ties"], 6)
    result["relative_to_chance_not_a_decipherment"] = True
    return result


def run(zl_raw: bytes, it_raw: bytes) -> dict:
    b09.checked_bytes(zl_raw, b09.SOURCES["ZL3b"]["sha256"])
    b09.checked_bytes(it_raw, b09.SOURCES["IT2a"]["sha256"])
    zlmeta, itmeta = b09.parse_ivtff(zl_raw), b09.parse_ivtff(it_raw)
    split = b09.fixed_split(zlmeta, itmeta)
    zl, zdiscard = parse_lines(zl_raw)
    it, idiscard = parse_lines(it_raw)
    return {
        "experiment": "B17-OPEN-001",
        "method": "held-out pairwise orientation diagnostic, NOT full-line beam reordering",
        "not_reimplementation_of_private_b17": True,
        "prior_exploration_of_test_folios": True,
        "same_physical_manuscript_in_two_transcriptions": True,
        "fixed_model_selection": "no held-out or validation tuning; fixed alpha=1, edge prior=10",
        "source_hashes": {k: v["sha256"] for k, v in b09.SOURCES.items()},
        "source_urls": {k: v["url"] for k, v in b09.SOURCES.items()},
        "folio_split_counts": {k: len(v) for k, v in split.items()},
        "folio_split_hashes": {k: sha256(("\n".join(sorted(v))+"\n").encode()).hexdigest()
                               for k, v in split.items()},
        "actual_plaintext_or_semantic_accuracy": "NOT_ESTIMABLE",
        "results": {
            "ZL3b": compare_transcription("ZL3b", zl, split, zdiscard),
            "IT2a": compare_transcription("IT2a", it, split, idiscard),
        }
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--download", action="store_true")
    parser.add_argument("--zl3b", type=Path)
    parser.add_argument("--it2a", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.download:
        if args.zl3b or args.it2a:
            parser.error("--download and local files are mutually exclusive")
        zl, it = b09.download("ZL3b"), b09.download("IT2a")
    else:
        if not args.zl3b or not args.it2a:
            parser.error("Provide both local source paths or --download")
        zl, it = args.zl3b.read_bytes(), args.it2a.read_bytes()
    result = run(zl, it)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    for name, x in result["results"].items():
        print("B17_PUBLIC", json.dumps({
            "source": name,
            "heldout_pairs": x["word_pair_direction"]["n_distinct_spelling_pairs"],
            "directed_pair_PA": x["word_pair_direction"]["pairwise_orientation_accuracy_with_half_credit_ties"],
            "shuffled_PA": x["shuffled_training_null"]["pairwise_orientation_accuracy_with_half_credit_ties"],
            "edge_position_PA": x["edge_position_only"]["pairwise_orientation_accuracy_with_half_credit_ties"],
            "observed_minus_shuffled": x["observed_minus_shuffled_pair_accuracy"]
        }, sort_keys=True))
    print("B17_PUBLIC: structural pair ordering only; SEMANTICS NOT_ESTIMABLE.")


if __name__ == "__main__":
    main()
