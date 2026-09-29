# Guia de decisão: imbalance-strategy

## Pergunta que esta skill resolve

Tratar desbalanceamento de classes de acordo com prevalência, decisão e custo dos erros.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Ranking já atende capacidade | Ajustar política/threshold antes de reamostrar | Balancear pode não resolver a decisão. |
| Probabilidade será usada em expectativa | Verificar calibração sob prevalência de uso | Probabilidades após reamostragem podem não refletir população. |
| Sintetização mistura grupos/tempo | Rejeitar ou restringir ao treino apropriado | Exemplos artificiais podem ser impossíveis. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

SMOTE antes do split; otimizar acurácia em classe rara; confundir class weight com calibração garantida.

Aumentar recall tem consequências de capacidade e falsos positivos; discutir a ação associada antes de concluir melhora.

## Contrato de entrega

Diagnóstico; alternativas; avaliação na população-alvo; threshold e calibração.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
