
resposta = input("Deseja cadastrar um novo produto? (S/N) ")
while resposta.upper() == "S": #a função .upper() transforma a variável resposta em letras maiúsculas, caso a entrada tenha alguma letra minúscula
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    qtd = int(input("Digite a quantidade do produto em estoque: "))
    resposta = input("Deseja cadastrar um novo produto? (S/N)")

def cadastrar_produto_estoque(nome, preco,qtd):
    print("Produto Cadastrado.")  

#utilizamos a variável de controle resposta para que o processo de cadastro de produtos seja continuamente controlado pela usuária.
#poderíamos adicionar, nesse código, outras validações, como uma condicional para o caso de a resposta ser diferente de S ou N, a entrada em qtd ser diferente de um número inteiro