---
name: missing-value-strategy
description: Escolher e validar tratamento de ausências considerando mecanismo, disponibilidade e efeito operacional.
metadata:
  version: "0.2.0"
  category: data-preparation
  language: pt-BR
---

# Purpose

Escolher e validar tratamento de ausências considerando mecanismo, disponibilidade e efeito operacional.

# When to use

Quando a tarefa requer esta decisão dentro de preparação de dados. Trabalhar no escopo solicitado e entregar resultado utilizável; não transformar uma demanda de trabalho em sabatina. No modo explicativo, mostrar o porquê das escolhas junto do resultado.

# Inputs

Padrão de missing por campo/safra; modelo; splits; semântica de ausência e latência.

Usar o contexto já fornecido. Se faltar dado que altera materialmente a decisão, perguntar de forma focada; continuar a análise independente com premissas marcadas. Sem dados acessíveis, entregar desenho e verificações propostas, nunca resultados simulados como observados.

# Process

1. Separar ausência estrutural, indisponibilidade temporária, não resposta, sentinela e erro de coleta. Investigar concentração por grupos e tempo.
2. Discutir hipóteses MCAR/MAR/MNAR sem afirmar que o mecanismo foi provado pelos dados observados. Considerar se a ausência carrega informação disponível na decisão.
3. Comparar manutenção nativa, indicador, imputação simples, por grupo e modelos de imputação; avaliar custo, estabilidade e suporte a novas categorias.
4. Aprender parâmetros apenas no treino de cada fold e aplicar aos demais conjuntos. Definir fallback para grupo ou campo totalmente ausente.
5. Medir desempenho e comportamento por padrão de ausência, incluindo aumento de missing em produção. Documentar monitoramento e limites.
6. Explicar ao usuário a decisão, a alternativa descartada e a evidência que mudaria a recomendação. Registrar o que foi executado, o que é hipótese e o próximo passo verificável.

Consultar [critérios e trade-offs](references/decision-guide.md) para comparar alternativas e [caso trabalhado](examples/worked-case.md) para a profundidade esperada. Ler somente o apoio relevante, não todo o catálogo.

# Output contract

Matriz de tratamentos; hipótese do mecanismo; experimento comparativo; política de fallback.

Organizar a resposta em `Decisão recomendada`, `Evidências e execução`, `Alternativas e critérios`, `Limitações` e `Próximo passo`. Adaptar o tamanho à tarefa. Para cada achado relevante, explicar o significado e a consequência prática; anexar consultas/código ou localização de evidências quando houver. Números devem trazer unidade, população e período. Não esconder pendências em uma conclusão definitiva.

# Common mistakes

Imputar antes de split; transformar todo nulo em zero; usar alvo para preencher features futuras.

Excluir linhas muda a população atendida. Explicar cobertura perdida e reconhecer que qualidade preditiva não identifica o mecanismo de missing.

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

"Use $missing-value-strategy no meu projeto. Explique os critérios de decisão, proponha ou execute as verificações possíveis e separe resultados de premissas."

## Apoio transversal

Para decisões que exigem justificativa estatística ou operacional, consultar o trecho relevante do [aprofundamento metodológico](../../guides/method-depth.md). Para organizar evidências e comunicar a recomendação, usar o [protocolo de decisão](../../guides/decision-protocol.md). Não carregar ambos por obrigação em tarefas simples.
