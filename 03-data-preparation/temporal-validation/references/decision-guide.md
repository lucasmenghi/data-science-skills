# Guia de decisão: temporal-validation

## Pergunta que esta skill resolve

Verificar consistência temporal e maturação de dados antes de estabelecer folds e avaliação futura.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Backfill corrige meses passados | Usar histórico de versões quando disponível | A tabela atual pode representar informação que não existia. |
| Janela do alvo atravessa corte de treino | Purgar exemplos não observáveis ou ajustar corte | Gap não é número arbitrário de dias. |
| Frequências irregulares | Basear corte em timestamps reais | Número fixo de linhas não equivale a intervalo fixo. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Usar só event_time; confundir ordenação com garantia de ausência de futuro.

Esta skill valida o dado temporal; `cross-validation-planner` escolhe o protocolo de estimação e `oot-validation` avalia o modelo congelado.

## Contrato de entrega

Contrato de relógios; regras de maturação; auditoria de bordas; tabela de cortes válidos.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
