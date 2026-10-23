# Guia de decisão: hyperparameter-planner

## Pergunta que esta skill resolve

Planejar busca de hiperparâmetros com orçamento, espaço coerente e avaliação independente.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Poucos hiperparâmetros discretos | Grade curta informada | Grade gigante desperdiça orçamento em dimensões pouco úteis. |
| Escalas variam por ordens de grandeza | Distribuição log quando apropriada | Passos lineares podem quase ignorar região útil. |
| Melhor trial isolado | Reavaliar estabilidade e escolher por evidência | Vencedor pode ser sorte de seed ou fold. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Ajustar espaço após olhar teste; omitir trials ruins; usar todas as CPUs sem avaliar concorrência.

Otimização mais sofisticada não corrige métrica errada, leakage ou dado pouco representativo.

## Contrato de entrega

Plano de busca; orçamento; espaço; protocolo; registro de trials e decisão.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
