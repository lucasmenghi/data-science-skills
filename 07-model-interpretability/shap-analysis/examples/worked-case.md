# Caso trabalhado: shap-analysis

Cenário sintético de decisão; não é resultado executado em dados reais.

## Situação e análise

Uma feature contribui +0,4 na escala de log-odds. Não dizer que elevou a chance em 40 pontos percentuais; mostrar a escala, baseline e transformação da saída final.

## Recomendação explicada

Antes de recomendar ação sobre uma feature, verificar se ela é acionável e se há evidência causal separada. Uma atribuição não é uma recomendação de intervenção.

## O que entregar

Configuração do explicador; background; checagens; explicações locais/globais e limites.

## Como verificar

Apresentar casos típicos e falhas, agregação global e limites. Valores SHAP descrevem atribuição do modelo sob convenção, não causalidade.

## Contraponto

Atribuições não resolvem automaticamente causalidade. Se a premissa do caso mudar, reavaliar a decisão em vez de reutilizar a conclusão. Informar o que falta para passar de hipótese a evidência.
