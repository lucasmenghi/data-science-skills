# Data Science Skills

**68 skills em 13 temas para apoiar o trabalho diário de um cientista de dados, explicando as decisões e produzindo entregas verificáveis.**

A biblioteca cobre entendimento do negócio, descoberta, preparação, features, modelos, validação, interpretabilidade, experimentação, deployment, monitoramento, impacto, documentação e assistentes. Python e SQL são a base; Databricks/PySpark entram quando o ambiente ou o volume justificam.

**[Comece pelo guia de uso](QUICKSTART.md)** ou consulte o [catálogo completo](STRUCTURE.md).

## Uma entrada para o trabalho diário

```text
Use $ds-workbench. Quero revisar este projeto de Data Science.
Inspecione os artefatos disponíveis, identifique as decisões mais importantes,
execute as verificações possíveis e explique o que encontrou e por que importa.
```

O assistente escolhe as skills necessárias ao pedido, trabalha nos artefatos autorizados e entrega recomendação, evidência, alternativas e limitações. Ele não impõe sabatina quando o objetivo é uma entrega profissional.

## Profundidade e estrutura

- Cada skill de trabalho tem processo próprio, critérios condicionais, falhas comuns e caso sintético.
- O [aprofundamento metodológico](guides/method-depth.md) trata estimandos, dependência, leakage, seleção, utilidade, interpretação, causalidade e operação.
- O [protocolo de decisão](guides/decision-protocol.md) orienta explicar observação, consequência e verificação sem inventar resultados.
- Os [casos integrados](examples/workflows/retention-decision.md) mostram como combinar etapas; não é preciso rodar todas em cada tarefa.
- Cinco utilitários determinísticos apoiam framing, janelas, priorização, critérios e avaliação de políticas de threshold. Não substituem julgamento metodológico.

Há 61 skills de trabalho, incluindo o coordenador, e 7 agentes de aprendizagem. Os 60 nomes do catálogo original estão implementados. O conteúdo é uma biblioteca de instruções e referências; não é um serviço de agentes executando permanentemente.

## Aprendizagem e entrevista

Para estudar com tentativa, feedback e progresso, use `$ds-mentor` e [o guia de estudo](learning/START-HERE.md). O programa de entrevista e os registros locais foram preservados. Contexto pessoal fica em `private/`, ignorado pelo Git.

## Uso no Codex e outros assistentes

Abra a pasta deste repositório como projeto. As entradas `.agents/skills/` apontam para as instruções canônicas nas categorias. Se a skill não aparecer, peça ao assistente para ler o `SKILL.md` pelo caminho. Mantenha o repositório completo, pois há referências relativas compartilhadas. Outros assistentes podem ler as instruções; integração com cada produto não foi testada.

## Verificação e manutenção

Python 3.11+ para os utilitários; PyYAML é necessário apenas para a validação do repositório.

```sh
python -m pip install -r requirements-dev.txt
python scripts/build_codex_entries.py
python validate_skills.py
python -m unittest discover -s tests -v
```

Consulte o [escopo da verificação realizada](guides/validation-status.md). Leia [AGENTS.md](AGENTS.md) para manutenção. O gerador protege entradas manuais e rejeita nomes duplicados; ele não apaga ponteiros órfãos silenciosamente. A validação estrutural não comprova a eficácia de todas as skills em trabalho real. Exemplos e testes locais não comprovam integração em Databricks ou serviço externo.

## Fontes e dados

[Fontes primárias](guides/sources.md) apoiam consulta metodológica e de APIs. Materiais de estudo fornecidos pelo usuário têm [atribuição e ressalvas](learning/sources.md); PDFs originais não são redistribuídos. Não incluir dados de clientes, credenciais, histórico pessoal ou evidência confidencial em commits.
