# Caso trabalhado: leakage-check

Cenário sintético de decisão; não é resultado executado em dados reais.

## Situação e análise

Modelo de atraso usa status de cobrança preenchido após inadimplência. Mesmo com split aleatório perfeito, a feature é impossível na decisão. Retirar e reconstruir avaliação temporal antes de interpretar queda de AUC.

## Recomendação explicada

Sem logs de disponibilidade, declarar risco não verificável. Diferenciar falha comprovada, suspeita e hipótese descartada.

## O que entregar

Matriz feature-disponibilidade; achados com evidência; impacto; correção e plano de reavaliação.

## Como verificar

Verificar seleção de modelo/threshold e uso repetido do teste. Propor avaliação nova quando o holdout já participou das decisões.

## Contraponto

A presença por si só não prova leakage. Se a premissa do caso mudar, reavaliar a decisão em vez de reutilizar a conclusão. Informar o que falta para passar de hipótese a evidência.
