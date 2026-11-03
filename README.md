# Estrutura De Dados

# Order Book & Matching Engine Simulator

Um motor de negociação financeira (*Matching Engine*) de alta performance construído em **Python** para simular a recepção, ordenação e cruzamento de ordens de compra (*Bids*) e venda (*Asks*) em tempo real.

O diferencial técnico do projeto reside na **implementação "do zero" das estruturas de dados lineares**, sem o uso de bibliotecas nativas de alto nível (como `list` ou `collections.deque`), garantindo o controle manual de alocação de memória, ponteiros e referências.

---

## Arquitetura e Estruturas de Dados Personalizadas

Para garantir controle estrito sobre a complexidade de tempo e espaço, todas as estruturas foram construídas manipulando nós (`Node`) e ponteiros (`next` / `prev`)[cite: 2, 3]:

### 1. Fila de Entrada (FIFO Queue)
* **Finalidade:** Funciona como *buffer* de alta eficiência para recepção cronológica de novas ordens.
* **Implementação:** Encadeamento simples de nós com ponteiros para início e fim.
* **Complexidade:** Operações de enfileirar (`enqueue`) e desenfileirar (`dequeue`) em $O(1)$.

### 2. Livro de Ofertas (Listas Duplamente Encadeadas Ordenadas)
* **Lista de Compras (Bids):** Mantida dinamicamente em **ordem decrescente de preço** (maior oferta no topo).
* **Lista de Vendas (Asks):** Mantida dinamicamente em **ordem crescente de preço** (menor oferta no topo)[cite: 2].
* **Complexidade:** Inserção ordenada e busca com custo assintótico $O(n)$[cite: 2]; remoção e religamento de ponteiros em $O(1)$ após a localização do nó[cite: 2].

### 3. Sistema de Cancelamento / Undo (LIFO Stack)
* **Finalidade:** Rastreamento do histórico de ordens ativas para suporte a cancelamentos rápidos[cite: 2].
* **Complexidade:** Empilhar (`push`) e desempilhar (`pop`) em $O(1)$[cite: 2].

---

## ⚙️ Funcionamento da Matching Engine

Cada ordem de negociação possui os seguintes atributos:
* **ID (`int`):** Identificador único da ordem[cite: 1].
* **Tipo (`char`):** `C` para Compra ou `V` para Venda[cite: 1].
* **Preço (`float`):** Valor unitário limite[cite: 2].
* **Quantidade (`int`):** Volume de ativos[cite: 2].
* **Timestamp (`t`):** Momento de entrada no sistema[cite: 2].

```text
[ Nova Ordem ] ➔ ( Fila FIFO ) ➔ [ Matching Engine ]
                                        │
                         ┌──────────────┴──────────────┐
                         ▼                             ▼
                 Match Realizado?             Inserção Ordenada
             (Preço Compra ≥ Venda)          (Livro Bids / Asks)
                         │                             │
                         ▼                             ▼
                Execução & Ajuste              Pilha de Undo O(1)
