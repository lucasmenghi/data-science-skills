# AGENTS.md

Repository instructions for Genie Code and other compatible coding agents.

## Repository purpose

`data-science-skills` is a modular library of reusable Data Science skills for AI assistants. Skills encode repeatable Data Science methods as Markdown instructions and may include deterministic Python utilities, methodological references, reusable assets, and synthetic examples.

This repository is a methodology and reference library, not a deployable application.

## Current scope

The planned lifecycle contains 13 categories:

1. `01-business-understanding`
2. `02-data-discovery`
3. `03-data-preparation`
4. `04-feature-engineering`
5. `05-model-development`
6. `06-model-validation`
7. `07-model-interpretability`
8. `08-experimentation`
9. `09-deployment`
10. `10-monitoring`
11. `11-business-impact`
12. `12-documentation`
13. `13-ai-assistants`

Only `01-business-understanding` is currently implemented. Do not claim planned categories or skills already exist.

## Implemented Business Understanding skills

- `problem-framing`
- `target-definition`
- `business-hypothesis-builder`
- `success-criteria-definition`

Recommended sequence:

```text
problem-framing
→ target-definition
→ business-hypothesis-builder
→ success-criteria-definition
```

Skills must also work independently.

## Skill package contract

```text
<NN-category>/<skill-name>/
├── SKILL.md
├── assets/
├── references/
├── scripts/
└── examples/
```

- `SKILL.md` is mandatory.
- Supporting directories are optional in principle, but existing skills use all four.
- Do not create filler files merely to satisfy the structure.

## Required SKILL.md structure

Frontmatter:

```yaml
---
name: skill-name
description: Clear one-line description.
version: 0.1.0
category: category-name
language: pt-BR
---
```

Required sections:

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

Rules:

- Keep one clear responsibility per skill.
- Make skills reusable and independently callable.
- Use numbered process steps.
- Define stable output sections or schemas.
- Explicitly identify missing context and assumptions.
- Never invent business rules.
- Include realistic failure modes and a verifiable checklist.
- State what the skill must not do.

## Business Understanding rules

When working in `01-business-understanding`:

- start with the business objective, decision, and available action;
- do not assume Machine Learning is required;
- distinguish business success from model performance;
- define population and unit of analysis;
- define prediction or decision time;
- separate observation, gap, and performance windows;
- account for censored or immature outcomes;
- distinguish predictive and causal hypotheses;
- document operational capacity, privacy, governance, compliance, and fairness constraints;
- require stakeholder validation for unresolved definitions.

## File responsibilities

### assets

Use for reusable output templates, blank schemas, and checklists.

- Use `[REQUIRED]` and `[OPTIONAL]` placeholders in blank Markdown templates.
- Keep assets neutral and reusable.
- Ensure JSON and YAML assets are valid.

### references

Use for stable methods, definitions, decision rules, glossaries, and anti-patterns.

- Avoid project-specific or company-specific facts.
- Do not present arbitrary thresholds as universal standards.
- Clearly separate correlation, prediction, and causality.

### scripts

Use only for deterministic calculations or validation.

- Python 3.11 compatible.
- Use `argparse`, type hints, clear validation, and explicit UTF-8 file handling.
- Separate reusable functions from `main()`.
- Prefer stdlib, `pandas`, and `numpy` in the initial version.
- Never include credentials, production paths, catalog names, or internal identifiers.
- Add `--output` when reusable machine-readable output is useful.

### examples

Use realistic synthetic or anonymized scenarios.

- Demonstrate expected structure and depth.
- Do not contain real customer data or confidential business rules.
- Examples do not override the skill contract.

## Naming

- Categories: `NN-category-name/`.
- Skill directories: `kebab-case`.
- Python: `snake_case.py`.
- Frontmatter `name` must match the skill directory.
- Frontmatter `category` must match the category directory without its numeric prefix.
- Use English for paths, identifiers, and frontmatter keys.
- Skill content may be written in Brazilian Portuguese.

## Agent workflow

Before changing a skill:

1. Read this file and `CLAUDE.md`.
2. Read the category `README.md` and `manifest.json`.
3. Inspect an existing skill in the same category.
4. Make the smallest focused change that satisfies the request.
5. Avoid editing unrelated skills.

After changing a skill:

1. Update examples and supporting files when needed.
2. Update category README and manifest if inventory changed.
3. Run `python validate_skills.py`.
4. Run smoke tests for modified scripts.
5. Report changed files, test results, and unresolved limitations.

## Validation expectations

The repository validator should verify:

- required `SKILL.md` files;
- valid frontmatter and required keys;
- directory/frontmatter name consistency;
- mandatory sections;
- numbered process steps;
- checklist syntax;
- Python compilation;
- parseable JSON/YAML assets;
- valid category manifests.

Do not state that validation passed unless the command was actually executed.

## Databricks and Genie Code guidance

- Prefer Spark SQL or PySpark only when the task actually targets Databricks-scale data.
- Do not rewrite small standard-library utilities into Spark unnecessarily.
- When creating Databricks examples, use generic catalogs, schemas, tables, and volumes.
- Do not assume access to Unity Catalog objects that are not visible in the current context.
- Do not fabricate table schemas or column definitions.
- Ask for or clearly mark missing table context before generating production SQL.
- Prefer explicit column selection over `SELECT *` in production examples.
- Avoid collecting large Spark DataFrames to the driver.
- Make temporal joins, reference dates, and leakage risks explicit.
- Treat generated code as unexecuted until it has been reviewed and run.

## Governance and safety

- Never expose secrets, credentials, personal data, or confidential metadata.
- Use synthetic or anonymized examples.
- Preserve access controls and human approvals.
- Surface privacy, fairness, regulatory, explainability, and operational risks when relevant.
- Do not present an AI-generated business definition as approved by a stakeholder.

## Definition of done

A change is complete only when:

- the skill remains focused and independent;
- the full `SKILL.md` contract is respected;
- supporting files have a clear purpose;
- examples are safe and realistic;
- category documentation is current;
- scripts pass relevant smoke tests;
- validation passes or failures are explicitly reported.
