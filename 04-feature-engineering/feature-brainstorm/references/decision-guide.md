# Guia de decisão: feature-brainstorm

## Pergunta que esta skill resolve

Propor features por hipótese de mecanismo, disponibilidade e custo de manutenção.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Feature forte mas indisponível a tempo | Redesenhar proxy ou descartar | Ganho retrospectivo não compensa impossibilidade operacional. |
| Muitas variantes de janela | Testar famílias com validação protegida | Seleção repetida aumenta otimismo. |
| Sinal difícil de manter | Comparar ganho marginal com custo e fragilidade | Mais features não significa melhor produto. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Gerar milhares de colunas sem mecanismo; confundir correlação com requisito obrigatório.

Restrições de privacidade e uso devem estar ligadas às fontes reais; não solicitar atributos sensíveis apenas para ampliar o espaço de busca.

## Contrato de entrega

Backlog de hipóteses; especificações; priorização; plano de ablação.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
