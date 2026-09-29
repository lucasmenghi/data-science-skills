# Caso trabalhado: serving-readiness

Cenário sintético de decisão; não é resultado executado em dados reais.

## Situação e análise

Uma previsão de campanha ocorre uma vez ao dia. Um job batch versionado pode atender melhor que API online; testar reexecução idempotente e completude da população.

## Recomendação explicada

Se não houver ambiente/carga representativa, declarar performance não verificada em vez de extrapolar benchmark pequeno.

## O que entregar

Contrato de serving; testes; SLO; dependências; falhas e recomendação de prontidão.

## Como verificar

Executar testes locais autorizados e documentar pendências de infraestrutura; distinguir protótipo funcional de capacidade demonstrada.

## Contraponto

p50 não garante SLO p95. Se a premissa do caso mudar, reavaliar a decisão em vez de reutilizar a conclusão. Informar o que falta para passar de hipótese a evidência.
