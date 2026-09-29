# Guia de decisão: lift-analysis

## Pergunta que esta skill resolve

Avaliar concentração de eventos em rankings e faixas operacionais sem confundir lift com efeito causal.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Lift alto em poucos casos | Mostrar contagens e incerteza | Uma faixa com um evento pode produzir razão extrema. |
| Empates no corte | Fixar desempate ou incluir faixa inteira | Resultado muda com ordenação incidental. |
| Prevalência muda | Reportar lift junto da precisão absoluta | Mesmo lift pode gerar volumes de eventos muito diferentes. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Confundir lift cumulativo e por faixa; usar resposta histórica tratada como efeito incremental.

Documentar se pesos representam amostragem ou valor de negócio. Uma razão sem denominador claro pode induzir decisão errada.

## Contrato de entrega

Tabela de decis/faixas; curvas de ganho; capacidade; comparação e limites.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
