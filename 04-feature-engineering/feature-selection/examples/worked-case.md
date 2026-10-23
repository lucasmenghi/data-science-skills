# Caso trabalhado: feature-selection

Cenário sintético de decisão; não é resultado executado em dados reais.

## Situação e análise

Selecionar top-20 correlações em todos os dados antes da CV superestima a qualidade. Refazer ranking em cada treino de fold e comparar o pipeline completo com todas as features.

## Recomendação explicada

O produto da seleção é um procedimento reproduzível, não uma lista supostamente universal de melhores variáveis.

## O que entregar

Protocolo; conjuntos comparados; estabilidade; custo; conjunto escolhido e justificativa.

## Como verificar

Escolher conjunto parcimonioso dentro da incerteza da comparação; congelar e avaliar no teste final reservado.

## Contraponto

Diferença pontual pode ser ruído de seleção. Se a premissa do caso mudar, reavaliar a decisão em vez de reutilizar a conclusão. Informar o que falta para passar de hipótese a evidência.
