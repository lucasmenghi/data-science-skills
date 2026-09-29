---
name: shap-analysis
description: Planejar e interpretar explicações SHAP com background, escala de saída e dependências explícitos.
metadata:
  version: "0.2.0"
  category: model-interpretability
  language: pt-BR
---

# Purpose

Planejar e interpretar explicações SHAP com background, escala de saída e dependências explícitos.

# When to use

Quando a tarefa requer esta decisão dentro de interpretabilidade. Trabalhar no escopo solicitado e entregar resultado utilizável; não transformar uma demanda de trabalho em sabatina. No modo explicativo, mostrar o porquê das escolhas junto do resultado.

# Inputs

Modelo; tarefa; amostra/background; unidade da saída; pergunta local/global; orçamento.

Usar o contexto já fornecido. Se faltar dado que altera materialmente a decisão, perguntar de forma focada; continuar a análise independente com premissas marcadas. Sem dados acessíveis, entregar desenho e verificações propostas, nunca resultados simulados como observados.

# Process

1. Definir qual saída será explicada: score, log-odds, probabilidade ou outra. Confirmar suporte da versão do explicador e do modelo.
2. Selecionar background representativo da comparação desejada e justificar tamanho/amostragem, sem expor dados individuais indevidamente.
3. Escolher abordagem de dependência e explicador compatível; explicar que escolhas mudam a referência e as atribuições.
4. Verificar reconstrução da saída/base quando aplicável, dimensões multiclass e estabilidade; não interpretar arrays sem confirmar classes/escala.
5. Apresentar casos típicos e falhas, agregação global e limites. Valores SHAP descrevem atribuição do modelo sob convenção, não causalidade.
6. Explicar ao usuário a decisão, a alternativa descartada e a evidência que mudaria a recomendação. Registrar o que foi executado, o que é hipótese e o próximo passo verificável.

Consultar [critérios e trade-offs](references/decision-guide.md) para comparar alternativas e [caso trabalhado](examples/worked-case.md) para a profundidade esperada. Ler somente o apoio relevante, não todo o catálogo.

# Output contract

Configuração do explicador; background; checagens; explicações locais/globais e limites.

Organizar a resposta em `Decisão recomendada`, `Evidências e execução`, `Alternativas e critérios`, `Limitações` e `Próximo passo`. Adaptar o tamanho à tarefa. Para cada achado relevante, explicar o significado e a consequência prática; anexar consultas/código ou localização de evidências quando houver. Números devem trazer unidade, população e período. Não esconder pendências em uma conclusão definitiva.

# Common mistakes

Usar gráfico sem verificar unidade; afirmar efeito individual causal; ignorar versão da API.

Antes de recomendar ação sobre uma feature, verificar se ela é acionável e se há evidência causal separada. Uma atribuição não é uma recomendação de intervenção.

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

"Use $shap-analysis no meu projeto. Explique os critérios de decisão, proponha ou execute as verificações possíveis e separe resultados de premissas."

## Apoio transversal

Para decisões que exigem justificativa estatística ou operacional, consultar o trecho relevante do [aprofundamento metodológico](../../guides/method-depth.md). Para organizar evidências e comunicar a recomendação, usar o [protocolo de decisão](../../guides/decision-protocol.md). Não carregar ambos por obrigação em tarefas simples.
