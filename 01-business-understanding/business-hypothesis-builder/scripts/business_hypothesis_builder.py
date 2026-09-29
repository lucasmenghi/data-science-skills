import argparse
import csv
import math
from pathlib import Path

WEIGHTS = {
    "impact": 0.4,
    "evidence": 0.35,
    "effort": 0.25
}

def score(row: dict, weights: dict | None = None) -> float:
    weights = WEIGHTS if weights is None else weights
    if set(weights) != set(WEIGHTS) or any(not math.isfinite(v) or v < 0 for v in weights.values()) or not math.isclose(sum(weights.values()), 1.0):
        raise ValueError("Weights must be finite, nonnegative and sum to 1")
    impact = float(row["impact"])
    evidence = float(row["evidence"])
    effort = float(row["effort"])
    if any(not math.isfinite(v) or not 1 <= v <= 5 for v in (impact, evidence, effort)):
        raise ValueError("Impact, evidence and effort must be finite values between 1 and 5")
    return round(
        impact * weights["impact"]
        + evidence * weights["evidence"]
        + (6 - effort) * weights["effort"],
        2
    )

def main() -> None:
    parser = argparse.ArgumentParser(description="Prioritize business hypotheses.")
    parser.add_argument("--input", required=True, help="CSV with id, hypothesis, impact, evidence and effort.")
    parser.add_argument("--output", required=True, help="Output ranked CSV.")
    parser.add_argument("--impact-weight", type=float, default=0.4)
    parser.add_argument("--evidence-weight", type=float, default=0.35)
    parser.add_argument("--effort-weight", type=float, default=0.25)
    args = parser.parse_args()

    input_path = Path(args.input)
    rows = []
    weights = {"impact": args.impact_weight, "evidence": args.evidence_weight, "effort": args.effort_weight}
    try:
        score({"impact": 1, "evidence": 1, "effort": 1}, weights)
    except ValueError as exc:
        parser.error(str(exc))

    with input_path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        required = {"id", "hypothesis", "impact", "evidence", "effort"}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError(f"Required columns: {sorted(required)}")
        for row in reader:
            row["priority_score"] = score(row, weights)
            rows.append(row)

    rows.sort(key=lambda item: item["priority_score"], reverse=True)

    with Path(args.output).open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=list(rows[0].keys()) if rows else list(reader.fieldnames or []) + ["priority_score"])
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    main()
