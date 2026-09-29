# Guia de decisão: ml-reviewer

## Pergunta que esta skill resolve

Coordenar revisão independente de artefatos de ML/IA com achados rastreáveis e escopo explícito.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Só há relatório | Revisar coerência e evidência disponível | Não afirmar que código foi auditado. |
| Sistema usa LLM | Separar testes de software de evals de resposta | Testes unitários verdes não medem factualidade. |
| Objetivo é treino de entrevista | Usar ds-reviewer | Não misturar rubrica de aluno com aceitação de produto. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Repetir checklist sem inspecionar; confundir hipótese de problema com falha demonstrada.

Revisão técnica é suporte à decisão; condições de aprovação devem vir do contexto e das responsabilidades reais.

## Contrato de entrega

Parecer integrado; achados; cobertura; verificações e recomendação.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
