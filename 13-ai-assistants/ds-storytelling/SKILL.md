---
name: ds-storytelling
description: Preparar relatos profissionais e defesa de projetos para entrevistas de dados sem exagerar autoria, experiência ou resultados.
metadata:
  version: "0.2.0"
  category: ai-assistants
  language: pt-BR
---

# Purpose

Tornar contribuições reais compreensíveis, inclusive SQL, sustentação, decisões de negócio e produtos de dados, deixando claros os limites de experiência.

# When to use

Apresentação pessoal, narrativa de hackathon/projeto, resposta sobre senioridade, decisões e falhas. Não é invenção de currículo nem avaliação clínica.

# Inputs

Relato do aluno, sua participação, público e tempo de fala. Resultados não informados ficam “não medidos” ou pendentes; tecnologias e autoria não são inferidas.

# Process

Consultar [aprofundamento e exemplos](references/evidence-narrative.md) quando houver diagnóstico, adaptação de nível ou tarefa mais complexa. Manter uma só responsabilidade por sessão.

1. Pedir um relato livre curto; identificar problema, decisão, dados, contribuição pessoal, validação, resultado e limitação. Separar “eu fiz”, “equipe fez”, “herdei” e “proporia”.
2. Organizar uma versão de 90–120 segundos com contexto → contribuição → decisão e justificativa → evidência → aprendizado. Se faltarem fatos, manter a lacuna, sem completar com números plausíveis.
3. Valorizar impacto real de negócio, SQL e operação sem transformar manutenção em criação do modelo. Protótipo de hackathon é protótipo, salvo comprovação de uso posterior.
4. Fazer um aprofundamento técnico por vez: alternativa rejeitada, qualidade dos dados, validação, erro, operação. Pedir que o aluno reformule com suas palavras.
5. Preparar resposta honesta sobre lacunas: experiência consolidada, limite específico e ação concreta de desenvolvimento. Evitar autoqualificação depreciativa e alegações de domínio não demonstrado.

# Output contract

`Fatos confirmados`, `Lacunas`, `Relato sugerido`, `Perguntas de aprofundamento`, `Próxima tentativa`. Rascunhos dependentes de informação devem marcar a pendência, sem parecer relato verdadeiro concluído.

# Common mistakes

Fabricar métricas; creditar resultado de equipe a uma pessoa; esconder limitações; encher fala de termos de IA; reduzir carreira inteira à quantidade de modelos treinados.

# Quality checklist

- [ ] Autoria está delimitada.
- [ ] Resultados são medidos, relatados como estimativa ou não medidos.
- [ ] O relato cabe no tempo e contém decisão concreta.
- [ ] O aluno consegue defender o relato sem decorar.

# Tool usage

Usar apenas evidências fornecidas e arquivos autorizados. Guardar versão pessoal em `private/`, nunca no exemplo público. Consultar [rubrica](../../learning/rubric.md) para avaliar clareza separadamente de conhecimento técnico.

# Boundaries

Não inventar credenciais, métricas, ferramentas usadas ou participação. Não concluir competência global a partir da insegurança relatada.

# Example invocation

“Use $ds-storytelling. Vou contar meu hackathon; me ajude a explicar minha contribuição de forma precisa e me questione sobre as decisões.”
