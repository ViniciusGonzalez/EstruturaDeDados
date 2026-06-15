class No:
    """
    No generico de encadeamento simples, usado pela Fila e pela Pilha.
    Guarda um valor e uma referencia para o proximo no.
    """

    def __init__(self, valor):
        self.valor = valor   # na Fila e uma Ordem; na Pilha e um ID (int)
        self.prox = None     # referencia para o proximo no


# ---------------------------------------------------------------------
#  FILA DE ENTRADA  (FIFO - First In, First Out)
#  Insere no FIM, remove do INICIO. Todas as operacoes em O(1).
# ---------------------------------------------------------------------
class Fila:

    def __init__(self):
        self.inicio = None   # primeiro no (o proximo a sair)
        self.fim = None      # ultimo no (onde se insere)
        self.tamanho = 0

    def esta_vazia(self):
        return self.tamanho == 0

    def ve_tamanho(self):
        return self.tamanho

    def enfileira(self, valor):
        """Insere um elemento no FIM da fila. O(1)."""
        novo = No(valor)
        if self.esta_vazia():
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.prox = novo   # liga o antigo ultimo no ao novo
            self.fim = novo        # o novo passa a ser o ultimo
        self.tamanho += 1

    def desenfileira(self):
        """Remove e devolve o elemento do INICIO da fila. O(1)."""
        if self.esta_vazia():
            raise Exception("A fila de entrada esta vazia: nada a remover.")
        removido = self.inicio
        self.inicio = self.inicio.prox
        if self.inicio is None:   # a fila ficou vazia: zera tambem o fim
            self.fim = None
        self.tamanho -= 1
        return removido.valor

    def ve_inicio(self):
        """Consulta (sem remover) o elemento do inicio. O(1)."""
        if self.esta_vazia():
            raise Exception("A fila de entrada esta vazia.")
        return self.inicio.valor

    def __str__(self):
        atual = self.inicio
        saida = "Inicio -> "
        while atual:
            saida += f"[{atual.valor}] -> "
            atual = atual.prox
        return saida + "Fim"


# ---------------------------------------------------------------------
#  PILHA DE UNDO  (LIFO - Last In, First Out)
#  Armazena os IDs das ordens inseridas com sucesso no livro de
#  ofertas. Insere e remove sempre pelo TOPO. Operacoes em O(1).
# ---------------------------------------------------------------------
class Pilha:

    def __init__(self):
        self.topo = None     # no do topo da pilha
        self.tamanho = 0

    def esta_vazia(self):
        return self.tamanho == 0

    def ve_tamanho(self):
        return self.tamanho

    def empilha(self, valor):
        """Insere um elemento no TOPO da pilha. O(1)."""
        novo = No(valor)
        novo.prox = self.topo   # o novo aponta para quem era o topo
        self.topo = novo        # o novo passa a ser o topo
        self.tamanho += 1

    def desempilha(self):
        """Remove e devolve o elemento do TOPO da pilha. O(1)."""
        if self.esta_vazia():
            raise Exception("A pilha de undo esta vazia: nada a desempilhar.")
        removido = self.topo
        self.topo = self.topo.prox
        self.tamanho -= 1
        return removido.valor

    def ve_topo(self):
        """Consulta (sem remover) o elemento do topo. O(1)."""
        if self.esta_vazia():
            raise Exception("A pilha de undo esta vazia.")
        return self.topo.valor

    def __str__(self):
        atual = self.topo
        saida = "Topo -> "
        while atual:
            saida += f"[{atual.valor}] -> "
            atual = atual.prox
        return saida + "Base"


# ---------------------------------------------------------------------
#  Teste rapido (so executa quando o arquivo e rodado diretamente).
#  Rode de dentro da pasta 'pacote':  python entrada_undo.py
# ---------------------------------------------------------------------
if __name__ == "__main__":
    from ordem import Ordem

    print("=== Teste da Fila de Entrada (FIFO) ===\n")
    fila = Fila()
    fila.enfileira(Ordem(1, "C", 450.00, 1000))
    fila.enfileira(Ordem(2, "V", 400.00, 800))
    fila.enfileira(Ordem(3, "C", 455.00, 500))
    print(fila)
    print(f"Tamanho da fila: {fila.ve_tamanho()}")

    print("\nProcessando a fila na ordem de chegada (FIFO):")
    while not fila.esta_vazia():
        ordem = fila.desenfileira()
        print(f"  Saiu: {ordem}")
    print(f"Fila vazia? {fila.esta_vazia()}")

    print("\n=== Teste da Pilha de Undo (LIFO) ===\n")
    pilha = Pilha()
    for id_ordem in (1, 2, 3):
        pilha.empilha(id_ordem)
        print(f"  Empilhou ID {id_ordem}")
    print(pilha)

    print("\nCancelando a ultima acao (desempilha do topo):")
    print(f"  Ultimo ID inserido foi: {pilha.desempilha()}")
    print(pilha)