# Referências primárias

Consultadas em 29/09/2026 para verificação metodológica e de conceitos de API. Os procedimentos, exemplos e matrizes de decisão da biblioteca são sínteses originais de trabalho, não reproduções dos manuais. Revalidar APIs na versão instalada antes de executar código; links `stable` e `latest` podem mudar.

| Tema | Fonte e uso |
|---|---|
| Preparação e leakage | [scikit-learn: common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) — referência para separação entre aprender e aplicar transformações |
| Folds e dependência | [scikit-learn: cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html) — esquemas e limitações de avaliação |
| Calibração | [scikit-learn: probability calibration](https://scikit-learn.org/stable/modules/calibration.html) — curvas, losses e métodos |
| Importância por permutação | [scikit-learn: permutation importance](https://scikit-learn.org/stable/modules/permutation_importance.html) — interpretação dependente do modelo e da métrica |
| PDP/ICE | [scikit-learn: partial dependence](https://scikit-learn.org/stable/modules/partial_dependence.html) — comportamento do modelo e limitações de suporte |
| SHAP | [TreeExplainer](https://shap.readthedocs.io/en/latest/generated/shap.TreeExplainer.html) — background, dependências e escala da saída |
| Inferência causal | [DoWhy: estimating causal effects](https://www.pywhy.org/dowhy/v0.13/user_guide/causal_tasks/estimating_causal_effects/index.html) — distinguir modelagem, identificação, estimação e refutação; referência versionada |
| Features temporais | [Feast: point-in-time joins](https://docs.feast.dev/getting-started/concepts/point-in-time-joins) — reconstrução de features no tempo |
| Registro de modelos | [MLflow Model Registry](https://mlflow.org/docs/latest/ml/model-registry/) — linhagem, versões e aliases |
| Execução distribuída | [Spark SQL performance tuning](https://spark.apache.org/docs/latest/sql-performance-tuning.html) — planos, estatísticas e estratégias de join |
| Documentação de modelos | [Model Cards for Model Reporting](https://research.google/pubs/model-cards-for-model-reporting/) — intenção de uso, avaliação e limites |

Para os materiais de estudo fornecidos, suas ressalvas e referências de IA, consultar [learning/sources.md](../learning/sources.md). Eles não são norma de contratação nem especificação de produção. Nenhuma fonte substitui os dados, regras e restrições do projeto atual.
