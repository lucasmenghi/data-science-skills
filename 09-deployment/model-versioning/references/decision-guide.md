# Guia de decisão: model-versioning

## Pergunta que esta skill resolve

Versionar modelo, dados, features e política para reprodução e rollback coerentes.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Só threshold mudou | Versionar política mesmo com mesmos pesos | Comportamento em produção mudou. |
| Feature schema mudou | Versionar contrato e consumidores | Rollback só do modelo pode ficar incompatível. |
| Dados mutáveis | Referenciar snapshot/data version | Nome da tabela não identifica o treino. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Usar latest sem rastreabilidade; sobrescrever arquivo anterior; prometer determinismo absoluto.

Versionar tudo não significa copiar dados sensíveis para o repositório. Usar referências autorizadas e controle de acesso.

## Contrato de entrega

Manifesto versionado; compatibilidade; evidência de reprodução; plano de rollback.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
