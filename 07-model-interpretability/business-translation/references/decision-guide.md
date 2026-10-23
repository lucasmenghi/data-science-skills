# Guia de decisão: business-translation

## Pergunta que esta skill resolve

Traduzir resultados e explicações de um modelo em implicações de negócio sem exagerar evidência.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| AUC melhorou | Traduzir em desempenho na política relevante | AUC sozinha não determina contatos úteis ou ganho. |
| Feature importante | Explicar associação usada pelo modelo | Não dizer que mudar a feature causará o resultado. |
| Público quer decisão | Dar recomendação com limite e próxima evidência | Relatório só descritivo deixa decisão implícita. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Converter métrica em lucro sem premissas; simplificar até alterar o significado.

Manter precisão mesmo com linguagem simples. A incerteza deve fazer parte da mensagem principal quando muda a decisão.

## Contrato de entrega

Mensagem executiva; exemplo operacional; recomendação; limites; referência técnica.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
