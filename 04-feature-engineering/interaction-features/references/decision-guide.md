# Guia de decisão: interaction-features

## Pergunta que esta skill resolve

Projetar interações, razões e transformações com justificativa e controle de complexidade.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Razão com denominador próximo de zero | Definir domínio e fallback explícitos | Adicionar epsilon arbitrário pode gerar valores sem significado. |
| Modelo linear insuficiente | Testar interação motivada e regularizada | Produtos indiscriminados ampliam seleção oportunista. |
| Árvores já capturam parte do padrão | Exigir ganho adicional ou simplificação | Duplicar expressividade pode não ajudar. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Criar relação matemática sem sentido de negócio; interpretar interação preditiva como mecanismo causal.

Uma feature derivada precisa de contrato próprio: unidade, domínio, disponibilidade e erro aceitável.

## Contrato de entrega

Especificação dimensional; casos extremos; ablação; interpretação.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
