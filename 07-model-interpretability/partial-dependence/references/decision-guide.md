# Guia de decisão: partial-dependence

## Pergunta que esta skill resolve

Analisar PDP/ICE e alternativas sem ignorar suporte dos dados e interações.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Correlação forte entre features | Restringir domínio e considerar ALE/condicionais | PDP pode avaliar combinações não observadas. |
| Curva média quase plana | Inspecionar ICE/interações | Efeitos opostos podem cancelar na média. |
| Extremos pouco observados | Marcar extrapolação e limitar conclusão | Linha suave não cria suporte empírico. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Curva preditiva como dose-resposta causal; esconder densidade do eixo.

A pergunta respondida depende de como as demais variáveis foram mantidas ou integradas. Explicar esse procedimento em linguagem comum.

## Contrato de entrega

Curvas ou tabelas; domínio suportado; heterogeneidade; limites e interpretação.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
