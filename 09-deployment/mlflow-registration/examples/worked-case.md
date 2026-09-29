# Caso trabalhado: mlflow-registration

Cenário sintético de decisão; não é resultado executado em dados reais.

## Situação e análise

Um run possui boa métrica, mas a transformação não foi empacotada. Registrar só o estimador quebra inferência; validar o pipeline completo antes de criar versão consumível.

## Recomendação explicada

Consultar documentação oficial da versão instalada antes de gerar chamadas. O nome da skill não implica que uma conexão ao MLflow exista.

## O que entregar

Manifesto de artefato; evidências de carregamento; plano/comando de registro; status real.

## Como verificar

Executar somente a operação autorizada e verificar referência resultante. Sem acesso, entregar instrução revisável e marcar registro pendente.

## Contraponto

Salvar pickle não garante reexecução. Se a premissa do caso mudar, reavaliar a decisão em vez de reutilizar a conclusão. Informar o que falta para passar de hipótese a evidência.
