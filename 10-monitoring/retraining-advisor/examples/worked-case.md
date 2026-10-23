# Caso trabalhado: retraining-advisor

Cenário sintético de decisão; não é resultado executado em dados reais.

## Situação e análise

Um encoder trocou categorias após deploy. O remédio inicial é restaurar a transformação compatível e verificar resultados, não treinar imediatamente nos dados transformados incorretamente.

## Recomendação explicada

Recomendação é condicionada à evidência observada. Na ausência de labels adequados, descrever incerteza e a coleta necessária.

## O que entregar

Matriz de alternativas; causa provável; experimento challenger; critérios e plano de mudança.

## Como verificar

Entregar recomendação e plano reversível. Uma agenda de retreino não autoriza promover automaticamente modelo inferior.

## Contraponto

Ganho médio pode não justificar promoção. Se a premissa do caso mudar, reavaliar a decisão em vez de reutilizar a conclusão. Informar o que falta para passar de hipótese a evidência.
