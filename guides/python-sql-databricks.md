# Python e SQL, com adaptação a Databricks/PySpark

## Escolher o motor

Começar por schema, volume, partições, onde o dado já está e qual entrega é necessária. Python local é adequado para amostras que cabem com folga em memória e experimentos pequenos. SQL evita transferir tabelas quando a operação é agregação, filtro ou join. PySpark faz sentido quando o ambiente ou o volume exige execução distribuída; não converter um pequeno utilitário para Spark por hábito.

Não inferir credenciais, Unity Catalog, nomes de tabelas ou permissões a partir do nome da plataforma. Gerar código com nomes fornecidos; se faltarem, usar exemplo sintético claramente identificado. Não executar placeholders como se fossem destinos reais.

## Portabilidade sem falsa equivalência

| Tema | Python/SQL local | Databricks/PySpark |
|---|---|---|
| Leitura | Conferir tamanho e tipos; projetar colunas | Filtrar partições e projetar colunas na origem |
| Perfil | Quantis/distinct exatos se viáveis | Marcar quando quantis/distinct são aproximados |
| Joins | Validar cardinalidade e chaves nulas | Conferir plano, skew, shuffle e cardinalidade |
| Transformação | Pipeline fit no treino | Separar fit/transform e conferir semântica da implementação |
| Aleatoriedade | Seed e ordenação quando necessária | Seed não garante mesma partição/ordem após mudanças |
| Resultados | DataFrames pequenos | Agregar no cluster; coletar só resultado limitado |
| Persistência | Artefato e dependências versionados | Referenciar snapshots/versões e ambiente autorizado |

Em pandas, chaves nulas podem se comportar de modo diferente de joins SQL; confirmar a operação concreta. Em SQL, `NULL` exige tratamento explícito e pode afetar filtros, contagens e igualdade. Datas devem usar fuso e convenções de borda documentados. Valores monetários precisam de precisão e arredondamento definidos, não apenas dtype “numérico”.

## Procedimento para uma consulta analítica

1. Escrever a unidade de uma linha de cada fonte e da saída.
2. Estimar filtro/volume e inspecionar plano quando a consulta pode ser cara.
3. Validar chave antes da junção; medir correspondência e perdas.
4. Agregar cada fonte na granularidade necessária antes de combinar eventos de vários lados.
5. Definir denominadores e exposição. `AVG(taxa)` não equivale a `SUM(numerador)/SUM(denominador)`.
6. Reconciliar contagens, montantes e chaves após a transformação.

Otimização vem depois da correção lógica. Broadcast só deve ser usado quando o lado pequeno cabe de forma segura e o plano justifica; cache só quando existe reutilização que compensa materialização/memória. Evitar UDF Python quando funções nativas atendem ao mesmo significado e são testadas.

## Preparação e modelagem

O split define a fronteira de informação. Limpeza determinística por linha, como parse de formato documentado, não aprende uma distribuição. Imputação, escala, vocabulário de categorias raras, PCA, seleção pelo alvo e tuning aprendem dos dados e precisam ser ajustados no treino de cada fold.

Depois da seleção, pode-se refazer o treinamento no conjunto de desenvolvimento autorizado, mantendo o teste independente. Refit não permite voltar a escolher hiperparâmetros pelo teste. A inferência aplica transformações congeladas; ela não executa fit novamente.

Não prometer equivalência automática entre estimadores locais e distribuídos: loss, regularização, missing, categorias, otimização e tolerâncias podem diferir. Usar casos pequenos com valores esperados e comparar previsões/transformações dentro de tolerância justificada.

## Evidência de execução

Registrar motor/versão, dados ou referência de snapshot, parâmetros, comandos e resultado. Se o ambiente Databricks não estiver acessível, preparar código e checks, mas marcar como não executados. Conferir APIs na documentação da versão usada; a biblioteca não fixa uma versão universal de Spark, scikit-learn ou MLflow.
