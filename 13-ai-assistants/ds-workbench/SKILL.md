---
name: ds-workbench
description: Coordenar tarefas reais de Data Science do problema à operação, escolhendo skills e explicando decisões ao usuário.
metadata:
  version: "0.2.0"
  category: ai-assistants
  language: pt-BR
---

# Purpose

Coordenar tarefas reais de Data Science do problema à operação, escolhendo skills e explicando decisões ao usuário.

# When to use

Quando a tarefa requer esta decisão dentro de assistentes de trabalho e aprendizagem. Trabalhar no escopo solicitado e entregar resultado utilizável; não transformar uma demanda de trabalho em sabatina. No modo explicativo, mostrar o porquê das escolhas junto do resultado.

# Inputs

Pedido de trabalho; artefatos disponíveis; decisão desejada; ambiente; restrições e estado do projeto.

Usar o contexto já fornecido. Se faltar dado que altera materialmente a decisão, perguntar de forma focada; continuar a análise independente com premissas marcadas. Sem dados acessíveis, entregar desenho e verificações propostas, nunca resultados simulados como observados.

# Process

1. Identificar a entrega solicitada e localizar o estágio atual sem reiniciar etapas já resolvidas. Pedir apenas contexto que muda a ação imediata.
2. Ler o catálogo de trabalho e selecionar o menor conjunto de skills necessário. Separar revisão, planejamento, análise executada e mudança operacional.
3. Inspecionar artefatos e aplicar primeiro a skill que resolve a dependência bloqueadora, como granularidade antes de modelagem ou desenho antes de inferência causal.
4. Conduzir o trabalho e explicar decisões em linguagem simples: observação, implicação e próximo teste. Não impor perguntas de sabatina em modo trabalho.
5. Consolidar resultados e divergências, entregar artefatos revisáveis e indicar a próxima decisão. Usar habilidades especializadas sequencialmente; não exigir ferramentas de subagentes.
6. Explicar ao usuário a decisão, a alternativa descartada e a evidência que mudaria a recomendação. Registrar o que foi executado, o que é hipótese e o próximo passo verificável.

Consultar [critérios e trade-offs](references/decision-guide.md) para comparar alternativas e [caso trabalhado](examples/worked-case.md) para a profundidade esperada. Ler somente o apoio relevante, não todo o catálogo.

# Output contract

Entrega solicitada; mapa de decisões; evidência; pendências; próximo passo e artefatos.

Organizar a resposta em `Decisão recomendada`, `Evidências e execução`, `Alternativas e critérios`, `Limitações` e `Próximo passo`. Adaptar o tamanho à tarefa. Para cada achado relevante, explicar o significado e a consequência prática; anexar consultas/código ou localização de evidências quando houver. Números devem trazer unidade, população e período. Não esconder pendências em uma conclusão definitiva.

# Common mistakes

Orquestrar por palavras-chave sem objetivo; rodar todos os agentes; ler histórico pessoal em tarefa profissional sem necessidade.

Os papéis são instruções reutilizáveis, não processos autônomos. O assistente realiza o trabalho na conversa e usa somente ferramentas e permissões realmente disponíveis.

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

"Use $ds-workbench no meu projeto. Explique os critérios de decisão, proponha ou execute as verificações possíveis e separe resultados de premissas."

## Apoio transversal

Para decisões que exigem justificativa estatística ou operacional, consultar o trecho relevante do [aprofundamento metodológico](../../guides/method-depth.md). Para organizar evidências e comunicar a recomendação, usar o [protocolo de decisão](../../guides/decision-protocol.md). Não carregar ambos por obrigação em tarefas simples.

## Roteamento

Escolher pelo [catálogo](../../STRUCTURE.md) e pelos [exemplos de pedido](../../QUICKSTART.md). Para fluxo integrado, consultar [retenção](../../examples/workflows/retention-decision.md); para queda de qualidade, [triagem de incidente](../../examples/workflows/incident-triage.md). Para LLM/RAG, usar o [guia de IA aplicada](../../guides/applied-ai-workflow.md).
