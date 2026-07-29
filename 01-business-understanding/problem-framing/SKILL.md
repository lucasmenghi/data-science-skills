---
name: problem-framing
description: Transform a vague business request into a structured data science problem.
version: 0.1.0
category: business-understanding
language: pt-BR
---

# Purpose

Transformar uma necessidade de negócio ainda vaga em uma definição estruturada e acionável de problema de Data Science.

# When to use

- No início de um novo projeto de Data Science.
- Quando a solicitação do stakeholder estiver ampla, ambígua ou orientada diretamente a uma solução.
- Quando ainda não estiver claro qual decisão será apoiada pelo modelo.
- Antes de definir target, população, horizonte temporal ou métricas técnicas.

# Inputs

- Descrição inicial do problema ou oportunidade.
- Stakeholders envolvidos.
- Decisão ou ação que o resultado deverá apoiar.
- Processo de negócio relacionado.
- Restrições conhecidas de prazo, custo, dados, compliance ou operação.

# Process

1. Reformular a solicitação em linguagem de negócio, evitando assumir que Machine Learning é necessariamente a solução.
2. Identificar a decisão que deverá ser tomada com base na análise ou modelo.
3. Definir a unidade de análise e a população potencialmente afetada.
4. Identificar o evento, comportamento ou resultado que se deseja prever, estimar, recomendar ou otimizar.
5. Definir o momento da decisão e o horizonte temporal relevante.
6. Mapear ações possíveis após a geração do resultado.
7. Definir critérios de sucesso de negócio e critérios mínimos de viabilidade.
8. Registrar riscos, dependências, premissas e perguntas ainda abertas.
9. Recomendar o tipo de problema analítico mais aderente: classificação, regressão, ranking, clusterização, previsão temporal, causalidade, otimização ou análise descritiva.

# Output contract

A resposta final deve ser estruturada com as seguintes seções:

- `Executive Context`
- `Business Objective`
- `Decision to Support`
- `Unit of Analysis`
- `Population`
- `Analytical Problem`
- `Prediction or Decision Moment`
- `Time Horizon`
- `Available Actions`
- `Business Success Criteria`
- `Constraints`
- `Risks`
- `Assumptions`
- `Open Questions`
- `Recommended Analytical Approach`

Quando uma informação não estiver disponível:

1. declare explicitamente a lacuna;
2. registre uma premissa temporária quando for seguro;
3. não invente regras de negócio;
4. destaque o impacto da incerteza na recomendação.

# Common mistakes

- Começar escolhendo algoritmo antes de entender a decisão de negócio.
- Confundir o objetivo empresarial com a métrica técnica do modelo.
- Assumir que todo problema precisa de Machine Learning.
- Não identificar quem utilizará o resultado e qual ação será tomada.
- Definir o problema sem considerar horizonte temporal ou momento da previsão.
- Ignorar restrições operacionais, regulatórias ou de capacidade.

# Quality checklist

- [ ] O objetivo de negócio está explícito.
- [ ] A decisão apoiada está definida.
- [ ] A unidade de análise está identificada.
- [ ] A população está delimitada.
- [ ] O momento da decisão está definido.
- [ ] O horizonte temporal está definido.
- [ ] As ações possíveis estão documentadas.
- [ ] O sucesso de negócio está mensurável.
- [ ] Riscos e premissas estão registrados.
- [ ] A abordagem analítica recomendada está justificada.

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
Use a skill `problem-framing` para estruturar esta solicitação:

[descreva aqui o problema ou contexto]
```
