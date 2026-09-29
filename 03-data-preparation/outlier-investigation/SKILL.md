---
name: outlier-investigation
description: Investigar valores extremos antes de decidir corrigir, limitar, transformar ou preservar.
metadata:
  version: "0.2.0"
  category: data-preparation
  language: pt-BR
---

# Purpose

Investigar valores extremos antes de decidir corrigir, limitar, transformar ou preservar.

# When to use

Quando a tarefa requer esta decisão dentro de preparação de dados. Trabalhar no escopo solicitado e entregar resultado utilizável; não transformar uma demanda de trabalho em sabatina. No modo explicativo, mostrar o porquê das escolhas junto do resultado.

# Inputs

Unidades; regras de domínio; distribuição por grupos/tempo; origem e modelo de destino.

Usar o contexto já fornecido. Se faltar dado que altera materialmente a decisão, perguntar de forma focada; continuar a análise independente com premissas marcadas. Sem dados acessíveis, entregar desenho e verificações propostas, nunca resultados simulados como observados.

# Process

1. Localizar extremos por quantis e métodos robustos, complementados por regras de domínio. Separar univariado de combinações anômalas.
2. Rastrear fonte, unidade, duplicação, erro de sinal e processamento. Distinguir falha confirmada de evento raro legítimo.
3. Comparar manter, transformar, modelo robusto, cap ou exclusão pelo custo do erro e objetivo. Não escolher só pela aparência da distribuição.
4. Ajustar limites aprendidos apenas no treino e versionar regras. Avaliar sensibilidade das métricas e cobertura de casos raros.
5. Entregar decisão por causa e segmento, com exemplos preservados e teste de invariantes antes/depois.
6. Explicar ao usuário a decisão, a alternativa descartada e a evidência que mudaria a recomendação. Registrar o que foi executado, o que é hipótese e o próximo passo verificável.

Consultar [critérios e trade-offs](references/decision-guide.md) para comparar alternativas e [caso trabalhado](examples/worked-case.md) para a profundidade esperada. Ler somente o apoio relevante, não todo o catálogo.

# Output contract

Inventário de extremos; causas; alternativas; análise de sensibilidade; regras versionadas.

Organizar a resposta em `Decisão recomendada`, `Evidências e execução`, `Alternativas e critérios`, `Limitações` e `Próximo passo`. Adaptar o tamanho à tarefa. Para cada achado relevante, explicar o significado e a consequência prática; anexar consultas/código ou localização de evidências quando houver. Números devem trazer unidade, população e período. Não esconder pendências em uma conclusão definitiva.

# Common mistakes

Z-score automático em distribuição muito assimétrica; remover anomalias do conjunto de detecção de anomalia.

Anomalia é relativa à referência e não sinônimo de erro, fraude ou evento causal. Contexto e custo orientam o tratamento.

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

"Use $outlier-investigation no meu projeto. Explique os critérios de decisão, proponha ou execute as verificações possíveis e separe resultados de premissas."

## Apoio transversal

Para decisões que exigem justificativa estatística ou operacional, consultar o trecho relevante do [aprofundamento metodológico](../../guides/method-depth.md). Para organizar evidências e comunicar a recomendação, usar o [protocolo de decisão](../../guides/decision-protocol.md). Não carregar ambos por obrigação em tarefas simples.
