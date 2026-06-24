class Node:

    def __init__(self, ordem):

        self.ordem = ordem
        self.next = None
        self.prev = None

class ListaCompras:

    def __init__(self):
        self.head = None
        self.tail = None

    def inserecompra(self, ordem):
        novo = Node(ordem)

        if self.head is None:
            self.head = novo
            self.tail = novo
            return

        elif ordem.preco > self.head.ordem.preco:
            novo.next = self.head
            self.head.prev = novo
            self.head = novo
            return

        atual = self.head

        while atual is not None:
            if ordem.preco > atual.ordem.preco:
                break
            atual = atual.next

        if atual is None:
            self.tail.next = novo
            novo.prev = self.tail
            self.tail = novo

        else:
            anterior = atual.prev
            anterior.next = novo
            novo.prev = anterior
            novo.next = atual
            atual.prev = novo


    def removecompra(self, node):

        if node == self.head and node == self.tail:
            self.head = None
            self.tail = None

        elif node == self.head:
            self.head = node.next
            self.head.prev = None

        elif node == self.tail:
            self.tail = node.prev
            self.tail.next = None

        else:
            anterior = node.prev
            proximo = node.next
            anterior.next = proximo
            proximo.prev = anterior


    def mostracompras(self):

        atual = self.head

        while atual is not None:
            oferta = atual.ordem
            print(
                "ID -",oferta.id,
                "Preço -",oferta.preco,
                "Quantidade -",oferta.quantidade
            )
            atual = atual.next


class ListaVendas:

    def __init__(self):
        self.head = None
        self.tail = None

    def inserevenda(self, ordem):
        novo = Node(ordem)

        if self.head is None:
            self.head = novo
            self.tail = novo
            return


        if ordem.preco < self.head.ordem.preco:
            novo.next = self.head
            self.head.prev = novo
            self.head = novo
            return

        atual = self.head

        while atual is not None:
            if ordem.preco < atual.ordem.preco:
                break
            atual = atual.next

        if atual is None:
            self.tail.next = novo
            novo.prev = self.tail
            self.tail = novo

        else:
            anterior = atual.prev
            anterior.next = novo
            novo.prev = anterior
            novo.next = atual
            atual.prev = novo


    def removevenda(self, node):

        if node == self.head and node == self.tail:
            self.head = None
            self.tail = None

        elif node == self.head:
            self.head = node.next
            self.head.prev = None

        elif node == self.tail:
            self.tail = node.prev
            self.tail.next = None

        else:
            anterior = node.prev
            proximo = node.next
            anterior.next = proximo
            proximo.prev = anterior


    def mostravendas(self):
        atual = self.head

        while atual is not None:
            oferta = atual.ordem
            print(
                "ID -",oferta.id,
                "Preço -",oferta.preco,
                "Quantidade -",oferta.quantidade
            )
            atual = atual.next


class LivroOfertas:

    def __init__(self):
        self.compras = ListaCompras()
        self.vendas = ListaVendas()

    def insereordem(self, ordem):
        if ordem.tipo == 'C':
            self.compras.inserecompra(ordem)
        else:
            self.vendas.inserevenda(ordem)

    def mostrar(self):
        print("*** COMPRAS ***")
        self.compras.mostracompras()
        print("\n*** VENDAS ***")
        self.vendas.mostravendas()


