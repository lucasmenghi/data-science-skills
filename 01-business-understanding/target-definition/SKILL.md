---
name: target-definition
description: Definir alvo supervisionado, elegibilidade e janelas temporais sem confundir censura com ausência de evento.
metadata:
  version: "0.2.0"
  category: business-understanding
  language: pt-BR
---

# Purpose

Definir alvo supervisionado, elegibilidade e janelas temporais sem confundir censura com ausência de evento.

# When to use

Quando a tarefa requer esta decisão dentro de entendimento do negócio. Trabalhar no escopo solicitado e entregar resultado utilizável; não transformar uma demanda de trabalho em sabatina. No modo explicativo, mostrar o porquê das escolhas junto do resultado.

# Inputs

Evento-alvo; entity_id; tempo de decisão; datas de eventos e disponibilidade; cobertura até uma data de corte.

Usar o contexto já fornecido. Se faltar dado que altera materialmente a decisão, perguntar de forma focada; continuar a análise independente com premissas marcadas. Sem dados acessíveis, entregar desenho e verificações propostas, nunca resultados simulados como observados.

# Process

1. Especificar unidade e evento positivo observável, com regras de reversão, repetição e eventos concorrentes. Distinguir status atual de evento futuro.
2. Fixar convenções de borda das janelas de observação, gap e desfecho. Especificar fuso, data de referência e se o dia corrente já fechou.
3. Construir elegibilidade apenas com fatos disponíveis na decisão. Calcular a primeira data em que o rótulo se torna maduro incluindo atraso de publicação.
4. Representar resultados ainda não observáveis como censurados ou pendentes, nunca negativos por conveniência. Avaliar survival quando tempo até evento e censura forem centrais.
5. Validar casos manuais nas bordas, múltiplos contratos e eventos tardios. Comparar taxas por safra antes de liberar a tabela de rótulos.
6. Explicar ao usuário a decisão, a alternativa descartada e a evidência que mudaria a recomendação. Registrar o que foi executado, o que é hipótese e o próximo passo verificável.

Consultar [critérios e trade-offs](references/decision-guide.md) para comparar alternativas e [caso trabalhado](examples/worked-case.md) para a profundidade esperada. Ler somente o apoio relevante, não todo o catálogo.

# Output contract

Contrato do alvo; SQL/pseudocódigo de rotulagem; calendário de maturação; tabela de casos de borda.

Organizar a resposta em `Decisão recomendada`, `Evidências e execução`, `Alternativas e critérios`, `Limitações` e `Próximo passo`. Adaptar o tamanho à tarefa. Para cada achado relevante, explicar o significado e a consequência prática; anexar consultas/código ou localização de evidências quando houver. Números devem trazer unidade, população e período. Não esconder pendências em uma conclusão definitiva.

# Common mistakes

Rotular ausência de dado como negativo; usar evento futuro na elegibilidade.

Separar target válido de target útil: mesmo bem rotulado, pode chegar tarde para a ação. Janelas e latência são decisões do produto.

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

"Use $target-definition no meu projeto. Explique os critérios de decisão, proponha ou execute as verificações possíveis e separe resultados de premissas."

## Recursos específicos

- [temporal-windows.md](references/temporal-windows.md): recurso específico já existente; consultar quando necessário.
- [target-definition-template.md](assets/target-definition-template.md): recurso específico já existente; consultar quando necessário.
- [churn-30d-example.md](examples/churn-30d-example.md): recurso específico já existente; consultar quando necessário.
- [target_definition.py](scripts/target_definition.py): recurso específico já existente; consultar quando necessário.

## Apoio transversal

Para decisões que exigem justificativa estatística ou operacional, consultar o trecho relevante do [aprofundamento metodológico](../../guides/method-depth.md). Para organizar evidências e comunicar a recomendação, usar o [protocolo de decisão](../../guides/decision-protocol.md). Não carregar ambos por obrigação em tarefas simples.
