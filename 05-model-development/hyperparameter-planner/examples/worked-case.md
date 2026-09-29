# Caso trabalhado: hyperparameter-planner

Cenário sintético de decisão; não é resultado executado em dados reais.

## Situação e análise

Buscar regularização entre valores muito pequenos e grandes exige amostrar escalas, não milhares de passos lineares. A busca termina por orçamento definido e o vencedor é congelado antes do teste.

## Recomendação explicada

Otimização mais sofisticada não corrige métrica errada, leakage ou dado pouco representativo.

## O que entregar

Plano de busca; orçamento; espaço; protocolo; registro de trials e decisão.

## Como verificar

Registrar trials, falhas, seeds, tempo e critério de escolha; usar avaliação externa/nested CV quando necessário para estimar seleção.

## Contraponto

Vencedor pode ser sorte de seed ou fold. Se a premissa do caso mudar, reavaliar a decisão em vez de reutilizar a conclusão. Informar o que falta para passar de hipótese a evidência.
