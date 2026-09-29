---
name: temporal-validation
description: Verificar consistência temporal e maturação de dados antes de estabelecer folds e avaliação futura.
metadata:
  version: "0.2.0"
  category: data-preparation
  language: pt-BR
---

# Purpose

Verificar consistência temporal e maturação de dados antes de estabelecer folds e avaliação futura.

# When to use

Quando a tarefa requer esta decisão dentro de preparação de dados. Trabalhar no escopo solicitado e entregar resultado utilizável; não transformar uma demanda de trabalho em sabatina. No modo explicativo, mostrar o porquê das escolhas junto do resultado.

# Inputs

event_time; available_at; reference_time; janelas de features/alvo; revisões e atraso de fontes.

Usar o contexto já fornecido. Se faltar dado que altera materialmente a decisão, perguntar de forma focada; continuar a análise independente com premissas marcadas. Sem dados acessíveis, entregar desenho e verificações propostas, nunca resultados simulados como observados.

# Process

1. Documentar dois relógios: quando ocorreu e quando ficou disponível. Fixar fuso, fechamento diário e convenções de borda.
2. Confirmar que features disponíveis em reference_time não usam eventos ou correções posteriores. Auditar snapshots e backfills.
3. Calcular maturação de alvos e excluir/representar pendentes. Identificar sobreposição de janelas que compromete separação.
4. Simular cortes históricos e reconciliar o que o pipeline teria visto na época com a extração atual.
5. Entregar contrato temporal e restrições para cross-validation/oot; lacunas de reconstrução precisam aparecer como limitação.
6. Explicar ao usuário a decisão, a alternativa descartada e a evidência que mudaria a recomendação. Registrar o que foi executado, o que é hipótese e o próximo passo verificável.

Consultar [critérios e trade-offs](references/decision-guide.md) para comparar alternativas e [caso trabalhado](examples/worked-case.md) para a profundidade esperada. Ler somente o apoio relevante, não todo o catálogo.

# Output contract

Contrato de relógios; regras de maturação; auditoria de bordas; tabela de cortes válidos.

Organizar a resposta em `Decisão recomendada`, `Evidências e execução`, `Alternativas e critérios`, `Limitações` e `Próximo passo`. Adaptar o tamanho à tarefa. Para cada achado relevante, explicar o significado e a consequência prática; anexar consultas/código ou localização de evidências quando houver. Números devem trazer unidade, população e período. Não esconder pendências em uma conclusão definitiva.

# Common mistakes

Usar só event_time; confundir ordenação com garantia de ausência de futuro.

Esta skill valida o dado temporal; `cross-validation-planner` escolhe o protocolo de estimação e `oot-validation` avalia o modelo congelado.

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

"Use $temporal-validation no meu projeto. Explique os critérios de decisão, proponha ou execute as verificações possíveis e separe resultados de premissas."

## Apoio transversal

Para decisões que exigem justificativa estatística ou operacional, consultar o trecho relevante do [aprofundamento metodológico](../../guides/method-depth.md). Para organizar evidências e comunicar a recomendação, usar o [protocolo de decisão](../../guides/decision-protocol.md). Não carregar ambos por obrigação em tarefas simples.
