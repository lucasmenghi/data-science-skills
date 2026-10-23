# Caso trabalhado: imbalance-strategy

Cenário sintético de decisão; não é resultado executado em dados reais.

## Situação e análise

Treinar com 50% positivos por oversampling e testar também em 50% não mostra a precisão esperada quando produção tem 1%. Preservar prevalência relevante na avaliação e reportar a diferença.

## Recomendação explicada

Aumentar recall tem consequências de capacidade e falsos positivos; discutir a ação associada antes de concluir melhora.

## O que entregar

Diagnóstico; alternativas; avaliação na população-alvo; threshold e calibração.

## Como verificar

Comparar recall/precision, custos e segmentos; escolher threshold em validação e documentar fallback.

## Contraponto

Exemplos artificiais podem ser impossíveis. Se a premissa do caso mudar, reavaliar a decisão em vez de reutilizar a conclusão. Informar o que falta para passar de hipótese a evidência.
