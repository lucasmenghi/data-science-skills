# Repository Structure

## Root Files

```
data-science-skills/
├── README.md               # Project overview and documentation
├── QUICKSTART.md           # Quick start guide
├── STRUCTURE.md            # Repository architecture
├── CLAUDE.md               # Claude Code instructions
├── AGENTS.md               # Genie Code instructions
├── validate_skills.py      # Skill validation utility
├── LICENSE
└── .gitignore
```

---

# Repository Architecture

The repository is organized into independent categories representing the complete Data Science lifecycle.

Each category contains reusable skills that can be executed individually or combined into larger workflows.

```
data-science-skills/

├── 01-business-understanding/
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

---

# Skill Structure

Every skill follows the same architecture.

```
<category>/<skill-name>/

├── SKILL.md
├── assets/
├── references/
├── scripts/
└── examples/
```

## SKILL.md

Behavioral instructions.

Contains:

- Purpose
- When to use
- Inputs
- Process
- Output contract
- Common mistakes
- Quality checklist
- Tool usage
- Boundaries
- Example invocation

---

## assets/

Reusable templates.

Examples

```
Executive Summary

Problem Framing

Model Card

Business Report

Markdown Template

YAML Template
```

---

## references/

Methodological knowledge.

Examples

```
CRISP-DM

MLflow

Business Rules

Target Leakage

Metric Definitions

Best Practices

Domain Documentation
```

---

## scripts/

Deterministic utilities.

Examples

```
Validation scripts

Metric calculators

Temporal window calculators

Quality validators

Feature generators
```

---

## examples/

Real-world examples demonstrating the expected usage.

Examples

```
Churn

Credit Risk

Fraud Detection

Customer Lifetime Value

Demand Forecasting
```

---

# Categories

## 01 — Business Understanding

Current Status: ✅

| Skill | Scripts | References | Assets | Examples |
|-------|:-------:|:----------:|:------:|:---------:|
| problem-framing | ✓ | ✓ | ✓ | ✓ |
| target-definition | ✓ | ✓ | ✓ | ✓ |
| business-hypothesis-builder | ✓ | ✓ | ✓ | ✓ |
| success-criteria-definition | ✓ | ✓ | ✓ | ✓ |

---

## 02 — Data Discovery

Current Status: 🚧

Planned Skills

- dataset-profiler
- schema-mapper
- granularity-check
- data-quality-audit
- relationship-mapper
- exploratory-analysis

---

## 03 — Data Preparation

Current Status: 🚧

Planned Skills

- missing-value-strategy
- outlier-investigation
- leakage-check
- temporal-validation
- feature-ready-validation

---

## 04 — Feature Engineering

Current Status: 🚧

Planned Skills

- feature-brainstorm
- feature-selection
- categorical-encoding
- temporal-features
- aggregation-features
- interaction-features

---

## 05 — Model Development

Current Status: 🚧

Planned Skills

- algorithm-selection
- baseline-builder
- hyperparameter-planner
- imbalance-strategy
- cross-validation-planner

---

## 06 — Model Validation

Current Status: 🚧

Planned Skills

- metric-selection
- threshold-optimization
- lift-analysis
- calibration-analysis
- oot-validation
- model-review

---

## 07 — Model Interpretability

Current Status: 🚧

Planned Skills

- feature-importance
- shap-analysis
- partial-dependence
- business-translation

---

## 08 — Experimentation

Current Status: 🚧

Planned Skills

- ab-test-design
- uplift-analysis
- causal-thinking
- experiment-review

---

## 09 — Deployment

Current Status: 🚧

Planned Skills

- mlflow-registration
- model-versioning
- serving-readiness
- deployment-checklist

---

## 10 — Monitoring

Current Status: 🚧

Planned Skills

- data-drift
- concept-drift
- performance-monitoring
- retraining-advisor

---

## 11 — Business Impact

Current Status: 🚧

Planned Skills

- financial-impact
- roi-estimation
- campaign-simulator
- prioritization

---

## 12 — Documentation

Current Status: 🚧

Planned Skills

- model-card
- technical-report
- executive-summary
- readme-generator

---

## 13 — AI Assistants

Current Status: 🚧

Planned Skills

- eda-assistant
- feature-engineering-assistant
- ml-reviewer
- business-translator

---

# Skill Lifecycle

Every skill should evolve following the same maturity model.

```
Draft

↓

Validated

↓

Production Ready

↓

Versioned

↓

Maintained
```

---

# Repository Statistics

| Metric | Value |
|---------|------:|
| Categories | 13 |
| Implemented Skills | 4 |
| Planned Skills | 50+ |
| Supported AI Assistants | Claude Code, Genie Code |
| Repository Type | Knowledge Framework |

---

# Future Architecture

As the project evolves, skills will become reusable building blocks for larger workflows.

```
Tool
      ↓

Skill
      ↓

Workflow
      ↓

AI Agent
```

This repository currently focuses on the **Skill layer**, which represents the reusable knowledge foundation for future AI-powered Data Science workflows and autonomous agents.

---

# Adding Company Knowledge

Company-specific documentation should never modify `SKILL.md`.

Instead, extend the repository through the `references/` folder.

Example

```
problem-framing/

├── SKILL.md

└── references/

    ├── company-business-rules.md

    ├── metric-definitions.md

    ├── churn-definition.md

    ├── segmentation-rules.md

    └── campaign-process.md
```

This keeps the core skills generic while allowing organization-specific knowledge to be injected dynamically.