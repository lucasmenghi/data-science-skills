# Guia de decisão: business-hypothesis-builder

## Pergunta que esta skill resolve

Formular e priorizar hipóteses descritivas, preditivas e causais com desenho de verificação adequado.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Associação histórica sugere intervenção | Desenhar identificação causal antes de recomendar efeito | Predizer resposta não estima benefício do tratamento. |
| Hipótese gera feature | Testar ganho fora da amostra com custo de disponibilidade | Correlação univariada baixa não elimina utilidade condicional. |
| Hipóteses muitas e dados poucos | Exploração marcada e confirmação em nova amostra | Não transformar buscas repetidas em um teste confirmatório. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Ranking de pesos como prova estatística; testar até obter p pequeno.

Preferir uma hipótese que possa mudar a decisão a uma lista extensa de correlações. O script de priorização usa pesos convencionais ajustáveis e não estima probabilidade de sucesso.

## Contrato de entrega

Backlog de hipóteses; tipo; desenho; evidência necessária; prioridade e critério de abandono.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
