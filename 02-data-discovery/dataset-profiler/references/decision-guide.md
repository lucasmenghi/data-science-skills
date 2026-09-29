# Guia de decisão: dataset-profiler

## Pergunta que esta skill resolve

Caracterizar cobertura, distribuição e qualidade inicial de um dataset sem confundir amostra com população.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Tabela muito grande | Agregações no banco e amostra estratificada para inspeção | LIMIT sem ordenação não garante amostra aleatória. |
| Alta cardinalidade | Investigar identificadores e granularidade | Não codificar IDs como variáveis contínuas por serem números. |
| Missing concentrado em período | Investigar carga e cobertura | A média global pode esconder quebra de fonte. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Gerar centenas de gráficos sem decisão; coletar toda a tabela no driver.

Perfil descreve o que foi lido, não garante qualidade semântica. Reportar aproximações de distinct e quantis quando usadas.

## Contrato de entrega

Perfil por coluna e safra; escopo da amostra; anomalias priorizadas; consultas reproduzíveis.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
