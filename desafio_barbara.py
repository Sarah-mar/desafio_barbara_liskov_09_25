import datetime 

import random

def data_aleatoria_str():
    ano = random.randint(2020, 2025)
    mes = random.randint(1, 12)
    dia = random.randint(1, 28)
    hora = random.randint(0, 23)
    minuto = random.randint(0, 59)
    segundo = random.randint(0, 59)
    microsegundo = random.randint(0, 9999)  # 4 dígitos como no seu exemplo
    return f"{ano:04d}-{mes:02d}-{dia:02d} {hora:02d}:{minuto:02d}:{segundo:02d}:{microsegundo:04d}"

# Lista de estoque com datas aleatórias em string
estoque = [
    ["Caneta", 12.0, 2, data_aleatoria_str()],
    ["Caderno", 15.5, 5, data_aleatoria_str()],
    ["Lápis", 1.2, 200, data_aleatoria_str()],
    ["Borracha", 0.8, 150, data_aleatoria_str()],
    ["Marcador", 3.0, 75, data_aleatoria_str()]
]

def cadastrar_produto_estoque(nome, preco,qtd):
    data = datetime.datetime.now() 
    produto = (nome, preco, qtd, data)
    print(f"Nome: {nome} \nPreço: {preco} \nQuantidade: {qtd} \nData: {data}")
    estoque.append(produto)
    print("Produto Cadastrado.")  

def exibir_estoque():

    if len(estoque) != 0:
        print("Estoque:")
        for produto in estoque: #Estamos percorrendo o estoque elemento por elemento (nesse caso, os elementos são os objetos produto, que tem o tipo lista)
            print("produto:")
            print(f"Nome: {produto[0]} \nPreço: {produto[1]} \nQuantidade: {produto[2]} \nData: {produto[3]}")
    else:
        print ("Estoque vazio")

def confere_produto_no_estoque(nome):
    for produto in estoque:
        if produto[0] == nome and produto[2] != 0: #produto existe no estoque e tem unidades disponíveis
            existe = 1
            break #precisamos do break nessa solução pois, na ausência dele, o laço for continuaria percorrendo o estoque e encontraria produtos diferentes do nome fornecido. Nesse caso, a função sempre retorna 0
        elif produto[0] == nome and produto[2] == 0: #produto existe no estoque mas não tem unidades disponíveis
            existe = 0
            break
        else: #o produto não existe no estoque
            existe = -1
    return existe

def criar_pedido():
    continua = "S"
    pedido = []
    while continua.upper() == "S":
        exibir_estoque()
        nome_pedido = input("Qual produto deseja comprar? ")
        estado_no_estoque = confere_produto_no_estoque(nome_pedido) # a função confere_produto_no_estoque procurará, entre os nomes dos produtos no estoque, o nome fornecido no pedido
        while estado_no_estoque != 1:
            print ("Produto indisponível")
            nome_pedido = input("Qual produto deseja comprar? ")
            estado_no_estoque = confere_produto_no_estoque(nome_pedido)
        qtd_pedido = int(input("Qual a quantidade desejada? "))
        for produto in estoque:
            if produto[0] == nome_pedido and produto[2] >= qtd_pedido:
                pedido.append([nome_pedido, qtd_pedido, datetime.datetime.now()])
                produto[2] = produto[2] - qtd_pedido #atualização do estoque
            elif produto[0] == nome_pedido and produto[2] < qtd_pedido:
                while qtd_pedido > produto[2]:
                    print("Quantidade indisponível")
                    print ("Produto:", produto[0],"Quantidade disponível:" , produto[2])
                    qtd_pedido = int(input("Qual a quantidade desejada? "))
                pedido.append([nome_pedido, qtd_pedido, datetime.datetime.now()])
                produto[2] = produto[2] - qtd_pedido #atualização do estoque
            else:
                continue
        continua = input("Deseja continuar o pedido? (S/N) ")
    print("Pedido encerrado. Confira abaixo seu pedido: ")
    for produto in pedido:
        print(produto[0], "-------", produto[1], "-------" ,produto[2])
    return pedido

def pagamento(pedido):
    total = 0
    for item in pedido:
        for produto in estoque:
            if item[0] == produto[0]:
                total += item[1] * produto[1]
    print("Total:", total)
    forma_de_pagamento = int(input("Digite a forma de pagamento (1-cartão, 2-dinheiro): "))
    if forma_de_pagamento == 2:
     din_recebido = float(input("Digite o valor em dinheiro entregue ao caixa: "))
    while din_recebido < total:
        print("Valor insuficiente.")
        din_recebido = float(input("Digite o valor em dinheiro entregue ao caixa: "))
    troco = din_recebido - total   
    print ("Troco:", troco)
    return total, forma_de_pagamento, troco


resposta = input("Deseja cadastrar um novo produto? (S/N) ")
while resposta.upper() == "S": 
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    qtd = int(input("Digite a quantidade do produto em estoque: "))
    cadastrar_produto_estoque(nome,preco,qtd) 
    resposta = input("Deseja cadastrar um novo produto? (S/N) ") 

pagamento(criar_pedido())