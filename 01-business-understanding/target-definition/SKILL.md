---
name: target-definition
description: Define and validate the target variable for a supervised machine learning problem.
version: 0.1.0
category: business-understanding
language: pt-BR
---

# Purpose

Definir de forma operacional, temporal e reproduzível a variável target de um problema supervisionado.

# When to use

- Após o enquadramento inicial do problema.
- Antes da construção da base analítica.
- Quando existirem diferentes interpretações para o evento positivo.
- Quando houver risco de censura, atraso de informação ou ambiguidade no label.

# Inputs

- Objetivo de negócio.
- Unidade de análise.
- Evento positivo esperado.
- Momento da previsão.
- Janela de observação.
- Janela de performance ou resposta.
- Fontes de dados utilizadas para construir o label.

# Process

1. Definir exatamente o que representa o target positivo e negativo.
2. Definir a granularidade do label.
3. Definir o instante de referência da previsão.
4. Separar janela de observação, gap temporal e janela de performance.
5. Mapear casos ambíguos, censurados ou ainda não maduros.
6. Avaliar disponibilidade e atraso das fontes utilizadas no label.
7. Verificar se o target pode ser reproduzido historicamente.
8. Avaliar possíveis proxies e riscos de circularidade.
9. Documentar regras de exclusão, elegibilidade e tratamento de exceções.
10. Propor testes de qualidade e estabilidade do label.

# Output contract

A resposta final deve ser estruturada com as seguintes seções:

- `Target Name`
- `Business Definition`
- `Positive Class`
- `Negative Class`
- `Unit of Analysis`
- `Reference Date`
- `Observation Window`
- `Gap Window`
- `Performance Window`
- `Eligibility Rules`
- `Exclusion Rules`
- `Ambiguous Cases`
- `Censoring Rules`
- `Data Sources`
- `Data Availability`
- `Label Quality Tests`
- `Risks and Limitations`

Quando uma informação não estiver disponível:

1. declare explicitamente a lacuna;
2. registre uma premissa temporária quando for seguro;
3. não invente regras de negócio;
4. destaque o impacto da incerteza na recomendação.

# Common mistakes

- Definir target apenas como o nome de uma coluna.
- Usar informações posteriores ao momento da previsão.
- Ignorar casos ainda não maduros.
- Misturar eventos com granularidades diferentes.
- Não documentar regras de elegibilidade.
- Criar um target que não possa ser reproduzido historicamente.

# Quality checklist

- [ ] Classe positiva e negativa estão definidas.
- [ ] A granularidade está explícita.
- [ ] A data de referência está definida.
- [ ] As janelas temporais estão separadas.
- [ ] Casos censurados foram tratados.
- [ ] Regras de elegibilidade estão documentadas.
- [ ] A disponibilidade histórica das fontes foi validada.
- [ ] O label pode ser reproduzido.
- [ ] Testes de qualidade foram definidos.

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
Use a skill `target-definition` para estruturar esta solicitação:

[descreva aqui o problema ou contexto]
```
