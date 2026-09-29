# Guia de decisão: retraining-advisor

## Pergunta que esta skill resolve

Decidir entre manter, recalibrar, corrigir dados, retreinar ou substituir uma solução.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Problema é probabilidade, ranking estável | Comparar recalibração | Retreino completo pode ser custo desnecessário. |
| Dados corrompidos | Corrigir origem antes de treinar | Aprender falha cristaliza o problema. |
| Novo modelo perde em grupo relevante | Investigar trade-off e guardrails | Ganho médio pode não justificar promoção. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Retreino periódico como garantia; promoção pelo menor erro de treino.

Recomendação é condicionada à evidência observada. Na ausência de labels adequados, descrever incerteza e a coleta necessária.

## Contrato de entrega

Matriz de alternativas; causa provável; experimento challenger; critérios e plano de mudança.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
