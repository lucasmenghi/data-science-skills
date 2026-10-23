# Caso trabalhado: schema-mapper

Cenário sintético de decisão; não é resultado executado em dados reais.

## Situação e análise

Duas fontes possuem amount, uma em centavos e outra em unidades monetárias. O mapeamento documenta a escala e exige reconciliação após conversão, evitando uma diferença de 100 vezes.

## Recomendação explicada

Quando a semântica não está confirmada, produzir contrato provisório com dono da dúvida. Tipagem válida não prova significado correto.

## O que entregar

Dicionário; mapeamento fonte-destino; chaves candidatas; regras de compatibilidade.

## Como verificar

Propor verificações de compatibilidade e responsáveis por alterações; construir dicionário com exemplos sintéticos e campos desconhecidos explícitos.

## Contraponto

Aceitar nova coluna não implica aceitar novo significado. Se a premissa do caso mudar, reavaliar a decisão em vez de reutilizar a conclusão. Informar o que falta para passar de hipótese a evidência.
