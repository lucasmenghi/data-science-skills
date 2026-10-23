# Guia de decisão: campaign-simulator

## Pergunta que esta skill resolve

Simular políticas de campanha sob orçamento, capacidade, efeito e custos explícitos.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Orçamento com custos variáveis | Otimizar valor/custo sob restrição apropriada | Top-k por score ignora custos. |
| Clientes de alta propensão | Verificar incrementalidade | Podem responder mesmo sem campanha. |
| Contatos repetidos | Modelar exposição e canibalização | Somar efeitos independentes pode exagerar ganho. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Tratar simulação como experimento realizado; enviar mensagens por implicação do pedido.

Execução da campanha é ação externa distinta. A simulação deve deixar claro quais efeitos são dados e quais são hipóteses.

## Contrato de entrega

Políticas; seleção simulada; orçamento; cenários de benefício; próximos testes.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
