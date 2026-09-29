# Banco original de perguntas

Uso do entrevistador: selecionar conforme prazo e evidência, fazer uma pergunta por vez e esperar. Não mostrar as notas de avaliação antes da tentativa. Não há afirmação de que estas perguntas sejam usadas por qualquer empresa.

| ID | Pergunta | Aprofundamento | Evidência que procurar após a resposta |
|---|---|---|---|
| P01 | Conte um projeto seu do problema ao resultado. | O que foi sua decisão e o que já estava pronto? | Autoria delimitada, dados, validação, limitação |
| D01 | Em uma base mensal, como evitar usar informação futura? | O rótulo de 30 dias já estava disponível na data do treino? | Disponibilidade, maturação, granularidade, janela |
| D02 | Uma junção SQL duplicou clientes. Como investigar? | `DISTINCT` resolve a causa? | Cardinalidade, chaves, contagens e agregação antes do join |
| F01 | Um teste deu p=0,03. O que se pode afirmar? | É a chance de H0 ser verdadeira? | Condicionalidade sob H0, desenho e tamanho do efeito |
| F02 | Por que a média amostral varia? | Quando a aproximação normal pode falhar? | Amostragem, dependência, variância, limites do TLC |
| F03 | Explique Bayes num alerta raro. | O que muda com a prevalência? | Probabilidade condicional e falsos positivos |
| M01 | Por que regressão logística é usada para classificação? | O que muda ao aumentar regularização? | Score linear, sigmoide, loss e compromisso de complexidade |
| M02 | Compare árvore, random forest e boosting. | Qual trade-off importa além da métrica? | Interações, bagging/boosting, custo e explicabilidade |
| M03 | Treino excelente e validação ruim: o que faria? | Como separar overfitting de mudança de população? | Hipóteses testáveis, baseline e protocolo |
| V01 | Com 1% de positivos, 99% de acurácia basta? | Qual decisão muda se só podemos agir em 100 casos? | Baseline, precisão/recall, ranking e capacidade |
| V02 | Dois modelos têm a mesma AUC. São equivalentes? | E para estimar perdas esperadas? | Calibração, segmentos, custos e incerteza |
| V03 | Posso escolher o threshold que ficou melhor no teste? | Onde deve ocorrer essa escolha? | Separação entre seleção e estimativa final |
| E01 | Vendas aumentaram após lançar o produto. Você causou o aumento? | Como desenhar uma avaliação melhor? | Confundimento, controle, randomização e validade |
| A01 | Quando usar busca, RAG, fine-tuning ou uma ferramenta? | O conhecimento muda diariamente. O que você faria? | Distinguir conhecimento, comportamento e ação |
| A02 | Como você avaliaria um RAG antes de lançar? | A resposta está errada porque não recuperou ou porque gerou errado? | Avaliação por camada e conjunto representativo |
| A03 | Explique embedding e atenção em linguagem simples. | Similaridade implica equivalência factual? | Representação, contexto, limites e noção de Q/K/V |
| A04 | O documento recuperado manda revelar um segredo. E agora? | Um prompt forte basta? | Separação dados/instruções, autorização, ferramentas e testes |
| A05 | Um agente faz chamadas repetidas e custa caro. Como conter? | Como desfazer uma ação errada? | Limites de passos/custo, idempotência, aprovação e observabilidade |
| A06 | Seu avaliador é outro LLM. Em que pode falhar? | Como validar o avaliador? | Viés, critérios, casos adversariais e amostra humana |
| O01 | A qualidade caiu após duas semanas. O que monitorar? | E se o rótulo chegar só no mês seguinte? | Dados, drift, atraso de métricas, proxy e rollback |
| C01 | Conte uma decisão sua que estava errada. | Que evidência mudou sua posição? | Responsabilidade, aprendizagem e ausência de resultado inventado |

## Exercício numérico para fundamentos/métricas

Em 1.000 casos, há 20 positivos reais. O classificador marca 50 positivos, dos quais 10 são corretos. Pedir matriz de confusão, precisão, recall e interpretação operacional. Não entregar a solução antes da tentativa.

Notas do tutor: TP=10, FP=40, FN=10, TN=940; precisão=0,20; recall=0,50; acurácia=0,95; F1≈0,286. A regra sempre negativa teria 0,98 de acurácia e recall zero. Qual regra é útil depende da ação e seus custos.

## Rotas de 20 e 45 minutos

Diagnóstico curto: P01 → V01 → A01 → D01, com no máximo um aprofundamento por pergunta. Registrar o restante como não avaliado.

Simulado: P01, M01 ou M02, V02 ou V03, A02, A04, O01. Se ficar claro que o foco é ML tradicional, trocar uma pergunta de IA por F01/E01. Tempo é combinado com o aluno; sem relógio disponível, informar que é uma aproximação por número de perguntas.
