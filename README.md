# Estrutura De Dados
Motor de negociação financeira (Matching Engine) concebido para a simulação e execução de ordens de compra e venda em tempo real. O projeto implementa estruturas de dados lineares personalizadas construídas de raiz — sem recurso a tipos nativos (como list) ou bibliotecas como collections.deque —, garantindo o controlo manual de ponteiros, alocação de memória e análise de complexidade assintótica.   
_______________________________________

Arquitetura:

Fila de Entrada (FIFO): Buffer cronológico para receção e processamento de ordens com operações em O(1).   
Captura de Tela 2026-11-03 às 17.07.48.jpg
Livro de Ofertas (Listas Duplamente Encadeadas Ordenadas): Gestão dinâmica de ordens de compra (em ordem decrescente) e de venda (em ordem crescente).   
Motor de Match: Algoritmo de cruzamento automático com atualização e remoção direta de nós.   
Sistema de Cancelamento (Pilha LIFO): Rastreio de histórico que possibilita o cancelamento rápido em O(1).   
Análise de Desempenho: Benchmarks empíricos e gráficos no Jupyter Notebook que comparam a complexidade teórica (O(1) e O(n)) ao processar grandes volumes de dados.   
_______________________________________

Tecnologias: Python 3, Jupyter Notebook, Matplotlib e Pandas.
