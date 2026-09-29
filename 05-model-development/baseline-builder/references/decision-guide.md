# Guia de decisão: baseline-builder

## Pergunta que esta skill resolve

Construir referência simples e reproduzível para demonstrar o valor adicional de modelos.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Classe rara | Medir recall/precision e ação, além de acurácia | Sempre negativo pode parecer excelente pela acurácia. |
| Forecasting com sazonalidade | Usar último período comparável como referência | Média global é referência fraca. |
| Já existe regra operacional | Reproduzir elegibilidade e capacidade da regra | Comparar políticas em populações diferentes é injusto. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Escolher baseline propositalmente ruim; usar média do teste para prever teste.

O baseline inclui tratamento de dados e política de ação; um número de referência isolado não garante comparação reproduzível.

## Contrato de entrega

Baseline executável ou especificado; resultados; cobertura; custo e limite de comparação.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
