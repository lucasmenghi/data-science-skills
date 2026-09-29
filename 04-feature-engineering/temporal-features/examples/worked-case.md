# Caso trabalhado: temporal-features

Cenário sintético de decisão; não é resultado executado em dados reais.

## Situação e análise

Para uma previsão às 09h, uma compra de ontem recebida às 10h de hoje não pertence ao histórico disponível. O teste deve usar os dois relógios, não apenas a data da compra.

## Recomendação explicada

Reusar cálculo temporal exige preservar a convenção de borda; pequenas diferenças entre engines mudam o significado da feature.

## O que entregar

Especificação de features; SQL/Python; casos de borda; contrato de disponibilidade.

## Como verificar

Verificar manualmente exemplos nas bordas e paridade offline/serving; comparar janelas pela validação definida.

## Contraponto

Zero eventos não equivale a zero dias observados. Se a premissa do caso mudar, reavaliar a decisão em vez de reutilizar a conclusão. Informar o que falta para passar de hipótese a evidência.
