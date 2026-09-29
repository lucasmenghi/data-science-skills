# Guia de decisão: feature-engineering-assistant

## Pergunta que esta skill resolve

Coordenar construção e validação de um conjunto de features com contratos e disponibilidade temporal.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Objetivo é só uma agregação | Executar aggregation-features diretamente | Coordenação não deve ampliar escopo. |
| Muitas ideias sem dados disponíveis | Priorizar viabilidade temporal | Feature impossível em serving não entra por AUC. |
| Feature store solicitada | Definir contrato e paridade antes da tecnologia | Tabela chamada feature store não garante point-in-time. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Construir feature sem contrato; seleção guiada pelo teste; duplicar transformações offline e online.

O fluxo deve preservar autoria e contexto do trabalho, mas não exigir que o usuário programe sozinho como em uma aula.

## Contrato de entrega

Catálogo; pipeline; testes; comparação incremental e decisões.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
