---
name: dataset-profiler
description: Caracterizar cobertura, distribuição e qualidade inicial de um dataset sem confundir amostra com população.
metadata:
  version: "0.2.0"
  category: data-discovery
  language: pt-BR
---

# Purpose

Caracterizar cobertura, distribuição e qualidade inicial de um dataset sem confundir amostra com população.

# When to use

Quando a tarefa requer esta decisão dentro de descoberta e diagnóstico de dados. Trabalhar no escopo solicitado e entregar resultado utilizável; não transformar uma demanda de trabalho em sabatina. No modo explicativo, mostrar o porquê das escolhas junto do resultado.

# Inputs

Dataset ou acesso autorizado; esquema; período; unidade esperada; limites de processamento.

Usar o contexto já fornecido. Se faltar dado que altera materialmente a decisão, perguntar de forma focada; continuar a análise independente com premissas marcadas. Sem dados acessíveis, entregar desenho e verificações propostas, nunca resultados simulados como observados.

# Process

1. Inspecionar metadados, partições, período e estimativa de volume antes de varrer dados. Definir amostra representativa por tempo e segmentos se necessário.
2. Medir linhas, entidades, duplicações de chave, cardinalidade, missing e cobertura por período. Diferenciar nulo, vazio, zero e sentinela.
3. Resumir numéricas com quantis, amplitude e unidades; categóricas com frequência e categorias novas; datas com atraso e lacunas.
4. Comparar perfis por safras e grupos relevantes. Identificar mudanças que possam ser mistura populacional ou falha de ingestão.
5. Entregar achados com contagens, denominadores, consultas e alcance da análise; propor investigação, não limpeza automática.
6. Explicar ao usuário a decisão, a alternativa descartada e a evidência que mudaria a recomendação. Registrar o que foi executado, o que é hipótese e o próximo passo verificável.

Consultar [critérios e trade-offs](references/decision-guide.md) para comparar alternativas e [caso trabalhado](examples/worked-case.md) para a profundidade esperada. Ler somente o apoio relevante, não todo o catálogo.

# Output contract

Perfil por coluna e safra; escopo da amostra; anomalias priorizadas; consultas reproduzíveis.

Organizar a resposta em `Decisão recomendada`, `Evidências e execução`, `Alternativas e critérios`, `Limitações` e `Próximo passo`. Adaptar o tamanho à tarefa. Para cada achado relevante, explicar o significado e a consequência prática; anexar consultas/código ou localização de evidências quando houver. Números devem trazer unidade, população e período. Não esconder pendências em uma conclusão definitiva.

# Common mistakes

Gerar centenas de gráficos sem decisão; coletar toda a tabela no driver.

Perfil descreve o que foi lido, não garante qualidade semântica. Reportar aproximações de distinct e quantis quando usadas.

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

"Use $dataset-profiler no meu projeto. Explique os critérios de decisão, proponha ou execute as verificações possíveis e separe resultados de premissas."

## Apoio transversal

Para decisões que exigem justificativa estatística ou operacional, consultar o trecho relevante do [aprofundamento metodológico](../../guides/method-depth.md). Para organizar evidências e comunicar a recomendação, usar o [protocolo de decisão](../../guides/decision-protocol.md). Não carregar ambos por obrigação em tarefas simples.
