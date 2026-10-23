# Guia de decisão: aggregation-features

## Pergunta que esta skill resolve

Construir agregações em SQL/Python com denominadores, granularidade e cobertura explícitos.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Média de taxas com denominadores diferentes | Recalcular razão de somas ou justificar peso | Média simples responde a outra pergunta. |
| Zero registros | Distinguir ausência de atividade e falha de cobertura | COALESCE zero sem contexto cria sinal falso. |
| Dimensão muitos-para-muitos | Definir alocação ou agregar antes | Join pode inflar montantes. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Somar saldos de snapshots como fluxo; contar linhas após join como eventos únicos.

Verificar aditividade: estoques, percentuais e quantis não podem ser somados indiscriminadamente entre períodos ou entidades.

## Contrato de entrega

Catálogo de medidas; SQL; invariantes de reconciliação; política para vazios.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
