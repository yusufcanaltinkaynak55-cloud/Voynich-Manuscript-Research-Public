"""Deterministic regression audit of B10-OPEN-001 published aggregate outputs.

This checks the exact code/data/seed/version combination. It is NOT an
independent academic replication and NOT verification of a Voynich reading.
"""
import argparse
import json
from pathlib import Path


def verify(actual: dict, expected: dict):
    if actual["experiment"] != expected["experiment"]:
        raise AssertionError("Unexpected experiment")
    required = {
        "semantic_decipherment_accuracy": "NOT_ESTIMABLE",
        "historically_independent_corpora": False,
        "previously_explored_folios": True,
        "bidirectional_context_required": True,
        "fairer_context_model_grid": True,
    }
    for key, value in required.items():
        if actual.get(key) != value:
            raise AssertionError(f"Disclosure gate failed: {key}")
    for name in ("ZL3b", "IT2a"):
        result = actual["transcriptions"][name]
        known = expected[name]
        coverage = result["coverage"]
        for field in ("all_test_tokens", "ambiguous_evaluable",
                      "unknown_transformed_code",
                      "known_code_but_unseen_original_form",
                      "only_one_form_candidate"):
            if coverage[field] != known[field]:
                raise AssertionError(f"{name} coverage {field}: {coverage[field]} vs {known[field]}")
        for model, output_field in (
                ("frequency", "frequency_baseline"),
                ("position", "position_only"),
                ("context", "position_and_neighbour_codes")):
            for measure in ("top1", "bits_per_token"):
                actual_value = result[output_field][measure]
                expected_value = known[model][measure]
                if actual_value != expected_value:
                    raise AssertionError(
                        f"{name} {model} {measure}: {actual_value} vs {expected_value}"
                    )
        delta = result["context_gain_over_position"]
        checks = {
            "context_vs_position_bpt": delta["bits_per_token_context_advantage"],
            "bootstrap95": delta["folio_bootstrap95"],
            "permutation_p": result["neighbour_code_permutation_control"][
                "empirical_p_for_shuffled_bpt_le_observed"],
            "shuffled_median_bpt": result["neighbour_code_permutation_control"][
                "shuffled_median_bpt"],
        }
        for field, observed in checks.items():
            if observed != known[field]:
                raise AssertionError(f"{name} {field}: {observed} vs {known[field]}")
    print("B10 public regression PASS: both transcriptions, fixed candidate set and all controls.")
    print("No authenticated historical decipherment is claimed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--actual", type=Path, required=True)
    parser.add_argument("--expected", type=Path,
                        default=Path(__file__).with_name("expected_metrics.json"))
    args = parser.parse_args()
    verify(json.loads(args.actual.read_text(encoding="utf-8")),
           json.loads(args.expected.read_text(encoding="utf-8")))
