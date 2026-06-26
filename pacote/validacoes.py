def dados_formatados():  
    tipo = input("(C) - Compra / (V) - Venda\n")
    while tipo != "C" and tipo != "(C)" and tipo != "V" and tipo != "(V)":
        tipo = input("(C) - Compra / (V) - Venda\n")
    if tipo == "(C)" or tipo == "C":
        tipo = "C"
        preço = ""
        while type(preço) != float:
            preço = input("Qual o preço de compra?\n")
            if preço.isnumeric():
                preço = float(preço)
        quantidade = ""
        while type(quantidade) != int:
            quantidade = input("Quantas ações deseja comprar?\n")
            if quantidade.isnumeric().is_integer():
                quantidade = int(quantidade)
    elif tipo == "(V)" or tipo == "V":
        tipo = "V"
        preço = ""
        while type(preço) != float:
            preço = input("Qual o preço de venda?\n")
            if preço.isnumeric():
                preço = float(preço)
        quantidade = ""
        while type(quantidade) != int:
            quantidade = input("Quantas ações deseja vender?\n")
            if quantidade.isnumeric().is_integer():
                quantidade = int(quantidade)
    return tipo, preco, quantidade