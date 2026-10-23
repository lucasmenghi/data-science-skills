# Guia de decisão: readme-generator

## Pergunta que esta skill resolve

Criar README que permite entender, instalar e reproduzir um projeto com comandos verificados.

## Critérios condicionais

| Evidência ou condição | Abordagem inicial | Risco e alternativa a explicar |
|---|---|---|
| Sem acesso à infraestrutura | Documentar dependência e execução não verificada | Não escrever que basta rodar se falta serviço. |
| Exemplo sintético | Marcar como demo | Não confundir com pipeline produtivo. |
| Projeto mudou | Reescrever visão em torno do comportamento atual | Evitar roadmap descrito como funcionalidade. |

Esses critérios são condicionais, não thresholds universais. Se duas opções atendem ao objetivo, comparar custo, fragilidade e incerteza do ganho; justificar quando a solução simples basta. Registrar a evidência que levaria a trocar a recomendação.

## Armadilhas e limites de interpretação

Documentar arquivos inexistentes; copiar comandos não testados; badge de licença sem licença.

Explicação de uso precisa corresponder ao estado real. Uma biblioteca pode estar completa no escopo sem ter integração validada em todos os ambientes.

## Contrato de entrega

README navegável; quickstart; comandos verificados; pré-requisitos e limitações.

Uma recomendação deve ser rastreável: condição observada → decisão → consequência esperada → verificação. Se não há acesso aos dados, escrever essa cadeia como proposta. O [caso trabalhado](../examples/worked-case.md) é sintético e demonstra como interpretar a saída.
