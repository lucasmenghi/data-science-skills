---
name: business-hypothesis-builder
description: Formular e priorizar hipóteses descritivas, preditivas e causais com desenho de verificação adequado.
metadata:
  version: "0.2.0"
  category: business-understanding
  language: pt-BR
---

# Purpose

Formular e priorizar hipóteses descritivas, preditivas e causais com desenho de verificação adequado.

# When to use

Quando a tarefa requer esta decisão dentro de entendimento do negócio. Trabalhar no escopo solicitado e entregar resultado utilizável; não transformar uma demanda de trabalho em sabatina. No modo explicativo, mostrar o porquê das escolhas junto do resultado.

# Inputs

Problema; mecanismo proposto; evidência existente; variáveis disponíveis; esforço e possíveis ações.

Usar o contexto já fornecido. Se faltar dado que altera materialmente a decisão, perguntar de forma focada; continuar a análise independente com premissas marcadas. Sem dados acessíveis, entregar desenho e verificações propostas, nunca resultados simulados como observados.

# Process

1. Converter cada ideia em afirmação refutável com população, exposição ou tratamento, resultado, horizonte e comparação.
2. Classificar a hipótese como descritiva, preditiva ou causal. Especificar o estimando quando se quer efeito e explicitar confundidores plausíveis.
3. Propor teste de menor custo capaz de mudar uma decisão: análise exploratória, validação fora da amostra ou experimento conforme o tipo.
4. Definir sinais que refutam a hipótese e riscos de medição, seleção e causalidade reversa. Planejar multiplicidade se muitas hipóteses serão testadas.
5. Priorizar por valor de informação, evidência e esforço, discutindo sensibilidade dos pesos. Separar score de organização de evidência científica.
6. Explicar ao usuário a decisão, a alternativa descartada e a evidência que mudaria a recomendação. Registrar o que foi executado, o que é hipótese e o próximo passo verificável.

Consultar [critérios e trade-offs](references/decision-guide.md) para comparar alternativas e [caso trabalhado](examples/worked-case.md) para a profundidade esperada. Ler somente o apoio relevante, não todo o catálogo.

# Output contract

Backlog de hipóteses; tipo; desenho; evidência necessária; prioridade e critério de abandono.

Organizar a resposta em `Decisão recomendada`, `Evidências e execução`, `Alternativas e critérios`, `Limitações` e `Próximo passo`. Adaptar o tamanho à tarefa. Para cada achado relevante, explicar o significado e a consequência prática; anexar consultas/código ou localização de evidências quando houver. Números devem trazer unidade, população e período. Não esconder pendências em uma conclusão definitiva.

# Common mistakes

Ranking de pesos como prova estatística; testar até obter p pequeno.

Preferir uma hipótese que possa mudar a decisão a uma lista extensa de correlações. O script de priorização usa pesos convencionais ajustáveis e não estima probabilidade de sucesso.

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

"Use $business-hypothesis-builder no meu projeto. Explique os critérios de decisão, proponha ou execute as verificações possíveis e separe resultados de premissas."

## Recursos específicos

- [hypothesis-types.md](references/hypothesis-types.md): recurso específico já existente; consultar quando necessário.
- [hypothesis-backlog.csv](assets/hypothesis-backlog.csv): recurso específico já existente; consultar quando necessário.
- [churn-hypotheses.csv](examples/churn-hypotheses.csv): recurso específico já existente; consultar quando necessário.
- [business_hypothesis_builder.py](scripts/business_hypothesis_builder.py): recurso específico já existente; consultar quando necessário.

## Apoio transversal

Para decisões que exigem justificativa estatística ou operacional, consultar o trecho relevante do [aprofundamento metodológico](../../guides/method-depth.md). Para organizar evidências e comunicar a recomendação, usar o [protocolo de decisão](../../guides/decision-protocol.md). Não carregar ambos por obrigação em tarefas simples.
