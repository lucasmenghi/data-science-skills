# Guia de decisão: feature-importance

## Pergunta que esta skill resolve

Interpretar importância de features como dependência do modelo sob método e população definidos.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Features correlacionadas | Analisar grupos e ablação conjunta | Permutar uma só pode subestimar dependência compartilhada. |
| Impureza em árvores | Complementar com avaliação independente | Alta cardinalidade pode favorecer ranking por impureza. |
| Coeficientes lineares | Considerar escala e colinearidade | Magnitude bruta não permite comparação automática. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Importância como causalidade; explicar modelo sem desempenho útil; ranking sem definição de método.

Importância depende do modelo, métrica e distribuição. Não descreve uma propriedade intrínseca e imutável da variável.

## Contrato de entrega

Método; população; ranking com estabilidade; limitações e implicação.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
