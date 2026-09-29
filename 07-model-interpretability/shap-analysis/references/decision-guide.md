# Guia de decisão: shap-analysis

## Pergunta que esta skill resolve

Planejar e interpretar explicações SHAP com background, escala de saída e dependências explícitos.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Saída em log-odds | Explicar nessa unidade ou converter com cuidado | Somar contribuições em log-odds não dá pontos percentuais. |
| Background muda | Reavaliar interpretação relativa | A mesma previsão pode ter atribuições diferentes. |
| Dependência forte | Explicitar convenção e comparar sensibilidade | Atribuições não resolvem automaticamente causalidade. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Usar gráfico sem verificar unidade; afirmar efeito individual causal; ignorar versão da API.

Antes de recomendar ação sobre uma feature, verificar se ela é acionável e se há evidência causal separada. Uma atribuição não é uma recomendação de intervenção.

## Contrato de entrega

Configuração do explicador; background; checagens; explicações locais/globais e limites.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
