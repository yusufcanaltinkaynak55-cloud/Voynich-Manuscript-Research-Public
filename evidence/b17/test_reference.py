"""Synthetic regression tests for the narrow B17 public reference diagnostic."""
import unittest

import reference as b17


def fixture(n=210):
    lines=["#=IVTFF Eva- 2.0 M 5"]
    for i in range(1,n+1):
        f=f"f{i}r"
        lines += [f"<{f}> <! $H=1 $L=A $I=H>",
                  f"<{f}.1,+P0> dai.chol.shol.qoke",
                  f"<{f}.2,+P0> shol.chol.dai.qoke",
                  f"<{f}.3,=Pt> qoke.shol.chol.dai<$>"]
    return ("\n".join(lines)+"\n").encode()


class B17Tests(unittest.TestCase):
    def test_pinned_byte_mutation_rejected(self):
        with self.assertRaises(ValueError):
            b17.b09.checked_bytes(b"modified","0"*64)

    def test_parser_keeps_physical_line_and_folio(self):
        pages,excluded=b17.parse_lines(fixture())
        self.assertEqual(len(pages),210)
        self.assertEqual(pages["f1r"][0],["dai","chol","shol","qoke"])
        self.assertEqual(len(pages["f210r"]),3)
        self.assertEqual(excluded,{})

    def test_ambiguous_line_excluded_without_merging(self):
        raw=fixture()+b"<f210r.4,+P0> dai.?x.shol.qoke\n"
        pages,excluded=b17.parse_lines(raw)
        self.assertEqual(len(pages["f210r"]),3)
        self.assertEqual(excluded.get("uncertain_or_non_eva_line"),1)

    def test_split_disjoint_and_deterministic(self):
        pages=b17.b09.parse_ivtff(fixture())
        one=b17.b09.fixed_split(pages,pages)
        two=b17.b09.fixed_split(pages,pages)
        self.assertEqual(one,two)
        self.assertTrue(set(one["train"]).isdisjoint(one["test"]))
        self.assertEqual(sum(map(len,one.values())),210)

    def test_direction_and_ties(self):
        model=b17.PairModel([("x",["ab","bc","cd"])]*3)
        self.assertEqual(model.direction("ab","cd"),(1,True))
        self.assertEqual(model.direction("cd","ab"),(-1,True))
        self.assertEqual(model.direction("z","x"),(0,False))
        self.assertEqual(model.direction("ab","ab"),(0,False))

    def test_shuffled_train_preserves_word_multisets_and_is_deterministic(self):
        lines=[("f1r",["a","b","c","d"]),("f2r",["b","a","c","d"])]
        a=b17.shuffled_training(lines)
        self.assertEqual(a,b17.shuffled_training(lines))
        for original,shuffled in zip(lines,a):
            self.assertEqual(original[0],shuffled[0])
            self.assertEqual(sorted(original[1]),sorted(shuffled[1]))

    def test_pair_accuracy_counts_correct_ties_half_credit(self):
        model=b17.PairModel([("f1r",["ab","bc","cd"])]*5)
        testing=[("f41r",["ab","bc","cd"])]*50
        score=b17.count_pairs(testing,model)
        self.assertEqual(score["n_distinct_spelling_pairs"],150)
        self.assertEqual(score["pairwise_orientation_accuracy_with_half_credit_ties"],1.0)
        tie=b17.count_pairs(testing,b17.PairModel([]))
        self.assertEqual(tie["pairwise_orientation_accuracy_with_half_credit_ties"],0.5)

    def test_position_model_has_expected_order_and_unknown_coverage(self):
        model=b17.EdgePositionModel([("f1r",["ab","cd","ef"])]*20)
        self.assertEqual(model.direction("ab","ef"),(1,True))
        self.assertEqual(model.direction("ef","ab"),(-1,True))
        self.assertEqual(model.direction("xy","zz"),(0,False))


if __name__=="__main__":
    unittest.main()
