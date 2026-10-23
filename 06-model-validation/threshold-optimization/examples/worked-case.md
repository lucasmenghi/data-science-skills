# Caso trabalhado: threshold-optimization

Cenário sintético de decisão; não é resultado executado em dados reais.

## Situação e análise

Na validação, baixar o corte captura mais eventos mas dobra revisões além da capacidade. Escolher política factível, mesmo com recall menor; informar o custo de oportunidade.

No [CSV de quatro observações](validation-predictions.csv), os pares (rótulo, score) são (1; 0,9), (0; 0,8), (1; 0,8) e (0; 0,2). Com benefício 10 por verdadeiro positivo, custo 2 por falso positivo e demais custos zero, o utilitário produz:

| Política | Ações | TP | FP | Utilidade |
|---|---:|---:|---:|---:|
| Não agir | 0 | 0 | 0 | 0 |
| Score ≥ 0,9 | 1 | 1 | 0 | 10 |
| Score ≥ 0,8 | 3 | 2 | 1 | 18 |
| Score ≥ 0,2 | 4 | 2 | 2 | 16 |

Com capacidade 3, escolher 0,8 maximiza a utilidade empírica entre as políticas avaliadas. Com capacidade 2, o script escolhe 0,9 e deixa uma vaga: ele preserva os empates em 0,8. Uma política top-k exigiria outro critério de desempate, definido sem consultar os rótulos. Os números foram conferidos nos testes locais; a amostra é didática e não sustenta uma recomendação de produção.

## Recomendação explicada

Para probabilidade calibrada e custos constantes, derivar a decisão por utilidades comparadas. Não usar fórmula de limiar fora dessas hipóteses.

## O que entregar

Curva threshold-volume-utilidade; política escolhida; sensibilidade; avaliação final.

## Como verificar

Congelar a política e avaliar uma vez no teste; registrar processo de revisão e consequências da capacidade variável.

## Contraponto

Fórmula de custo probabilística exige interpretação adequada. Se a premissa do caso mudar, reavaliar a decisão em vez de reutilizar a conclusão. Informar o que falta para passar de hipótese a evidência.
