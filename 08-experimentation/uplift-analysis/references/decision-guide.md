# Guia de decisão: uplift-analysis

## Pergunta que esta skill resolve

Estimar heterogeneidade de efeito de tratamento e avaliar políticas de intervenção.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Alta chance de resposta sem tratamento | Pode haver pouco benefício incremental | Ranking de propensão não é ranking de uplift. |
| Propensão próxima de zero/um | Restringir estimando e investigar overlap | Pesos extremos produzem alta variância. |
| Dados observacionais | Explicitar confundimento residual e sensibilidade | Modelo sofisticado não cria identificação causal. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Features pós-tratamento; afirmar efeito individual conhecido; avaliar só AUC de resposta.

O efeito individual não é diretamente observado. Avaliação usa pressupostos e agregações coerentes com o desenho, com limites explícitos.

## Contrato de entrega

Estimando; hipóteses; modelos; avaliação de política; incerteza e plano confirmatório.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
