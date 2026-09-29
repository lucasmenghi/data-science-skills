# Guia de decisão: model-review

## Pergunta que esta skill resolve

Revisar evidências de um modelo do framing à operação e classificar achados acionáveis.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Leakage comprovado | Invalidar conclusão afetada e refazer avaliação | Não apenas remover coluna e preservar métrica antiga. |
| Documentação ausente | Solicitar artefato ou marcar não verificável | Ausência de evidência não é prova automática de bug. |
| Pequena melhora sem estabilidade | Comparar incerteza e custo | Ranking pontual não basta para trocar solução. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Revisão só de estilo; emitir aprovação global com arquivos parciais.

Esta é revisão de trabalho real. Para treino de defesa de entrevista, usar `ds-reviewer`; não submeter o usuário a prova durante revisão profissional.

## Contrato de entrega

Parecer com escopo; achados rastreáveis; severidade; verificações e decisão condicionada.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
