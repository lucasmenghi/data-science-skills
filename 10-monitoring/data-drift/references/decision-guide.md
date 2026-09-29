# Guia de decisão: data-drift

## Pergunta que esta skill resolve

Detectar e investigar mudanças nas entradas e na cobertura sem presumir queda de qualidade.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Amostra enorme | Priorizar magnitude e impacto, não só p-valor | Diferença irrelevante pode ser estatisticamente detectável. |
| Mudança sazonal | Comparar período equivalente e histórico | Referência fixa inadequada gera alarmes recorrentes. |
| PSI alto | Inspecionar bins, zeros e origem | Cortes populares não são verdades universais. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Drift igual a erro; limiar PSI universal; retreino automático para qualquer mudança.

Testes de distribuição não revelam sozinhos causa ou relevância para a decisão. Relatar o que foi observado e o que segue desconhecido.

## Contrato de entrega

Plano de referência; métricas de mudança; causas; severidade operacional e ação.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
