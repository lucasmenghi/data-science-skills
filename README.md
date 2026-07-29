# 🧠 Data Science Skills

> A modular library of reusable AI skills designed to standardize, accelerate and improve the entire Data Science lifecycle.

<p align="center">

![Status](https://img.shields.io/badge/status-under%20development-blue)
![Python](https://img.shields.io/badge/python-3.10+-3776AB?logo=python)
![License](https://img.shields.io/badge/license-MIT-success)
![AI](https://img.shields.io/badge/AI-Claude%20%7C%20Genie%20Code-orange)

</p>

---

## 🚀 Overview

**Data Science Skills** is an open framework that encapsulates best practices from modern Data Science into reusable, composable AI skills.

Instead of relying on isolated prompts, the project provides structured knowledge modules that guide AI assistants through every stage of a Data Science initiative — from business understanding to production monitoring.

Each skill follows a standardized architecture composed of:

- 📄 Behavioral instructions
- 📚 Reference materials
- 🧩 Output templates
- 🐍 Utility scripts
- 💡 Practical examples

The result is an extensible foundation for building consistent, high-quality AI-assisted Data Science workflows.

---

# 🎯 Vision

The goal is to transform AI from a code generator into a **Senior Data Scientist** capable of reasoning through an entire project.

Instead of asking:

> "Generate a Random Forest"

the assistant should be capable of understanding:

- What is the business problem?
- Is Machine Learning really necessary?
- What is the correct prediction moment?
- Is there target leakage?
- Which features make sense?
- Which metric reflects business success?
- Can this model actually be deployed?

---

# 🏗 Project Architecture

```
data-science-skills/

├── 01-business-understanding
├── 02-data-discovery
├── 03-data-preparation
├── 04-feature-engineering
├── 05-model-development
├── 06-model-validation
├── 07-model-interpretability
├── 08-experimentation
├── 09-deployment
├── 10-monitoring
├── 11-business-impact
├── 12-documentation
└── 13-ai-assistants
```

Each category contains independent and reusable skills.

---

# 📦 Skill Architecture

Every skill follows exactly the same structure.

```
skill-name/

├── SKILL.md
├── assets/
├── references/
├── scripts/
└── examples/
```

### SKILL.md

Defines:

- purpose
- when to use
- inputs
- reasoning process
- output contract
- quality checklist
- common mistakes
- boundaries

---

### assets/

Reusable templates.

Examples:

- Model Cards
- Executive Summaries
- Business Documents
- Markdown Reports

---

### references/

Methodological knowledge.

Examples:

- CRISP-DM
- Target Leakage
- SHAP
- MLflow
- Business Metrics
- Experiment Design

---

### scripts/

Deterministic utilities.

Examples:

- temporal window calculators
- validation scripts
- metric calculators
- quality validators

---

### examples/

Realistic examples demonstrating how the skill should be used.

---

# 🧩 Current Skills

## ✅ Business Understanding

- Problem Framing
- Target Definition
- Business Hypothesis Builder
- Success Criteria Definition

---

## 🚧 Planned

### Data Discovery

- Dataset Profiler
- Schema Mapper
- Granularity Check
- Data Quality Assessment

### Data Preparation

- Missing Value Strategy
- Leakage Detection
- Outlier Investigation
- Temporal Validation

### Feature Engineering

- Feature Brainstorm
- Feature Selection
- Encoding Advisor
- Time-based Features

### Model Development

- Algorithm Selection
- Baseline Builder
- Hyperparameter Planning
- Imbalanced Learning

### Model Validation

- Metric Selection
- Threshold Optimization
- Lift Analysis
- Out-of-Time Validation

### Model Interpretability

- SHAP Analysis
- Feature Importance
- Business Translation

### Experimentation

- A/B Test Design
- Uplift Analysis
- Causal Thinking

### Deployment

- MLflow Registration
- Model Versioning
- Serving Readiness

### Monitoring

- Data Drift
- Concept Drift
- Retraining Advisor

### Business Impact

- ROI Estimation
- Financial Simulation
- Executive Recommendations

### Documentation

- Model Card Generator
- Technical Report
- Executive Summary
- README Generator

---

# 🧠 Design Principles

Every skill is designed to be:

- Modular
- Reusable
- Independent
- Explainable
- Versionable
- Testable

Skills should solve **one problem exceptionally well**.

---

# 🔄 Example Workflow

```
Problem Framing
        │
        ▼
Target Definition
        │
        ▼
Business Hypothesis Builder
        │
        ▼
Dataset Profiler
        │
        ▼
Feature Engineering
        │
        ▼
Model Development
        │
        ▼
Validation
        │
        ▼
Business Impact
        │
        ▼
Documentation
```

---

# 🤖 AI Compatibility

The project is designed to work with multiple AI coding assistants.

| Assistant | Status |
|------------|--------|
| Claude Code | ✅ |
| Genie Code | ✅ |
| GitHub Copilot | 🚧 |
| Cursor | 🚧 |

---

# 🛣 Roadmap

- [x] Business Understanding
- [ ] Data Discovery
- [ ] Data Preparation
- [ ] Feature Engineering
- [ ] Model Development
- [ ] Model Validation
- [ ] Interpretability
- [ ] Experimentation
- [ ] Deployment
- [ ] Monitoring
- [ ] Business Impact
- [ ] Documentation
- [ ] AI Workflows

---

# 🤝 Contributing

Contributions are welcome.

Before submitting a new skill, ensure that:

- it solves a single responsibility;
- follows the repository architecture;
- includes examples;
- contains reusable assets;
- documents common mistakes;
- defines quality checks.

---

# 📄 License

MIT License.

---

# ⭐ Why this project?

Modern AI tools can generate code.

This project teaches them **how experienced Data Scientists think**.

Rather than replacing analytical reasoning, it aims to standardize and augment it through reusable knowledge modules.
