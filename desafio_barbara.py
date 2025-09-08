
resposta = input("Deseja cadastrar um novo produto? (S/N) ")
while resposta.upper() == "S": #a função .upper() transforma a variável resposta em letras maiúsculas, caso a entrada tenha alguma letra minúscula
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    qtd = int(input("Digite a quantidade do produto em estoque: "))
    resposta = input("Deseja cadastrar um novo produto? (S/N)")

def cadastrar_produto_estoque(nome, preco,qtd): #aqui, "nome", "preco" e "qtd" são parâmetros, ou seja, podem receber qualquer valor quando a função é chamada e não são necessariamente as variáveis do laço while acima
    print("Produto Cadastrado.")  

