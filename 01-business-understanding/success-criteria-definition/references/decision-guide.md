# Guia de decisão: success-criteria-definition

## Pergunta que esta skill resolve

Definir métricas e critérios de aceitação de negócio, modelo e operação com direção e incerteza explícitas.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Métrica é custo ou erro | Direção menor é melhor e limites ordenados nessa direção | Um avaliador que assume maior é melhor inverte a decisão. |
| Ganho estimado com alta incerteza | Coletar evidência ou limitar piloto | Ponto estimado acima da meta não prova superioridade. |
| Guardrail falha | Revisar mesmo com métrica principal favorável | Benefício médio não elimina falha operacional crítica. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Confundir limiar de modelo com meta de negócio; usar um único número como autorização de produção.

Limites de aceitação são locais ao contexto. O utilitário verifica valores e direção, mas não valida premissas, significância ou aprovação organizacional.

## Contrato de entrega

Matriz de métricas; baseline; limites justificados; plano de medição; decisão condicionada.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
