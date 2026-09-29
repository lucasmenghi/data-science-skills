---
name: leakage-check
description: Auditar vazamento temporal, de rótulo, de entidades e de seleção ao longo de um pipeline.
metadata:
  version: "0.2.0"
  category: data-preparation
  language: pt-BR
---

# Purpose

Auditar vazamento temporal, de rótulo, de entidades e de seleção ao longo de um pipeline.

# When to use

Quando a tarefa requer esta decisão dentro de preparação de dados. Trabalhar no escopo solicitado e entregar resultado utilizável; não transformar uma demanda de trabalho em sabatina. No modo explicativo, mostrar o porquê das escolhas junto do resultado.

# Inputs

Momento de decisão; origem e disponibilidade das features; splits; transformações e histórico de experimentos.

Usar o contexto já fornecido. Se faltar dado que altera materialmente a decisão, perguntar de forma focada; continuar a análise independente com premissas marcadas. Sem dados acessíveis, entregar desenho e verificações propostas, nunca resultados simulados como observados.

# Process

1. Construir linha do tempo entre ocorrência, ingestão, cálculo da feature, treinamento, previsão e maturação do alvo.
2. Revisar cada feature quanto a informação futura, proxies do desfecho e disponibilidade operacional; verificar agregações e joins point-in-time.
3. Inspecionar imputação, escala, encoding, seleção e reamostragem dentro dos folds. Distinguir operações aprendidas de validações determinísticas por linha.
4. Auditar entidades repetidas, duplicatas, famílias ou sessões cruzando splits conforme generalização desejada; não impor exclusão de entidades se uso real é prever seu futuro.
5. Verificar seleção de modelo/threshold e uso repetido do teste. Propor avaliação nova quando o holdout já participou das decisões.
6. Explicar ao usuário a decisão, a alternativa descartada e a evidência que mudaria a recomendação. Registrar o que foi executado, o que é hipótese e o próximo passo verificável.

Consultar [critérios e trade-offs](references/decision-guide.md) para comparar alternativas e [caso trabalhado](examples/worked-case.md) para a profundidade esperada. Ler somente o apoio relevante, não todo o catálogo.

# Output contract

Matriz feature-disponibilidade; achados com evidência; impacto; correção e plano de reavaliação.

Organizar a resposta em `Decisão recomendada`, `Evidências e execução`, `Alternativas e critérios`, `Limitações` e `Próximo passo`. Adaptar o tamanho à tarefa. Para cada achado relevante, explicar o significado e a consequência prática; anexar consultas/código ou localização de evidências quando houver. Números devem trazer unidade, população e período. Não esconder pendências em uma conclusão definitiva.

# Common mistakes

Chamar qualquer correlação de leakage; confiar só em nomes de colunas; prometer Pipeline elimina todo vazamento.

Sem logs de disponibilidade, declarar risco não verificável. Diferenciar falha comprovada, suspeita e hipótese descartada.

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

"Use $leakage-check no meu projeto. Explique os critérios de decisão, proponha ou execute as verificações possíveis e separe resultados de premissas."

## Apoio transversal

Para decisões que exigem justificativa estatística ou operacional, consultar o trecho relevante do [aprofundamento metodológico](../../guides/method-depth.md). Para organizar evidências e comunicar a recomendação, usar o [protocolo de decisão](../../guides/decision-protocol.md). Não carregar ambos por obrigação em tarefas simples.
