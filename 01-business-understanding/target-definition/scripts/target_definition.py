import argparse
from dataclasses import dataclass
from datetime import date, timedelta

@dataclass
class TargetWindow:
    reference_date: date
    observation_days: int
    gap_days: int
    performance_days: int

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

def main():
    parser = argparse.ArgumentParser(description="Calculate target observation and performance windows.")
    parser.add_argument("--reference-date", required=True, help="YYYY-MM-DD")
    parser.add_argument("--observation-days", required=True, type=int)
    parser.add_argument("--gap-days", default=0, type=int)
    parser.add_argument("--performance-days", required=True, type=int)
    args = parser.parse_args()

    window = TargetWindow(
        reference_date=date.fromisoformat(args.reference_date),
        observation_days=args.observation_days,
        gap_days=args.gap_days,
        performance_days=args.performance_days
    )
    print(window.calculate())

if __name__ == "__main__":
    main()
