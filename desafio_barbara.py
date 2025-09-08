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

resposta = input("Deseja cadastrar um novo produto? (S/N) ")
while resposta.upper() == "S": 
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    qtd = int(input("Digite a quantidade do produto em estoque: "))
    cadastrar_produto_estoque(nome,preco,qtd) 
    resposta = input("Deseja cadastrar um novo produto? (S/N) ") 


