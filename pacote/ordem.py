import time

class Ordem:
    """
    Representa uma ordem de negociacao (cada "tijolo" do livro de ofertas).

    Atributos de dados (conforme a especificacao do trabalho):
        id          (int)   : identificador unico da ordem
        tipo        (str)   : 'C' para Compra ou 'V' para Venda
        preco       (float) : valor unitario que o investidor aceita
        quantidade  (int)   : volume de acoes a serem negociadas
        timestamp   (float) : momento exato da entrada no sistema

    Atributos de encadeamento (usados pelo Livro de Ofertas):
        next : referencia para a proxima ordem da lista
        prev  : referencia para a ordem anterior da lista
    """
    ultimo_id = 0

    def __init__(self, tipo, preco, quantidade, timestamp=None):
        # ---- Validacao dos dados de entrada ----
        Ordem.ultimo_id += 1
        tipo = str(tipo).upper()
        if tipo not in ("C", "V"):
            raise ValueError("Tipo invalido: use 'C' (Compra) ou 'V' (Venda).")
        if preco <= 0:
            raise ValueError("O preco deve ser maior que zero.")
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")

        # ---- Dados da ordem ----
        self.id = Ordem.ultimo_id
        self.tipo = tipo
        self.preco = float(preco)
        self.quantidade = int(quantidade)
        # Se nenhum timestamp for informado, registra o instante atual.
        self.timestamp = time.time() if timestamp is None else timestamp

        # ---- Ponteiros de encadeamento (Livro de Ofertas - Parte 2) ----
        self.next = None   # proxima ordem na lista
        self.prev = None    # ordem anterior na lista

    # Representacao textual amigavel, util para depuracao e impressao.
    def __str__(self):
        lado = "COMPRA" if self.tipo == "C" else "VENDA"
        return (f"Ordem #{self.id} [{lado}] "
                f"{self.quantidade} acoes @ R$ {self.preco:.2f}")

    def __repr__(self):
        return self.__str__()
