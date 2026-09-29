# Guia de decisão: data-quality-audit

## Pergunta que esta skill resolve

Auditar regras de qualidade por impacto, distinguindo falha técnica, exceção legítima e ausência de cobertura.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Regra sem confirmação de negócio | Marcar suspeita e pedir evidência | Não apagar dados legítimos por preferência estética. |
| Falha numa partição | Conter e reprocessar escopo específico | Não bloquear ou reescrever todo o histórico sem necessidade. |
| Erro recorrente após correção | Mover controle para a origem | Uma limpeza downstream permanente pode mascarar causa raiz. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Métrica global sem segmentação; threshold de qualidade inventado; alterações destrutivas sem escopo.

A severidade depende do consumidor. Missing em uma feature opcional difere de chave de transação ausente; explicar essa diferença ao usuário.

## Contrato de entrega

Inventário de checks; evidência de falhas; impacto; plano de correção e prevenção.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
