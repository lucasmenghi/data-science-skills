# Caso trabalhado: deployment-checklist

Cenário sintético de decisão; não é resultado executado em dados reais.

## Situação e análise

Um modelo novo roda em shadow e gera o dobro de alertas. Antes do canary, verificar threshold, base elegível e capacidade; não tratar rollout como mera troca de arquivo.

## Recomendação explicada

Esta skill prepara e verifica o lançamento. Não cria um processo de aprovação extra quando a autorização já existe, nem amplia seu escopo.

## O que entregar

Plano de rollout; checklist com evidências; critérios de parada; rollback e responsáveis.

## Como verificar

Entregar checklist com estado/evidência, não caixas marcadas por suposição. Executar publicação somente dentro de autorização específica vigente.

## Contraponto

Modelo validado offline pode usar features diferentes. Se a premissa do caso mudar, reavaliar a decisão em vez de reutilizar a conclusão. Informar o que falta para passar de hipótese a evidência.
