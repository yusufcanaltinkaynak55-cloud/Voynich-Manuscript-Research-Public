"""Check a new B09-OPEN-001 run against its first published run.

Exact equality is appropriate here because the exact source bytes, fixed
folio split, rounding, trial seeds, and deterministic Python evaluator are
unchanged. This is a regression check, NOT an independent scientific audit.
"""
import argparse
import json
from pathlib import Path


def validate(actual: dict, expected: dict) -> None:
    if actual["experiment"] != expected["experiment"]:
        raise AssertionError("Experiment identifier changed")
    if actual["semantic_accuracy"] != "NOT_ESTIMABLE":
        raise AssertionError("Semantic status misrepresented")
    if actual["previously_explored_holdout"] is not True:
        raise AssertionError("Known holdout disclosure missing")
    for label in ("ZL3b", "IT2a"):
        a = actual["results"][label]
        e = expected[label]
        fields = {
            "oov_test_tokens": a["oov_test_tokens"],
            "remove_aeioy_rate": a["remove_aeioy"]["matched_oov_rate"],
            "remove_dklrs_rate": a["remove_dklrs_control"]["matched_oov_rate"],
            "random_median_rate": a["random_same_deletion_count_null"]["median"],
            "ambiguous_match_fraction": a["remove_aeioy"]["ambiguous_matched_token_fraction"],
        }
        for key, observed in fields.items():
            if observed != e[key]:
                raise AssertionError(
                    f"{label} {key}: expected {e[key]}, observed {observed}")
    print("B09 aggregate regression PASS: both transcriptions and all controls.")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--actual", required=True, type=Path)
    p.add_argument("--expected", default=Path(__file__).with_name("expected_metrics.json"), type=Path)
    o = p.parse_args()
    validate(json.loads(o.actual.read_text(encoding="utf-8")),
             json.loads(o.expected.read_text(encoding="utf-8")))


if __name__ == "__main__":
    main()
