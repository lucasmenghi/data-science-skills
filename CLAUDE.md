# CLAUDE.md

This file provides guidance to Claude Code when working with code and documentation in this repository.

## What this repository is

`data-science-skills` is a modular library of reusable Data Science skill definitions for AI coding assistants.

The repository is organized around the complete Data Science lifecycle, from business understanding to monitoring, business impact, documentation, and future AI assistants.

Skills are Markdown-based instruction packages. A skill may also include deterministic Python utilities, methodological references, reusable output templates, and realistic examples.

This is primarily a documentation, methodology, and reference library. It is not a deployable application and should not be treated as a single end-to-end framework.

## Current maturity

The target architecture contains 13 categories:

| # | Category | Status |
|---|---|---|
| 01 | business-understanding | Implemented |
| 02 | data-discovery | Planned |
| 03 | data-preparation | Planned |
| 04 | feature-engineering | Planned |
| 05 | model-development | Planned |
| 06 | model-validation | Planned |
| 07 | model-interpretability | Planned |
| 08 | experimentation | Planned |
| 09 | deployment | Planned |
| 10 | monitoring | Planned |
| 11 | business-impact | Planned |
| 12 | documentation | Planned |
| 13 | ai-assistants | Planned |

Do not invent missing categories or claim that planned skills already exist. When expanding the repository, preserve compatibility with the existing category and skill contracts.

## Current category organization

### 01-business-understanding

| Skill | Purpose |
|---|---|
| `problem-framing` | Transform a vague business request into a structured Data Science problem. |
| `target-definition` | Define a supervised-learning target in a temporal, operational, and reproducible way. |
| `business-hypothesis-builder` | Build and prioritize testable business hypotheses before modeling. |
| `success-criteria-definition` | Define business, analytical, technical, and operational success criteria. |

Recommended sequence:

```text
problem-framing
    ↓
target-definition
    ↓
business-hypothesis-builder
    ↓
success-criteria-definition
```

Each skill must remain independently usable. Do not create hidden dependencies between skills.

## Repository architecture

```text
data-science-skills/
├── CLAUDE.md
├── AGENTS.md
├── README.md
├── validate_skills.py
├── 01-business-understanding/
│   ├── README.md
│   ├── manifest.json
│   ├── problem-framing/
│   ├── target-definition/
│   ├── business-hypothesis-builder/
│   └── success-criteria-definition/
├── 02-data-discovery/
├── 03-data-preparation/
├── 04-feature-engineering/
├── 05-model-development/
├── 06-model-validation/
├── 07-model-interpretability/
├── 08-experimentation/
├── 09-deployment/
├── 10-monitoring/
├── 11-business-impact/
├── 12-documentation/
└── 13-ai-assistants/
```

Only create planned category directories when they contain at least one implemented skill or when explicitly requested.

## Skill structure

Every skill follows this structure:

```text
<NN-category>/<skill-name>/
├── SKILL.md          # Required: instructions and output contract
├── assets/           # Reusable output templates
├── references/       # Stable methodological guidance
├── scripts/          # Deterministic CLI utilities
└── examples/         # Realistic examples of usage and expected output
```

### Directory responsibilities

- `SKILL.md`: defines when and how the AI assistant should perform the task.
- `assets/`: provides reusable templates, schemas, checklists, or starter files.
- `references/`: stores stable concepts, definitions, frameworks, anti-patterns, and methodological guidance.
- `scripts/`: contains deterministic calculations or validations that should not be left to language-model reasoning.
- `examples/`: demonstrates realistic inputs, decisions, and expected outputs without becoming a hidden requirement.

Do not duplicate the same content across all four supporting directories. Each file should have a clear reason to exist.

## SKILL.md contract

Every `SKILL.md` must contain valid YAML frontmatter:

```yaml
---
name: skill-name
description: One-line description of what the skill does and when it is relevant.
version: 0.1.0
category: category-name
language: pt-BR
---
```

Every skill must contain these sections:

```markdown
# Purpose
# When to use
# Inputs
# Process
# Output contract
# Common mistakes
# Quality checklist
# Tool usage
# Boundaries
# Example invocation
```

### Skill design rules

- A skill should solve one clearly bounded problem.
- A skill must be reusable across projects and industries unless intentionally domain-specific.
- A skill must not silently depend on another skill.
- Inputs must describe the minimum context needed to produce a useful result.
- The process must use numbered, actionable steps.
- The output contract must define stable section names or a machine-readable schema.
- Missing information must be declared explicitly rather than invented.
- Assumptions must be visible and separated from confirmed facts.
- Common mistakes must describe realistic failure modes.
- The quality checklist must be verifiable.
- Boundaries must state what the skill should not do.

Do not create oversized skills that combine business framing, data preparation, modeling, validation, and communication in one file. Split them into focused skills.

## Business Understanding principles

Skills in `01-business-understanding` must:

- begin from the business objective, decision, and available action;
- avoid assuming that Machine Learning is necessarily the correct solution;
- distinguish business metrics from model metrics;
- identify the unit of analysis and eligible population;
- define the decision or prediction moment;
- treat observation, gap, and performance windows explicitly when relevant;
- document operational, regulatory, ethical, data, and capacity constraints;
- distinguish predictive hypotheses from causal hypotheses;
- connect technical evaluation to measurable business value;
- require stakeholder validation for unresolved business rules.

## Python utility scripts

Scripts are optional. Add a script only when it provides deterministic value.

### Conventions

- Use Python 3.11-compatible syntax.
- Use `argparse` for CLI interfaces.
- Use type hints for public functions.
- Separate core functions from `main()`.
- Validate file existence, required columns, argument ranges, and incompatible options.
- Return clear error messages.
- Use UTF-8 encoding explicitly for file I/O.
- Prefer standard library, `pandas`, and `numpy` for the initial repository version.
- Do not add a dependency merely to perform a trivial calculation.
- Never implement a statistical method manually when a future category explicitly permits a reliable established library; document the dependency decision instead.
- Scripts must not contain company-specific credentials, paths, catalogs, schemas, tokens, or production identifiers.

### Input and output

- Typical inputs: JSON, CSV, Parquet, or command-line values.
- Prefer an optional `--output` argument when a reusable artifact can be written.
- Console output should be human-readable.
- File output should be machine-readable where practical.
- Include a helpful `--help` description.

### Example

```bash
python 01-business-understanding/problem-framing/scripts/problem_framing.py \
  --input examples/problem_context.json
```

## Assets

- Markdown templates should use `[REQUIRED]` and `[OPTIONAL]` placeholders when distributed as blank templates.
- CSV assets must include stable headers and one blank or illustrative row.
- YAML and JSON assets must be valid and parseable.
- Do not place methodological explanations inside assets when they belong in `references/`.
- Keep templates neutral and reusable; examples belong in `examples/`.

## References

- References must contain stable methodological guidance rather than project-specific facts.
- Prefer concise definitions, decision rules, anti-patterns, and examples.
- Clearly distinguish prediction, association, and causality.
- Avoid presenting arbitrary thresholds as universal standards.
- Cite external sources in a future references bibliography when substantive external material is introduced.

## Examples

- Use realistic but synthetic or anonymized scenarios.
- Examples should illustrate reasoning, structure, and expected depth.
- Do not include confidential company names, table names, customer data, credentials, or internal business rules.
- An example must not override the corresponding skill's output contract.

## Naming conventions

- Category directories: `NN-category-name/`.
- Skill directories: `kebab-case`.
- Python files: `snake_case.py`.
- Markdown support files: `kebab-case.md` or `snake_case.md`; preserve the existing local convention within a skill.
- Skill `name` in YAML must exactly match its directory name.
- Category in YAML must match the category directory without the numeric prefix.
- Use English for directory names, file names, frontmatter keys, and code identifiers.
- Skill instructional content may be in Brazilian Portuguese while the repository remains internationally navigable.

## Validation

Run validation after adding or changing a skill:

```bash
python validate_skills.py
```

The validator should check at least:

- every skill directory contains `SKILL.md`;
- YAML frontmatter is parseable;
- `name`, `description`, `version`, `category`, and `language` exist;
- the YAML `name` matches the directory name;
- mandatory sections exist;
- `Process` contains numbered steps;
- `Quality checklist` contains checklist items;
- Python scripts compile successfully;
- JSON and YAML assets are parseable where applicable;
- category manifests reference only existing skills.

When the validator does not yet support one of these checks, improve the validator rather than claiming the repository is fully validated.

## Working rules for Claude Code

When asked to create or modify a skill:

1. Read this file, the category `README.md`, and `manifest.json`.
2. Inspect at least one existing skill in the same category.
3. Preserve the established skill contract and naming conventions.
4. Propose the smallest focused skill that satisfies the request.
5. Create supporting files only when they add real reusable value.
6. Add or update a realistic example.
7. Update the category manifest and README when the skill inventory changes.
8. Run validation and relevant script smoke tests.
9. Report exactly what changed and any validation limitations.

When reviewing a skill:

- verify scope and independence;
- inspect temporal correctness and potential leakage where relevant;
- check whether inputs are sufficient;
- check that outputs are usable and consistent;
- identify hidden assumptions;
- test scripts with valid and invalid inputs;
- avoid changing unrelated files.

## Safety, privacy, and governance

- Never add real credentials, access tokens, secrets, personal data, or confidential schemas.
- Use synthetic or anonymized examples.
- Do not create instructions that bypass governance, approvals, access controls, or human review.
- Treat model outputs as decision support unless the skill explicitly defines an approved automated decision process.
- Surface fairness, explainability, privacy, regulatory, and operational risks when relevant.
- Do not present generated business rules as stakeholder-approved facts.

## Definition of done

A new or modified skill is complete only when:

- its scope is clear and focused;
- `SKILL.md` follows the full contract;
- supporting files are purposeful;
- examples are synthetic or anonymized;
- manifests and category documentation are current;
- scripts pass smoke tests;
- repository validation passes, or failures are clearly documented;
- the final response summarizes changed files and unresolved limitations.

## Exemplar skills

For Business Understanding work, inspect in this order:

1. `01-business-understanding/problem-framing/`
2. `01-business-understanding/target-definition/`
3. `01-business-understanding/business-hypothesis-builder/`
4. `01-business-understanding/success-criteria-definition/`

Use `problem-framing` as the primary structural exemplar and `target-definition` as the primary temporal-reasoning exemplar.
