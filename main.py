import os
import time
import random as r

from pacote.entrada_undo import FilaEntrada, PilhaUndo
from pacote.livro_ofertas import ListaCompras, ListaVendas
from pacote.motor_match import executar_match

fila_de_entrada = None
lista_vendas = None
lista_compras = None
pilha_undo = None

def __str__():
    os.system("cls")
    print("="*71)
    print(f"{'Livro de Ofertas':^70}")
    print("="*71)

    # Exibição da quantidade de ordens da fila de entrada
    #if fila_de_entrada.tamanho == 1:
    #   print("Temos {fila_de_entrada.tamanho} ordem aguardando na fila de entrada")
    #else:
    print("Temos {fila_de_entrada.tamanho} ordens aguardando na fila de entrada")
    print("ID da última ordem adicionada ao Livro: {pilha_de_undo.ve_topo()}")
    print("-"*70)
    print(f"{'Operação':>23}"+"|"+f"{'Preço (R$)':^23}"+"|"+f"{'Quantidade':^23}")
    print("-"*23+"|"+"-"*23+"|"+"-"*23)

    # Exibição das 5 primeiras ordens de venda e compra
    #vendas_atual = lista_de_vendas.inicio
    #for i in range(4):
    #    if vendas_atual == None:
    #        break
    #    else:
    #        vendas_atual = vendas_atual.next
    #compras_atual = lista_de_compras.inicio
    for i in range(5):
        print(f"{'[VENDA]':>23}"+"|", end="")
        #if vendas_atual == None:
            #print(f"{'-':>23}"+"|"+f"{'-':>23}")
        #else:
        print("{vendas_atual.valor:>23.2f}".replace(".",",")+"|"+"{vendas_atual.quantidade:>23}")
            #vendas_atual = vendas_atual.prev
    print(" "*23+"|"+" "*23+"|"+" "*23)
    for i in range(5):
        print(f"{'[COMPRA]':>23}"+"|", end="")
        #if compras_atual == None:
            #print(f"{'-':>23}"+"|"+f"{'-':>23}")
        #else:
        print("{compras_atual.valor:>23.2f}".replace(".",",")+"|"+"{compras_atual.quantidade:>23}")
            #compras_atual = compras_atual.next
    print("-"*70)
    print()

    # Histórico de transações
    print("="*70)
    print(f"{'HISTÓRICO DE TRANSAÇÕES':^70}")
    print("="*70)
    # TODO: Colocar o histórico de transações AQUI!!!
    print("="*70)

while True:
    __str__()

    opcao = input("OPÇÕES: (1) Inserir Ordem | (2) Processar Próxima Ordem\n"
                  " (3) Undo | (4) Simulação"
                  " (5) Controle de Tempo | (6) Sair")

    # Adição de uma ordem à fila de entradas

    if opcao == 1:
        tipo = input("(C) - Compra / (V) - Venda")
        while tipo != "C" or tipo != "(C)" or tipo != "V" or tipo != "(V)":
            tipo = input("(C) - Compra / (V) - Venda")
        if tipo == "(C)" or tipo == "C":
            tipo = "C"
            preço = input("Qual o preço de compra?")
            while type(preço) != float:
                preço = input("Qual o preço de compra?")
            quantidade = input("Quantas ações deseja comprar?")
            while type(quantidade) != int:
                quantidade = input("Quantas ações deseja comprar?")
        elif tipo == "(V)" or tipo == "V":
            tipo = "V"
            preço = input("Qual o preço de venda?")
            while type(preço) != float:
                preço = input("Qual o preço de venda?")
            quantidade = input("Quantas ações deseja comprar?")
            while type(quantidade) != int:
                quantidade = input("Quantas ações deseja vender?")
        #fila_de_entrada.adicionar(Ordem(tipo, preço, quantidade))

    # Processamento da ordem na frente da fila de entrada

    elif opcao == 2:
        #lista_de_ofertas.proximo() TODO
        pass
        
    elif opcao == 3:
        #pilha_de_undo.undo() TODO
        pass

    elif opcao == 4:
        quantidade = input("Quantas ordens você deseja simular?")
        while type(quantidade) != int and quantidade <= 0:
            quantidade = input("ERRO: Digite um número positivo, quantas ordens você deseja simular?")
        for i in range(quantidade):
            venda_ou_compra = r.randint(0,1)
        if venda_ou_compra == 0:
            #fila_de_entrada.adicionar("C", preco = random.gauss(100,10), r.randint(1,150))
            pass
        else:
            #fila_de_entrada.adicionar("V", preco = random.gauss(105,10), r.randint(1,150))
            pass

    elif opcao == 5:
        #if fila_de_entrada.head == None:
            input("\nA fila de entrada está vazia! Gere ordens na opção (1) ou (4) primeiro. [Enter]")
            continue
    

    elif opcao == 6:
        break