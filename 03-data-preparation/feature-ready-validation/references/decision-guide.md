# Guia de decisão: feature-ready-validation

## Pergunta que esta skill resolve

Verificar contrato de entrada de um modelo e equivalência entre treinamento e inferência.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Categoria inédita | Fallback explícito ou rejeição prevista | Não aprender encoder em produção silenciosamente. |
| Colunas reordenadas | Validar assinatura por nome/tipo | Array posicional pode trocar significado sem erro. |
| Paridade falha | Investigar implementação, fuso e precisão | Boa métrica offline não corrige entrada divergente. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Declarar pronto apenas porque não há nulos; aceitar colunas com semântica alterada.

Se houver apenas schema, avaliar contrato estático e listar checks dependentes de execução como pendentes.

## Contrato de entrega

Contrato executável; casos de teste; relatório de paridade; lacunas e aceite condicionado.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
