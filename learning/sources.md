# Fontes, mapa de leitura e ressalvas

Consulta: 28/09/2026. Os documentos foram fornecidos pelo usuário como materiais de estudo. Não há evidência de que constituam manual oficial, perguntas garantidas ou critérios atuais do Itaú. Não reproduzir integralmente os PDFs no repositório.

- **Sabatina, 2ª edição**, Douglas Lisboa Marques, 23/11/2024. Arquivo fornecido: `sabatina itau.pdf`, 151 páginas físicas. Autoria e data constam na página física 3; aviso de direitos na 4.
- **Data Science: um guia teórico de Ciência de Dados e Machine Learning**, Luiza Reixach Castro. Arquivo fornecido: `PDF CIENCIA DE DADOS -  LUIZA REIXACH CASTRO.pdf`, 114 páginas físicas. Data editorial não confirmada.

As páginas abaixo são físicas, contando a capa como 1. A paginação impressa pode divergir. O mapa usa sumários e inspeção de trechos; não é uma auditoria exaustiva das 265 páginas.

| Tema | Sabatina | Guia teórico | Uso no programa |
|---|---|---|---|
| Álgebra e estatística | 17–32 | 6–21 | Fundamentos e inferência |
| Preparação e PCA | 33–44 | 22–32 | Features, transformação e dados |
| Validação e seleção | 45–50 | 33–49 | Generalização e comparação |
| Classificadores | 51–76 | 58–86 | Logística, árvores e ensembles |
| Métricas de classificação | 77–80 | Conteúdo distribuído em ML e classificação | Limiar e avaliação |
| Regressão e avaliação | 81–92 | 50–57 | Loss, regularização e interpretação |
| Agrupamento | 93–112 | 87–101 | Trilha condicional |
| IA generativa | 113–116 | Sem capítulo dedicado identificado no sumário | Apenas introdução; complementar |

## Pontos revisados

1. **Threshold não é imutável em KNN, árvores ou SVM.** A página física 80 da Sabatina descreve cortes fixos. Em classificadores com probabilidades ou scores, a regra de decisão pode ser alterada; score de SVM não é automaticamente probabilidade. Ajustar limiar em validação adequada, não no teste final. Ver [scikit-learn: decision threshold](https://scikit-learn.org/stable/modules/classification_threshold.html).
2. **Encoding ordinal precisa de ordem explícita.** Na página física 29 do guia, o exemplo usa `LabelEncoder` numa feature de escolaridade. Na API do scikit-learn, `LabelEncoder` destina-se ao alvo `y`; para features, escolher codificação apropriada e, se ordinal, explicitar a ordem sem presumir que códigos automáticos a representem. Ver [LabelEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html).
3. **Preparação aprende apenas com treino.** Ler capítulos de preparação junto com validação. Imputação, escala, seleção e reamostragem aprendidas usando validação/teste contaminam a avaliação; pipelines ajudam a manter as etapas nos folds corretos. Ver [Common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html).

Os dois primeiros trechos também foram conferidos visualmente. Outras explicações devem ser verificadas conforme surgirem, especialmente APIs e generalizações estatísticas. Distinguir resumo da fonte de correção metodológica.

## Complementos primários para IA

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762): referência original da arquitetura Transformer; ler motivação e atenção antes de aprofundar detalhes.
- [Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401): referência original para combinar recuperação e geração; não implica que qualquer aplicação atual implemente exatamente o paper.
- [Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices): conjuntos específicos da tarefa, avaliação contínua e revisão humana; aqui usamos conceitos, não dependemos de uma plataforma de evals.
- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents): distinguir fluxo predefinido de escolha dinâmica pelo modelo; adicionar complexidade apenas quando justificada.

O caso, a rubrica e as perguntas deste repositório são exercícios originais. Sugestões de estudo refletem o prazo e o objetivo relatados, não informações internas de contratação. Preços, modelos disponíveis, bibliotecas e APIs precisam de nova verificação na documentação oficial antes de implementação.
