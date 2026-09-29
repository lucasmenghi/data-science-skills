# Caso trabalhado: target-definition

Cenário sintético de decisão; não é resultado executado em dados reais.

## Situação e análise

Em 01/03, observar histórico anterior e prever cancelamento nos próximos 30 dias. Uma extração em 10/03 não permite rotular como negativos todos os que ainda não cancelaram. Marcar como pendentes e definir a primeira extração que completa a janela e o atraso de registro.

## Recomendação explicada

Separar target válido de target útil: mesmo bem rotulado, pode chegar tarde para a ação. Janelas e latência são decisões do produto.

## O que entregar

Contrato do alvo; SQL/pseudocódigo de rotulagem; calendário de maturação; tabela de casos de borda.

## Como verificar

Validar casos manuais nas bordas, múltiplos contratos e eventos tardios. Comparar taxas por safra antes de liberar a tabela de rótulos.

## Contraponto

event_time sozinho não comprova disponibilidade. Se a premissa do caso mudar, reavaliar a decisão em vez de reutilizar a conclusão. Informar o que falta para passar de hipótese a evidência.
