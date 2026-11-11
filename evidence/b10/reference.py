#!/usr/bin/env python3
"""B10-OPEN-001. Public reference benchmark for written-form reconstruction.

No Sherlock implementation, training corpus or secret key is imported.
The shared, publicly released B09 source hash and folio split are reused.
This experiment does NOT measure a deciphered Voynich word.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import random
import re

# Import the published B09 source by an unambiguous module name. The B10 and
# B09 scripts are both called reference.py; ordinary imports may bind the
# wrong module during unittest discovery.
_b09_file = Path(__file__).resolve().parents[1] / "b09" / "reference.py"
_b09_spec = importlib.util.spec_from_file_location("b09_public_reference", _b09_file)
if _b09_spec is None or _b09_spec.loader is None:
    raise ImportError("Cannot locate public B09 integrity and split utilities")
b09 = importlib.util.module_from_spec(_b09_spec)
_b09_spec.loader.exec_module(b09)

TUNING = (0.0, 0.2, 0.4, 0.6, 0.8)
SIDE = (0.0, 0.15, 0.30)
ROLE_CATEGORIES = ("paragraph", "initial", "middle", "final", "single")
SMOOTH = 6.0


def events_from_ivtff(raw: bytes, eligible_folios: set[str]) -> list[dict]:
    """Parse P-line spelling events; mask target's exact spelling in model inputs.

    Uncertain slots are skipped, never corrected. Their position in the
    ORIGINAL slot sequence still determines the line-position category.
    For a target event only neighbouring reduced codes, not full forms,
    enter the conditioning fields.
    """
    meta = b09.parse_ivtff(raw)
    out = []
    current = None
    line_no = 0
    for record in raw.decode("utf-8-sig").splitlines():
        page = b09.HEADER.match(record)
        if page:
            current = page.group(1)
            line_no = 0
            continue
        line = b09.LOCUS.match(record)
        if not line or current not in eligible_folios:
            continue
        folio, locus, body = line.groups()
        if folio != current or not b09.BODY_LOCUS.search(locus):
            continue
        line_no += 1
        opens = "<%>" in body or locus.startswith(("@P", "*P"))
        body = body.replace("<->", ".")
        body = b09.EDITOR_COMMENT.sub(" ", body)
        body = body.split("!")[0]
        body = b09.UNCERTAIN.sub("?", body)
        body = b09.REMAINING_TAG.sub("", body)
        slots = [s for s in re.split(r"[.,\s=]+", body) if s]
        valid = []
        for index, word in enumerate(slots):
            if not b09.PURE_EVA.fullmatch(word):
                continue
            if len(slots) == 1:
                role = "single"
            elif index == 0:
                role = "paragraph" if opens else "initial"
            elif index == len(slots) - 1:
                role = "final"
            else:
                role = "middle"
            valid.append((word, role))
        codes = [b09.skeleton(w, b09.VOWEL_LIKE_EVA) for w, _ in valid]
        for i, ((word, role), code) in enumerate(zip(valid, codes)):
            out.append({
                "folio": folio,
                "line": line_no,
                "scope": meta[folio]["stratum"],
                "word": word,   # scoring truth; never passed as a model feature
                "code": code,
                "role": role,
                "left": codes[i - 1] if i else "<BOS>",
                "right": codes[i + 1] if i + 1 < len(codes) else "<EOS>",
            })
    return out


class Codebook:
    def __init__(self, training: list[dict]):
        self.base = defaultdict(Counter)
        self.roles = defaultdict(Counter)
        self.left = defaultdict(Counter)
        self.right = defaultdict(Counter)
        for e in training:
            group = (e["scope"], e["code"])
            self.base[group][e["word"]] += 1
            self.roles[(group, e["role"])][e["word"]] += 1
            self.left[(group, e["left"])][e["word"]] += 1
            self.right[(group, e["right"])][e["word"]] += 1

    def candidates(self, e: dict) -> Counter:
        return self.base.get((e["scope"], e["code"]), Counter())

    def predict(self, e: dict, weights: tuple[float, float, float]) -> dict:
        group = (e["scope"], e["code"])
        counts = self.base.get(group)
        if not counts:
            return {}
        r, l, right = weights
        if min(r, l, right) < 0 or r + l + right > 1 + 1e-10:
            raise ValueError("Mixture weights invalid")
        size = len(counts)
        total = sum(counts.values())
        prior = {word: (n + 0.5) / (total + 0.5 * size)
                 for word, n in counts.items()}

        def local(table: dict, condition: str) -> dict:
            row = table.get((group, condition), {})
            denominator = sum(row.values()) + SMOOTH
            return {w: (row.get(w, 0) + SMOOTH * prior[w]) / denominator
                    for w in counts}

        role = local(self.roles, e["role"]) if r else None
        left = local(self.left, e["left"]) if l else None
        ending = local(self.right, e["right"]) if right else None
        scores = {w: (1 - r - l - right) * p
                  + (r * role[w] if role is not None else 0)
                  + (l * left[w] if left is not None else 0)
                  + (right * ending[w] if ending is not None else 0)
                  for w, p in prior.items()}
        assert abs(sum(scores.values()) - 1.0) < 1e-7
        return scores


def eligibility(model: Codebook, samples: list[dict]):
    counts = Counter()
    eligible = []
    for e in samples:
        counts["all_test_tokens"] += 1
        candidates = model.candidates(e)
        if not candidates:
            counts["unknown_transformed_code"] += 1
        elif e["word"] not in candidates:
            counts["known_code_but_unseen_original_form"] += 1
        elif len(candidates) == 1:
            counts["only_one_form_candidate"] += 1
        else:
            eligible.append(e)
            counts["ambiguous_evaluable"] += 1
    return dict(counts), eligible


def metrics(model: Codebook, samples: list[dict], weights: tuple[float, float, float]):
    correct, logloss = 0, 0.0
    grouped = defaultdict(lambda: [0.0, 0.0, 0])
    for e in samples:
        distribution = model.predict(e, weights)
        truth = e["word"]  # label consulted only after prediction
        assert truth in distribution
        p = distribution[truth]
        prediction = min(distribution, key=lambda k: (-distribution[k], k))
        loss = -math.log2(p)
        correct += prediction == truth
        logloss += loss
        grouped[e["folio"]][0] += loss
        grouped[e["folio"]][1] += float(prediction == truth)
        grouped[e["folio"]][2] += 1
    n = len(samples)
    return {
        "eligible_tokens": n,
        "eligible_folios": len(grouped),
        "top1": round(correct / n, 7) if n else None,
        "bits_per_token": round(logloss / n, 7) if n else None
    }


def find_weights(model: Codebook, validation: list[dict]):
    _, subset = eligibility(model, validation)
    if len(subset) < 30:
        raise ValueError("Insufficient validation candidates")
    roles = [(r, 0.0, 0.0) for r in TUNING]
    # Critically, role-only candidates are a SUBSET of the contextual grid.
    combos = [(r, l, rr) for r in TUNING for l in SIDE for rr in SIDE
              if r + l + rr <= 1.0 + 1e-12]
    score_fn = lambda w: (metrics(model, subset, w)["bits_per_token"], w)
    best_role = min(roles, key=score_fn)
    best_context = min(combos, key=score_fn)
    return {
        "role": best_role,
        "context": best_context,
        "validation_eligible": len(subset),
        "role_validation_bpt": metrics(model, subset, best_role)["bits_per_token"],
        "context_validation_bpt": metrics(model, subset, best_context)["bits_per_token"],
        "fair_grid_contains_role_only": True,
    }


def bootstrap_gain(model: Codebook, data: list[dict],
                   role: tuple, context: tuple, reps: int = 500) -> dict:
    groups = defaultdict(lambda: [0.0, 0])
    for e in data:
        pa = model.predict(e, role)[e["word"]]
        pb = model.predict(e, context)[e["word"]]
        bucket = groups[e["folio"]]
        bucket[0] += math.log2(pb / pa)
        bucket[1] += 1
    ids = sorted(groups)
    numerator = sum(v[0] for v in groups.values())
    denominator = sum(v[1] for v in groups.values())
    rng = random.Random(408)
    vals = []
    for _ in range(reps):
        chosen = [groups[ids[rng.randrange(len(ids))]] for __ in ids]
        vals.append(sum(v[0] for v in chosen) / sum(v[1] for v in chosen))
    vals.sort()
    return {
        "bits_per_token_context_advantage": round(numerator / denominator, 7),
        "folio_bootstrap95": [round(vals[int(reps * .025)], 7),
                              round(vals[min(reps - 1, int(reps * .975))], 7)],
        "informative_folios": len(ids),
    }


def permute_context(model: Codebook, data: list[dict],
                    weights: tuple, reps: int = 99) -> dict:
    """Shuffle PAIRS of neighbouring codes within (scope, target code, role).

    Target written forms and all training counts remain held fixed.
    """
    base = metrics(model, data, weights)["bits_per_token"]
    buckets = defaultdict(list)
    for idx, e in enumerate(data):
        buckets[(e["scope"], e["code"], e["role"])].append(idx)
    rng = random.Random(1104)
    null = []
    movable = sum(len(v) for v in buckets.values() if len(v) > 1)
    for _ in range(reps):
        scratch = list(data)
        for indices in buckets.values():
            if len(indices) == 1:
                continue
            shuffled = [(data[i]["left"], data[i]["right"]) for i in indices]
            rng.shuffle(shuffled)
            for i, (left, right) in zip(indices, shuffled):
                scratch[i] = {**data[i], "left": left, "right": right}
        null.append(metrics(model, scratch, weights)["bits_per_token"])
    null.sort()
    return {
        "permutations": reps,
        "shuffled_median_bpt": null[len(null) // 2],
        "observed_bpt": base,
        "test_fraction_permutable": round(movable / len(data), 7),
        "empirical_p_for_shuffled_bpt_le_observed": round(
            (1 + sum(v <= base + 1e-12 for v in null)) / (reps + 1), 7),
        "null_limited_by_singleton_groups": True,
    }


def evaluate_source(name: str, events: list[dict], split: dict,
                    frozen: dict | None = None, bootstrap_reps=500,
                    null_reps=99) -> tuple[dict, dict]:
    by_folio = {k: set(v) for k, v in split.items()}
    train = [e for e in events if e["folio"] in by_folio["train"]]
    valid = [e for e in events if e["folio"] in by_folio["validation"]]
    test = [e for e in events if e["folio"] in by_folio["test"]]
    model = Codebook(train)
    selected = find_weights(model, valid) if frozen is None else frozen
    coverage, subset = eligibility(model, test)
    if len(subset) < 100:
        raise ValueError("Too few eligible held-out ambiguous spellings")
    role = tuple(selected["role"])
    context = tuple(selected["context"])
    return ({
        "transcription": name,
        "training_events": len(train),
        "validation_events": len(valid),
        "test_events": len(test),
        "coverage": coverage,
        "frequency_baseline": metrics(model, subset, (0.0, 0.0, 0.0)),
        "position_only": metrics(model, subset, role),
        "position_and_neighbour_codes": metrics(model, subset, context),
        "context_gain_over_position": bootstrap_gain(
            model, subset, role, context, bootstrap_reps),
        "neighbour_code_permutation_control": permute_context(
            model, subset, context, null_reps),
        "evaluable_subset_is_selected_using_training_candidate_knowledge": True,
    }, selected)


def run(zl: bytes, it: bytes, *, null_reps=99, bootstrap_reps=500) -> dict:
    b09.checked_bytes(zl, b09.SOURCES["ZL3b"]["sha256"])
    b09.checked_bytes(it, b09.SOURCES["IT2a"]["sha256"])
    zlmeta, itmeta = b09.parse_ivtff(zl), b09.parse_ivtff(it)
    split = b09.fixed_split(zlmeta, itmeta)
    wanted = set(sum(split.values(), []))
    zle = events_from_ivtff(zl, wanted)
    ite = events_from_ivtff(it, wanted)
    z, frozen = evaluate_source("ZL3b", zle, split,
                                bootstrap_reps=bootstrap_reps,
                                null_reps=null_reps)
    i, _ = evaluate_source("IT2a", ite, split, frozen,
                            bootstrap_reps=bootstrap_reps,
                            null_reps=null_reps)
    return {
        "experiment": "B10-OPEN-001",
        "evaluation": "full EVA written-form selection, not translation",
        "sources_sha256": {k: v["sha256"] for k, v in b09.SOURCES.items()},
        "source_urls": {k: v["url"] for k, v in b09.SOURCES.items()},
        "shared_physical_folios": {k: len(v) for k, v in split.items()},
        "shared_folio_hashes": {k: hashlib.sha256(
            ("\n".join(sorted(v)) + "\n").encode()).hexdigest()
            for k, v in split.items()},
        "historically_independent_corpora": False,
        "previously_explored_folios": True,
        "model_tuning_on": "ZL3b validation only; reuse parameters on IT2a",
        "fairer_context_model_grid": True,
        "bidirectional_context_required": True,
        "semantic_decipherment_accuracy": "NOT_ESTIMABLE",
        "source_frozen_parameters": frozen,
        "transcriptions": {"ZL3b": z, "IT2a": i},
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--download", action="store_true")
    parser.add_argument("--zl3b", type=Path)
    parser.add_argument("--it2a", type=Path)
    parser.add_argument("--bootstrap-reps", type=int, default=500)
    parser.add_argument("--null-reps", type=int, default=99)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    if args.bootstrap_reps < 10 or args.null_reps < 1:
        parser.error("Not enough repetitions")
    if args.download:
        if args.zl3b or args.it2a:
            parser.error("Use either --download or local source paths")
        zl, it = b09.download("ZL3b"), b09.download("IT2a")
    else:
        if not (args.zl3b and args.it2a):
            parser.error("Both local paths required")
        zl, it = args.zl3b.read_bytes(), args.it2a.read_bytes()
    result = run(zl, it, null_reps=args.null_reps,
                 bootstrap_reps=args.bootstrap_reps)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n",
                        encoding="utf-8")
    for name, v in result["transcriptions"].items():
        print("B10_PUBLIC", json.dumps({
            "source": name, "coverage": v["coverage"],
            "frequency": v["frequency_baseline"],
            "position": v["position_only"],
            "context": v["position_and_neighbour_codes"],
            "gain": v["context_gain_over_position"],
            "permutation": v["neighbour_code_permutation_control"],
        }, sort_keys=True))
    print("B10_PUBLIC scientific status: ORTHOGRAPHIC_ONLY; SEMANTICS_NOT_ESTIMABLE")


if __name__ == "__main__":
    main()
