---
name: algorithm-selection
description: Escolher famílias de modelos por tarefa, dados, restrições e protocolo de comparação.
metadata:
  version: "0.2.0"
  category: model-development
  language: pt-BR
---

# Purpose

Escolher famílias de modelos por tarefa, dados, restrições e protocolo de comparação.

# When to use

Quando a tarefa requer esta decisão dentro de desenvolvimento de modelos. Trabalhar no escopo solicitado e entregar resultado utilizável; não transformar uma demanda de trabalho em sabatina. No modo explicativo, mostrar o porquê das escolhas junto do resultado.

# Inputs

Objetivo; modalidade; tamanho/estrutura; rótulos; baseline; latência, custo e explicabilidade.

Usar o contexto já fornecido. Se faltar dado que altera materialmente a decisão, perguntar de forma focada; continuar a análise independente com premissas marcadas. Sem dados acessíveis, entregar desenho e verificações propostas, nunca resultados simulados como observados.

# Process

1. Classificar tarefa e saída: regressão, classificação, ranking, agrupamento, forecasting ou outra. Confirmar se há rótulo e decisão acionável.
2. Relacionar tamanho, sparsity, cardinalidade, relações não lineares, dependência temporal e escala às famílias candidatas.
3. Selecionar baseline e poucas alternativas com hipóteses de ganho distintas; comparar custo de treino, inferência e manutenção.
4. Fixar mesmo split, métrica, orçamento e preparação apropriada por família. Evitar favorecer um modelo com mais tuning ou acesso a dados.
5. Usar resultados e incerteza para escolher; documentar quando interpretação, latência ou estabilidade justificam perder pequena performance pontual.
6. Explicar ao usuário a decisão, a alternativa descartada e a evidência que mudaria a recomendação. Registrar o que foi executado, o que é hipótese e o próximo passo verificável.

Consultar [critérios e trade-offs](references/decision-guide.md) para comparar alternativas e [caso trabalhado](examples/worked-case.md) para a profundidade esperada. Ler somente o apoio relevante, não todo o catálogo.

# Output contract

Matriz de candidatos; hipóteses de ganho; protocolo justo; recomendação condicionada.

Organizar a resposta em `Decisão recomendada`, `Evidências e execução`, `Alternativas e critérios`, `Limitações` e `Próximo passo`. Adaptar o tamanho à tarefa. Para cada achado relevante, explicar o significado e a consequência prática; anexar consultas/código ou localização de evidências quando houver. Números devem trazer unidade, população e período. Não esconder pendências em uma conclusão definitiva.

# Common mistakes

Escolher algoritmo por popularidade; tratar todos os dados como iid; declarar vencedor sem comparação.

Selecionar algoritmo envolve capacidade e adequação, não rankings universais. A recomendação sem experimento é provisória.

# Quality checklist

- [ ] Entradas, unidade e população necessárias estão definidas ou marcadas como pendentes.
- [ ] A decisão segue os critérios específicos da referência e explicita a alternativa principal.
- [ ] Evidência observada, hipótese e execução proposta estão separadas.
- [ ] O caso-limite relevante foi verificado ou consta como limitação.
- [ ] O próximo passo tem condição de conclusão verificável.

# Tool usage

Preferir Python e SQL; usar [orientações de ambiente](../../guides/python-sql-databricks.md) para adaptar a Databricks/PySpark sem coletar grandes tabelas no driver. Inspecionar schema e versões reais antes de gerar código dependente de APIs. Consultar [fontes primárias](../../guides/sources.md) quando o método ou a API exigir verificação. Executar apenas dentro do escopo e acesso disponíveis; relatar comandos e resultados reais. Um exemplo sintético não comprova resultado no dataset do usuário.

# Boundaries

Não inventar regras, dados, resultados, significância ou aprovação. Não ampliar o pedido para mutações externas, publicação ou deployment sem autorização correspondente. Não usar exemplos como política obrigatória. Explicação descritiva/preditiva não estabelece causalidade.

# Example invocation

"Use $algorithm-selection no meu projeto. Explique os critérios de decisão, proponha ou execute as verificações possíveis e separe resultados de premissas."

## Apoio transversal

Para decisões que exigem justificativa estatística ou operacional, consultar o trecho relevante do [aprofundamento metodológico](../../guides/method-depth.md). Para organizar evidências e comunicar a recomendação, usar o [protocolo de decisão](../../guides/decision-protocol.md). Não carregar ambos por obrigação em tarefas simples.
