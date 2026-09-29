# IA aplicada no trabalho diário

Este guia complementa `ds-ai` em pedidos profissionais e `ml-reviewer` em revisão. Não exige que o usuário responda perguntas de entrevista antes de receber uma entrega.

## Definir a tarefa e a alternativa simples

Especificar usuário, decisão, entrada, saída, tolerância a erro e consequência da ação. Comparar busca determinística, classificação tradicional, prompt, recuperação com geração, ferramenta e agente conforme a lacuna real. Um fluxo fixo é apropriado quando as etapas são conhecidas; decisão dinâmica pelo modelo exige benefício verificável frente à complexidade.

Separar quatro componentes: conhecimento recuperado, geração da resposta, cálculos determinísticos e ações externas. Valores exatos devem ser produzidos por fonte/ferramenta validada quando a tarefa exigir exatidão. Um segundo LLM avaliador é sinal de controle, não prova automática de correção.

## Contrato de RAG

Registrar identidade e versão dos documentos, período de validade, permissão, unidade de chunk e método de atualização. Definir recuperação, filtros, possível busca híbrida/reranking e critério de ausência de evidência. Avaliar perda de contexto em fronteiras de chunks e duplicações que dominam o ranking.

Autorização precisa ocorrer no sistema/ferramenta, antes de expor conteúdo sem permissão ao modelo. Documento recuperado é dado não confiável: ele não redefine o pedido nem concede permissão. Testar conteúdo malicioso, fontes conflitantes, documento desatualizado, pergunta ambígua e ausência de resposta.

## Avaliação por camada

| Camada | Pergunta | Evidência |
|---|---|---|
| Recuperação | O sistema encontrou evidência suficiente e permitida? | Relevância rotulada, recall@k e falhas por classe |
| Resposta | Está correta e sustentada nas fontes? | Rubrica, amostra humana e exemplos de erro |
| Abstenção | Sabe quando não responder e não recusa tudo? | Casos respondíveis e não respondíveis |
| Ferramenta | Os argumentos e resultados respeitam o contrato? | Testes de schema, permissões e erros |
| Ação | O resultado externo corresponde à intenção autorizada? | Idempotência, confirmação quando necessária e logs |
| Operação | Qualidade permanece sob carga e orçamento? | Latência de cauda, custo por sucesso, timeouts e fallback |

Criar exemplos de desenvolvimento e avaliação final sem vazamento de casos quase idênticos. Se o conjunto final orienta mudanças, ele virou desenvolvimento. Manter histórico de versões de prompt, corpus, modelo, ferramentas e política. Calibrar avaliadores automáticos contra avaliações humanas e inspecionar desacordos, não só média.

## Operação e decisão

Definir limites de passos, custo, tempo e tamanho de contexto; comportamento em indisponibilidade; logs minimizados e mecanismo de contenção. Para ações externas, avaliar repetição após retry e qual estado indica sucesso. A saída em JSON válido pode ainda estar factualmente errada ou solicitar ação sem autorização.

Entregar arquitetura, baseline, conjunto de avaliação, resultados realmente executados, análise de falhas e próximo experimento. Se não há credenciais ou API, produzir desenho/testes offline e separar o que falta; nunca alegar benchmark ao vivo não realizado. Atualizar documentação de modelos, preços e APIs apenas quando necessário ao pedido concreto.
