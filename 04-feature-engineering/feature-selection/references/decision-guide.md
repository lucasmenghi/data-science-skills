# Guia de decisão: feature-selection

## Pergunta que esta skill resolve

Selecionar features por utilidade fora da amostra, estabilidade e custo sem contaminar validação.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Features redundantes | Comparar seleção por grupos e custo | Importância dividida não prova irrelevância conjunta. |
| Filtro pelo alvo | Ajustar dentro dos folds | Selecionar antes do split revela informação dos rótulos de validação. |
| Ganho mínimo e instável | Preferir conjunto simples se atende requisitos | Diferença pontual pode ser ruído de seleção. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Selecionar pelo teste; remover uma variável só porque é pouco correlacionada individualmente.

O produto da seleção é um procedimento reproduzível, não uma lista supostamente universal de melhores variáveis.

## Contrato de entrega

Protocolo; conjuntos comparados; estabilidade; custo; conjunto escolhido e justificativa.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
