import argparse
import json
import math
from pathlib import Path

def evaluate(metric_value: float, minimum: float, target: float, direction: str = "maximize") -> str:
    """minimum is the acceptance boundary (an upper bound for minimization)."""
    if not all(math.isfinite(v) for v in (metric_value, minimum, target)):
        raise ValueError("Metric and thresholds must be finite")
    if direction not in ("maximize", "minimize"):
        raise ValueError("direction must be maximize or minimize")
    sign = 1 if direction == "maximize" else -1
    value, boundary, goal = (sign * v for v in (metric_value, minimum, target))
    if boundary > goal:
        raise ValueError("Target must be at least as favorable as acceptance boundary")
    if value < boundary:
        return "NO-GO"
    if value < goal:
        return "REVISE"
    return "GO"

def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate a metric against go/revise/no-go thresholds.")
    parser.add_argument("--metric-value", required=True, type=float)
    parser.add_argument("--minimum", required=True, type=float, help="Acceptance boundary; upper bound when minimizing")
    parser.add_argument("--target", required=True, type=float)
    parser.add_argument("--output")
    parser.add_argument("--direction", choices=("maximize", "minimize"), default="maximize")
    args = parser.parse_args()

    try:
        decision = evaluate(args.metric_value, args.minimum, args.target, args.direction)
    except ValueError as exc:
        parser.error(str(exc))

    result = {
        "metric_value": args.metric_value,
        "minimum_threshold": args.minimum,
        "target_threshold": args.target,
        "direction": args.direction,
        "decision": decision,
        "scope": "Single metric only; not a deployment approval"
    }
    rendered = json.dumps(result, indent=2)

    if args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
    else:
        print(rendered)

if __name__ == "__main__":
    main()
