import datetime #essa é uma library nativa do python, por isso apenas o import é suficiente para que ela funcione. No caso de librarys não nativas, precisamos instalar os arquivos na library no nosso computador usando o comando pip install 

resposta = input("Deseja cadastrar um novo produto? (S/N) ")
while resposta.upper() == "S": 
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    qtd = int(input("Digite a quantidade do produto em estoque: "))
    resposta = input("Deseja cadastrar um novo produto? (S/N) ") 

def cadastrar_produto_estoque(nome, preco,qtd): #aqui, "nome", "preco" e "qtd" são parâmetros, ou seja, podem receber qualquer valor quando a função é chamada e não são necessariamente as variáveis do laço while acima
    print(f"Nome: {nome} \nPreço: {preco} \nQuantidade: {qtd} \nData: {datetime.datetime.now()}")
    #/n adiciona parágrafos ao nosso print
    #a função datetime.datetime.now() é uma função da biblioteca adicionada, que mostra  a data e hora exatos do momento em que é chamada
    print("Produto Cadastrado.")  

cadastrar_produto_estoque(nome,preco,qtd)