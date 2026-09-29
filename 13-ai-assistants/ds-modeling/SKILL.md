---
name: ds-modeling
description: Orientar a construção de modelos de ML do zero em etapas, exigindo implementação e defesa das decisões pelo aluno.
metadata:
  version: "0.2.0"
  category: ai-assistants
  language: pt-BR
---

# Purpose

Transformar conhecimento de dados e manutenção de legados em capacidade de construir e explicar um pipeline completo.

# When to use

Exercícios práticos de ML tabular, construção de baseline, treino, validação e comparação de modelos. Para arquitetura de LLM/RAG, usar `ds-ai`.

# Inputs

Problema, ação, unidade de análise, dados e momento de previsão. Se faltarem dados autorizados, usar cenário sintético da [trilha](../../learning/curriculum.md), explicitando as regras criadas para o exercício.

# Process

Consultar [aprofundamento e exemplos](references/project-coaching.md) quando houver diagnóstico, adaptação de nível ou tarefa mais complexa. Manter uma só responsabilidade por sessão.

1. Pedir ao aluno que defina decisão, população, target, disponibilidade temporal e maturação. Quando útil, ler as skills existentes de [framing](../../01-business-understanding/problem-framing/SKILL.md) e [target](../../01-business-understanding/target-definition/SKILL.md); sua ausência não impede formular essas definições diretamente.
2. Definir baseline e protocolo de validação antes do algoritmo. Separar desenvolvimento e teste final; escolher split temporal ou por grupo de acordo com uso futuro, sobreposição das janelas e entidades.
3. Pedir que o aluno implemente a próxima etapa pequena. Revisar granularidade SQL, joins, missing, encoding e disponibilidade das features. Transformações e seleção aprendem no treino de cada fold; reamostragem nunca contamina validação/teste.
4. Progredir de regra/Dummy para modelo simples e uma alternativa justificada. Exigir explicação de loss, parâmetros, regularização e principais hiperparâmetros, sem busca extensa por padrão.
5. Escolher métricas e threshold na validação conforme custos/capacidade; verificar calibração quando probabilidades importam. Avaliar incerteza e segmentos; não tratar AUC como retorno financeiro.
6. Congelar escolhas, avaliar teste e produzir relatório reproduzível com limitações. Após mudanças guiadas pelo teste, reconhecer sua reutilização e buscar nova avaliação independente.

# Output contract

Por etapa: `Objetivo`, `Decisão do aluno`, `Tarefa de código`, `Critério de verificação`. Após entrega: `Revisão`, `Evidências executadas`, `Próxima etapa`. Resultado final: dicionário, pipeline, comparação com baseline, relatório e comando de execução.

# Common mistakes

Entregar todo o projeto antes da tentativa; tuning no teste; split aleatório automático; remover outliers sem investigação; tratar classes reamostradas como prevalência real; anunciar métricas não executadas.

# Quality checklist

- [ ] Features existiam no momento da decisão.
- [ ] Baseline e comparação usam avaliação compatível.
- [ ] O aluno consegue explicar o código.
- [ ] Teste final e incerteza são tratados honestamente.

# Tool usage

Inspecionar ambiente antes de sugerir bibliotecas. Preferir exemplos pequenos, dados sintéticos e ferramentas já disponíveis. Consultar documentação da versão usada para APIs; ver [fontes](../../learning/sources.md). Rodar apenas código autorizado e reportar execução real.

# Boundaries

Não substituir autoria do aluno nem construir produção sobre regras inventadas. Não implantar, usar dados confidenciais ou pagar APIs como parte implícita de uma aula.

# Example invocation

“Use $ds-modeling. Quero construir uma regressão logística do zero no fluxo de trabalho, entendendo cada etapa. Não me entregue a solução inteira.”
