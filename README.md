# Data Science Skills

Biblioteca de métodos de Data Science e agentes de aprendizagem em português. O objetivo é apoiar decisões de projeto e desenvolver competência demonstrável em ciência de dados e IA.

**Preparando uma entrevista? [Comece aqui](learning/START-HERE.md).** Há uma [trilha de 24–72 horas](learning/emergency-plan.md) e uma [formação por competências](learning/curriculum.md).

## O que existe

| Categoria | Implementado |
|---|---|
| [01-business-understanding](01-business-understanding/README.md) | Framing, target, hipóteses e critérios de sucesso |
| [13-ai-assistants](13-ai-assistants/README.md) | Mentor, fundamentos, modelagem, IA aplicada, revisor, entrevistador e comunicação |

São 11 skills canônicas. As categorias 02 a 12 continuam planejadas; não são funcionalidades disponíveis.

## Usar os agentes

Abra este repositório no Codex e envie:

```text
Use $ds-mentor. Quero me preparar para uma entrevista de Data Science com foco em IA.
Comece pelo diagnóstico, uma pergunta por vez, e espere minha resposta.
```

Se a descoberta automática não estiver disponível, peça para ler `13-ai-assistants/ds-mentor/SKILL.md`. As instruções também podem ser lidas por outros assistentes com acesso aos arquivos; não houve teste de integração com cada produto.

Os agentes são skills que orientam papéis na conversa. Não há um serviço de agentes rodando em segundo plano. O material funciona sem contratar APIs adicionais. Para usar fora desta pasta, mantenha o repositório completo e seus links relativos.

## Como o estudo funciona

Diagnóstico por respostas → prioridade conforme prazo → exercício → feedback → nova tentativa independente → registro local. Notas sem evidência ficam como não avaliadas. O programa distingue domínio conceitual, aplicação, julgamento e comunicação, sem prometer aprovação ou atribuir senioridade por uma média.

Os PDFs fornecidos orientaram o [mapa de fontes](learning/sources.md); os originais não são redistribuídos. Há correções metodológicas e complementos para IA aplicada. Este projeto não é material oficial de recrutamento de nenhuma empresa.

## Estrutura e contribuição

Veja [STRUCTURE.md](STRUCTURE.md), [AGENTS.md](AGENTS.md) e [CLAUDE.md](CLAUDE.md). Preserve as skills existentes e mantenha as referências verificáveis.

```sh
python -m pip install -r requirements-dev.txt
python scripts/build_codex_entries.py
python validate_skills.py
python -m unittest discover -s tests -v
```

As entradas `.agents/skills/` são geradas; as instruções canônicas ficam nas categorias. `private/` guarda contexto e sessões pessoais e é ignorada pelo Git. Não inclua dados de clientes, credenciais ou materiais de terceiros sem autorização.
