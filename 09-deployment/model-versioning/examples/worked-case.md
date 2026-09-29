# Caso trabalhado: model-versioning

Cenário sintético de decisão; não é resultado executado em dados reais.

## Situação e análise

Voltar pesos antigos com encoder novo troca a interpretação das categorias. O rollback deve recuperar o conjunto compatível, não apenas um arquivo de modelo.

## Recomendação explicada

Versionar tudo não significa copiar dados sensíveis para o repositório. Usar referências autorizadas e controle de acesso.

## O que entregar

Manifesto versionado; compatibilidade; evidência de reprodução; plano de rollback.

## Como verificar

Definir rollback do conjunto compatível e validar referências, mantendo histórico sem sobrescrever artefatos antigos.

## Contraponto

Nome da tabela não identifica o treino. Se a premissa do caso mudar, reavaliar a decisão em vez de reutilizar a conclusão. Informar o que falta para passar de hipótese a evidência.
