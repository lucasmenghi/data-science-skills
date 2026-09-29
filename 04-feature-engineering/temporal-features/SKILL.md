---
name: temporal-features
description: Construir features temporais point-in-time com janelas, lags e disponibilidade reproduzíveis.
metadata:
  version: "0.2.0"
  category: feature-engineering
  language: pt-BR
---

# Purpose

Construir features temporais point-in-time com janelas, lags e disponibilidade reproduzíveis.

# When to use

Quando a tarefa requer esta decisão dentro de engenharia de features. Trabalhar no escopo solicitado e entregar resultado utilizável; não transformar uma demanda de trabalho em sabatina. No modo explicativo, mostrar o porquê das escolhas junto do resultado.

# Inputs

Entidade; reference_time; eventos; available_at; frequência; janelas e tarefa.

Usar o contexto já fornecido. Se faltar dado que altera materialmente a decisão, perguntar de forma focada; continuar a análise independente com premissas marcadas. Sem dados acessíveis, entregar desenho e verificações propostas, nunca resultados simulados como observados.

# Process

1. Especificar cutoff de cada previsão e bordas exatas da janela; distinguir evento, registro e disponibilidade da fonte.
2. Projetar lags, rolling, recência, tendência e sazonalidade que usem apenas passado disponível, incluindo regras para histórico curto.
3. Implementar joins as-of e desempates determinísticos; excluir o próprio evento quando a tarefa o exige e evitar janelas centradas.
4. Considerar atrasos, backfills, timezone, daylight saving quando aplicável e eventos fora de ordem.
5. Verificar manualmente exemplos nas bordas e paridade offline/serving; comparar janelas pela validação definida.
6. Explicar ao usuário a decisão, a alternativa descartada e a evidência que mudaria a recomendação. Registrar o que foi executado, o que é hipótese e o próximo passo verificável.

Consultar [critérios e trade-offs](references/decision-guide.md) para comparar alternativas e [caso trabalhado](examples/worked-case.md) para a profundidade esperada. Ler somente o apoio relevante, não todo o catálogo.

# Output contract

Especificação de features; SQL/Python; casos de borda; contrato de disponibilidade.

Organizar a resposta em `Decisão recomendada`, `Evidências e execução`, `Alternativas e critérios`, `Limitações` e `Próximo passo`. Adaptar o tamanho à tarefa. Para cada achado relevante, explicar o significado e a consequência prática; anexar consultas/código ou localização de evidências quando houver. Números devem trazer unidade, população e período. Não esconder pendências em uma conclusão definitiva.

# Common mistakes

Rolling inclui linha-alvo; usar total do mês ainda não fechado.

Reusar cálculo temporal exige preservar a convenção de borda; pequenas diferenças entre engines mudam o significado da feature.

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

"Use $temporal-features no meu projeto. Explique os critérios de decisão, proponha ou execute as verificações possíveis e separe resultados de premissas."

## Apoio transversal

Para decisões que exigem justificativa estatística ou operacional, consultar o trecho relevante do [aprofundamento metodológico](../../guides/method-depth.md). Para organizar evidências e comunicar a recomendação, usar o [protocolo de decisão](../../guides/decision-protocol.md). Não carregar ambos por obrigação em tarefas simples.

## Exemplo SQL

Consultar [join point-in-time](../../examples/sql/point-in-time.sql) para distinguir tempo do evento e disponibilidade. O exemplo exige cobertura completa da fonte para representar ausência como zero; adaptar schema e dialeto antes de executar.
