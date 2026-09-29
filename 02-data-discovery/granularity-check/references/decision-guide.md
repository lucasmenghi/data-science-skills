# Guia de decisão: granularity-check

## Pergunta que esta skill resolve

Verificar unidade de análise, chaves e multiplicação de linhas antes de agregações e joins.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Join de duas tabelas de eventos | Agregar separadamente antes de combinar | Dois eventos por três eventos geram seis pares. |
| Várias versões por chave | Resolver as-of ou versão válida com desempate | DISTINCT pode esconder a seleção errada. |
| Unidade muda após agregação | Redefinir denominadores e pesos | Média por linha não equivale a média por cliente. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Aplicar DISTINCT sem causa raiz; testar apenas contagem total.

Preservar registros legítimos e expor ambiguidades. Uma junção pode manter contagem e ainda ligar a entidade errada.

## Contrato de entrega

Contrato de grão; cardinalidades; invariantes; SQL de diagnóstico e correção.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
