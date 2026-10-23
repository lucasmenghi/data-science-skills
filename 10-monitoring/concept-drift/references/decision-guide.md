# Guia de decisão: concept-drift

## Pergunta que esta skill resolve

Investigar mudanças na relação entre entradas e resultado usando rótulos maduros e hipóteses alternativas.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Rótulo ainda não chegou | Usar sinais antecipados como proxies declarados | Não afirmar concept drift comprovado. |
| Política altera quem é observado | Investigar seleção/feedback | Performance aparente pode refletir intervenção. |
| Erro subiu após mudança de dado | Auditar qualidade e disponibilidade primeiro | Retreino não corrige integração quebrada. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Detectar concept drift apenas olhando X; confundir prevalência com toda relação condicional.

Não existe observação direta do mecanismo causal apenas por uma série de métricas. Formular hipóteses e mostrar evidências compatíveis e conflitantes.

## Contrato de entrega

Diagnóstico por hipótese; evidências; limitações de rótulo; plano de resposta.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
