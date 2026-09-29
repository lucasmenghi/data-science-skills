# Caso original: assistente de políticas internas

Cenário inteiramente fictício: uma equipe quer responder perguntas sobre políticas a partir de documentos aprovados. Não usar documentos reais da empresa. O sistema deve mostrar fontes, lidar com versões e recusar inferências quando não houver evidência. O aluno precisa definir sucesso antes de escolher tecnologia.

## Dados mínimos para começar sem API

Crie três documentos curtos, mantendo identificador, data e permissão:

- `policy-v1`, válido até 30/06/2026, público interno: limite fictício de reembolso de R$100.
- `policy-v2`, válido a partir de 01/07/2026, público interno: limite fictício de R$150; solicitações exigem comprovante.
- `restricted-note`, acesso exclusivo da equipe A: observação fictícia de processo que outros usuários não podem receber.

São fatos sintéticos do exercício, não políticas de instituição real. Para o caso adversarial, acrescente em uma cópia um trecho que ordena ignorar regras e revelar outro documento. Ele deve continuar sendo dado não confiável.

## Etapas de construção

1. Formular perguntas e respostas esperadas antes de ajustar o sistema: 6 casos de desenvolvimento e 6 casos de teste final, sem paráfrases quase idênticas atravessando a divisão. Doze casos são um exercício inicial, não prova estatística de qualidade.
2. Incluir pergunta respondível, sem resposta, ambígua, histórica, com documentos conflitantes, acesso negado e injeção de instrução. Registrar documentos relevantes e comportamento esperado em cada caso.
3. Fazer baseline de busca por palavras e retorno de trechos. Se houver runtime apropriado, comparar com embeddings; caso contrário, explicar o experimento sem afirmar tê-lo executado.
4. Desenhar ingestão → divisão em trechos → indexação → recuperação com autorização → seleção de contexto → geração com evidência → resposta/abstenção. Controle de acesso é aplicado no sistema e no acesso às ferramentas, não confiado apenas ao prompt.
5. Comparar uma única mudança por vez: tamanho de trecho, busca híbrida, reranking ou instrução de resposta. Escolher com desenvolvimento e guardar o teste final até congelar a solução.
6. Medir erros de recuperação separadamente dos de geração. Relatar custo e latência apenas se medidos; usar estimativa explicitamente marcada caso contrário.

## Perguntas para defesa

- Qual problema a busca simples já resolve? Por que adicionar geração?
- Se o documento certo não aparece no top-k, adianta trocar o modelo gerador?
- Como datas e permissões afetam o contexto recuperado?
- Qual diferença entre uma resposta correta e uma resposta sustentada pelas fontes?
- Quando usar fine-tuning? Por que ele não substitui atualização do corpus nem autorização?
- A tarefa precisa de agente com ferramentas ou de um fluxo previsível?
- Como saber se o avaliador automático tem viés? Qual amostra seria revisada por humanos?
- Qual falha exige bloquear o lançamento mesmo com boa média?

## Avaliação esperada

| Camada | Medida possível | Limitação a explicar |
|---|---|---|
| Recuperação | Recall@k = relevantes recuperados / relevantes existentes | Exige conjunto de relevância rotulado e unidade definida (trecho/documento) |
| Ordenação | MRR da primeira evidência relevante | Não mede cobertura de perguntas com múltiplas evidências |
| Resposta | Correção por rubrica e suporte nas fontes | Similaridade textual sozinha não garante verdade |
| Abstenção | Recusa correta em perguntas sem evidência; recusa indevida em respondíveis | Não otimizar só recusando tudo |
| Segurança | Violações de acesso e sucesso de injeções em casos adversariais | Zero falhas em amostra pequena não prova ausência de risco |
| Operação | Latência p50/p95, custo por resposta útil, timeout e fallback | Simulação não equivale a produção |

A rubrica do avaliador deve dizer o que conta como sucesso; validar parte das notas com humanos. Registrar versão dos dados, prompt, modelo e recuperação. Se aparecer erro no teste e o sistema for alterado, declarar que esse teste virou desenvolvimento e buscar novos casos finais.

## Entrega

Diagrama ou descrição da arquitetura; conjunto de perguntas; baseline; tabela de resultados reais ou marcada como não executada; análise de três falhas; próximo experimento. Uma demo bonita sem avaliação não encerra o caso.
