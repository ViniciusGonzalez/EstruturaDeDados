class NoTransacao:
    ultimo_id = 0

    def __init__(self, preco, quantidade):
        NoTransacao.ultimo_id += 1
        self.id_transacao = NoTransacao.ultimo_id  # int
        self.preco = float(preco)                  # float
        self.quantidade = int(quantidade)          # int
        self.next = None                           # Ponteiro para a próxima transação

class PilhaTransacoes:

    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.tamanho == 0

    def empilha_transacao(self, preco, quantidade):
        """Cria e empilha uma transação diretamente no TOPO em O(1)"""
        # O próprio nó gera o seu ID automaticamente ao ser criado
        novo_no = NoTransacao(preco, quantidade)
        novo_no.next = self.topo
        self.topo = novo_no
        self.tamanho += 1

    def imprime_ultimas_três(self):
        """Percorre os ponteiros e exibe até as 3 transações mais recentes diretamente"""
        if self.esta_vazia():
            print(f"{'Nenhuma transação efetuada até o momento.':^71}")
            return

        atual = self.topo
        contador = 0
        while atual is not None and contador < 3:
            # Formatação manual sem uso de coleções do Python
            print(f"{f'Transação #{atual.id_transacao:04d} | Preço: R$ {atual.preco:>7.2f} | Qtd: {atual.quantidade:>4d}':^70}")
            atual = atual.next
            contador += 1

def executar_match(lista_compras, lista_vendas, pilha_transacoes):
    """
    Executa uma transação de ordens.
    A negociação ocorre SEMPRE pelo preço proposto pelo comprador (compra.preco).
    """
    while (
        lista_compras.head is not None
        and lista_vendas.head is not None
        and lista_compras.head.preco >= lista_vendas.head.preco
    ):
        compra = lista_compras.head
        venda = lista_vendas.head

        # Define a quantidade negociada (o mínimo entre as duas)
        quantidade_negociada = min(compra.quantidade, venda.quantidade)

        # REGRA: Preço é definido estritamente pela proposta do comprador
        preco_fechamento = compra.preco

        # Salva na Pilha de Transações (sem dicionários e sem passar ID manual)
        pilha_transacoes.empilha_transacao(preco_fechamento, quantidade_negociada)

        # Abate as quantidades correspondentes nas ordens reais do livro
        compra.quantidade -= quantidade_negociada
        venda.quantidade -= quantidade_negociada

        # Remove dos livros os nós cujas quantidades zeraram
        if compra.quantidade == 0:
            lista_compras.removecompra(compra)

        if venda.quantidade == 0:
            lista_vendas.removevenda(venda)
