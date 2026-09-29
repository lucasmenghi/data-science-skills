# Guia de decisão: temporal-features

## Pergunta que esta skill resolve

Construir features temporais point-in-time com janelas, lags e disponibilidade reproduzíveis.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Lag por posição com tempo irregular | Reindexar ou usar janela baseada em tempo | Linha anterior pode estar muito distante. |
| Evento antigo chega tarde | Filtrar também available_at | O passado cronológico pode ser futuro informacional. |
| Histórico curto | Indicador de cobertura e fallback acordado | Zero eventos não equivale a zero dias observados. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Rolling inclui linha-alvo; usar total do mês ainda não fechado.

Reusar cálculo temporal exige preservar a convenção de borda; pequenas diferenças entre engines mudam o significado da feature.

## Contrato de entrega

Especificação de features; SQL/Python; casos de borda; contrato de disponibilidade.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
