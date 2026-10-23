# Guia de decisão: categorical-encoding

## Pergunta que esta skill resolve

Escolher codificação categórica compatível com semântica, cardinalidade, modelo e categorias futuras.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Nominal de baixa cardinalidade | One-hot é baseline interpretável | Ordinal arbitrário pode impor estrutura inexistente. |
| Ordinal confirmada | Mapeamento com ordem e tratamento de novos níveis | Ordenação alfabética não é ordem de negócio. |
| Alta cardinalidade | Comparar nativo/hashing/target encoding | Memorização de IDs e vazamento são riscos distintos. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

LabelEncoder em features por conveniência; média do alvo calculada antes da CV.

Não aplicar tratamento de categorias novas que altere o número ou significado das colunas sem atualizar a assinatura do modelo.

## Contrato de entrega

Contrato de encoding; vocabulário/fallback; protocolo; comparação.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
