---
name: business-hypothesis-builder
description: Generate structured, testable business hypotheses before modeling.
version: 0.1.0
category: business-understanding
language: pt-BR
---

# Purpose

Converter conhecimento de negócio e sinais iniciais em hipóteses testáveis, priorizadas e conectadas a possíveis variáveis.

# When to use

- Antes da EDA aprofundada.
- Durante workshops com stakeholders.
- Quando for necessário orientar a busca por dados e features.
- Quando o projeto estiver excessivamente guiado apenas pelos dados disponíveis.

# Inputs

- Problema de negócio estruturado.
- Conhecimento dos stakeholders.
- Jornada ou processo relacionado.
- Possíveis causas já conhecidas.
- Fontes e domínios de dados disponíveis.

# Process

1. Identificar comportamentos, eventos, restrições e mecanismos que podem influenciar o resultado.
2. Transformar cada ideia em uma hipótese falsificável.
3. Relacionar a hipótese ao mecanismo causal ou comportamental esperado.
4. Definir sinais ou variáveis observáveis que poderiam sustentar ou refutar a hipótese.
5. Definir análise ou teste mínimo necessário.
6. Classificar a hipótese por impacto potencial, evidência disponível, esforço e risco.
7. Separar hipóteses preditivas de hipóteses causais.
8. Priorizar o backlog inicial de investigação.

# Output contract

A resposta final deve ser estruturada com as seguintes seções:

- `Hypothesis ID`
- `Business Hypothesis`
- `Expected Mechanism`
- `Observable Signals`
- `Candidate Data Sources`
- `Suggested Test`
- `Expected Direction`
- `Hypothesis Type`
- `Impact`
- `Evidence`
- `Effort`
- `Priority`
- `Risks`

Quando uma informação não estiver disponível:

1. declare explicitamente a lacuna;
2. registre uma premissa temporária quando for seguro;
3. não invente regras de negócio;
4. destaque o impacto da incerteza na recomendação.

# Common mistakes

- Criar hipóteses vagas que não podem ser testadas.
- Confundir correlação esperada com causalidade.
- Gerar hipóteses somente a partir das colunas já disponíveis.
- Ignorar conhecimento operacional dos stakeholders.
- Não priorizar as hipóteses.
- Usar a hipótese como confirmação de uma conclusão já desejada.

# Quality checklist

- [ ] Cada hipótese é testável.
- [ ] O mecanismo esperado está descrito.
- [ ] Existem sinais observáveis.
- [ ] O teste mínimo está definido.
- [ ] A direção esperada está registrada.
- [ ] Hipóteses causais e preditivas estão diferenciadas.
- [ ] Impacto, evidência e esforço foram avaliados.
- [ ] O backlog está priorizado.

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
Use a skill `business-hypothesis-builder` para estruturar esta solicitação:

[descreva aqui o problema ou contexto]
```
