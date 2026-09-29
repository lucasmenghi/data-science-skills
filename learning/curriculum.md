# Trilha por evidências

O cronograma longo começa após a urgência. Proposta inicial: seis ciclos, cada um com uma ou mais semanas conforme disponibilidade e diagnóstico. Não prometer domínio em seis semanas.

| Ciclo | Conteúdo e pré-requisitos | Entrega verificável |
|---|---|---|
| 1. Decisão e dados | Negócio, SQL, população, granularidade, alvo e momento de decisão | Especificação de target, consulta temporal e auditoria de leakage |
| 2. Fundamentos | Probabilidade condicional, Bayes, média/variância, amostragem, IC, testes; vetores, produto interno, derivada | Exercícios explicados sem consulta e uma simulação pequena |
| 3. Primeiro modelo | Baseline, regressão linear/logística, loss, gradiente, regularização; árvores e ensembles | Pipeline simples reproduzível, comparação justa e explicação das escolhas |
| 4. Validação | Split temporal/grupos, CV, seleção dentro dos folds, desbalanceamento, threshold e calibração | Relatório com incerteza, erros por segmento e teste final preservado |
| 5. IA aplicada | Tokens, embeddings, atenção, RAG, ferramentas, fine-tuning, avaliação e segurança | Protótipo em dados sintéticos com conjunto de avaliação separado |
| 6. Operação e defesa | Versionamento, monitoramento, atraso de rótulos, rollback, experimentação e comunicação | Model card, plano de monitoramento e defesa oral com contrapontos |

Distribuição inicial por sessão: 10 min recuperação ativa, 20 min explicação focada, 30 min exercício, 10 min feedback e registro. Ajustar à energia, agenda e dificuldade observada. Revisões em 1, 3 e 7 dias são uma convenção inicial, ajustável; não preencher datas sem a data real da sessão.

## Projeto ML: priorização de contato

Dados sintéticos de clientes com eventos datados. Em cada `reference_date`, prever um evento nos próximos 30 dias. O aluno define população, maturação do rótulo e features disponíveis no momento da decisão. Construir primeiro uma regra simples e um baseline; só depois regressão logística e um ensemble.

Entregas: dicionário de dados; SQL sem informação futura; teste de duplicação por joins; pipeline com transformações ajustadas no treino; validação temporal com janelas de rótulo que não invadam o período indisponível; escolha de threshold na validação conforme capacidade de contato; teste final; relatório e instrução de execução. IDs repetidos devem ser tratados conforme generalização desejada (novos clientes versus períodos futuros dos mesmos clientes). Não exigir grupos disjuntos indiscriminadamente.

Critérios: outro leitor reproduz; aluno explica o que cada etapa aprende; métricas comparáveis; custo operacional explícito; ganho financeiro somente como cenário hipotético, salvo medição real. Um modelo que não supera a regra simples é um resultado válido.

## Projeto IA: assistente documental

Use [o caso de IA](ai-case.md). Comece com busca e respostas com fonte; depois compare uma variante. O aluno escreve o código e defende o experimento; o tutor ajuda em bloqueios sem entregar um projeto inteiro antes da tentativa. Sem APIs disponíveis, executar a recuperação e avaliar respostas preparadas manualmente, identificadas como tal.

## Tópicos condicionais

Clustering/PCA para segmentação; séries temporais para forecasting; NLP/visão conforme vaga; redes profundas, otimização e reforço após os pré-requisitos. O volume dos PDFs não define a ordem de estudo. Consulta orientada em [sources.md](sources.md).
