# Preparação de 24 a 72 horas

Objetivo: explicar experiências reais, reconhecer limites e raciocinar sob perguntas. O prazo não permite reconstruir toda a formação. “IA” pode significar ML tradicional, IA generativa ou ambos; confirme a descrição da vaga quando disponível. Até lá, priorize fundamentos compartilhados e IA aplicada.

## Se a entrevista for amanhã

| Bloco | Tempo | Ação | Evidência ao terminar |
|---|---:|---|---|
| Diagnóstico | 20 min | Mentor faz 4 perguntas, uma por vez: projeto, validação, IA e métricas | Lacunas observadas, sem rótulo global de senioridade |
| Experiência | 40 min | Explicar um projeto em que participou e sua contribuição exata | Relato de 2 minutos e respostas a 3 aprofundamentos |
| IA aplicada | 50 min | Desenhar busca/RAG e comparar com prompt, ferramenta e fine-tuning | Arquitetura com avaliação, limites e falhas |
| Pausa | 10 min | Interromper o estudo | Retomar no próximo bloco |
| ML essencial | 40 min | Leakage, split temporal, overfitting, precisão/recall, calibração | Resolver um caso sem consultar |
| Simulado | 35 min | 5 perguntas e aprofundamentos; feedback ao final | Erros separados de falta de clareza |
| Correção | 20 min | Refazer as duas respostas mais fracas com cenário diferente | Resposta independente |
| Fechamento | 10 min | Escrever uma página de revisão | Lista curta para a manhã |

Total: 3h45 incluindo pausa. Se começar às 18h30, termina às 22h15. Se começar tarde, use a versão de 90 minutos abaixo. A janela disponível até 02h é um limite possível, não uma meta de carga. Priorize encerrar a tempo de descansar antes da entrevista.

Versão de 90 minutos: 10 diagnóstico + 20 relato + 25 RAG/avaliação + 20 leakage/métricas + 15 minissimulado. Não iniciar um curso extenso nem um projeto completo nesta janela.

## Se houver mais duas noites

Noite 2: 45 min fundamentos identificados no diagnóstico; 60 min exercício de avaliação de IA; 15 min pausa; 45 min validação/modelagem; 30 min defesa do hackathon ou de outro projeto. O exercício de IA está em [ai-case.md](ai-case.md). Se o hackathon não usou IA, não inventar esse vínculo.

Noite 3: 50 min sabatina; 15 min pausa; 45 min corrigir duas lacunas; 30 min contar dois projetos e uma falha; 20 min perguntas à equipe. Deixar tópicos periféricos para depois. Se a vaga revelar ênfase em ML tradicional, substituir parte do bloco de RAG por regressão logística, ensembles e validação temporal.

## O que conseguir explicar sem decorar

- Qual problema resolvi, minha contribuição, alternativas, validação e limitação.
- Por que separo treino, validação e teste; como impedir informação futura nas features.
- Como um modelo linear/logístico aprende; por que regularizar; como bagging e boosting diferem.
- Por que acurácia, AUC e qualidade de probabilidade respondem a perguntas diferentes.
- O que embeddings e atenção fazem; como RAG recupera contexto; quando ferramenta ou fine-tuning faz sentido.
- Como medir recuperação, resposta final, custo, latência e falhas de um produto de IA.
- Como um documento malicioso pode tentar instruir o agente e onde se aplicam permissões reais.

## Na entrevista

Use: contexto → decisão → justificativa → evidência → limitação. Se não souber, diga o que sabe, explicite a hipótese e descreva como verificaria. Não transforme protótipo em produção, participação em autoria integral ou hipótese em ganho medido.

Perguntas úteis à equipe: “O foco é IA generativa, modelos preditivos ou ambos?”, “Como vocês avaliam qualidade antes de colocar em produção?”, “Que autonomia e responsabilidades esperam dessa posição?”.
