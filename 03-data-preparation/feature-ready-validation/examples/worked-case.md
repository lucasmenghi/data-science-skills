# Caso trabalhado: feature-ready-validation

Cenário sintético de decisão; não é resultado executado em dados reais.

## Situação e análise

Um serviço envia renda em centavos, enquanto o treino usou unidades monetárias. A assinatura deve incluir unidade e teste de exemplo, pois dtype numérico sozinho não captura o erro.

## Recomendação explicada

Se houver apenas schema, avaliar contrato estático e listar checks dependentes de execução como pendentes.

## O que entregar

Contrato executável; casos de teste; relatório de paridade; lacunas e aceite condicionado.

## Como verificar

Classificar violações bloqueadoras, fallback e advertências; entregar prontidão de entrada sem confundir com qualidade do modelo.

## Contraponto

Boa métrica offline não corrige entrada divergente. Se a premissa do caso mudar, reavaliar a decisão em vez de reutilizar a conclusão. Informar o que falta para passar de hipótese a evidência.
