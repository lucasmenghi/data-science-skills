# Caso trabalhado: data-drift

Cenário sintético de decisão; não é resultado executado em dados reais.

## Situação e análise

Entradas mudam porque uma nova região foi incorporada. Separar mistura de populações de falha de ETL e verificar qualidade nesse grupo antes de concluir que o modelo envelheceu.

## Recomendação explicada

Testes de distribuição não revelam sozinhos causa ou relevância para a decisão. Relatar o que foi observado e o que segue desconhecido.

## O que entregar

Plano de referência; métricas de mudança; causas; severidade operacional e ação.

## Como verificar

Investigar causas upstream e ligar alertas a ações e métricas de qualidade quando disponíveis; drift isolado não autoriza retreino.

## Contraponto

Cortes populares não são verdades universais. Se a premissa do caso mudar, reavaliar a decisão em vez de reutilizar a conclusão. Informar o que falta para passar de hipótese a evidência.
