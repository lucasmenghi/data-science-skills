# Caso trabalhado: aggregation-features

Cenário sintético de decisão; não é resultado executado em dados reais.

## Situação e análise

Grupo A tem 1 conversão em 2 contatos e B tem 9 em 98. Conversão total é 10/100, não a média simples de 50% e 9,18%. Documentar se a unidade desejada é contato ou grupo.

## Recomendação explicada

Verificar aditividade: estoques, percentuais e quantis não podem ser somados indiscriminadamente entre períodos ou entidades.

## O que entregar

Catálogo de medidas; SQL; invariantes de reconciliação; política para vazios.

## Como verificar

Reconciliar totais com dados de origem e testar decomposição por grupos; registrar aproximações de quantis/distinct em grandes volumes.

## Contraponto

Join pode inflar montantes. Se a premissa do caso mudar, reavaliar a decisão em vez de reutilizar a conclusão. Informar o que falta para passar de hipótese a evidência.
