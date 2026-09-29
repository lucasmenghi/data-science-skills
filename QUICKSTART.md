# Como usar no trabalho

## Primeiro uso

1. Abra esta pasta do repositório como projeto no Codex.
2. Descreva o resultado que precisa, os arquivos/tabelas disponíveis e restrições conhecidas.
3. Use `$ds-workbench` para escolher o caminho ou chame uma skill temática diretamente.
4. Revise a decisão, as evidências e as limitações. Se algo foi apenas proposto, ele deve estar marcado como não executado.

```text
Use $ds-workbench. Preciso construir uma análise de cancelamento.
Tenho estas tabelas e este objetivo: [descrever ou indicar arquivos].
Trabalhe em Python e SQL. Explique suas escolhas e execute o que for possível
com os dados e permissões disponíveis. Não transforme a tarefa em entrevista.
```

Se a skill não aparecer no seletor, envie: “Leia `13-ai-assistants/ds-workbench/SKILL.md` e aplique ao meu pedido”. A pasta completa é necessária para os links relativos. Não precisa instalar bibliotecas de ML para usar as instruções; a execução de um projeto concreto depende do ambiente desse projeto.

## Escolher pelo problema

| Pedido | Entrada recomendada |
|---|---|
| “O negócio pediu um modelo, mas a decisão não está clara” | `problem-framing` |
| “Não conheço esta base” | `eda-assistant` ou `dataset-profiler` |
| “O total aumentou depois de um join” | `granularity-check` |
| “Como tratar dados ausentes?” | `missing-value-strategy` |
| “Preciso de features no tempo correto” | `temporal-features` |
| “Quero escolher um modelo e comparar alternativas” | `algorithm-selection` + `cross-validation-planner` |
| “Como decidir quem recebe uma ação?” | `threshold-optimization` |
| “A variável explica por que o resultado aconteceu?” | `feature-importance` para modelo; `causal-thinking` para efeito |
| “Quero medir se minha iniciativa funciona” | `ab-test-design` |
| “O modelo está pronto para servir?” | `serving-readiness` |
| “A qualidade caiu” | `performance-monitoring` + `retraining-advisor` |
| “Quanto valor o projeto pode gerar?” | `financial-impact` |
| “Preciso de uma decisão executiva com evidências” | `business-translator` |
| “Quero construir/revisar um RAG” | `ds-workbench` + guia de IA aplicada |

As combinações são sugestões. O assistente deve selecionar o mínimo necessário e respeitar trabalho já concluído. Catálogo completo em [STRUCTURE.md](STRUCTURE.md).

## Exemplos copiáveis

```text
Use $granularity-check. Esta consulta duplicou o valor total após o join.
Identifique a unidade das tabelas, encontre a causa e proponha a correção.
Mostre verificações antes e depois e explique a consequência do problema.
```

```text
Use $model-review neste notebook. Quero achados rastreáveis sobre alvo,
leakage, seleção de modelo, métricas e capacidade de generalização.
Separe falha comprovada, suspeita e evidência ausente.
```

```text
Use $ds-ai em modo trabalho. Desenhe um assistente documental com RAG.
Compare com busca simples, defina avaliação por camada e explique limites.
Se não houver API disponível, entregue desenho e testes offline sem alegar execução ao vivo.
```

## O que a resposta deve conter

Uma recomendação ligada à decisão, evidência observada, alternativas plausíveis, verificações feitas e limitações materiais. Código deve respeitar schema e motor reais. Números vêm de execução ou de exemplos explicitamente sintéticos. Uma análise não autoriza por si só publicar, enviar mensagens, alterar bases ou implantar serviço.

## Utilitários locais

Executar a partir da raiz. Os exemplos abaixo usam cenários sintéticos e não precisam de bibliotecas externas:

```sh
python 01-business-understanding/target-definition/scripts/target_definition.py --reference-date 2026-09-29 --observation-days 90 --gap-days 0 --performance-days 30
python 01-business-understanding/success-criteria-definition/scripts/success_criteria_definition.py --metric-value 7 --minimum 10 --target 5 --direction minimize
python 06-model-validation/threshold-optimization/scripts/threshold_policy.py --input 06-model-validation/threshold-optimization/examples/validation-predictions.csv --tp-benefit 10 --fp-cost 2 --capacity 3
```

No avaliador de metas, `--minimum` é o limite de aceitação: na minimização, funciona como teto. O resultado é de uma métrica isolada, não aprovação de lançamento. No utilitário de políticas, custos são hipóteses do exemplo e o conjunto precisa ser de validação; o script não consegue verificar a origem dos scores. Empates são mantidos juntos, logo pode sobrar capacidade. Há opção de não agir.

## Estudo pessoal

Para aula, exercícios ou entrevista, use `$ds-mentor` e [START-HERE](learning/START-HERE.md). Nesse modo, o assistente espera suas tentativas e registra evidências em `private/`. O trabalho diário e a aprendizagem compartilham métodos, mas têm dinâmicas diferentes.

## Manutenção

Edite instruções nas categorias, atualize manifests e rode geração, validação e testes descritos no README. As entradas `.agents/skills/` são geradas; não editar à mão. Manter fontes, exemplos e contratos coerentes com o comportamento final. Não adicionar instruções longas só para aumentar volume: cada referência deve apoiar uma decisão real.
