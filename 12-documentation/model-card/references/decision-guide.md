# Guia de decisão: model-card

## Pergunta que esta skill resolve

Produzir model card rastreável com usos, avaliação, limitações e responsabilidades.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Métrica sem protocolo | Solicitar avaliação ou marcar não verificável | Número isolado não demonstra qualidade. |
| Uso novo fora da população | Exigir nova evidência de adequação | Card antiga não autoriza extrapolação. |
| Ausência de análise por grupo | Documentar lacuna | Não afirmar equidade não avaliada. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Inventar dados/métricas; preencher todas as seções com frases vagas.

Uma model card comunica evidência e limites; não é certificação de conformidade ou segurança.

## Contrato de entrega

Model card versionada; fontes de evidência; pendências e processo de atualização.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
