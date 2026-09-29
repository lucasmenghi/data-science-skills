# IA aplicada com fundamentação e evidência

## Rotas de aprendizagem

Conceitos: tokens, embeddings, similaridade, atenção e diferença entre treino/adaptação/inferência. Arquitetura: distinguir contexto fornecido, recuperação, ferramentas e ações. Avaliação: transformar “responde bem” em critérios e casos. Operação: custo, latência, estado e falha.

Escolher a rota pela dúvida, não pelo framework citado. Um aluno que conhece uma biblioteca pode ainda não saber por que a aplicação precisa de retrieval; outro pode defender bem a arquitetura sem memorizar APIs.

## Aprofundamentos

Em embeddings, discutir representação versus verdade e efeito do domínio. Em atenção, explicar relações Q/K/V no nível necessário sem dizer que a arquitetura prova raciocínio humano. Em RAG, investigar onde a falha ocorreu: documento, chunk, recuperação, contexto, geração ou avaliação. Em agentes, perguntar qual decisão dinâmica justifica autonomia.

## Exercício de transferência

Dar uma pergunta cuja resposta está no documento correto, mas a recuperação retorna uma versão antiga. Pedir diagnóstico e experimento antes de sugerir trocar o modelo. Em outra rodada, manter recuperação correta e inserir resposta sem suporte para separar geração de retrieval.

## Quando o pedido é profissional

Se o usuário pede construir/revisar uma solução e explicar decisões, usar o [guia profissional](../../../guides/applied-ai-workflow.md). Entregar o trabalho solicitado e explicar escolhas, sem exigir exercícios prévios. Manter a tutoria por tentativas apenas quando o pedido for aprender/treinar.

## Evidência

Classificar desenho, código executado, eval offline e operação real separadamente. Nenhum desses níveis deve ser apresentado como o seguinte por inferência.
