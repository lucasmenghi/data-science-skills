# Guia de decisão: oot-validation

## Pergunta que esta skill resolve

Avaliar modelo congelado em períodos posteriores com maturação, cobertura e mudança populacional.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Alvos recentes incompletos | Aguardar maturação ou usar análise apropriada de censura | Taxa baixa pode ser simples atraso. |
| Pipeline mudou junto com população | Auditar paridade antes de culpar modelo | Retreinar não corrige unidade errada. |
| Uma única safra boa | Coletar outras condições temporais | Não garante robustez sazonal. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Retunar no OOT e manter selo de teste; escolher retrospectivamente o melhor mês.

Validação temporal estima condições observadas, não garante resistência a todo regime futuro. Explicar limites de cobertura.

## Contrato de entrega

Plano OOT; tabela por safra; decomposição de falhas; recomendação de continuidade.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
