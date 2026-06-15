from pacote.entrada_undo import FilaEntrada, PilhaUndo
from pacote.livro_ofertas import ListaCompras, ListaVendas
from pacote.motor_match import executar_match

def __str__(lista_vendas = None, lista_compras = None):
    #v_inicio = lista_vendas.head.valor
    #v_quantidade = lista_vendas.head.quantidade
    #c_inicio = lista_compras.head.valor
    #c_quantidade = lista_compras.head.quantidade
    v_inicio = 100000000
    v_quantidade = 400
    c_inicio = 10000
    c_quantidade = 300

    print("Valor".ljust(len(v_inicio) + 5)+"Quantidade".ljust(len(v_quantidade) + 5))
    #for i in range(5, 0, -1):
    #print("Lista de Vendas:".center(len(str(v_inicio)) + 5))
    #print(f"R${v_inicio:.2f}".replace(".", ",").center(16))
    #print(f"Quantidade: {v_quantidade}")
    #print("Lista de Compras:".center(len(str(c_inicio)) + 5))
    #print(f"R${c_inicio:.2f}".replace(".", ",").center(16))
    #print(f"Quantidade: {c_quantidade}")

__str__()
