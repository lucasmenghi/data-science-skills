"""Check decisions and edge cases, not generated documentation wording."""
from __future__ import annotations

import importlib.util
import math
import sys
import unittest
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(relative: str, name: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


windows = load("01-business-understanding/target-definition/scripts/target_definition.py", "target_windows_test")
criteria = load("01-business-understanding/success-criteria-definition/scripts/success_criteria_definition.py", "criteria_test")
hypotheses = load("01-business-understanding/business-hypothesis-builder/scripts/business_hypothesis_builder.py", "hypotheses_test")
framing = load("01-business-understanding/problem-framing/scripts/problem_framing.py", "framing_test")
policies = load("06-model-validation/threshold-optimization/scripts/threshold_policy.py", "policies_test")


class DecisionUtilityTests(unittest.TestCase):
    def test_window_crosses_leap_day(self) -> None:
        result = windows.TargetWindow(date(2024, 2, 29), 2, 1, 2).calculate()
        self.assertEqual(result, {"observation_start": "2024-02-28", "observation_end": "2024-02-29",
                                  "performance_start": "2024-03-02", "performance_end": "2024-03-03"})

    def test_invalid_windows(self) -> None:
        for observation, gap, performance in [(0, 0, 1), (1, -1, 1), (1, 0, 0), (True, 0, 1)]:
            with self.assertRaises(ValueError):
                windows.TargetWindow(date(2026, 1, 1), observation, gap, performance)

    def test_lower_is_better(self) -> None:
        self.assertEqual(criteria.evaluate(5, 10, 5, "minimize"), "GO")
        self.assertEqual(criteria.evaluate(7, 10, 5, "minimize"), "REVISE")
        self.assertEqual(criteria.evaluate(11, 10, 5, "minimize"), "NO-GO")
        self.assertEqual(criteria.evaluate(0.8, 0.7, 0.8), "GO")

    def test_bad_criteria(self) -> None:
        for args in [(math.nan, 0, 1), (1, 2, 1), (1, 1, 2, "minimize")]:
            with self.assertRaises(ValueError):
                criteria.evaluate(*args)

    def test_hypothesis_effort_and_weights(self) -> None:
        easy = hypotheses.score({"impact": 4, "evidence": 4, "effort": 1})
        hard = hypotheses.score({"impact": 4, "evidence": 4, "effort": 5})
        self.assertGreater(easy, hard)
        with self.assertRaises(ValueError):
            hypotheses.score({"impact": 99, "evidence": 2, "effort": 3})
        with self.assertRaises(ValueError):
            hypotheses.score({"impact": 1, "evidence": 2, "effort": 3}, {"impact": 1, "evidence": 1, "effort": 1})

    def test_framing_rejects_wrong_container_and_blank(self) -> None:
        with self.assertRaises(ValueError):
            framing.validate_context([])
        result = framing.validate_context({key: " " for key in framing.REQUIRED_FIELDS})
        self.assertFalse(result["is_complete"])
        self.assertEqual(result["completeness_score"], 0)

    def test_capacity_does_not_split_score_ties(self) -> None:
        result = policies.evaluate_policies([1, 0, 1, 0], [0.9, 0.8, 0.8, 0.2],
                                            tp_benefit=10, fp_cost=2, capacity=2)
        self.assertEqual(result["selected_policy"]["actions"], 1)
        self.assertEqual(result["selected_policy"]["utility"], 10)
        self.assertEqual([p["actions"] for p in result["policies"]], [0, 1, 3, 4])

    def test_utility_and_confusion(self) -> None:
        result = policies.evaluate_policies([1, 0, 1, 0], [0.9, 0.8, 0.8, 0.2],
                                            tp_benefit=10, fp_cost=2, capacity=3)
        best = result["selected_policy"]
        self.assertEqual((best["tp"], best["fp"], best["fn"], best["tn"]), (2, 1, 0, 1))
        self.assertEqual(best["utility"], 18)

    def test_no_action_and_undefined_rates(self) -> None:
        result = policies.evaluate_policies([0, 0], [0.5, 0.2], tp_benefit=1, fp_cost=2)
        self.assertEqual(result["selected_policy"]["policy"], "no_action")
        self.assertIsNone(result["selected_policy"]["recall"])
        self.assertIsNone(result["selected_policy"]["precision"])

    def test_bad_policy_inputs(self) -> None:
        for labels, scores in [([], []), ([1], [math.nan]), ([2], [0.5]), ([1], [0.1, 0.2])]:
            with self.assertRaises(ValueError):
                policies.evaluate_policies(labels, scores, tp_benefit=1, fp_cost=1)
        with self.assertRaises(ValueError):
            policies.evaluate_policies([1], [0.5], tp_benefit=-1, fp_cost=1)


if __name__ == "__main__":
    unittest.main()
