# Guia de decisão: outlier-investigation

## Pergunta que esta skill resolve

Investigar valores extremos antes de decidir corrigir, limitar, transformar ou preservar.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Erro de unidade comprovado | Corrigir na origem ou transformação rastreável | Excluir perde sinal e deixa falha reaparecer. |
| Evento raro de interesse | Preservar e avaliar separadamente | Remover pode apagar exatamente a classe-alvo. |
| Cauda legítima prejudica loss | Comparar transformação e loss robusta | Caps modificam o problema e exigem justificativa. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Z-score automático em distribuição muito assimétrica; remover anomalias do conjunto de detecção de anomalia.

Anomalia é relativa à referência e não sinônimo de erro, fraude ou evento causal. Contexto e custo orientam o tratamento.

## Contrato de entrega

Inventário de extremos; causas; alternativas; análise de sensibilidade; regras versionadas.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
