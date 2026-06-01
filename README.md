O arquivo calculadora_viagem.py funciona da seguinte maneira:
- Siga as instruções dos inputs
- Responda apenas com números (exceto para escrever o destino da viagem)
- Divirta-se usando :)


Perguntas teóricas:
1. O git add . envia as alterações para a Área de Estágio, preparando os arquivos que serão salvos.
O git commit -m "mensagem" grava em definitivo essas alterações preparadas no histórico do repositório.

2. A função input() sempre lê os dados salvos do usuário como texto (string), mesmo que sejam digitados apenas números.
O casting converte esse texto em int ou float para que o Python consiga realizar operações matemáticas com ele.

3. O Python interrompe a execução e exibe um erro de tipo (TypeError), pois não mistura texto e número automaticamente.


O arquivo inventario_lab.py funciona da seguinte maneira:

- Rode o arquivo inventario_lab.py no terminal.

- Confira o total e quais os tipos de reagentes únicos estão disponíveis no laboratório.
- Analise a lista detalhada com o lote, nome e pureza de cada frasco individual.
- Pegue a lista final para identificar instantaneamente quais lotes têm pureza a partir de 98% e estão liberados para experimentos sensíveis.

Perguntas teóricas:

1. As chaves de um dicionário (dict) devem ser obrigatoriamente únicas. Como o nosso inventário físico possui múltiplos lotes associados ao mesmo composto (por exemplo, várias entradas diferentes de "Etanol"), ao tentar converter o mapeamento diretamente em um dicionário utilizando o nome do reagente como chave, cada nova ocorrência do mesmo reagente sobrescreveria o lote anterior. No final do processo, o dicionário conteria apenas um lote para cada composto (o último a ser lido), ocasionando perda massiva de dados e inviabilizando o controle total do estoque.

2. A função zip() gera um objeto iterador (especificamente do tipo zip). Esse objeto utiliza uma estratégia de processamento sob demanda. Em vez de alocar memória instantaneamente para combinar todas as listas e construir uma nova estrutura volumosa, o iterador apenas armazena referências para as coleções originais e gera as tuplas correspondentes uma a uma, à medida que são solicitadas (por exemplo, dentro de um laço for). Forçar a conversão com list() consolida esses valores e efetivamente os armazena de forma persistente em memória.

3. O List Comprehension unifica o processo de inicialização da lista, a estrutura de repetição for, e as cláusulas condicionais de filtragem (if) em uma única linha com sintaxe matemática e declarativa. Do ponto de vista de desempenho, ela elimina a necessidade e o custo computacional de invocar repetidamente o método .append() em tempo de execução no interpretador Python, processando a inserção dos dados de forma otimizada em nível interno (C-level), o que torna o código não apenas mais limpo e legível, mas também consideravelmente mais rápido.
