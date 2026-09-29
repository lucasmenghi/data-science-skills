---
name: data-quality-audit
description: Auditar regras de qualidade por impacto, distinguindo falha técnica, exceção legítima e ausência de cobertura.
metadata:
  version: "0.2.0"
  category: data-discovery
  language: pt-BR
---

# Purpose

Auditar regras de qualidade por impacto, distinguindo falha técnica, exceção legítima e ausência de cobertura.

# When to use

Quando a tarefa requer esta decisão dentro de descoberta e diagnóstico de dados. Trabalhar no escopo solicitado e entregar resultado utilizável; não transformar uma demanda de trabalho em sabatina. No modo explicativo, mostrar o porquê das escolhas junto do resultado.

# Inputs

Contrato; dados; regras conhecidas; consumidores; frequência e criticidade.

Usar o contexto já fornecido. Se faltar dado que altera materialmente a decisão, perguntar de forma focada; continuar a análise independente com premissas marcadas. Sem dados acessíveis, entregar desenho e verificações propostas, nunca resultados simulados como observados.

# Process

1. Derivar regras de completude, validade, unicidade, integridade, atualidade e consistência do uso dos dados. Explicitar denominador e tolerância acordada.
2. Executar checks com contagem de violações, severidade e exemplos minimizados. Separar erro de origem, transformação e interpretação.
3. Verificar reconciliação entre camadas e tendências por partição para localizar quando a falha começou.
4. Definir quarentena, correção ou aceite de exceção com rastreabilidade. Não corrigir automaticamente valores que apenas parecem extremos.
5. Propor contrato executável e alertas acionáveis com dono, prazo e condição de retorno, distinguindo checks executados dos planejados.
6. Explicar ao usuário a decisão, a alternativa descartada e a evidência que mudaria a recomendação. Registrar o que foi executado, o que é hipótese e o próximo passo verificável.

Consultar [critérios e trade-offs](references/decision-guide.md) para comparar alternativas e [caso trabalhado](examples/worked-case.md) para a profundidade esperada. Ler somente o apoio relevante, não todo o catálogo.

# Output contract

Inventário de checks; evidência de falhas; impacto; plano de correção e prevenção.

Organizar a resposta em `Decisão recomendada`, `Evidências e execução`, `Alternativas e critérios`, `Limitações` e `Próximo passo`. Adaptar o tamanho à tarefa. Para cada achado relevante, explicar o significado e a consequência prática; anexar consultas/código ou localização de evidências quando houver. Números devem trazer unidade, população e período. Não esconder pendências em uma conclusão definitiva.

# Common mistakes

Métrica global sem segmentação; threshold de qualidade inventado; alterações destrutivas sem escopo.

A severidade depende do consumidor. Missing em uma feature opcional difere de chave de transação ausente; explicar essa diferença ao usuário.

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

"Use $data-quality-audit no meu projeto. Explique os critérios de decisão, proponha ou execute as verificações possíveis e separe resultados de premissas."

## Apoio transversal

Para decisões que exigem justificativa estatística ou operacional, consultar o trecho relevante do [aprofundamento metodológico](../../guides/method-depth.md). Para organizar evidências e comunicar a recomendação, usar o [protocolo de decisão](../../guides/decision-protocol.md). Não carregar ambos por obrigação em tarefas simples.
