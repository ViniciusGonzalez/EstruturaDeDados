from pacote.ordem import Ordem

class Fila:

    def __init__(self):
        self.head = None   # primeiro no (o proximo a sair)
        self.tail = None      # ultimo no (onde se insere)
        self.tamanho = 0

    def esta_vazia(self):
        return self.tamanho == 0

    def ve_tamanho(self):
        return self.tamanho

    def enfileira(self, tipo, preco, quantidade):
        """Insere um elemento no FIM da fila. O(1)."""
        novo = Ordem(tipo, preco, quantidade)
        if self.esta_vazia():
            self.head = novo
            self.tail = novo
        else:
            self.tail.next = novo   # liga o antigo ultimo no ao novo
            self.tail = novo        # o novo passa a ser o ultimo
        self.tamanho += 1

    def desenfileira(self):
        """Remove e devolve o elemento do INICIO da fila. O(1)."""
        if self.esta_vazia():
            raise Exception("A fila de entrada esta vazia: nada a remover.")
        removido = self.head
        self.head = self.head.next
        if self.head is None:   # a fila ficou vazia: zera tambem o fim
            self.tail = None
        self.tamanho -= 1
        return removido

    def ve_inicio(self):
        """Consulta (sem remover) o elemento do inicio. O(1)."""
        if self.esta_vazia():
            raise Exception("A fila de entrada esta vazia.")
        return self.head.preco

    def __str__(self):
        atual = self.head
        saida = "Inicio -> "
        while atual:
            saida += f"[{atual.preco}] -> "
            atual = atual.next
        return saida + "Fim"


# ---------------------------------------------------------------------
#  PILHA DE UNDO  (LIFO - Last In, First Out)
#  Armazena os IDs das ordens inseridas com sucesso no livro de
#  ofertas. Insere e remove sempre pelo TOPO. Operacoes em O(1).
# ---------------------------------------------------------------------
class IdPilha:
    def __init__(self, id):
        self.id = id
        self.next = None

class Pilha:

    def __init__(self):
        self.topo = None     # no do topo da pilha
        self.tamanho = 0

    def esta_vazia(self):
        return self.tamanho == 0

    def ve_tamanho(self):
        return self.tamanho

    def empilha(self, id):
        """Insere um elemento no TOPO da pilha. O(1)."""
        novo = IdPilha(id)
        novo.next = self.topo   # o novo aponta para quem era o topo
        self.topo = novo        # o novo passa a ser o topo
        self.tamanho += 1

    def desempilha(self):
        """Remove e devolve o elemento do TOPO da pilha. O(1)."""
        if self.esta_vazia():
            raise Exception("A pilha de undo esta vazia: nada a desempilhar.")
        removido = self.topo
        self.topo = self.topo.next
        self.tamanho -= 1
        return removido.id

    def ve_topo(self):
        """Consulta (sem remover) o elemento do topo. O(1)."""
        if self.esta_vazia():
            return None
        else:
            return self.topo.id

    def __str__(self):
        atual = self.topo
        saida = "Topo -> "
        while atual:
            saida += f"[{atual.id_ordem}] -> "
            atual = atual.next
        return saida + "Base"
