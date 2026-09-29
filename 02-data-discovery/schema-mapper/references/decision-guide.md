# Guia de decisão: schema-mapper

## Pergunta que esta skill resolve

Mapear semântica, tipos, chaves e contratos de dados entre fontes e camadas analíticas.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Campo monetário em float | Avaliar representação decimal e arredondamento acordado | Não alterar precisão silenciosamente. |
| IDs com zeros à esquerda | Preservar representação textual se zeros forem semânticos | Cast inteiro pode colapsar entidades. |
| Schema drift | Classificar adição compatível versus quebra de tipo/semântica | Aceitar nova coluna não implica aceitar novo significado. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Inferir regra apenas pelo nome; inventar schema de tabela não acessível.

Quando a semântica não está confirmada, produzir contrato provisório com dono da dúvida. Tipagem válida não prova significado correto.

## Contrato de entrega

Dicionário; mapeamento fonte-destino; chaves candidatas; regras de compatibilidade.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
