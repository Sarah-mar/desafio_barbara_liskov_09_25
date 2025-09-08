import datetime #essa é uma library nativa do python, por isso apenas o import é suficiente para que ela funcione. No caso de librarys não nativas, precisamos instalar os arquivos na library no nosso computador usando o comando pip install 

estoque = []

def cadastrar_produto_estoque(nome, preco,qtd):
    data = datetime.datetime.now() #precisamos criar uma variável local data, pois não recebemos esse valor nos parâmetros.
    produto = (nome, preco, qtd, data)
    print(f"Nome: {nome} \nPreço: {preco} \nQuantidade: {qtd} \nData: {data}")
    estoque.append(produto)
    print("Produto Cadastrado.")  

resposta = input("Deseja cadastrar um novo produto? (S/N) ")
while resposta.upper() == "S": 
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    qtd = int(input("Digite a quantidade do produto em estoque: "))
    cadastrar_produto_estoque(nome,preco,qtd) #para que a função cadastrar_produto_estoque funcione corretamente, ela deve ser chamada a cada entrada de dados de um novo produto
    resposta = input("Deseja cadastrar um novo produto? (S/N) ") 




