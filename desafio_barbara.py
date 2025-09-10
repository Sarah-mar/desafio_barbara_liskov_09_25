import datetime 

estoque = []

def cadastrar_produto_estoque(nome, preco,qtd):
    data = datetime.datetime.now() 
    produto = [nome, preco, qtd, data]
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
    if len(estoque) == 0: #fazemos essa validação para caso o estoque esteja vazio
        existe = -1 
    else:
        for produto in estoque:
            if produto[0] == nome and produto[2] != 0:
                existe = 1
                break 
            elif produto[0] == nome and produto[2] == 0: 
                existe = 0
                break
            else: 
                existe = -1
    return existe

def criar_pedido():
    pedido = []
    continua = "S"
    while continua.upper() == "S":
        exibir_estoque()
        nome_pedido = input("Qual produto deseja comprar? ")
        estado_no_estoque = confere_produto_no_estoque(nome_pedido) 
        if estado_no_estoque != 1:
           print ("Produto indisponível")
           continua = input("Deseja continuar o pedido? (S/N) ")
        else: 
            qtd_pedido = int(input("Qual a quantidade desejada? "))
            for produto in estoque:
                if produto[0] == nome_pedido and produto[2] >= qtd_pedido:
                    pedido.append([nome_pedido, qtd_pedido, datetime.datetime.now()])
                elif produto[0] == nome_pedido and produto[2] < qtd_pedido:
                    while qtd_pedido > produto[2]:
                        print("Quantidade indisponível")
                        print ("Produto:", produto[0],"Quantidade disponível:" , produto[2])
                        qtd_pedido = int(input("Qual a quantidade desejada? "))
                    pedido.append([nome_pedido, qtd_pedido, datetime.datetime.now()])
                else:
                    continue
            continua = input("Deseja continuar o pedido? (S/N) ")
            atualizar_estoque(pedido) 
    if len(pedido) != 0:
        print("Pedido encerrado. Confira abaixo seu pedido: ")
        for produto in pedido:
            print(produto[0], "-------", produto[1], "-------" ,produto[2])  
    return pedido

def atualizar_estoque(pedido):
    for produto in pedido:
        for item in estoque:
            if item[0] == produto[0]:
                item[2] = item[2] - produto[1]

def pagamento(pedido):
    total = 0
    for produto in pedido:
        for item in estoque:
            if produto[0] == item[0]:
                total += produto[1] * item[1]
    print("Total:", total)
    forma_de_pagamento = int(input("Qual será a forma de pagamento? (1-cartão, 2-dinheiro) "))
    if forma_de_pagamento ==  1:
        troco = 0
        print("Compra encerrada. Agradecemos a preferência!")
    elif forma_de_pagamento == 2:
        valor_recebido = float(input("Digite o valor pago em dinheiro: "))
        troco = valor_recebido - total
        print("Troco:", troco)
        print("Compra encerrada. Agradecemos a preferência!")
    return total, forma_de_pagamento, troco

def exibir_pedidos_registrados():
    print("Pedidos registrados:")
    for item in pedidos_registrados.keys():
        print(item)
        for campo in pedidos_registrados[item].keys():
            print(campo, ":", pedidos_registrados[item][campo])



pedido_a_registrar ={
    }
pedidos_registrados = {
    }
contador_pedidos = 1

repete = True
while repete:
    processo = int(input("Olá! Qual ação deseja realizar? \n 1 - Ver o estoque \n 2 - Criar o pedido \n 3 - Adicionar itens no estoque \n 4 - Mostrar todos os pedidos \n 5 - Sair "))
    if processo == 1:
        exibir_estoque()
    elif processo == 2:
        infos_pedido = criar_pedido()
        if len(infos_pedido) == 0:
            print("Pedido não registrado.")
        else:
            total, forma_de_pagamento, troco  = pagamento(infos_pedido)
            itens = []
            if forma_de_pagamento == 1:
                forma_de_pagamento = "cartão"
            else:
                forma_de_pagamento = "dinheiro"
            for produto in infos_pedido:
                itens.append([produto[0], produto[1]])
                data = [produto[2]]
            pedido_a_registrar = {"Itens": itens,
                            "Data": data,
                            "Total" : total, 
                            "Forma de pagamento" : forma_de_pagamento,
                            "Troco" : troco}
            pedidos_registrados[contador_pedidos] = pedido_a_registrar
            contador_pedidos += 1
    elif processo == 3:
        resposta = input("Deseja cadastrar um novo produto? (S/N) ")
        while resposta.upper() == "S": 
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            qtd = int(input("Digite a quantidade do produto em estoque: "))
            cadastrar_produto_estoque(nome,preco,qtd) 
            resposta = input("Deseja cadastrar um novo produto? (S/N) ") 
    elif processo == 4:
        exibir_pedidos_registrados()
    else:
        print("Atendimento encerrado.")
        repete =  False

