# 13 — AI Assistants

Sete agentes de aprendizagem em português, implementados como skills. Cada papel funciona isoladamente; `ds-mentor` coordena a sequência na mesma conversa.

| Skill | Responsabilidade |
|---|---|
| [ds-mentor](ds-mentor/SKILL.md) | Diagnóstico, prioridade e progresso |
| [ds-foundations](ds-foundations/SKILL.md) | Matemática, estatística e inferência |
| [ds-modeling](ds-modeling/SKILL.md) | Construção de ML com autoria do aluno |
| [ds-ai](ds-ai/SKILL.md) | IA aplicada, RAG, ferramentas e avaliação |
| [ds-reviewer](ds-reviewer/SKILL.md) | Revisão metodológica e defesa |
| [ds-interviewer](ds-interviewer/SKILL.md) | Sabatina interativa |
| [ds-storytelling](ds-storytelling/SKILL.md) | Comunicação de experiência real |

Comece em [START-HERE](../learning/START-HERE.md). Os materiais compartilhados ficam em `learning/`; os arquivos pessoais em `private/` são ignorados pelo Git. Os agentes precisam do repositório completo, pois compartilham rubrica e referências por links relativos.

As entradas de descoberta `.agents/skills/` são geradas por `scripts/build_codex_entries.py`. Edite as instruções aqui e regenere somente quando nome/descrição mudar. Não existe processo autônomo permanente nem dependência de API externa. Simulações reais ainda dependem da interação do aluno.
