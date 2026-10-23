# Caso trabalhado: algorithm-selection

Cenário sintético de decisão; não é resultado executado em dados reais.

## Situação e análise

Um modelo complexo melhora AUC em 0,002 num único split, mas demora dez vezes mais para servir. Verificar variabilidade e custo antes de substituir a alternativa simples.

## Recomendação explicada

Selecionar algoritmo envolve capacidade e adequação, não rankings universais. A recomendação sem experimento é provisória.

## O que entregar

Matriz de candidatos; hipóteses de ganho; protocolo justo; recomendação condicionada.

## Como verificar

Usar resultados e incerteza para escolher; documentar quando interpretação, latência ou estabilidade justificam perder pequena performance pontual.

## Contraponto

Não comparar por split aleatório. Se a premissa do caso mudar, reavaliar a decisão em vez de reutilizar a conclusão. Informar o que falta para passar de hipótese a evidência.
