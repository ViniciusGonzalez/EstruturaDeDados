def executar_match(lista_compras, lista_vendas, pilha_transacoes):

    while (
        lista_compras.head is not None
        and lista_vendas.head is not None
        and lista_compras.head.preco >= lista_vendas.head.preco
    ):

        compra = lista_compras.head
        venda = lista_vendas.head

        quantidade_negociada = min(
            compra.quantidade,
            venda.quantidade
        )

        transacao = {
            "id_compra": compra.id,
            "id_venda": venda.id,
            "preco": venda.preco,
            "quantidade": quantidade_negociada
        }

        pilha_transacoes.push(transacao)

        compra.quantidade -= quantidade_negociada
        venda.quantidade -= quantidade_negociada

        if compra.quantidade == 0:
            lista_compras.remover(compra)

        if venda.quantidade == 0:
            lista_vendas.remover(venda)