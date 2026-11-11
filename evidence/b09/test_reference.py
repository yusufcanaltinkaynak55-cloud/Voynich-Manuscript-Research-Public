"""Synthetic-only regression tests for the public B09 reference evaluator."""
import unittest
from collections import Counter

from reference import (
    VOWEL_LIKE_EVA, checked_bytes, fixed_split, parse_ivtff,
    randomized_skeleton, score, skeleton,
)


def fixture(n=210):
    parts = ["#=IVTFF Eva- 2.0 M 5"]
    for i in range(1, n + 1):
        folio = f"f{i}r"
        parts.extend([
            f"<{folio}> <! $H=1 $L=A $I=H>",
            f"<{folio}.1,+P0> dain.dan.dor",
            f"<{folio}.2,+P0> chol.shol.daiin",
            f"<{folio}.3,=Pt> otol.kchol.dain<$>",
        ])
    return ("\n".join(parts) + "\n").encode()


class PublicB09Tests(unittest.TestCase):
    def test_hash_verification_rejects_mutations(self):
        with self.assertRaises(ValueError):
            checked_bytes(b"not an expected corpus", "0" * 64)

    def test_skeleton_is_a_code_not_a_word(self):
        self.assertEqual(skeleton("daiin", VOWEL_LIKE_EVA), "dn")
        self.assertEqual(skeleton("aeioy", VOWEL_LIKE_EVA), "∅")
        self.assertEqual(skeleton("dklrs", VOWEL_LIKE_EVA), "dklrs")

    def test_random_control_preserves_removed_character_count(self):
        for word in ("daiin", "choly", "aeioy", "sol", "k"):
            for trial in (1, 2, 30):
                output = randomized_skeleton(word, trial)
                removed = sum(ch in VOWEL_LIKE_EVA for ch in word)
                self.assertEqual(
                    len(output) if output != "∅" else 0, len(word) - removed
                )
                self.assertEqual(output, randomized_skeleton(word, trial))

    def test_transcription_markup_is_not_silently_joined(self):
        head = b"<f211r> <! $H=1 $L=A $I=H>\n"
        line = (b"<f211r.1,+P0> daiin.dan<->dor.{x}.d?e."
                b"<!editor>chol<$>\n")
        blob = head + line
        self.assertEqual(parse_ivtff.__name__, "parse_ivtff")
        # The production parser refuses toy-sized manuscripts; append benign
        # synthetic pages solely to exercise its parsing contract.
        toy = fixture(210) + blob
        pages = parse_ivtff(toy)
        self.assertEqual(pages["f211r"]["words"], ["daiin", "dan", "dor", "chol"])
        self.assertEqual(pages["f211r"]["p_lines"], 1)

    def test_folio_partition_is_repeatable_and_disjoint(self):
        pages = parse_ivtff(fixture(210))
        one, two = fixed_split(pages, pages), fixed_split(pages, pages)
        self.assertEqual(one, two)
        self.assertTrue(set(one["train"]).isdisjoint(one["test"]))
        self.assertEqual(sum(map(len, one.values())), 210)
        self.assertTrue(one["test"] and one["validation"])

    def test_oov_collision_and_ambiguity(self):
        train = ["dain", "dan", "dak"]
        oov = ["dein", "diin", "dok", "xxx"]
        result = score(train, oov, lambda w: skeleton(w, VOWEL_LIKE_EVA))
        self.assertEqual(result["matched_oov_tokens"], 3)
        self.assertEqual(result["matched_oov_rate"], 0.75)
        self.assertEqual(result["ambiguous_matched_token_fraction"], 0.666667)

    def test_folio_threshold_fails_loudly(self):
        with self.assertRaises(ValueError):
            parse_ivtff(b"<f1r> <! $H=1>\n<f1r.1,+P0> dain.dan\n")


if __name__ == "__main__":
    unittest.main()
