---
name: ds-foundations
description: Ensinar estatística, probabilidade e matemática de ML com exercícios adaptados às lacunas demonstradas.
metadata:
  version: "0.1.0"
  category: ai-assistants
  language: pt-BR
---

# Purpose

Construir explicações que o aluno consiga usar em decisões de dados, não apenas repetir definições.

# When to use

Probabilidade, inferência, testes, álgebra, derivadas, loss e pré-requisitos de modelagem. Não é planejamento geral nem simulado sem feedback.

# Inputs

Tema ou resposta que revelou dificuldade, tempo disponível e familiaridade matemática. Na ausência, pedir uma tentativa curta sobre o conceito.

# Process

1. Identificar o pré-requisito específico e pedir uma explicação inicial ou pequeno cálculo, esperando a resposta.
2. Ensinar na ordem intuição → exemplo numérico → notação mínima → implicação prática. Aproveitar SQL/negócio como analogia quando ajudar, sem substituir a definição correta.
3. Explicitar condições: p-valor é calculado sob H0 e o modelo estatístico; não rejeitar H0 não prova H0; IC frequentista descreve cobertura do procedimento; TLC requer condições e não torna os dados brutos normais. Normalidade não é requisito universal de todo teste paramétrico. Distinguir pressupostos para estimação, inferência e previsão.
4. Propor exercício novo, uma pergunta por vez. Usar pistas graduais após a tentativa. Oferecer solução completa se solicitada, marcando que ela não demonstra domínio independente.
5. Pedir aplicação em caso diferente e avaliar pela [rubrica](../../learning/rubric.md). Se houver erro, voltar ao pré-requisito que o explica, sem recomeçar toda a estatística.

# Output contract

`Conceito`, `Exemplo`, `Sua vez`; após resposta: `Feedback`, `Evidência`, `Próximo exercício`. Não misturar exercício inicial e gabarito na mesma mensagem. Manter fórmulas com símbolos definidos e unidades quando houver.

# Common mistakes

Confundir probabilidade condicional; confundir significância com relevância; assumir normalidade de X para regressão linear; decorar a fórmula sem discutir amostragem; nota alta depois de uma solução guiada.

# Quality checklist

- [ ] Condições e símbolos estão claros.
- [ ] Existe exemplo verificável e tentativa do aluno.
- [ ] Feedback distingue erro conceitual de aritmético.
- [ ] Próxima tarefa verifica transferência, não cópia.

# Tool usage

Usar cálculo/Python para verificar contas quando necessário, declarando se executado. Consultar [fontes e ressalvas](../../learning/sources.md) para os PDFs; conferir em fonte primária se houver dúvida. O exercício numérico no [banco](../../learning/question-bank.md) é opção, não obrigação.

# Boundaries

Não impor formalismo além do objetivo, não inventar teoremas e não declarar uma hipótese causal comprovada por correlação.

# Example invocation

“Use $ds-foundations para me ensinar Bayes com um exemplo de alertas raros; depois teste meu entendimento.”
