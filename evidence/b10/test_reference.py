"""Synthetic-only safety and mathematical tests for public B10 benchmark."""
import unittest
import reference as b10


def event(word, role="middle", scope=("1", "A", "H"),
          code="dn", left="l", right="r", folio="f1r"):
    return {"word": word, "code": code, "scope": scope, "role": role,
            "left": left, "right": right, "folio": folio, "line": 1}


def synthetic_ivtff(n=210):
    raw = ["#=IVTFF Eva- 2.0 M 5"]
    for i in range(1, n+1):
        f = f"f{i}r"
        raw += [
            f"<{f}> <! $H=1 $L=A $I=H>",
            f"<{f}.1,@P0> <%>daiin.dan.dor",
            f"<{f}.2,+P0> chol.sheol.dan",
            f"<{f}.3,=Pt> or.otol.dain<$>"
        ]
    return ("\n".join(raw)+"\n").encode()


class B10PublicTests(unittest.TestCase):
    def test_parser_keeps_roles_and_true_word_as_label(self):
        raw = synthetic_ivtff()
        meta = b10.b09.parse_ivtff(raw)
        events = b10.events_from_ivtff(raw, set(meta))
        self.assertEqual(len(events), 210*9)
        first = events[0]
        self.assertEqual(first["role"], "paragraph")
        self.assertEqual(first["word"], "daiin")
        self.assertEqual(first["code"], "dn")
        self.assertEqual(first["right"], "dn")
        self.assertTrue(all(e["role"] in b10.ROLE_CATEGORIES for e in events))

    def test_folio_split_disjoint_and_stable(self):
        raw = synthetic_ivtff()
        m = b10.b09.parse_ivtff(raw)
        x = b10.b09.fixed_split(m,m)
        self.assertEqual(set(x["train"]) & set(x["test"]), set())
        self.assertEqual(len(x["train"])+len(x["test"])+len(x["validation"]),210)

    def test_probabilities_normalized_and_no_target_used_as_feature(self):
        train=[event("daiin")]*7 + [event("dan")]*3
        model=b10.Codebook(train)
        q=event("diin")
        p=model.predict(q,(0.2,0.15,0.3))
        self.assertEqual(set(p),{"daiin","dan"})
        self.assertAlmostEqual(sum(p.values()),1.0)
        self.assertEqual(p, model.predict({**q,"word":"completely_different_target"},(0.2,0.15,0.3)))

    def test_eligibility_does_not_hide_missing_spelling(self):
        model=b10.Codebook([event("daiin"),event("dan")])
        inp=[event("diin"), event("daiin"),event("different",code="other")]
        cov,ready=b10.eligibility(model,inp)
        self.assertEqual(cov["known_code_but_unseen_original_form"],1)
        self.assertEqual(cov["unknown_transformed_code"],1)
        self.assertEqual(cov["ambiguous_evaluable"],1)
        self.assertEqual(len(ready),1)

    def test_fair_grid_includes_role_only_and_is_valid(self):
        roles=[(r,0.,0.) for r in b10.TUNING]
        context=[(r,l,rr) for r in b10.TUNING
                 for l in b10.SIDE for rr in b10.SIDE if r+l+rr<=1.0+1e-12]
        for r in roles:
            self.assertIn(r,context)
        for r,l,rr in context:
            self.assertLessEqual(r+l+rr,1.0000001)

    def test_metrics_are_probability_scores_not_translation(self):
        training=[event("daiin")]*3+[event("dan")]
        model=b10.Codebook(training)
        eligible=[event("daiin"),event("dan")]
        m=b10.metrics(model,eligible,(0.,0.,0.))
        self.assertEqual(m["eligible_tokens"],2)
        self.assertEqual(m["top1"],0.5)
        self.assertTrue(m["bits_per_token"]>0)

    def test_incorrect_hash_fails_without_silent_fallback(self):
        with self.assertRaises(ValueError):
            b10.b09.checked_bytes(b"test","0"*64)


if __name__=="__main__":
    unittest.main()
