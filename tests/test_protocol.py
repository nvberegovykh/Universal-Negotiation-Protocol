"""Adversarial checks of record invariants, not a proof of diplomatic fairness."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("unp_validate", ROOT / "scripts/validate.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
BASE = json.loads((ROOT / "examples/session.json").read_text())


class ProtocolTests(unittest.TestCase):
    def setUp(self):
        self.record = copy.deepcopy(BASE)

    def rejected(self, phrase):
        errors = MODULE.validate(self.record)
        self.assertTrue(any(phrase in e for e in errors), errors)

    def test_valid_synthetic_record(self):
        self.assertEqual([], MODULE.validate(self.record))

    def test_second_correction_is_rejected(self):
        self.record["corrections"].append(copy.deepcopy(self.record["corrections"][0]))
        self.rejected("duplicate")

    def test_more_than_one_round_is_rejected(self):
        self.record["cycle"]["correction_round_limit"] = 2
        self.rejected("exactly one")

    def test_unapproved_agency_is_rejected(self):
        self.record["agency"]["approved_by"] = ["east"]
        self.rejected("every side must approve")

    def test_duplicate_representative_is_rejected(self):
        self.record["sides"][1]["representative_id"] = "east-representative"
        self.rejected("multiple sides")

    def test_missing_correction_is_rejected(self):
        self.record["corrections"].pop()
        self.rejected("one disposed opportunity")

    def test_different_baseline_is_rejected(self):
        self.record["corrections"][0]["baseline_sha256"] = "0" * 64
        self.rejected("same frozen baseline")

    def test_early_no_response_is_rejected(self):
        self.record["corrections"][0]["disposition"] = "no_response"
        self.rejected("before opportunity expires")

    def test_missing_consent_is_rejected(self):
        self.record["closure"]["ratifications"].pop()
        self.rejected("missing explicit ratification")

    def test_unknown_ratifying_actor_is_rejected(self):
        self.record["closure"]["ratifications"][0]["side_id"] = "proxy"
        self.rejected("unknown side")

    def test_changed_text_is_rejected(self):
        self.record["proposals"][0]["terms"] += " New obligation."
        self.rejected("content digest mismatch")

    def test_wrong_evaluation_version_is_rejected(self):
        self.record["reviews"][0]["proposal_sha256"] = "0" * 64
        self.rejected("exact proposal version")

    def test_wrong_ratification_version_is_rejected(self):
        self.record["closure"]["ratifications"][0]["proposal_sha256"] = "0" * 64
        self.rejected("differs from final text")

    def test_expired_source_is_rejected(self):
        self.record["reviews"][0]["sources"][0]["fresh_until"] = "2026-10-30T15:49:00Z"
        self.rejected("evidence expired")

    def test_expired_review_is_rejected(self):
        self.record["reviews"][0]["valid_until"] = "2026-10-30T15:49:00Z"
        self.rejected("review is not valid")

    def test_unresolved_material_doubt_is_rejected(self):
        self.record["doubts"][0]["material_to"] = ["coexistence-1"]
        self.rejected("unresolved material doubt")

    def test_incomplete_stability_window_is_rejected(self):
        self.record["closure"]["stable_since"] = "2026-10-30T15:49:00Z"
        self.rejected("observation window incomplete")

    def test_timeout_does_not_make_adoption_stable(self):
        self.record["closure"]["at"] = self.record["cycle"]["deadline_at"]
        self.record["closure"]["stable"] = False
        self.rejected("adoption requires demonstrated")

    def test_exclusion_cannot_be_called_stable(self):
        self.record["closure"]["exclusion_triggered"] = True
        self.rejected("cannot be labeled stable")

    def test_condition_needs_evidence(self):
        self.record["reviews"][0]["disposition"] = "conditional"
        self.rejected("satisfaction evidence")

    def test_missing_professional_signoff_is_rejected(self):
        self.record["reviews"][0]["signoff_ref"] = ""
        self.rejected("signoff reference")

    def test_review_cannot_postdate_stability(self):
        self.record["reviews"][0]["issued_at"] = "2026-10-30T15:46:00Z"
        self.rejected("review is not valid")

    def test_unresolved_closure_is_valid(self):
        c = self.record["closure"]
        c.update(status="closed_unresolved", stable=False, stable_since=None,
                 adopted_proposal_ids=[], ratifications=[])
        self.record["doubts"][0]["material_to"] = ["coexistence-1"]
        self.assertEqual([], MODULE.validate(self.record))

    def test_emergency_incomplete_orbit_is_explicit(self):
        c = self.record["closure"]
        c.update(status="closed_unsafe", at="2026-10-30T15:20:00Z", stable=False,
                 stable_since=None, exclusion_triggered=True,
                 candidate_proposal_ids=[], adopted_proposal_ids=[], ratifications=[])
        self.record["corrections"] = []
        self.assertEqual([], MODULE.validate(self.record))

    def test_malformed_record_returns_errors(self):
        self.assertTrue(MODULE.validate({}))


if __name__ == "__main__":
    unittest.main()
