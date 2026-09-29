# Caso integrado: priorização de retenção

Cenário sintético. Uma equipe pode fazer 500 contatos semanais com clientes ativos. Quer reduzir cancelamentos nos 30 dias após cada decisão. Ainda não há evidência do efeito do contato.

## 1. Framing e dados

`problem-framing` distingue prever risco de escolher intervenção. `target-definition` especifica cliente-semana, população em risco, janela futura e maturação. `granularity-check` testa compras e contatos antes do join. `temporal-validation` verifica event_time e available_at; eventos recebidos após a decisão não entram retrospectivamente.

Decisão explicada: começar por ranking de risco pode apoiar investigação, mas não demonstra quem se beneficia mais do contato. Manter essa limitação no produto e planejar experimento.

## 2. Features e desenvolvimento

`aggregation-features` calcula frequência, recência e gasto sobre período conhecido; histórico incompleto recebe indicador de cobertura. `categorical-encoding` define vocabulário e desconhecidos. `cross-validation-planner` escolhe cortes temporais que preservam maturação; todo fit acontece nos treinos dos folds.

Comparar regra atual, regressão regularizada e uma alternativa de árvore sob mesmo protocolo. Não fazer busca extensa antes de verificar baseline e leakage. `feature-selection` busca estabilidade e custo, mantendo teste final sem participação na escolha.

## 3. Validação e política

`metric-selection` prioriza captura e precisão em 500 contatos, além de calibração se houver uso de probabilidades. `threshold-optimization` avalia top-k e empates. `oot-validation` aplica a solução congelada a safras posteriores maduras. Reportar contagens e variação, não apenas AUC.

Se o modelo não supera a regra na capacidade relevante, recomendar manter a regra e investigar erros. Se supera, isso justifica avaliar um piloto, não atribuir cancelamentos evitados ao modelo.

## 4. Impacto e causalidade

`ab-test-design` define randomização, estimando e guardrails para medir efeito do contato. `financial-impact` só usa efeito incremental observado ou cenário explicitamente assumido. Uma campanha com muitos clientes de alto risco pode ter grande taxa de cancelamento mesmo ajudando; comparar tratados com população distinta distorce a conclusão.

## 5. Operação e entrega

`model-versioning` fixa dados, features, modelo e política. `serving-readiness` considera batch semanal em vez de endpoint online desnecessário. `performance-monitoring` acompanha previsão por safra e completude do alvo. `model-card` delimita população e uso; `executive-summary` recomenda próximo passo com evidências.

## Entregáveis mínimos e critérios de fechamento

- Contrato de decisão/alvo com janelas e população verificadas.
- SQL/pipeline reproduzível e testes de cardinalidade/tempo.
- Comparação justa contra regra atual na capacidade real.
- Política congelada e avaliação futura madura.
- Plano de piloto e monitoramento com pendências explícitas.

O assistente não precisa executar todas essas etapas se o usuário pediu apenas revisar um join. Este caso demonstra encadeamento e condições de passagem; não é um rito obrigatório.
