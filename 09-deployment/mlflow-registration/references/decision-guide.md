# Guia de decisão: mlflow-registration

## Pergunta que esta skill resolve

Preparar registro de artefatos no MLflow com linhagem, assinatura e evidências reproduzíveis.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Backend Unity Catalog | Verificar nome completo, assinatura e permissões | Não inferir catálogo/schema real. |
| Alias aponta produção | Tratar atualização como mudança operacional | Registrar versão não autoriza promoção. |
| Dependências ausentes | Resolver ambiente reproduzível antes do aceite | Salvar pickle não garante reexecução. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Confundir tracking com registry; assumir APIs de versões diferentes; promover sem autorização.

Consultar documentação oficial da versão instalada antes de gerar chamadas. O nome da skill não implica que uma conexão ao MLflow exista.

## Contrato de entrega

Manifesto de artefato; evidências de carregamento; plano/comando de registro; status real.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
