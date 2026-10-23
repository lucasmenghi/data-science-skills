# Guia de decisão: causal-thinking

## Pergunta que esta skill resolve

Estruturar perguntas causais, DAGs e estratégias de identificação antes de estimar efeitos.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Variável é mediadora | Decidir se efeito total ou direto é a pergunta | Ajustar pode remover parte do efeito desejado. |
| Variável é collider | Evitar condicionamento sem justificativa | Ajuste pode criar associação espúria. |
| Antes/depois simples | Investigar tendência, sazonalidade e comparação | Mudança temporal não isola efeito. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Ajustar todas as variáveis disponíveis; confundir significância com identificação.

DAG expressa hipóteses de domínio, não relações comprovadas apenas pela correlação. Informar quais hipóteses permanecem não testáveis.

## Contrato de entrega

Pergunta causal; DAG textual/gráfico; estimando; estratégia; hipóteses e sensibilidade.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
