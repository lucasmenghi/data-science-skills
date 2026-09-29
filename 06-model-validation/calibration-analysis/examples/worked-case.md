# Caso trabalhado: calibration-analysis

Cenário sintético de decisão; não é resultado executado em dados reais.

## Situação e análise

Entre previsões próximas de 0,8, só 40% são positivos. Antes de usar essas probabilidades em expectativa, investigar amostra e calibrar com protocolo independente; não simplesmente dividir todas por dois.

## Recomendação explicada

Uma curva depende do binning e da amostra; poucas observações por faixa limitam o que se pode concluir.

## O que entregar

Reliability diagram/tabela; losses; comparação; método e avaliação independente.

## Como verificar

Documentar uso permitido das probabilidades e monitoramento; calibrar não corrige features inválidas nem discriminação ausente.

## Contraponto

Média pode esconder erros opostos. Se a premissa do caso mudar, reavaliar a decisão em vez de reutilizar a conclusão. Informar o que falta para passar de hipótese a evidência.
