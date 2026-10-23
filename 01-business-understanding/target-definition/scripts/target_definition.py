import argparse
import json
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path

@dataclass
class TargetWindow:
    reference_date: date
    observation_days: int
    gap_days: int
    performance_days: int

    def __post_init__(self) -> None:
        if not isinstance(self.reference_date, date):
            raise ValueError("reference_date must be a date")
        for name in ("observation_days", "gap_days", "performance_days"):
            value = getattr(self, name)
            if isinstance(value, bool) or not isinstance(value, int):
                raise ValueError(f"{name} must be an integer")
        if self.observation_days < 1 or self.performance_days < 1 or self.gap_days < 0:
            raise ValueError("Observation/performance days must be positive; gap cannot be negative")

    def calculate(self) -> dict:
        observation_end = self.reference_date
        observation_start = observation_end - timedelta(days=self.observation_days - 1)
        performance_start = observation_end + timedelta(days=self.gap_days + 1)
        performance_end = performance_start + timedelta(days=self.performance_days - 1)
        return {
            "observation_start": observation_start.isoformat(),
            "observation_end": observation_end.isoformat(),
            "performance_start": performance_start.isoformat(),
            "performance_end": performance_end.isoformat()
        }

def main() -> None:
    parser = argparse.ArgumentParser(description="Calculate target observation and performance windows.")
    parser.add_argument("--reference-date", required=True, help="YYYY-MM-DD")
    parser.add_argument("--observation-days", required=True, type=int)
    parser.add_argument("--gap-days", default=0, type=int)
    parser.add_argument("--performance-days", required=True, type=int)
    parser.add_argument("--output", type=Path, help="Optional UTF-8 JSON output")
    args = parser.parse_args()

    try:
        window = TargetWindow(date.fromisoformat(args.reference_date), args.observation_days, args.gap_days, args.performance_days)
        result = window.calculate()
    except (ValueError, OverflowError) as exc:
        parser.error(str(exc))
    rendered = json.dumps(result, indent=2)
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered)

if __name__ == "__main__":
    main()
