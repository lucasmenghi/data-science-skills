import argparse
import json
from pathlib import Path

REQUIRED_FIELDS = [
    "business_request",
    "stakeholders",
    "decision",
    "population",
    "prediction_moment",
    "time_horizon",
    "available_actions",
    "business_success"
]

def validate_context(data: dict) -> dict:
    missing = [field for field in REQUIRED_FIELDS if not data.get(field)]
    completeness = round((len(REQUIRED_FIELDS) - len(missing)) / len(REQUIRED_FIELDS), 2)
    return {
        "is_complete": len(missing) == 0,
        "completeness_score": completeness,
        "missing_fields": missing
    }

def main():
    parser = argparse.ArgumentParser(
        description="Validate the minimum context required for problem framing."
    )
    parser.add_argument("--input", required=True, help="Path to a JSON context file.")
    parser.add_argument("--output", help="Optional path for validation output.")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    with input_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    result = validate_context(data)
    rendered = json.dumps(result, ensure_ascii=False, indent=2)

    if args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
    else:
        print(rendered)

if __name__ == "__main__":
    main()
