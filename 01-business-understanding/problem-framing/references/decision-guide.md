# Guia de decisão: problem-framing

## Pergunta que esta skill resolve

Transformar uma demanda de negócio em decisão analítica, comparando regra, análise, experimento e ML.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Pergunta é o que aconteceu | Análise descritiva com denominadores e períodos comparáveis | Modelo preditivo adicionaria complexidade sem responder melhor. |
| Pergunta é quem deve receber uma ação | Separar propensão ao resultado do efeito incremental da ação | Um cliente de alto risco pode não responder ao tratamento. |
| Nenhuma ação ou dado em tempo útil | Reformular o produto ou documentar inviabilidade | Não treinar um modelo apenas para atender um pedido nominal. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Confundir desempenho preditivo com mudança de negócio; deixar população e ação implícitas.

Um resultado útil pode ser concluir que um dashboard ou ajuste de processo atende melhor. Exigir decisão documentada, não a presença de ML.

## Contrato de entrega

Mapa da decisão; alternativas; escopo e não escopo; premissas; proposta de avaliação.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
