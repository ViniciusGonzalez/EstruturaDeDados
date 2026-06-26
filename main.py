import time
import random as r

from pacote.ordem import Ordem
from pacote.entrada_undo import Fila, Pilha
from pacote.livro_ofertas import ListaCompras, ListaVendas
from pacote.motor_match import executar_match, PilhaTransacoes
from pacote.interface import interface
from pacote.validacoes import dados_formatados

# Estruturas globais
fila_de_entrada = Fila()
lista_vendas = ListaVendas()
lista_compras = ListaCompras()
pilha_undo = Pilha()
pilha_transacoes = PilhaTransacoes()

# Variáveis auxiliares
modo_de_adicao = "1"
tempo_padrao = 1
delay_padrao = 0.05

def processar_ordem():
    if fila_de_entrada.esta_vazia():
        return
    ordem = fila_de_entrada.desenfileira()
    if ordem.tipo == "C":
        lista_compras.inserecompra(ordem)
    elif ordem.tipo == "V":
        lista_vendas.inserevenda(ordem)
    pilha_undo.empilha(ordem.id)
    executar_match(lista_compras, lista_vendas, pilha_transacoes)

# Loop Principal do Sistema

while True:

    # Modo Default: Adicionar todas as ordens até esvaziar a fila de entrada

    if modo_de_adicao == "1":
        print("Processando todas as ordens da fila de entrada...")
        while not fila_de_entrada.esta_vazia():
            processar_ordem()
        interface(fila_de_entrada, lista_vendas, lista_compras, pilha_undo, pilha_transacoes)
        
    # Modo Loop Manual: Tempo determinado t, controlado via input

    elif modo_de_adicao == "2":
        while True:
            interface(fila_de_entrada, lista_vendas, lista_compras, pilha_undo, pilha_transacoes)
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
            interface(fila_de_entrada, lista_vendas, lista_compras, pilha_undo, pilha_transacoes)

    # Menu de opções do usuário

    opcao = input("OPÇÕES: (1) Inserir Ordem | (2) Processar Próxima Ordem\n"
                  "        (3) Undo | (4) Simulação\n"
                  "        (5) Configurações | (6) Sair\n"
                  "        Escolha uma opção acima: ")

    # Adição de uma ordem à fila de entradas

    if opcao == 1 or opcao == "1":
        tipo, preco, quantidade = dados_formatados()
        fila_de_entrada.enfileira(tipo, preco, quantidade)

    # Processamento da ordem na frente da fila de entrada

    elif opcao == 2 or opcao == "2":
        processar_ordem()
        
    # Remove a última ordem adicionada ao livro de ofertas (se ainda existir)

    elif opcao == 3 or opcao == "3":
        if not pilha_undo.esta_vazia():
            undo = pilha_undo.desempilha()
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
                    lista_vendas.removevenda(venda_atual)
                    removido = True
                    break
            if removido:
                print(f"A ordem de ID: {undo} foi removida")
            else:
                print("ERRO: Remoção não realizada. A transação já foi efetuada")
        else:
            print("Ainda não foram adicionadas ordens ao livro de ofertas")

    # Simulação aleatória de ordens de compra ou venda 

    elif opcao == 4 or opcao == "4":
        numero_ordens = input("Quantas ordens você deseja simular?\n")
        while type(numero_ordens) != int and int(numero_ordens) <= 0:
            numero_ordens = input("ERRO: Digite um número positivo, quantas ordens você deseja simular?\n")
        numero_ordens = int(numero_ordens)
        for i in range(numero_ordens):
            venda_ou_compra = r.randint(0,1)
            if venda_ou_compra == 0:
                fila_de_entrada.enfileira("C", preco = r.gauss(105,10), quantidade = r.randint(1,150))
            elif venda_ou_compra == 1:
                fila_de_entrada.enfileira("V", preco = r.gauss(100,10), quantidade = r.randint(1,150))

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
