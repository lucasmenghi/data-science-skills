# Guia de decisão: target-definition

## Pergunta que esta skill resolve

Definir alvo supervisionado, elegibilidade e janelas temporais sem confundir censura com ausência de evento.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Janela futura ainda aberta | Excluir da avaliação binária madura ou modelar censura explicitamente | Tratar como zero reduz artificialmente a taxa do evento. |
| Evento ocorreu antes da previsão | Retirar da população em risco ou redefinir tarefa | O modelo não deve prever o que já aconteceu. |
| Fonte atualizada retroativamente | Usar versão disponível à época ou declarar limitação de reconstrução | event_time sozinho não comprova disponibilidade. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Rotular ausência de dado como negativo; usar evento futuro na elegibilidade.

Separar target válido de target útil: mesmo bem rotulado, pode chegar tarde para a ação. Janelas e latência são decisões do produto.

## Contrato de entrega

Contrato do alvo; SQL/pseudocódigo de rotulagem; calendário de maturação; tabela de casos de borda.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
