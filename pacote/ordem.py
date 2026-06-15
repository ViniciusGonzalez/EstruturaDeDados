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
        prox : referencia para a proxima ordem da lista
        ant  : referencia para a ordem anterior da lista
    """

    def __init__(self, id, tipo, preco, quantidade, timestamp=None):
        # ---- Validacao dos dados de entrada ----
        tipo = str(tipo).upper()
        if tipo not in ("C", "V"):
            raise ValueError("Tipo invalido: use 'C' (Compra) ou 'V' (Venda).")
        if preco <= 0:
            raise ValueError("O preco deve ser maior que zero.")
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")

        # ---- Dados da ordem ----
        self.id = int(id)
        self.tipo = tipo
        self.preco = float(preco)
        self.quantidade = int(quantidade)
        # Se nenhum timestamp for informado, registra o instante atual.
        self.timestamp = time.time() if timestamp is None else timestamp

        # ---- Ponteiros de encadeamento (Livro de Ofertas - Parte 2) ----
        self.prox = None   # proxima ordem na lista
        self.ant = None    # ordem anterior na lista

    # Representacao textual amigavel, util para depuracao e impressao.
    def __str__(self):
        lado = "COMPRA" if self.tipo == "C" else "VENDA"
        return (f"Ordem #{self.id} [{lado}] "
                f"{self.quantidade} acoes @ R$ {self.preco:.2f}")

    def __repr__(self):
        return self.__str__()


# ---------------------------------------------------------------------
#  Teste rapido (so executa quando o arquivo e rodado diretamente,
#  nao quando ele e importado por outro modulo).
#  Rode de dentro da pasta 'pacote':  python ordem.py
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("=== Teste da classe Ordem ===\n")

    o1 = Ordem(id=1, tipo="C", preco=450.00, quantidade=1000)
    o2 = Ordem(id=2, tipo="V", preco=400.00, quantidade=800)
    print(o1)
    print(o2)
    print(f"\nTimestamp da ordem #1: {o1.timestamp}")
    print(f"Ponteiros iniciais da ordem #1 -> prox={o1.prox}, ant={o1.ant}")

    print("\n--- Teste de validacao (deve gerar erros controlados) ---")
    for dados in [("X", 100, 10), ("C", -5, 10), ("V", 100, 0)]:
        try:
            Ordem(id=99, tipo=dados[0], preco=dados[1], quantidade=dados[2])
        except ValueError as erro:
            print(f"Rejeitada corretamente: {erro}")