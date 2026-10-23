# Guia de decisão: metric-selection

## Pergunta que esta skill resolve

Escolher métricas alinhadas à decisão, distinguindo discriminação, calibração, erro e utilidade.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Probabilidades orientam decisão de custo | Avaliar calibração e loss própria além de AUC | Boa ordenação não garante valores confiáveis. |
| Erro percentual e zeros | Escolher alternativa ou domínio explicitamente | MAPE é indefinida em zero e distorce pequenos denominadores. |
| Capacidade limitada | Precision/recall/lift em k ou orçamento | Threshold fixo pode exceder operação. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Tratar AP como qualquer integração de PR; R² sempre entre zero e um; AUC como lucro.

Métrica sem população, período e política é ambígua. Taxas macro e micro respondem a ponderações diferentes.

## Contrato de entrega

Contrato de métricas; baseline; fórmulas; avaliação por segmentos e interpretação.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
