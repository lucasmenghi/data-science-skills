# Guia de decisão: roi-estimation

## Pergunta que esta skill resolve

Estimar retorno de projeto com investimento, custos recorrentes, horizonte e cenários comparáveis.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Benefício começa depois do investimento | Modelar cronograma | ROI simples pode esconder atraso e caixa. |
| Custo zero ou indefinido | Não dividir silenciosamente | Métrica pode ser indefinida. |
| Premissas muito incertas | Usar sensibilidade e valor de informação | Mais casas decimais não aumentam confiança. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

ROI sem horizonte; margem confundida com receita; taxa de desconto inventada.

Comparabilidade exige a mesma definição de custos e benefícios entre opções. Métricas financeiras não substituem restrições estratégicas ou operacionais.

## Contrato de entrega

Fluxos/premissas; ROI definido; cenários; break-even; recomendação condicionada.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
