import argparse
import csv
from pathlib import Path

WEIGHTS = {
    "impact": 0.4,
    "evidence": 0.35,
    "effort": 0.25
}

def score(row: dict) -> float:
    impact = float(row["impact"])
    evidence = float(row["evidence"])
    effort = float(row["effort"])
    return round(
        impact * WEIGHTS["impact"]
        + evidence * WEIGHTS["evidence"]
        + (6 - effort) * WEIGHTS["effort"],
        2
    )

def main():
    parser = argparse.ArgumentParser(description="Prioritize business hypotheses.")
    parser.add_argument("--input", required=True, help="CSV with id, hypothesis, impact, evidence and effort.")
    parser.add_argument("--output", required=True, help="Output ranked CSV.")
    args = parser.parse_args()

    input_path = Path(args.input)
    rows = []

    with input_path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        required = {"id", "hypothesis", "impact", "evidence", "effort"}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError(f"Required columns: {sorted(required)}")
        for row in reader:
            row["priority_score"] = score(row)
            rows.append(row)

    rows.sort(key=lambda item: item["priority_score"], reverse=True)

    with Path(args.output).open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=list(rows[0].keys()) if rows else [])
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    main()
