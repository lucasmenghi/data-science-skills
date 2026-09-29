---
name: success-criteria-definition
description: Definir métricas e critérios de aceitação de negócio, modelo e operação com direção e incerteza explícitas.
metadata:
  version: "0.2.0"
  category: business-understanding
  language: pt-BR
---

# Purpose

Definir métricas e critérios de aceitação de negócio, modelo e operação com direção e incerteza explícitas.

# When to use

Quando a tarefa requer esta decisão dentro de entendimento do negócio. Trabalhar no escopo solicitado e entregar resultado utilizável; não transformar uma demanda de trabalho em sabatina. No modo explicativo, mostrar o porquê das escolhas junto do resultado.

# Inputs

Decisão; baseline; métricas; custos; capacidade; horizonte; tolerâncias e responsáveis.

Usar o contexto já fornecido. Se faltar dado que altera materialmente a decisão, perguntar de forma focada; continuar a análise independente com premissas marcadas. Sem dados acessíveis, entregar desenho e verificações propostas, nunca resultados simulados como observados.

# Process

1. Separar resultado de negócio, proxy analítica, desempenho técnico e restrições operacionais. Fixar população, denominador, horizonte e direção de cada métrica.
2. Definir comparação com baseline e efeito mínimo relevante com o responsável. Documentar de onde vieram os limites, sem inventar padrões universais.
3. Associar cada critério a método de medição, tamanho/representatividade dos dados e incerteza. Diferenciar valor pontual de limite de confiança.
4. Distinguir requisitos obrigatórios de metas desejáveis. Impedir compensação de violação grave por média alta em outra dimensão.
5. Especificar estados aprovar para próxima etapa, revisar ou interromper, com responsável e próxima evidência. Critérios de análise não autorizam deployment.
6. Explicar ao usuário a decisão, a alternativa descartada e a evidência que mudaria a recomendação. Registrar o que foi executado, o que é hipótese e o próximo passo verificável.

Consultar [critérios e trade-offs](references/decision-guide.md) para comparar alternativas e [caso trabalhado](examples/worked-case.md) para a profundidade esperada. Ler somente o apoio relevante, não todo o catálogo.

# Output contract

Matriz de métricas; baseline; limites justificados; plano de medição; decisão condicionada.

Organizar a resposta em `Decisão recomendada`, `Evidências e execução`, `Alternativas e critérios`, `Limitações` e `Próximo passo`. Adaptar o tamanho à tarefa. Para cada achado relevante, explicar o significado e a consequência prática; anexar consultas/código ou localização de evidências quando houver. Números devem trazer unidade, população e período. Não esconder pendências em uma conclusão definitiva.

# Common mistakes

Confundir limiar de modelo com meta de negócio; usar um único número como autorização de produção.

Limites de aceitação são locais ao contexto. O utilitário verifica valores e direção, mas não valida premissas, significância ou aprovação organizacional.

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

"Use $success-criteria-definition no meu projeto. Explique os critérios de decisão, proponha ou execute as verificações possíveis e separe resultados de premissas."

## Recursos específicos

- [success-layers.md](references/success-layers.md): recurso específico já existente; consultar quando necessário.
- [success-criteria-template.md](assets/success-criteria-template.md): recurso específico já existente; consultar quando necessário.
- [classification-example.md](examples/classification-example.md): recurso específico já existente; consultar quando necessário.
- [success_criteria_definition.py](scripts/success_criteria_definition.py): recurso específico já existente; consultar quando necessário.

## Apoio transversal

Para decisões que exigem justificativa estatística ou operacional, consultar o trecho relevante do [aprofundamento metodológico](../../guides/method-depth.md). Para organizar evidências e comunicar a recomendação, usar o [protocolo de decisão](../../guides/decision-protocol.md). Não carregar ambos por obrigação em tarefas simples.
