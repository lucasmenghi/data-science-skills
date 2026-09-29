# Estrutura implementada

```text
data-science-skills/
├── AGENTS.md / CLAUDE.md       # Instruções para manutenção e estudo
├── README.md
├── requirements-dev.txt       # PyYAML para validação
├── validate_skills.py
├── .agents/skills/            # 7 entradas geradas para descoberta no Codex
├── 01-business-understanding/ # 4 skills existentes, preservadas
├── 13-ai-assistants/          # 7 agentes instrucionais de aprendizagem
├── learning/                  # Trilha, rubrica, fontes, perguntas e casos
│   └── templates/             # Estado inicial e registro de sessão
├── scripts/                   # Geração determinística das entradas
├── tests/                     # Validação e proteção contra sobrescrita
└── private/                   # Apenas local; ignorada pelo Git
```

## Contrato de skill

Cada skill canônica fica em `<NN-category>/<skill-name>/SKILL.md`, com nome, descrição e metadados. As novas skills usam `metadata` para versão, categoria e idioma, mantendo compatibilidade com o formato Agent Skills. O validador aceita também os campos legados no topo.

As seções obrigatórias estão em [AGENTS.md](AGENTS.md). Pastas `assets/`, `references/`, `scripts/` e `examples/` são opcionais; não criar arquivos sem função. Os agentes compartilham os recursos de `learning/` por links explícitos, sem duplicar conteúdo.

## Inventário

- `01-business-understanding`: problem-framing, target-definition, business-hypothesis-builder, success-criteria-definition.
- `13-ai-assistants`: ds-mentor, ds-foundations, ds-modeling, ds-ai, ds-reviewer, ds-interviewer, ds-storytelling.

Total: 2 categorias implementadas, 11 skills canônicas e 7 entradas de descoberta. As entradas não são skills adicionais com novas responsabilidades.

## Roadmap

Continuam planejadas: 02-data-discovery, 03-data-preparation, 04-feature-engineering, 05-model-development, 06-model-validation, 07-model-interpretability, 08-experimentation, 09-deployment, 10-monitoring, 11-business-impact e 12-documentation.

O agente de modelagem ensina esses assuntos; isso não implementa automaticamente cada categoria da biblioteca. Não declarar pastas planejadas como existentes.
