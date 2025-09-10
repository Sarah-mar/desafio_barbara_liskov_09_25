
import datetime 

estoque = []

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
            elif produto[0] == nome_pedido and produto[2] < qtd_pedido:
                while qtd_pedido > produto[2]:
                    print("Quantidade indisponível")
                    print ("Produto:", produto[0],"Quantidade disponível:" , produto[2])
                    qtd_pedido = int(input("Qual a quantidade desejada? "))
                pedido.append([nome_pedido, qtd_pedido, datetime.datetime.now()])
            else:
                continue
        continua = input("Deseja continuar o pedido? (S/N) ")
    print("Pedido encerrado. Confira abaixo seu pedido: ")
    for produto in pedido:
        print(produto[0], "-------", produto[1], "-------" ,produto[2])
    atualizar_estoque(pedido)

def atualizar_estoque(pedido):
    print("Estoque anterior:", estoque)
    for produto in pedido:
        for item in estoque:
            if item[0] == produto[0]:
                item[2] = item[2] - produto[1]
    print("Estoque atualizado:",estoque)


resposta = input("Deseja cadastrar um novo produto? (S/N) ")
while resposta.upper() == "S": 
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    qtd = int(input("Digite a quantidade do produto em estoque: "))
    cadastrar_produto_estoque(nome,preco,qtd) 
    resposta = input("Deseja cadastrar um novo produto? (S/N) ") 
