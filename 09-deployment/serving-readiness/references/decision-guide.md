# Guia de decisão: serving-readiness

## Pergunta que esta skill resolve

Avaliar prontidão de inferência batch ou online sob contrato, carga e falhas reais.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Decisão diária | Batch pode ser suficiente e mais simples | Online aumenta dependências sem benefício necessário. |
| Ferramenta externa falha | Fallback e timeout com efeito documentado | Retry ilimitado amplia custo e latência. |
| Latência média aceitável | Medir cauda e pico | p50 não garante SLO p95. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Testar apenas exemplo feliz; considerar notebook executado como serviço pronto.

Se não houver ambiente/carga representativa, declarar performance não verificada em vez de extrapolar benchmark pequeno.

## Contrato de entrega

Contrato de serving; testes; SLO; dependências; falhas e recomendação de prontidão.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
