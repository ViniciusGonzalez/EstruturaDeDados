import os
import time
import random as r

from pacote.ordem import Ordem
from pacote.entrada_undo import Fila, Pilha
from pacote.livro_ofertas import ListaCompras, ListaVendas
from pacote.motor_match import executar_match

fila_de_entrada = Fila()
lista_vendas = ListaVendas()
lista_compras = ListaCompras()
pilha_undo = Pilha()
modo_de_adicao = "1"
tempo_padrao = 5
delay_padrao = 0

def __str__():
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
            print(f"ID da última ordem adicionada ao Livro: {pilha_undo.ve_topo().id:010d}")
        print("-"*70)
        print(f"{'Operação':>23}"+"|"+f"{'Preço (R$)':^23}"+"|"+f"{'Quantidade':^23}")
        print("-"*23+"|"+"-"*23+"|"+"-"*23)

    # Exibição das 5 primeiras ordens de venda e compra
    vendas_atual = lista_vendas.head
    for i in range(4):
        if vendas_atual == None:
            break
        else:
            vendas_atual = vendas_atual.next
    compras_atual = lista_compras.head
    for i in range(5):
        print(f"{'[VENDA]':>23}"+"|", end="")
        if vendas_atual == None:
            print(f"{'-':>23}"+"|"+f"{'-':>23}")
        else:
            print(f"{vendas_atual.valor:>23.2f}".replace(".",",")+"|"+f"{vendas_atual.quantidade:>23}")
            vendas_atual = vendas_atual.prev
    print(" "*23+"|"+" "*23+"|"+" "*23)
    for i in range(5):
        print(f"{'[COMPRA]':>23}"+"|", end="")
        if compras_atual == None:
            print(f"{'-':>23}"+"|"+f"{'-':>23}")
        else:
            print(f"{compras_atual.valor:>23.2f}".replace(".",",")+"|"+f"{compras_atual.quantidade:>23}")
            compras_atual = compras_atual.next
    print("-"*70)
    print()

    # Histórico de transações
    print("="*70)
    print(f"{'HISTÓRICO DE TRANSAÇÕES':^70}") #TODO TODO TODO
    print("="*70)
    # TODO: Colocar o histórico de transações AQUI!!! TODO TODO TODO
    print("="*70)

def processar_ordem(fila_de_entrada = fila_de_entrada,
                    lista_vendas = lista_vendas, 
                    lista_compras = lista_compras, 
                    pilha_undo = pilha_undo):
    ordem = fila_de_entrada.desenfileira()
    if ordem.tipo == "C":
        lista_compras.inserecompra(ordem)
    elif ordem.tipo == "V":
        lista_vendas.inserevenda(ordem)
    pilha_undo.empilha(ordem.id)
    executar_match()

while True:

    # Modo Default: Adicionar todas as ordens até esvaziar a fila de entrada

    if modo_de_adicao == "1":
        print("Processando todas as ordens da fila de entrada...")
        while not fila_de_entrada.esta_vazia():
            processar_ordem()
        __str__()
        
    # Modo Loop Manual: Tempo determinado t, controlado via input

    elif modo_de_adicao == "2":
        while True:
            __str__()
            comando = input("(1) continuar por t segundos\n"
                            "(0) Sair do loop\n")
            if comando == "0":
                break
            elif comando == "1":
                if fila_de_entrada.esta_vazia():
                    input("A fila de entrada já está vazia! [Enter]")
                    break
                tempo_inicial = time.time()
                while time.time() - tempo_inicial < tempo_padrao:
                    if fila_de_entrada.esta_vazia():
                        break
                    processar_ordem()
                    time.sleep(delay_padrao)

    # Modo Loop automatico: Tempo determinado t

    elif modo_de_adicao == "3":
        while not fila_de_entrada.esta_vazia():
            tempo_inicial = time.time()
            while time.time() - tempo_inicial < tempo_padrao:
                if fila_de_entrada.esta_vazia():
                    break
                processar_ordem()
                time.sleep(delay_padrao)
            __str__()

    opcao = input("OPÇÕES: (1) Inserir Ordem | (2) Processar Próxima Ordem\n"
                  "        (3) Undo | (4) Simulação\n"
                  "        (5) Configurações | (6) Sair\n")

    # Adição de uma ordem à fila de entradas

    if opcao == 1 or opcao == "1":
        tipo = input("(C) - Compra / (V) - Venda\n")
        while tipo != "C" and tipo != "(C)" and tipo != "V" and tipo != "(V)":
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
        fila_de_entrada.adicionar(Ordem(tipo, preço, quantidade))

    # Processamento da ordem na frente da fila de entrada

    elif opcao == 2 or opcao == "2":
        processar_ordem()
        
    # Remove a última ordem adicionada ao livro de ofertas (se ainda existir)

    elif opcao == 3 or opcao == "3":
        if not pilha_undo.esta_vazia():
            undo = pilha_undo.ve_topo()
            compra_atual = lista_compras.head
            venda_atual = lista_vendas.head
            removido = False
            while compra_atual != None:
                if compra_atual.id == undo:
                    lista_compras.removecompra(compra_atual)
                    removido = True
                    break
                compra_atual = compra_atual.next
            while venda_atual != None and not removido:
                if venda_atual.id == undo:
                    lista_vendas.removevende(venda_atual)
                    removido = True
                    break
            if removido:
                print(f"A ordem de ID: {undo} foi removida")
            else:
                print("ERRO: Remoção não realizada. A transação já foi efetuada")
        else:
            print("Ainda não foram adicionadas ordens ao livro de ofertas")

    elif opcao == 4 or opcao == "4":
        numero_ordens = input("Quantas ordens você deseja simular?\n")
        while type(numero_ordens) != int and int(numero_ordens) <= 0:
            numero_ordens = input("ERRO: Digite um número positivo, quantas ordens você deseja simular?")
        numero_ordens = int(numero_ordens)
        for i in range(numero_ordens):
            venda_ou_compra = r.randint(0,1)
        if venda_ou_compra == 0:
            fila_de_entrada.adicionar("C", preco = r.gauss(100,10), quantidade = r.randint(1,10))
        else:
            fila_de_entrada.adicionar("V", preco = r.gauss(105,10), quantidade = r.randint(1,150))

    elif opcao == 5 or opcao == "5":
        config = input("\nQual parâmetro deseja configurar:\n"
                       "(1) Modo de exibição\n"
                       "(2) Período por loop\n"
                       "(3) Delay entre cada ordem\n")
        if config == "1":
            modo_de_adicao = input(
                "\n Selecione o modo de adição de ordens ao livro de ofertas:\n"
                "(1) Modo Default (Adicão de todas as ordens instantaneamente)\n"
                "(2) Modo Loop manual (Adicão de ordens por t segundos, a cada loop)\n"
                "(3) Modo Loop automatico (Adicão de ordens por t segundos, automaticamente)\n"
                )
        if config == "2":
            tempo_padrao = float(input("Loop: "))
        if config == "3":
            delay_padrao = float(input("Delay: "))        

    elif opcao == 6 or opcao == "6":
        break
