---
name: feature-ready-validation
description: Verificar contrato de entrada de um modelo e equivalência entre treinamento e inferência.
metadata:
  version: "0.2.0"
  category: data-preparation
  language: pt-BR
---

# Purpose

Verificar contrato de entrada de um modelo e equivalência entre treinamento e inferência.

# When to use

Quando a tarefa requer esta decisão dentro de preparação de dados. Trabalhar no escopo solicitado e entregar resultado utilizável; não transformar uma demanda de trabalho em sabatina. No modo explicativo, mostrar o porquê das escolhas junto do resultado.

# Inputs

Dataset de features; assinatura esperada; transformações; exemplos de inferência; splits.

Usar o contexto já fornecido. Se faltar dado que altera materialmente a decisão, perguntar de forma focada; continuar a análise independente com premissas marcadas. Sem dados acessíveis, entregar desenho e verificações propostas, nunca resultados simulados como observados.

# Process

1. Confirmar chave, unidade, ordem/nome de features, tipos, faixa, nulabilidade e categorias previstas no contrato.
2. Validar ausência de alvo/identificadores indevidos e integridade temporal usando informações de origem disponíveis.
3. Executar transformações congeladas em exemplos de treino e inferência, incluindo nulos, categorias novas, esquema incompleto e extremos.
4. Reconciliar resultados offline/online dentro de tolerância justificada e verificar que fit não é executado durante inferência.
5. Classificar violações bloqueadoras, fallback e advertências; entregar prontidão de entrada sem confundir com qualidade do modelo.
6. Explicar ao usuário a decisão, a alternativa descartada e a evidência que mudaria a recomendação. Registrar o que foi executado, o que é hipótese e o próximo passo verificável.

Consultar [critérios e trade-offs](references/decision-guide.md) para comparar alternativas e [caso trabalhado](examples/worked-case.md) para a profundidade esperada. Ler somente o apoio relevante, não todo o catálogo.

# Output contract

Contrato executável; casos de teste; relatório de paridade; lacunas e aceite condicionado.

Organizar a resposta em `Decisão recomendada`, `Evidências e execução`, `Alternativas e critérios`, `Limitações` e `Próximo passo`. Adaptar o tamanho à tarefa. Para cada achado relevante, explicar o significado e a consequência prática; anexar consultas/código ou localização de evidências quando houver. Números devem trazer unidade, população e período. Não esconder pendências em uma conclusão definitiva.

# Common mistakes

Declarar pronto apenas porque não há nulos; aceitar colunas com semântica alterada.

Se houver apenas schema, avaliar contrato estático e listar checks dependentes de execução como pendentes.

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

"Use $feature-ready-validation no meu projeto. Explique os critérios de decisão, proponha ou execute as verificações possíveis e separe resultados de premissas."

## Apoio transversal

Para decisões que exigem justificativa estatística ou operacional, consultar o trecho relevante do [aprofundamento metodológico](../../guides/method-depth.md). Para organizar evidências e comunicar a recomendação, usar o [protocolo de decisão](../../guides/decision-protocol.md). Não carregar ambos por obrigação em tarefas simples.
