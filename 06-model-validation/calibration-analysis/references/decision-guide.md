# Guia de decisão: calibration-analysis

## Pergunta que esta skill resolve

Avaliar e ajustar probabilidades com dados independentes e diagnóstico por faixa/população.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Poucos eventos | Método menos flexível e intervalos amplos | Isotônico pode sobreajustar. |
| Reamostragem no treino | Verificar probabilidades na prevalência de uso | Ranking útil pode coexistir com probabilidades distorcidas. |
| Calibração global boa | Inspecionar segmentos relevantes com suporte | Média pode esconder erros opostos. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Calibrar e medir no mesmo conjunto; assumir Brier é medida pura de calibração.

Uma curva depende do binning e da amostra; poucas observações por faixa limitam o que se pode concluir.

## Contrato de entrega

Reliability diagram/tabela; losses; comparação; método e avaliação independente.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
