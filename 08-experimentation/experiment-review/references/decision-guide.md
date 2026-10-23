# Guia de decisão: experiment-review

## Pergunta que esta skill resolve

Revisar resultados experimentais quanto à integridade do desenho, estimação e decisão.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Proporções dos braços divergiram | Investigar instrumentação/seleção antes da leitura causal | Não corrigir apenas com teste de efeito. |
| Subgrupo vencedor encontrado depois | Marcar exploratório e buscar confirmação | Selecionar melhor recorte aumenta falso positivo. |
| IC inclui efeitos úteis e prejudiciais | Resultado inconclusivo para a decisão | Não é demonstração de efeito zero. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Escolher métrica favorável depois; ignorar guardrails; usar significância como único critério.

Um experimento tecnicamente válido ainda pode ter baixo valor prático ou população que não representa o rollout.

## Contrato de entrega

Parecer de integridade; estimativas; desvios; implicações e próxima decisão.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
