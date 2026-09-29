# Guia de decisão: performance-monitoring

## Pergunta que esta skill resolve

Definir monitoramento de qualidade, política e operação com coortes maduras e ações claras.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Métrica por data de chegada do label | Reagrupar por coorte de previsão | Misturar atraso com qualidade distorce tendência. |
| Muitos subgrupos pequenos | Mostrar incerteza e suprimir conclusão sem suporte | Alarme por flutuação aumenta fadiga. |
| Latência normal e cobertura baixa | Monitorar ambos | Serviço rápido que não atende parte da população não está saudável. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Dashboard sem ação/dono; usar labels imaturos; comparar versões em públicos diferentes.

Monitoramento útil precisa ligar sintoma a decisão e evidência de recuperação. Um gráfico por si só não define processo operacional.

## Contrato de entrega

Contrato de logs; painel/métricas; regras de maturação; alertas e runbook.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
