---
name: success-criteria-definition
description: Define business, analytical, technical and operational success criteria for a data science initiative.
version: 0.1.0
category: business-understanding
language: pt-BR
---

# Purpose

Estabelecer critérios claros para decidir se uma iniciativa de Data Science deve avançar, ser implantada e permanecer em produção.

# When to use

- Durante o planejamento do projeto.
- Antes do desenvolvimento do modelo.
- Antes de comparar alternativas analíticas.
- Antes de um piloto ou implantação.

# Inputs

- Objetivo de negócio.
- Decisão apoiada.
- Ações possíveis.
- Baseline atual.
- Custos, capacidade operacional e restrições.
- Métricas técnicas candidatas.

# Process

1. Separar sucesso de negócio, analítico, técnico e operacional.
2. Definir baseline e cenário de comparação.
3. Definir métricas primárias e métricas de proteção.
4. Definir critérios mínimos de aceitação e critérios desejáveis.
5. Relacionar métricas técnicas às consequências de negócio.
6. Incluir custos de falsos positivos, falsos negativos e ausência de ação.
7. Definir critérios de capacidade, latência, frequência e cobertura.
8. Definir critérios de fairness, compliance e explicabilidade quando aplicável.
9. Definir regras de go, revise e no-go.

# Output contract

A resposta final deve ser estruturada com as seguintes seções:

- `Business Success Metrics`
- `Analytical Success Metrics`
- `Technical Success Metrics`
- `Operational Success Metrics`
- `Baseline`
- `Minimum Acceptance Threshold`
- `Target Threshold`
- `Guardrail Metrics`
- `Cost of Errors`
- `Go Criteria`
- `Revise Criteria`
- `No-Go Criteria`
- `Measurement Plan`

Quando uma informação não estiver disponível:

1. declare explicitamente a lacuna;
2. registre uma premissa temporária quando for seguro;
3. não invente regras de negócio;
4. destaque o impacto da incerteza na recomendação.

# Common mistakes

- Usar somente ROC-AUC como critério de sucesso.
- Não comparar com o processo atual.
- Não definir custo dos erros.
- Ignorar capacidade operacional de agir sobre os scores.
- Definir metas sem plano de mensuração.
- Confundir desempenho offline com impacto real.

# Quality checklist

- [ ] Existe baseline.
- [ ] Métricas de negócio e técnicas estão separadas.
- [ ] Há limite mínimo de aceitação.
- [ ] Custos dos erros estão documentados.
- [ ] Capacidade operacional foi considerada.
- [ ] Guardrails estão definidos.
- [ ] Critérios de go, revise e no-go estão explícitos.
- [ ] Existe plano de mensuração.

# Tool usage

- Use os scripts da pasta `scripts/` apenas para validações determinísticas ou cálculos auxiliares.
- Use os arquivos em `references/` para interpretar conceitos, critérios e exemplos.
- Use os templates em `assets/` para produzir saídas consistentes.
- Não trate um template como regra de negócio definitiva.

# Boundaries

Esta skill não deve:

- treinar modelos;
- selecionar algoritmos de forma definitiva sem contexto;
- executar engenharia de features;
- substituir validação do stakeholder;
- assumir que Machine Learning é obrigatoriamente a melhor solução.

# Example invocation

```text
Use a skill `success-criteria-definition` para estruturar esta solicitação:

[descreva aqui o problema ou contexto]
```
