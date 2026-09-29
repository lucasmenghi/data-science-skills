# Guia de decisão: missing-value-strategy

## Pergunta que esta skill resolve

Escolher e validar tratamento de ausências considerando mecanismo, disponibilidade e efeito operacional.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Ausência estrutural | Codificar estado semântico separado | Zero pode representar valor real distinto de não aplicável. |
| Imputação por grupo | Estimar no treino e fallback global treinado | Grupos novos não podem consultar o teste para preencher. |
| Missing mudou na produção | Investigar fonte antes de retreinar | Imputar pode esconder indisponibilidade upstream. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Imputar antes de split; transformar todo nulo em zero; usar alvo para preencher features futuras.

Excluir linhas muda a população atendida. Explicar cobertura perdida e reconhecer que qualidade preditiva não identifica o mecanismo de missing.

## Contrato de entrega

Matriz de tratamentos; hipótese do mecanismo; experimento comparativo; política de fallback.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
