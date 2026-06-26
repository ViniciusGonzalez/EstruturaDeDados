from ordem import Ordem

class ListaCompras:

    def __init__(self):
        self.head = None
        self.tail = None

    def inserecompra(self, ordem):
        novo = ordem

        if self.head is None:
            self.head = novo
            self.tail = novo
            return

        elif ordem.preco > self.head.preco:
            novo.next = self.head
            self.head.prev = novo
            self.head = novo
            return

        atual = self.head

        while atual is not None:
            if ordem.preco > atual.preco:
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


    def removecompra(self, ordem):

        if ordem == self.head and ordem == self.tail:
            self.head = None
            self.tail = None

        elif ordem == self.head:
            self.head = ordem.next
            self.head.prev = None

        elif ordem == self.tail:
            self.tail = ordem.prev
            self.tail.next = None

        else:
            anterior = ordem.prev
            proximo = ordem.next
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
        novo = ordem

        if self.head is None:
            self.head = novo
            self.tail = novo
            return

        if ordem.preco < self.head.preco:
            novo.next = self.head
            self.head.prev = novo
            self.head = novo
            return

        atual = self.head

        while atual is not None:
            if ordem.preco < atual.preco:
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


    def removevenda(self, ordem):

        if ordem == self.head and ordem == self.tail:
            self.head = None
            self.tail = None

        elif ordem == self.head:
            self.head = ordem.next
            self.head.prev = None

        elif ordem == self.tail:
            self.tail = ordem.prev
            self.tail.next = None

        else:
            anterior = ordem.prev
            proximo = ordem.next
            anterior.next = proximo
            proximo.prev = anterior


    def mostravendas(self):
        atual = self.head

        while atual is not None:
            oferta = atual
            print(
                "ID -",oferta.id,
                "Preço -",oferta.preco,
                "Quantidade -",oferta.quantidade
            )
            atual = atual.next
