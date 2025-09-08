resposta = input("Deseja cadastrar um novo produto? (S/N) ")
while resposta == "S":
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    qtd = int(input("Digite a quantidade do produto em estoque: "))
    resposta = input("Deseja cadastrar um novo produto? (S/N)")

print("-------------------")
print("Cadastro encerrado.")

#utilizamos a variável de controle resposta para que o processo de cadastro de produtos seja continuamente controlado pela usuária.
#poderíamos adicionar, nesse código, outras validações, como uma condicional para o caso de a resposta ser diferente de S ou N, a entrada em qtd ser diferente de um número inteiro