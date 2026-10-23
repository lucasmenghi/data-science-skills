# Guia de decisão: leakage-check

## Pergunta que esta skill resolve

Auditar vazamento temporal, de rótulo, de entidades e de seleção ao longo de um pipeline.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Feature registrada após resultado | Excluir ou reconstruir versão disponível | Forte associação pode ser efeito do evento. |
| Transformação ajustada na base inteira | Refazer pipeline dentro do treino/folds | Ausência de alvo na transformação não garante independência. |
| Mesmo cliente em treino e futuro | Avaliar uso real e dependência temporal | A presença por si só não prova leakage. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Chamar qualquer correlação de leakage; confiar só em nomes de colunas; prometer Pipeline elimina todo vazamento.

Sem logs de disponibilidade, declarar risco não verificável. Diferenciar falha comprovada, suspeita e hipótese descartada.

## Contrato de entrega

Matriz feature-disponibilidade; achados com evidência; impacto; correção e plano de reavaliação.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
