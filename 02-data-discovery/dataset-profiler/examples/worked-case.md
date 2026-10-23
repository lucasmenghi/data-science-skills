# Caso trabalhado: dataset-profiler

Cenário sintético de decisão; não é resultado executado em dados reais.

## Situação e análise

Missing de renda é 4% no total e 80% numa semana. O perfil segmentado sugere problema de ingestão; imputar mediana antes de investigar esconderia a mudança.

## Recomendação explicada

Perfil descreve o que foi lido, não garante qualidade semântica. Reportar aproximações de distinct e quantis quando usadas.

## O que entregar

Perfil por coluna e safra; escopo da amostra; anomalias priorizadas; consultas reproduzíveis.

## Como verificar

Entregar achados com contagens, denominadores, consultas e alcance da análise; propor investigação, não limpeza automática.

## Contraponto

A média global pode esconder quebra de fonte. Se a premissa do caso mudar, reavaliar a decisão em vez de reutilizar a conclusão. Informar o que falta para passar de hipótese a evidência.
