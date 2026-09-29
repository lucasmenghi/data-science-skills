# Caso trabalhado: temporal-validation

Cenário sintético de decisão; não é resultado executado em dados reais.

## Situação e análise

Em 01/07 se treina com alvos de 30 dias. Registros de 20/06 ainda não completaram a observação; uma extração posterior não autoriza tratá-los como disponíveis no treino histórico de 01/07.

## Recomendação explicada

Esta skill valida o dado temporal; `cross-validation-planner` escolhe o protocolo de estimação e `oot-validation` avalia o modelo congelado.

## O que entregar

Contrato de relógios; regras de maturação; auditoria de bordas; tabela de cortes válidos.

## Como verificar

Entregar contrato temporal e restrições para cross-validation/oot; lacunas de reconstrução precisam aparecer como limitação.

## Contraponto

Número fixo de linhas não equivale a intervalo fixo. Se a premissa do caso mudar, reavaliar a decisão em vez de reutilizar a conclusão. Informar o que falta para passar de hipótese a evidência.
