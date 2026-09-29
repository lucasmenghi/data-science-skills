---
name: problem-framing
description: Transformar uma demanda de negócio em decisão analítica, comparando regra, análise, experimento e ML.
metadata:
  version: "0.2.0"
  category: business-understanding
  language: pt-BR
---

# Purpose

Transformar uma demanda de negócio em decisão analítica, comparando regra, análise, experimento e ML.

# When to use

Quando a tarefa requer esta decisão dentro de entendimento do negócio. Trabalhar no escopo solicitado e entregar resultado utilizável; não transformar uma demanda de trabalho em sabatina. No modo explicativo, mostrar o porquê das escolhas junto do resultado.

# Inputs

Demanda; decisor; ação possível; população; restrições e situação atual.

Usar o contexto já fornecido. Se faltar dado que altera materialmente a decisão, perguntar de forma focada; continuar a análise independente com premissas marcadas. Sem dados acessíveis, entregar desenho e verificações propostas, nunca resultados simulados como observados.

# Process

1. Reformular o pedido como decisão: quem decide o quê, quando e com qual alternativa atual. Uma solicitação de algoritmo não define o problema.
2. Separar indicador observado, objetivo e mecanismo pelo qual a ação poderia alterar o resultado. Localizar custo de não agir e custo de agir errado.
3. Definir unidade, população elegível, momento de decisão e horizonte. Distinguir cliente, contrato e evento; listar exclusões que mudam a população.
4. Comparar análise descritiva, regra, predição, experimento e otimização pela informação necessária e ação suportada. Escolher a opção mínima que responde à decisão.
5. Elaborar escopo, critérios de sucesso e perguntas bloqueadoras. Confirmar definições com o responsável sem declarar aprovação que não ocorreu.
6. Explicar ao usuário a decisão, a alternativa descartada e a evidência que mudaria a recomendação. Registrar o que foi executado, o que é hipótese e o próximo passo verificável.

Consultar [critérios e trade-offs](references/decision-guide.md) para comparar alternativas e [caso trabalhado](examples/worked-case.md) para a profundidade esperada. Ler somente o apoio relevante, não todo o catálogo.

# Output contract

Mapa da decisão; alternativas; escopo e não escopo; premissas; proposta de avaliação.

Organizar a resposta em `Decisão recomendada`, `Evidências e execução`, `Alternativas e critérios`, `Limitações` e `Próximo passo`. Adaptar o tamanho à tarefa. Para cada achado relevante, explicar o significado e a consequência prática; anexar consultas/código ou localização de evidências quando houver. Números devem trazer unidade, população e período. Não esconder pendências em uma conclusão definitiva.

# Common mistakes

Confundir desempenho preditivo com mudança de negócio; deixar população e ação implícitas.

Um resultado útil pode ser concluir que um dashboard ou ajuste de processo atende melhor. Exigir decisão documentada, não a presença de ML.

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

"Use $problem-framing no meu projeto. Explique os critérios de decisão, proponha ou execute as verificações possíveis e separe resultados de premissas."

## Recursos específicos

- [analytical-problem-types.md](references/analytical-problem-types.md): recurso específico já existente; consultar quando necessário.
- [problem-framing-template.md](assets/problem-framing-template.md): recurso específico já existente; consultar quando necessário.
- [churn-example.md](examples/churn-example.md): recurso específico já existente; consultar quando necessário.
- [problem_framing.py](scripts/problem_framing.py): recurso específico já existente; consultar quando necessário.

## Apoio transversal

Para decisões que exigem justificativa estatística ou operacional, consultar o trecho relevante do [aprofundamento metodológico](../../guides/method-depth.md). Para organizar evidências e comunicar a recomendação, usar o [protocolo de decisão](../../guides/decision-protocol.md). Não carregar ambos por obrigação em tarefas simples.
