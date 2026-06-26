import os

def interface(fila_de_entrada, lista_vendas, lista_compras, pilha_undo, pilha_transacoes):
    os.system("cls")
    print("="*71)
    print(f"{'Livro de Ofertas':^70}")
    print("="*71)

    # Exibição da quantidade de ordens da fila de entrada
    if fila_de_entrada.tamanho == 1:
       print(f"Temos {fila_de_entrada.tamanho} ordem aguardando na fila de entrada")
    else:
        print(f"Temos {fila_de_entrada.tamanho} ordens aguardando na fila de entrada")
        if pilha_undo.esta_vazia():
            print("ID da última ordem adicionada ao Livro: -")
        else:
            print(f"ID da última ordem adicionada ao Livro: {pilha_undo.ve_topo():010d}")
        print("-"*71)
        print(f"{'Operação':>23}"+"|"+f"{'Preço (R$)':^23}"+"|"+f"{'Quantidade':^23}")
        print("-"*23+"|"+"-"*23+"|"+"-"*23)

    # Exibição das 5 primeiras ordens de venda e compra
    total_vendas_exibiveis = 0
    venda_atual = lista_vendas.head
    while venda_atual is not None and total_vendas_exibiveis < 5:
        total_vendas_exibiveis += 1
        venda_atual = venda_atual.next
    for j in range(5):
        print(f"{'[VENDA]':>23}"+"|", end="")
        if j < (5 - total_vendas_exibiveis):
            print(f"{'-':>23}"+"|"+f"{'-':>23}")
        else:
            passos = total_vendas_exibiveis - 1 - (j - (5 - total_vendas_exibiveis))
            venda_alvo = lista_vendas.head
            for _ in range(passos):
                if venda_alvo != None:
                    venda_alvo = venda_alvo.next
            if venda_alvo != None:
                print(f"{venda_alvo.preco:>23.2f}".replace(".",",")+"|"+f"{venda_alvo.quantidade:>23}")
    print(" "*23+"|"+" "*23+"|"+" "*23)
    compra_atual = lista_compras.head
    for i in range(5):
        print(f"{'[COMPRA]':>23}"+"|", end="")
        if compra_atual == None:
            print(f"{'-':>23}"+"|"+f"{'-':>23}")
        else:
            print(f"{compra_atual.preco:>23.2f}".replace(".",",")+"|"+f"{compra_atual.quantidade:>23}")
            compra_atual = compra_atual.next
    print("-"*71)
    print()

    # Histórico de transações
    print("="*71)
    print(f"{'HISTÓRICO DE TRANSAÇÕES':^71}")
    print("="*71)
    pilha_transacoes.imprime_ultimas_três()
    print("="*71)