# Guia de decisão: ab-test-design

## Pergunta que esta skill resolve

Desenhar experimento controlado com estimando, randomização, potência e plano de análise.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Usuários influenciam uns aos outros | Randomizar clusters ou redes quando adequado | Independência individual seria hipótese falsa. |
| Exposição depende da adesão | Análise ITT responde ao efeito da oferta | Comparar só aderentes pode introduzir seleção. |
| Resultados vistos diariamente | Usar regra sequencial válida ou manter horizonte fixo | Parar no primeiro p pequeno altera erro de decisão. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Confundir não significância com equivalência; escolher MDE depois do resultado.

Testes exigem tamanho do efeito e incerteza, além de p-valor. Não assumir amostra normal e variância igual como requisito universal.

## Contrato de entrega

Protocolo; estimando; randomização; amostra; métricas; plano de análise e parada.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
