"""Validate category contracts, manifests, links and generated Codex entries."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote

try:
    import yaml
except ImportError:
    raise SystemExit("Install validation dependency: python -m pip install -r requirements-dev.txt")

from scripts.build_codex_entries import build_entries

SECTIONS = (
    "Purpose", "When to use", "Inputs", "Process", "Output contract",
    "Common mistakes", "Quality checklist", "Tool usage", "Boundaries", "Example invocation",
)


def validate(root: Path) -> list[str]:
    """Return actionable errors; do not import or execute repository utilities."""
    errors: list[str] = []
    categories = sorted(p for p in root.iterdir() if p.is_dir() and re.fullmatch(r"\d{2}-.+", p.name))
    if not categories:
        return ["No implemented categories found"]
    for category in categories:
        try:
            manifest = json.loads((category / "manifest.json").read_text(encoding="utf-8"))
            names = manifest["skills"]
            if not isinstance(names, list) or not names or any(not isinstance(n, str) for n in names):
                raise ValueError("skills must be a nonempty list of names")
            if len(names) != len(set(names)):
                raise ValueError("duplicate skill names")
            if any(not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", n) for n in names):
                raise ValueError("invalid skill name")
            if manifest.get("category") != category.name:
                raise ValueError("manifest category does not match directory")
            if not set(manifest.get("recommended_sequence", [])).issubset(names):
                raise ValueError("recommended_sequence includes unknown skill")
        except (OSError, ValueError, KeyError, TypeError) as exc:
            errors.append(f"{category.name}/manifest.json: {exc}")
            continue
        actual = {p.name for p in category.iterdir() if p.is_dir() and not p.name.startswith(".")}
        if actual != set(names):
            errors.append(f"{category.name}: manifest/directory mismatch {sorted(actual ^ set(names))}")
        if not (category / "README.md").is_file():
            errors.append(f"{category.name}: missing README.md")
        for name in names:
            path = category / name / "SKILL.md"
            try:
                content = path.read_text(encoding="utf-8")
                match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", content, re.DOTALL)
                if not match:
                    raise ValueError("missing YAML frontmatter")
                front = yaml.safe_load(match.group(1))
                if not isinstance(front, dict):
                    raise ValueError("frontmatter must be a mapping")
                metadata = front.get("metadata", {})
                if not isinstance(metadata, dict):
                    raise ValueError("metadata must be a mapping")
                fields = {**metadata, **front}
                for key in ("name", "description", "version", "category", "language"):
                    if not isinstance(fields.get(key), str) or not fields[key].strip():
                        errors.append(f"{path.relative_to(root)}: invalid or missing {key}")
                if fields.get("name") != name or fields.get("category") != category.name[3:]:
                    errors.append(f"{path.relative_to(root)}: name/category mismatch")
                body = content[match.end():]
                for heading in SECTIONS:
                    if not re.search(rf"^# {re.escape(heading)}\s*$", body, re.MULTILINE):
                        errors.append(f"{path.relative_to(root)}: missing section {heading}")
                process = re.search(r"^# Process\s*$(.*?)(?=^# |\Z)", body, re.MULTILINE | re.DOTALL)
                checklist = re.search(r"^# Quality checklist\s*$(.*?)(?=^# |\Z)", body, re.MULTILINE | re.DOTALL)
                if not process or not re.search(r"^\d+\. ", process.group(1), re.MULTILINE):
                    errors.append(f"{path.relative_to(root)}: Process needs numbered steps")
                if not checklist or not re.search(r"^- \[[ xX]\] ", checklist.group(1), re.MULTILINE):
                    errors.append(f"{path.relative_to(root)}: Quality checklist needs checkboxes")
            except (OSError, ValueError, yaml.YAMLError) as exc:
                errors.append(f"{path.relative_to(root)}: {exc}")
    # Restrict traversal to maintained public artifacts; never parse personal study notes.
    public_roots = categories + [root / "learning", root / "guides", root / "examples", root / "scripts", root / "tests", root / ".agents" / "skills"]
    files = list(root.glob("*.py"))
    for folder in public_roots:
        if folder.exists():
            files.extend(p for p in folder.rglob("*") if p.is_file() and "__pycache__" not in p.parts)
    files.extend(root.glob("*.md"))
    for path in files:
        try:
            if path.suffix == ".py":
                compile(path.read_text(encoding="utf-8"), str(path), "exec")
            elif path.suffix == ".json":
                json.loads(path.read_text(encoding="utf-8"))
            elif path.suffix in (".yaml", ".yml"):
                yaml.safe_load(path.read_text(encoding="utf-8"))
            elif path.suffix == ".md":
                for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
                    if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", link) or link.startswith("#"):
                        continue
                    target = unquote(link.split("#", 1)[0].split("?", 1)[0])
                    if target and not (path.parent / target).exists():
                        errors.append(f"{path.relative_to(root)}: broken local link {link}")
        except (OSError, ValueError, SyntaxError, yaml.YAMLError) as exc:
            errors.append(f"{path.relative_to(root)}: {exc}")
    if categories:
        try:
            stale = build_entries(root, check=True)
            if stale:
                errors.append(f"Missing/outdated Codex entries: {', '.join(stale)}")
        except (OSError, ValueError, KeyError, TypeError) as exc:
            errors.append(f"Codex entry check: {exc}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--output", type=Path, help="Write JSON validation report")
    args = parser.parse_args()
    if not args.root.is_dir():
        parser.error("--root must be an existing repository directory")
    errors = validate(args.root.resolve())
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps({"ok": not errors, "errors": errors}, ensure_ascii=False, indent=2), encoding="utf-8")
    print("\n".join(errors) if errors else "Validation passed: skills, manifests, assets, Python syntax, local links and Codex entries.")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
