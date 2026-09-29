# Caso trabalhado: missing-value-strategy

Cenário sintético de decisão; não é resultado executado em dados reais.

## Situação e análise

Renda só é informada por parte dos clientes. Comparar mediana com indicador de ausência e suporte nativo do modelo, medindo grupos. Não afirmar que a imputação recupera a renda verdadeira.

## Recomendação explicada

Excluir linhas muda a população atendida. Explicar cobertura perdida e reconhecer que qualidade preditiva não identifica o mecanismo de missing.

## O que entregar

Matriz de tratamentos; hipótese do mecanismo; experimento comparativo; política de fallback.

## Como verificar

Medir desempenho e comportamento por padrão de ausência, incluindo aumento de missing em produção. Documentar monitoramento e limites.

## Contraponto

Imputar pode esconder indisponibilidade upstream. Se a premissa do caso mudar, reavaliar a decisão em vez de reutilizar a conclusão. Informar o que falta para passar de hipótese a evidência.
