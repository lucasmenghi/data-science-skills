"""Evaluate tied-score threshold policies on a user-supplied validation set."""
from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path


def evaluate_policies(
    labels: list[int], scores: list[float], *, tp_benefit: float,
    fp_cost: float, fn_cost: float = 0, action_cost: float = 0,
    capacity: int | None = None,
) -> dict:
    """Maximize empirical utility, without splitting ties or fitting scores."""
    if not labels or len(labels) != len(scores):
        raise ValueError("Labels/scores must be nonempty and have equal length")
    if any(type(y) is not int or y not in (0, 1) for y in labels):
        raise ValueError("Labels must be integer 0 or 1")
    if any(not math.isfinite(s) for s in scores):
        raise ValueError("Scores must be finite")
    amounts = (tp_benefit, fp_cost, fn_cost, action_cost)
    if any(not math.isfinite(v) or v < 0 for v in amounts):
        raise ValueError("Benefit/costs must be finite and nonnegative")
    n = len(labels)
    if capacity is None:
        capacity = n
    if type(capacity) is not int or not 0 <= capacity <= n:
        raise ValueError("Capacity must be an integer between 0 and sample size")
    positives = sum(labels)
    negatives = n - positives

    def record(threshold: float | None, tp: int, fp: int) -> dict:
        fn, tn = positives - tp, negatives - fp
        actions = tp + fp
        utility = tp * tp_benefit - fp * fp_cost - fn * fn_cost - actions * action_cost
        if not math.isfinite(utility):
            raise ValueError("Utility overflow; check units and cost magnitudes")
        return {
            "threshold": threshold, "policy": "no_action" if threshold is None else "score_gte_threshold",
            "tp": tp, "fp": fp, "fn": fn, "tn": tn, "actions": actions,
            "precision": tp / actions if actions else None,
            "recall": tp / positives if positives else None,
            "utility": utility, "feasible": actions <= capacity,
        }

    policies = [record(None, 0, 0)]
    pairs = sorted(zip(scores, labels), reverse=True)
    tp = fp = 0
    index = 0
    while index < n:
        threshold = pairs[index][0]
        while index < n and pairs[index][0] == threshold:
            tp += pairs[index][1]
            fp += 1 - pairs[index][1]
            index += 1
        policies.append(record(threshold, tp, fp))
    best = max((p for p in policies if p["feasible"]), key=lambda p: (p["utility"], -p["actions"]))
    return {
        "rows": n, "positives": positives, "capacity": capacity,
        "costs": dict(zip(("tp_benefit", "fp_cost", "fn_cost", "action_cost"), amounts)),
        "selected_policy": best, "policies": policies,
        "assumptions": [
            "Input must be independent validation predictions; this script cannot verify data provenance.",
            "Costs are constant per outcome/action and true negatives have zero utility.",
            "Ties are kept together; fewer actions break equal-utility ties.",
            "Utility is empirical on this sample, not causal effect or production guarantee.",
            "Do not select the policy using the final test set.",
        ],
    }


def read_predictions(path: Path) -> tuple[list[int], list[float]]:
    labels: list[int] = []
    scores: list[float] = []
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if not {"label", "score"}.issubset(reader.fieldnames or []):
            raise ValueError("CSV requires label and score columns")
        for number, row in enumerate(reader, start=2):
            if row["label"] not in ("0", "1"):
                raise ValueError(f"Invalid label at CSV line {number}")
            labels.append(int(row["label"]))
            scores.append(float(row["score"]))
    return labels, scores


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--tp-benefit", type=float, required=True)
    parser.add_argument("--fp-cost", type=float, required=True)
    parser.add_argument("--fn-cost", type=float, default=0)
    parser.add_argument("--action-cost", type=float, default=0)
    parser.add_argument("--capacity", type=int)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        labels, scores = read_predictions(args.input)
        result = evaluate_policies(labels, scores, tp_benefit=args.tp_benefit, fp_cost=args.fp_cost,
                                   fn_cost=args.fn_cost, action_cost=args.action_cost, capacity=args.capacity)
        rendered = json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False)
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(rendered + "\n", encoding="utf-8")
        else:
            print(rendered)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
