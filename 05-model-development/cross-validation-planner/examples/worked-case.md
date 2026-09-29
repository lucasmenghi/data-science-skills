# Caso trabalhado: cross-validation-planner

Cenário sintético de decisão; não é resultado executado em dados reais.

## Situação e análise

Um modelo de pacientes tem dez exames por pessoa. Se a aplicação atende pacientes novos, exames da mesma pessoa não atravessam treino e validação. Se acompanha os mesmos no futuro, o desenho precisa respeitar tempo e disponibilidade.

## Recomendação explicada

O número de folds é uma decisão de viés, variância e custo. Descrever o cenário que o resultado estima é mais importante que decorar a quantidade.

## O que entregar

Diagrama de folds; regras temporais/grupos; pipeline de seleção; agregação e limitações.

## Como verificar

Agregar métricas com pesos compatíveis com o estimando e mostrar dispersão/heterogeneidade; não tratar folds correlacionados como amostras independentes para IC ingênuo.

## Contraponto

Mesmo CV seleciona e estima com otimismo. Se a premissa do caso mudar, reavaliar a decisão em vez de reutilizar a conclusão. Informar o que falta para passar de hipótese a evidência.
