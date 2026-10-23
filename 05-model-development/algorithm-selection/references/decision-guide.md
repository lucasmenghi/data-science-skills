# Guia de decisão: algorithm-selection

## Pergunta que esta skill resolve

Escolher famílias de modelos por tarefa, dados, restrições e protocolo de comparação.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Dados tabulares moderados | Comparar linear regularizado e árvores/boosting | Deep learning não é padrão obrigatório. |
| Poucos rótulos e alta dimensionalidade | Regularização e representação parcimoniosa | Modelo muito flexível pode memorizar. |
| Série temporal | Baseline ingênuo/sazonal e modelos com covariáveis disponíveis | Não comparar por split aleatório. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Escolher algoritmo por popularidade; tratar todos os dados como iid; declarar vencedor sem comparação.

Selecionar algoritmo envolve capacidade e adequação, não rankings universais. A recomendação sem experimento é provisória.

## Contrato de entrega

Matriz de candidatos; hipóteses de ganho; protocolo justo; recomendação condicionada.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
