# Caso trabalhado: granularity-check

Cenário sintético de decisão; não é resultado executado em dados reais.

## Situação e análise

Um cliente tem duas compras e três contatos. Somar compras após juntar diretamente produz seis linhas e triplica o total. Agregar compras por cliente e contatos por cliente mantém cada medida na unidade correta.

## Recomendação explicada

Preservar registros legítimos e expor ambiguidades. Uma junção pode manter contagem e ainda ligar a entidade errada.

## O que entregar

Contrato de grão; cardinalidades; invariantes; SQL de diagnóstico e correção.

## Como verificar

Entregar diagnóstico com contraexemplo e consulta corrigida, testando chaves nulas, múltiplos eventos e linhas sem correspondência.

## Contraponto

Média por linha não equivale a média por cliente. Se a premissa do caso mudar, reavaliar a decisão em vez de reutilizar a conclusão. Informar o que falta para passar de hipótese a evidência.
