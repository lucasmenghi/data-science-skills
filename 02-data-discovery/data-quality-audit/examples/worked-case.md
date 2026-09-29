# Caso trabalhado: data-quality-audit

Cenário sintético de decisão; não é resultado executado em dados reais.

## Situação e análise

Data de liquidação anterior à compra aparece em 0,2% dos registros. Antes de rejeitar, verificar fuso, estornos e significado dos campos; só então classificar inconsistência e isolar exemplos.

## Recomendação explicada

A severidade depende do consumidor. Missing em uma feature opcional difere de chave de transação ausente; explicar essa diferença ao usuário.

## O que entregar

Inventário de checks; evidência de falhas; impacto; plano de correção e prevenção.

## Como verificar

Propor contrato executável e alertas acionáveis com dono, prazo e condição de retorno, distinguindo checks executados dos planejados.

## Contraponto

Uma limpeza downstream permanente pode mascarar causa raiz. Se a premissa do caso mudar, reavaliar a decisão em vez de reutilizar a conclusão. Informar o que falta para passar de hipótese a evidência.
