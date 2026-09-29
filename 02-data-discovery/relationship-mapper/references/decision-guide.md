# Guia de decisão: relationship-mapper

## Pergunta que esta skill resolve

Investigar relações entre tabelas e entidades com cardinalidade, cobertura e consistência temporal.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Relação muda no tempo | Associar pela validade histórica | Dimensão atual pode reclassificar eventos passados. |
| Inner join perde grupo específico | Medir seleção e preferir preservação quando necessária | Cobertura alta no total pode esconder exclusão sistemática. |
| Chave não é única no domínio | Usar chave composta ou resolver ambiguidade | IDs de sistemas diferentes podem colidir. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Declarar chave estrangeira sem teste; usar nome como chave universal.

O mapa registra relações observadas e confirmadas; associação entre entidades não estabelece relação causal entre variáveis.

## Contrato de entrega

Mapa entidade-relação; contratos de join; cobertura e perdas por segmento.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
