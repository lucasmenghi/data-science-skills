---
name: feature-selection
description: Selecionar features por utilidade fora da amostra, estabilidade e custo sem contaminar validação.
metadata:
  version: "0.2.0"
  category: feature-engineering
  language: pt-BR
---

# Purpose

Selecionar features por utilidade fora da amostra, estabilidade e custo sem contaminar validação.

# When to use

Quando a tarefa requer esta decisão dentro de engenharia de features. Trabalhar no escopo solicitado e entregar resultado utilizável; não transformar uma demanda de trabalho em sabatina. No modo explicativo, mostrar o porquê das escolhas junto do resultado.

# Inputs

Conjunto candidato; modelo; grupos correlacionados; protocolo de CV; custos de aquisição/serving.

Usar o contexto já fornecido. Se faltar dado que altera materialmente a decisão, perguntar de forma focada; continuar a análise independente com premissas marcadas. Sem dados acessíveis, entregar desenho e verificações propostas, nunca resultados simulados como observados.

# Process

1. Definir objetivo da seleção: reduzir custo, variância, latência ou aumentar interpretabilidade. Eliminar primeiro impossibilidades de disponibilidade comprovadas.
2. Comparar filtros, métodos embutidos e wrappers de acordo com modelo e orçamento; manter interações potencialmente úteis.
3. Executar seleção aprendida dentro de cada fold; validar o processo completo, incluindo número de features e critérios.
4. Medir estabilidade entre folds/períodos e ganho incremental de grupos correlacionados. Importância individual baixa pode refletir redundância.
5. Escolher conjunto parcimonioso dentro da incerteza da comparação; congelar e avaliar no teste final reservado.
6. Explicar ao usuário a decisão, a alternativa descartada e a evidência que mudaria a recomendação. Registrar o que foi executado, o que é hipótese e o próximo passo verificável.

Consultar [critérios e trade-offs](references/decision-guide.md) para comparar alternativas e [caso trabalhado](examples/worked-case.md) para a profundidade esperada. Ler somente o apoio relevante, não todo o catálogo.

# Output contract

Protocolo; conjuntos comparados; estabilidade; custo; conjunto escolhido e justificativa.

Organizar a resposta em `Decisão recomendada`, `Evidências e execução`, `Alternativas e critérios`, `Limitações` e `Próximo passo`. Adaptar o tamanho à tarefa. Para cada achado relevante, explicar o significado e a consequência prática; anexar consultas/código ou localização de evidências quando houver. Números devem trazer unidade, população e período. Não esconder pendências em uma conclusão definitiva.

# Common mistakes

Selecionar pelo teste; remover uma variável só porque é pouco correlacionada individualmente.

O produto da seleção é um procedimento reproduzível, não uma lista supostamente universal de melhores variáveis.

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

"Use $feature-selection no meu projeto. Explique os critérios de decisão, proponha ou execute as verificações possíveis e separe resultados de premissas."

## Apoio transversal

Para decisões que exigem justificativa estatística ou operacional, consultar o trecho relevante do [aprofundamento metodológico](../../guides/method-depth.md). Para organizar evidências e comunicar a recomendação, usar o [protocolo de decisão](../../guides/decision-protocol.md). Não carregar ambos por obrigação em tarefas simples.
