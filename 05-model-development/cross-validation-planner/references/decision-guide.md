# Guia de decisão: cross-validation-planner

## Pergunta que esta skill resolve

Desenhar validação cruzada que reproduza a generalização desejada e a dependência dos dados.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Várias linhas por pessoa e previsão para pessoas novas | Separar grupos | Estratificação por classe não resolve dependência por pessoa. |
| Prever futuro | Walk-forward com relógio e alvos disponíveis | K-fold embaralhado pode usar futuro. |
| Comparar processo de tuning | Nested CV ou holdout externo | Mesmo CV seleciona e estima com otimismo. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Usar cinco folds como padrão sem critério; exigir grupos separados em todo problema; IC baseado só em desvio entre folds.

O número de folds é uma decisão de viés, variância e custo. Descrever o cenário que o resultado estima é mais importante que decorar a quantidade.

## Contrato de entrega

Diagrama de folds; regras temporais/grupos; pipeline de seleção; agregação e limitações.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
