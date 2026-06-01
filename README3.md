Por que seria incorreto usar a função dict() para transformar o resultado do nosso zip() em um dicionário, utilizando o nome do reagente como "Chave" e o lote como "Valor"?

As chaves de um dicionário (dict) devem ser obrigatoriamente únicas. Como o nosso inventário físico possui múltiplos lotes associados ao mesmo composto, ao tentar converter o mapeamento 
diretamente em um dicionário utilizando o nome do reagente como chave, cada nova ocorrência do mesmo reagente sobrescreveria o lote anterior. No final do processo, o dicionário conteria 
apenas um lote para cada composto (o último a ser lido), ocasionando perda massiva de dados e inviabilizando o controle total do estoque.

O que a função zip() gera na memória do Python antes de usarmos a função list() para forçar a visualização dos dados?

A função zip() gera um objeto iterador (especificamente do tipo zip). Esse objeto utiliza uma estratégia de processamento sob demanda conhecida como lazy evaluation (avaliação preguiçosa). 
Em vez de alocar memória instantaneamente para combinar todas as listas e construir uma nova estrutura volumosa, o iterador apenas armazena referências para as coleções originais e gera as tuplas 
correspondentes uma a uma, à medida que são solicitadas (por exemplo, dentro de um laço for). Forçar a conversão com list() consolida esses valores e efetivamente os armazena de forma persistente em memória.

De que forma o List Comprehension substitui a necessidade de criar uma lista vazia e usar a estrutura de repetição for tradicional acompanhada do método .append()?

Unifica o processo de inicialização da lista, a estrutura de repetição for, e as cláusulas condicionais de filtragem (if) em uma única linha com sintaxe matemática e declarativa. Do ponto de vista de desempenho, 
ela elimina a necessidade e o custo computacional de invocar repetidamente o método .append() em tempo de execução no interpretador Python, processando a inserção dos dados de forma otimizada em nível interno 
(C-level), o que torna o código não apenas mais limpo e legível, mas também consideravelmente mais rápido.
