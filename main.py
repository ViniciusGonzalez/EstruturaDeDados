import os

from pacote.entrada_undo import FilaEntrada, PilhaUndo
from pacote.livro_ofertas import ListaCompras, ListaVendas
from pacote.motor_match import executar_match

def __str__(lista_vendas = None, lista_compras = None):
    os.system("cls")
    print("="*71)
    print(f"{"Livro de Ofertas":^70}")
    print("="*71)
    #if fila_de_entrada.tamanho == 1:
    #   print("Temos {fila_de_entrada.tamanho} ordem aguardando na fila de entrada")
    #else:
    print("Temos {fila_de_entrada.tamanho} ordens aguardando na fila de entrada")
    print("ID da última ordem adicionada ao Livro: {pilha_de_undo.ve_topo()}")
    print("-"*70)
    print(f"{"Operação":^23}"+"|"+f"{"Preço (R$)":^23}"+"|"+f"{"Quantidade":^23}")
    print("-"*23+"|"+"-"*23+"|"+"-"*23)
    #vendas_atual = lista_de_vendas.inicio.next.next.next.next
    #compras_atual = lista_de_compras.inicio
    for i in range(5):
        print(f"{"[VENDA]":<23}"+"|"+"{vendas_atual.valor:^23.2f}".replace(".",",")+"|"+"{vendas_atual.quantidade:^23}")
        #vendas_atual = vendas_atual.ant
    print(" "*23+"|"+" "*23+"|"+" "*23)
    for i in range(5):
        print(f"{"[COMPRA]":<23}"+"|"+"{compras_atual.valor:^23.2f}".replace(".",",")+"|"+"{compras_atual.quantidade:^23}")
        #compras_atual = compras_atual.next
    print("-"*70)
    print()
    print("="*70)
    print(f"{"HISTÓRICO DE TRANSAÇÕES":^70}")
    print("="*70)
    #Colocar o histórico de transações AQUI!!!
    print("="*70)
    print("OPÇÕES: (1) Inserir Ordem | (2) Processar Próxima Ordem\n"
          "        (3) Undo | (4) Simulação | (5) Sair")
    #v_inicio = lista_vendas.head.valor
    #v_quantidade = lista_vendas.head.quantidade
    #c_inicio = lista_compras.head.valor
    #c_quantidade = lista_compras.head.quantidade

__str__()
