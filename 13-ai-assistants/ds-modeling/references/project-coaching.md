# Tutoria de projeto com autonomia crescente

## Dividir o projeto por decisões

Estabelecer entregas pequenas: contrato do problema e alvo; extração temporal; baseline; pipeline; comparação; erro; documentação. Cada etapa deve produzir artefato e explicação do aluno. Não entregar um notebook completo se o objetivo explícito é aprender a construir.

Usar as categorias de trabalho como referência metodológica: data-preparation para fit/transform, model-development para baselines/CV e model-validation para avaliação. Elas descrevem como executar; a tutoria decide quanto apoio oferecer conforme evidência.

## Escada de assistência

Primeira dificuldade: pedir que localize onde o resultado diverge da expectativa. Depois, oferecer um exemplo menor ou uma assinatura de função. Só fornecer solução completa após pedido ou bloqueio persistente, explicando cada decisão. Código colado sem compreensão não encerra a etapa.

## Critérios de passagem

O aluno deve reproduzir a execução, explicar o que aprende com os dados, identificar como poderia vazar informação e dizer qual resultado mudaria sua escolha. Se não supera o baseline, permitir concluir isso corretamente. Não incentivar tuning até obter melhora artificial.

## Exemplo

Ao implementar imputação, pedir primeiro onde ocorrerá fit em cada fold. Após código funcionar, propor categoria nova no teste e uma coluna completamente ausente para discutir contrato e fallback. O objetivo não é criar dezenas de testes espelhando código, mas verificar comportamento que afeta generalização.

## Profundidade avançada

Aprofundar dependência temporal/grupos, refit, calibração, incerteza e operação apenas conforme objetivo. Projeto completo inclui limitações e reprodução, mesmo que use um modelo simples.
