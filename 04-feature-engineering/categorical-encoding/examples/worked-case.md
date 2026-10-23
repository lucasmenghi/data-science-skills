# Caso trabalhado: categorical-encoding

Cenário sintético de decisão; não é resultado executado em dados reais.

## Situação e análise

Escolaridade possui ordem confirmada, enquanto cidade não. Criar ordem explícita para a primeira e comparar estratégias para cidade; um encoder de alvo não deve ser aplicado cegamente às features.

## Recomendação explicada

Não aplicar tratamento de categorias novas que altere o número ou significado das colunas sem atualizar a assinatura do modelo.

## O que entregar

Contrato de encoding; vocabulário/fallback; protocolo; comparação.

## Como verificar

Comparar validação, custo e estabilidade; documentar que códigos inteiros não implicam distância ou ordem real.

## Contraponto

Memorização de IDs e vazamento são riscos distintos. Se a premissa do caso mudar, reavaliar a decisão em vez de reutilizar a conclusão. Informar o que falta para passar de hipótese a evidência.
