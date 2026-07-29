import argparse
import json
from pathlib import Path

def evaluate(metric_value: float, minimum: float, target: float) -> str:
    if metric_value < minimum:
        return "NO-GO"
    if metric_value < target:
        return "REVISE"
    return "GO"

def main():
    parser = argparse.ArgumentParser(description="Evaluate a metric against go/revise/no-go thresholds.")
    parser.add_argument("--metric-value", required=True, type=float)
    parser.add_argument("--minimum", required=True, type=float)
    parser.add_argument("--target", required=True, type=float)
    parser.add_argument("--output")
    args = parser.parse_args()

    if args.minimum > args.target:
        raise ValueError("Minimum threshold cannot be greater than target threshold.")

    result = {
        "metric_value": args.metric_value,
        "minimum_threshold": args.minimum,
        "target_threshold": args.target,
        "decision": evaluate(args.metric_value, args.minimum, args.target)
    }
    rendered = json.dumps(result, indent=2)

    if args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
    else:
        print(rendered)

if __name__ == "__main__":
    main()
