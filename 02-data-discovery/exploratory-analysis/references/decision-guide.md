# Guia de decisão: exploratory-analysis

## Pergunta que esta skill resolve

Conduzir análise exploratória orientada a perguntas com comparações válidas e achados acionáveis.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Média mudou | Decompor mudança dentro dos grupos e mudança de composição | Pode ser mistura populacional, não comportamento individual. |
| Muitos segmentos explorados | Registrar exploração e validar em nova amostra | O melhor segmento pode ser acaso de seleção. |
| Correlação forte | Investigar tempo, medição e confundimento | Não propor causalidade automaticamente. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Descrever gráfico sem implicação; confundir ausência de evidência com ausência de efeito.

Mesmo sem treinar modelo, preservar uma amostra confirmatória quando os achados guiarão decisões de alto impacto ou seleção de features.

## Contrato de entrega

Perguntas; perfil mínimo; achados priorizados; gráficos explicados; hipóteses e próximos testes.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
