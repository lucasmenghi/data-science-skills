---
name: technical-report
description: Escrever relatório técnico reproduzível que conecta problema, método, resultados e limites.
metadata:
  version: "0.2.0"
  category: documentation
  language: pt-BR
---

# Purpose

Escrever relatório técnico reproduzível que conecta problema, método, resultados e limites.

# When to use

Quando a tarefa requer esta decisão dentro de documentação. Trabalhar no escopo solicitado e entregar resultado utilizável; não transformar uma demanda de trabalho em sabatina. No modo explicativo, mostrar o porquê das escolhas junto do resultado.

# Inputs

Objetivo; artefatos; experimentos; métricas; público; decisões e status de execução.

Usar o contexto já fornecido. Se faltar dado que altera materialmente a decisão, perguntar de forma focada; continuar a análise independente com premissas marcadas. Sem dados acessíveis, entregar desenho e verificações propostas, nunca resultados simulados como observados.

# Process

1. Identificar pergunta central e escopo; reunir caminhos/versões dos artefatos e separar experimentos efetivamente realizados.
2. Descrever dados, seleção, alvo, tempo e preparação com detalhes suficientes para avaliar leakage e representatividade.
3. Explicar métodos e alternativas por critérios, incluindo baseline, busca e protocolo de seleção.
4. Apresentar resultados com contagens, incerteza e análise de erros; relacionar tabelas à decisão sem extrapolar causalidade.
5. Concluir com recomendação, limitações, pendências e reprodução; verificar números consistentes entre texto, tabelas e fontes.
6. Explicar ao usuário a decisão, a alternativa descartada e a evidência que mudaria a recomendação. Registrar o que foi executado, o que é hipótese e o próximo passo verificável.

Consultar [critérios e trade-offs](references/decision-guide.md) para comparar alternativas e [caso trabalhado](examples/worked-case.md) para a profundidade esperada. Ler somente o apoio relevante, não todo o catálogo.

# Output contract

Relatório técnico; índice de artefatos; método; evidências; reprodução e conclusão.

Organizar a resposta em `Decisão recomendada`, `Evidências e execução`, `Alternativas e critérios`, `Limitações` e `Próximo passo`. Adaptar o tamanho à tarefa. Para cada achado relevante, explicar o significado e a consequência prática; anexar consultas/código ou localização de evidências quando houver. Números devem trazer unidade, população e período. Não esconder pendências em uma conclusão definitiva.

# Common mistakes

Relatar cronologia de tentativas sem conclusão; misturar metodologia e resultados supostos.

O leitor deve conseguir entender por que a decisão foi tomada e o que seria necessário para contestá-la ou reproduzi-la.

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

"Use $technical-report no meu projeto. Explique os critérios de decisão, proponha ou execute as verificações possíveis e separe resultados de premissas."

## Apoio transversal

Para decisões que exigem justificativa estatística ou operacional, consultar o trecho relevante do [aprofundamento metodológico](../../guides/method-depth.md). Para organizar evidências e comunicar a recomendação, usar o [protocolo de decisão](../../guides/decision-protocol.md). Não carregar ambos por obrigação em tarefas simples.
