import datetime
#essa é uma library nativa do python, por isso apenas o import é suficiente para que ela funcione. No caso de librarys não nativas, precisamos instalar os arquivos na library no nosso computador usando o comando pip install 

produtos = []

resposta = input("Deseja cadastrar um novo produto? (S/N) ")
while resposta.upper() == "S":
    #a função .upper() transforma a variável resposta em letras maiúsculas, caso a entrada tenha alguma letra minúscula
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    qtd = int(input("Digite a quantidade do produto em estoque: "))
    produto = [nome, preco, qtd]
    print(f"Nome: {produto[0]} \nPreço: {produto[1]} \nQuantidade: {produto[2]} \nData: {datetime.datetime.now()}")
    produtos.append(produto)
    resposta = input("Deseja cadastrar um novo produto? (S/N)")

print("-------------------")
print("Cadastro encerrado.")

#utilizamos a variável de controle resposta para que o processo de cadastro de produtos seja continuamente controlado pela usuária.
#poderíamos adicionar, nesse código, outras validações, como uma condicional para o caso de a resposta ser diferente de S ou N, a entrada em qtd ser diferente de um número inteiro