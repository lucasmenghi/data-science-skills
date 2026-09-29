# Aprofundamento metodológico por decisão

Consultar o trecho relevante; este guia não precisa ser carregado inteiro em cada tarefa. As condições abaixo ajudam a identificar quando uma solução simples basta e quando a análise precisa de mais evidência.

## População, unidade e estimando

Uma média por transação responde sobre transações; uma média calculada primeiro por cliente e depois entre clientes responde sobre clientes. Pesos diferentes definem perguntas diferentes. Antes de agregar, escrever o denominador e a exposição: eventos por cliente ativo, por dia observado ou por contrato não são equivalentes.

A população de treino pode resultar de seleção: só aprovados, só contatados, só clientes com rótulo. Avaliar no mesmo subconjunto não prova validade para todos os elegíveis. Documentar a seleção e o suporte dos dados. Se a política determina quem tem rótulo, o próprio sistema pode mudar a evidência disponível.

## Validade temporal e rótulos

Para cada previsão em t, a feature deve usar o que era conhecido em t. Uma transação ocorrida em t−2 mas disponibilizada em t+1 ainda é futura informacionalmente. Em bases revisadas, event_time e data da extração não bastam: identificar snapshots ou declarar que não é possível reconstruir o estado histórico com certeza.

Alvo de horizonte H requer observação até t+H e eventual atraso de registro. Se o treinamento ocorre antes disso, o rótulo ainda não estava disponível. Gap/purga deve seguir esse mecanismo e as janelas sobrepostas, não um número decorado. A mesma entidade em treino e teste pode ser apropriada para prever seu futuro e inadequada para generalizar a entidades novas; explicar qual situação se está estimando.

## Dados ausentes e transformação

MCAR, MAR e MNAR são hipóteses sobre o mecanismo de ausência. O padrão observado pode contrariar explicações simples, mas não identifica automaticamente o mecanismo. Comparar tratamentos por desempenho, cobertura e plausibilidade. Imputação estima uma representação útil; não recupera necessariamente o valor verdadeiro.

Transformações aprendidas precisam respeitar as fronteiras de validação. Uma mudança determinística de unidade documentada difere de estimar mediana, vocabulário, componentes PCA ou seleção pelo alvo. Essa distinção evita tanto leakage quanto uma regra excessiva de que absolutamente toda operação deve ser proibida antes do split.

## Seleção e incerteza

Validação serve para escolher; avaliação independente serve para estimar a solução escolhida. Quanto mais decisões usam o mesmo conjunto, maior o risco de ajustar peculiaridades dele. Nested CV ou holdout externo pode avaliar o procedimento de seleção, desde que a dependência de tempo/grupos seja respeitada.

Não calcular intervalo de confiança tratando os k resultados de folds sobrepostos como k observações independentes. Identificar primeiro a unidade de reamostragem: pessoa, grupo, bloco temporal ou outra unidade apropriada. Diferenças pequenas entre modelos precisam ser confrontadas com variabilidade, custo e estabilidade; um ranking pontual não é uma ordem universal.

## Loss, métrica e política

Loss guia ajuste de parâmetros; métrica de seleção escolhe candidatos; utilidade da política depende da ação e dos custos. Elas podem coincidir, mas não são sinônimos. Um modelo com melhor ranking pode ter pior calibração; um classificador com melhor F1 pode ultrapassar a capacidade disponível.

Para matriz de custos constante e probabilidade p calibrada, agir tem custo esperado C_FP(1−p) e não agir tem custo C_FN·p, se os demais custos forem zero. Agir é preferível quando p > C_FP/(C_FP+C_FN), com tratamento de empate e casos degenerados definido. Se há benefícios, custos de ação, efeitos heterogêneos ou capacidade, comparar utilidades completas; a fórmula simplificada deixa de representar a decisão.

Com capacidade fixa, top-k pode manter volume enquanto threshold fixo não mantém. Scores empatados exigem desempate explícito ou inclusão do grupo inteiro. Um ganho observado escolhendo o corte na validação precisa de avaliação final após congelamento. Custos devem ser fornecidos ou rotulados como cenário hipotético.

## Métricas de regressão e classificação

MAE dá penalidade linear ao erro absoluto; MSE/RMSE dão maior peso a erros grandes. A escolha depende do custo e não apenas de robustez desejada. R² pode ser negativo fora da amostra; percentuais de erro precisam de domínio que lide com zeros e denominadores pequenos. Quantile loss é útil quando o objetivo é um quantil e o custo é assimétrico, com validação de cobertura correspondente.

Precisão depende da prevalência e da política. ROC-AUC avalia ordenação; PR/AP dão outra visão em classe rara, mas AP e integração trapezoidal de uma curva PR não são sempre o mesmo cálculo. Relatar definição e biblioteca usada. Brier e log loss avaliam previsões probabilísticas e não são diagnósticos puros de calibração: observar também confiabilidade, tamanho dos bins e resolução.

## Explicação e intervenção

Importância por permutação pergunta quanto a métrica muda ao perturbar informação sob um procedimento definido. Features correlacionadas podem substituir umas às outras; importância baixa isolada não prova irrelevância conjunta. Coeficiente depende de escala e especificação; importância por impureza pode favorecer variáveis com muitas possibilidades de corte.

SHAP depende de saída e referência. Contribuições em log-odds não são pontos percentuais. PDP pode avaliar combinações sem suporte quando features são correlacionadas; ICE mostra heterogeneidade que a média esconde. Nenhum desses métodos prova o efeito de manipular a feature no mundo real. Para recomendar intervenção, formular uma pergunta causal distinta.

## Identificação causal e experimentos

Estimar efeito requer definir tratamento, comparação, resultado, população e hipótese de identificação. Ajustar por mediador pode remover parte do efeito total; ajustar por collider pode criar associação. Não escolher variáveis de ajuste apenas pelo poder preditivo. Em diferenças-em-diferenças, tendências paralelas é hipótese substantiva; pré-tendências compatíveis não a provam para o período tratado.

Randomização não dispensa checagem de implementação, exposição, perda de dados e interferência. Intenção de tratar estima efeito de oferecer/atribuir tratamento, não necessariamente efeito entre aderentes. Comparar aderentes pode reintroduzir seleção. Multiplicidade, parada e análises pós-hoc mudam a interpretação; não equivalência por p alto, nem relevância prática por p baixo.

## Operação, mudança e retreino

Monitorar separadamente integridade de entrada, distribuição, desempenho maduro e comportamento da política. Drift em X não demonstra alteração da relação P(y|X); queda de desempenho pode vir de pipeline, seleção ou rótulo. Antes de retreinar, tentar explicar a causa e verificar a menor intervenção adequada.

Rollback precisa do conjunto compatível de pesos, transformação, schema e política. Restaurar apenas o modelo pode manter o erro se o encoder mudou. Logs devem identificar versão na previsão original; recalcular retrospectivamente com a versão atual destrói a evidência do que o usuário recebeu.

## Impacto e comunicação

Receita observada em pessoas atendidas não equivale a receita incremental. Um cenário econômico deve mostrar contrafactual, margem, volume, efeito, custos e horizonte, sem dupla contagem. Mais precisão decimal não reduz incerteza das premissas. Sensibilidade e break-even frequentemente informam melhor a decisão que uma estimativa única.

Comunicar resultado com a condição que o torna válido: população, período, unidade e método. Usar “observamos”, “estimamos sob estas hipóteses” ou “propomos testar” de forma consistente. Quem lê deve distinguir entrega executada de proposta e entender o que faria a recomendação mudar.
