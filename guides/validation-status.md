# Escopo da verificação

Verificação local em 29/09/2026:

- Validador do repositório aprovado: manifests, contratos, arquivos de apoio, sintaxe Python, links locais e entradas de descoberta.
- Validador oficial de skills aprovado nas 68 instruções canônicas e 68 entradas de descoberta.
- 20 testes automatizados aprovados: utilitários de decisão, proteção do gerador e join temporal SQL em SQLite.
- Cinco utilitários executados pela CLI com entradas sintéticas; os três comandos do QUICKSTART foram executados com sucesso.

Essas verificações comprovam os comportamentos cobertos e a consistência estrutural. Não são uma avaliação independente das respostas de todas as skills, nem comprovam execução em Databricks/PySpark, MLflow ou serviços de IA. Os casos Markdown orientam o comportamento esperado; não são registros de execução em clientes reais.

Para avaliar uma skill em uso, escolher um pedido representativo com artefatos sintéticos, registrar a resposta e verificar se a decisão decorre das evidências, se o código executa no ambiente alvo e se as limitações são identificadas. Separar falha metodológica, falha de ferramenta e contexto insuficiente. Atualizar instruções com base em falhas observadas, sem transformar um caso particular em regra universal.
