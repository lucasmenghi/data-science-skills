# Caso integrado: a qualidade caiu

Cenário sintético: o painel mostra queda de precisão após uma mudança de pipeline. O negócio pede “retreine hoje”. Não há evidência suficiente para afirmar que o modelo envelheceu.

1. `performance-monitoring`: comparar coortes com igual maturação e versão. Conferir se o denominador mudou e se os rótulos chegaram.
2. `data-quality-audit`: inspecionar unidade, missing, cobertura e duplicações. `feature-ready-validation`: comparar transformação offline e online em casos controlados.
3. `data-drift`: localizar mudança nas entradas; separar mistura populacional de falha técnica. Se a mudança é escala de uma coluna, corrigir transformação e verificar recuperação antes de retreinar.
4. `concept-drift`: somente com rótulos adequados, investigar relação condicional, seleção e mudança de política.
5. `retraining-advisor`: comparar correção, recalibração, mudança de threshold e retreino. Registrar o custo e a evidência de cada alternativa.

Uma possível conclusão, condicionada à inspeção: “A coluna passou de unidades para centavos. Isso explica a divergência nos exemplos testados; restauramos a transformação autorizada e o contrato voltou a passar. Ainda falta verificar as métricas de coortes maduras para confirmar recuperação de qualidade.”

Evitar dizer que o problema está resolvido apenas porque o serviço responde ou o drift sumiu. O critério de recuperação deve corresponder ao impacto original. Se uma ação de rollback não estiver autorizada, preparar a mudança concreta e evidência para decisão, sem executar implicitamente.
