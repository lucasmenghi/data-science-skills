# Guia de decisão: threshold-optimization

## Pergunta que esta skill resolve

Escolher limiar ou política top-k por utilidade e capacidade, preservando teste final.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Custo muda por cliente | Política de valor esperado individual pode superar corte único | Uma probabilidade alta não implica maior valor. |
| Capacidade fixa | Top-k com desempate e volume definidos | Corte de score não garante número estável. |
| Scores não calibrados | Usar avaliação empírica da política ou calibrar | Fórmula de custo probabilística exige interpretação adequada. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Escolher corte no teste; fixar 0,5 sem justificativa; omitir custos de verdadeiros positivos.

Para probabilidade calibrada e custos constantes, derivar a decisão por utilidades comparadas. Não usar fórmula de limiar fora dessas hipóteses.

## Contrato de entrega

Curva threshold-volume-utilidade; política escolhida; sensibilidade; avaliação final.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
