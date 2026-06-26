from pacote.ordem import Ordem

class ListaCompras:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def inserecompra(self, ordem):
        ordem.next = None
        ordem.prev = None

        if self.head is None:
            self.head = ordem
            self.tail = ordem
            return

        elif ordem.preco >= self.head.preco:
            ordem.next = self.head
            self.head.prev = ordem
            self.head = ordem
            return

        atual = self.head
        while atual is not None and ordem.preco <= atual.preco:
            atual = atual.next

        if atual is None:
            self.tail.next = ordem
            ordem.prev = self.tail
            self.tail = ordem

        else:
            anterior = atual.prev
            if anterior is not None:
                anterior.next = ordem
            ordem.prev = anterior
            ordem.next = atual
            atual.prev = ordem


    def removecompra(self, ordem):

        if ordem == self.head and ordem == self.tail:
            self.head = None
            self.tail = None

        elif ordem == self.head:
            self.head = ordem.next
            if self.head is not None: 
                self.head.prev = None

        elif ordem == self.tail:
            self.tail = ordem.prev
            if self.tail is not None: 
                self.tail.next = None
                
        else:
            if ordem.prev is not None: 
                ordem.prev.next = ordem.next
            if ordem.next is not None: 
                ordem.next.prev = ordem.prev
            ordem.next = None
            ordem.prev = None

    def mostracompras(self):

        atual = self.head

        while atual is not None:
            oferta = atual
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
        ordem.next = None
        ordem.prev = None

        if self.head is None:
            self.head = ordem
            self.tail = ordem
            return

        if ordem.preco <= self.head.preco:
            ordem.next = self.head
            self.head.prev = ordem
            self.head = ordem
            return

        atual = self.head
        while atual is not None and ordem.preco >= atual.preco:
            atual = atual.next

        if atual is None:
            self.tail.next = ordem
            ordem.prev = self.tail
            self.tail = ordem
        else:
            anterior = atual.prev
            if anterior is not None:
                anterior.next = ordem
            ordem.prev = anterior
            ordem.next = atual
            atual.prev = ordem

    def removevenda(self, ordem):

        if ordem == self.head and ordem == self.tail:
            self.head = None
            self.tail = None

        elif ordem == self.head:
            self.head = ordem.next
            if self.head is not None: 
                self.head.prev = None

        elif ordem == self.tail:
            self.tail = ordem.prev
            if self.tail is not None: 
                self.tail.next = None
        else:
            if ordem.prev is not None: 
                ordem.prev.next = ordem.next
            if ordem.next is not None: 
                ordem.next.prev = ordem.prev

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
