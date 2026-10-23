# Guia de decisão: eda-assistant

## Pergunta que esta skill resolve

Conduzir descoberta e exploração de um dataset como fluxo integrado orientado a decisões.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Tabela isolada simples | Perfil e perguntas dirigidas bastam | Não criar workflow de seis etapas por obrigação. |
| Join central ao problema | Auditar chave e cobertura primeiro | Gráfico pode parecer plausível com contagens erradas. |
| Achado exploratório forte | Formular confirmação independente | Evitar anunciar descoberta causal. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Inventário de gráficos sem conclusão; repetir os mesmos perfis em várias skills.

Esta skill coordena exploração real. Quando o usuário quer entender uma técnica isolada, chamar a skill específica é suficiente.

## Contrato de entrega

Relatório exploratório integrado; consultas; achados; riscos e testes seguintes.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
