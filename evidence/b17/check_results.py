"""Audit B17-OPEN-001 results against first completed public computation.

Only frozen deterministic *pairwise orientation* statistics are compared.
This neither recreates the private full-line B17 algorithm nor authenticates
the manuscript's historical language.
"""
import argparse
import json
from pathlib import Path


def check(actual: dict, baseline: dict):
    assert actual["experiment"] == baseline["experiment"]
    assert actual["not_reimplementation_of_private_b17"] is True
    assert actual["prior_exploration_of_test_folios"] is True
    assert actual["same_physical_manuscript_in_two_transcriptions"] is True
    assert actual["actual_plaintext_or_semantic_accuracy"] == "NOT_ESTIMABLE"
    fields = (
        ("word_pair_direction","pairwise_orientation_accuracy_with_half_credit_ties","directed_pair_pa"),
        ("shuffled_training_null","pairwise_orientation_accuracy_with_half_credit_ties","shuffled_pa"),
        ("edge_position_only","pairwise_orientation_accuracy_with_half_credit_ties","edge_position_pa"),
    )
    for name in ("ZL3b","IT2a"):
        entry=actual["results"][name]
        recorded=baseline[name]
        assert entry["word_pair_direction"]["n_distinct_spelling_pairs"]==recorded["pairwise_pairs"]
        for group, field, expected in fields:
            observed=entry[group][field]
            if observed!=recorded[expected]:
                raise AssertionError(f"{name} {group}: {observed} differs from {recorded[expected]}")
        got=entry["observed_minus_shuffled_pair_accuracy"]
        if got!=recorded["observed_minus_shuffled"]:
            raise AssertionError(f"{name}: unexpected order-difference {got}")
    print("B17 deterministic public regression PASS: matched pinned outputs and controls")
    print("No full-line reconstruction or semantic decipherment claimed")


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--actual",type=Path,required=True)
    p.add_argument("--expected",type=Path,default=Path(__file__).with_name("expected_metrics.json"))
    a=p.parse_args()
    check(json.loads(a.actual.read_text(encoding="utf-8")),
          json.loads(a.expected.read_text(encoding="utf-8")))
