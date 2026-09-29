# Guia de decisão: deployment-checklist

## Pergunta que esta skill resolve

Preparar plano de lançamento gradual e reversível com critérios, observabilidade e responsáveis.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Impacto de erro alto e feedback lento | Rollout limitado e guardrails antecipados | Ausência de alarme inicial não prova qualidade. |
| Mudança não reversível | Planejar contenção e compensação antes do lançamento | Rollback de software não desfaz ação externa. |
| Shadow diverge da produção | Investigar paridade | Modelo validado offline pode usar features diferentes. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Confundir aprovação analítica com permissão de deploy; omitir dono da reversão.

Esta skill prepara e verifica o lançamento. Não cria um processo de aprovação extra quando a autorização já existe, nem amplia seu escopo.

## Contrato de entrega

Plano de rollout; checklist com evidências; critérios de parada; rollback e responsáveis.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
