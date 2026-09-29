# Caso trabalhado: concept-drift

Cenário sintético de decisão; não é resultado executado em dados reais.

## Situação e análise

Depois de alterar a política, só alguns casos recebem revisão e rótulo. Queda de precisão nessa amostra pode refletir seleção, não mudança real de P(y|X). Investigar o processo de observação.

## Recomendação explicada

Não existe observação direta do mecanismo causal apenas por uma série de métricas. Formular hipóteses e mostrar evidências compatíveis e conflitantes.

## O que entregar

Diagnóstico por hipótese; evidências; limitações de rótulo; plano de resposta.

## Como verificar

Propor recalibração, atualização de features, retreino ou mudança de política com experimento e condições de avaliação.

## Contraponto

Retreino não corrige integração quebrada. Se a premissa do caso mudar, reavaliar a decisão em vez de reutilizar a conclusão. Informar o que falta para passar de hipótese a evidência.
