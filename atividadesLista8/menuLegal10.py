"""Crie um menu com funções para:
Cadastrar nomes
Listar nomes
Sair do programa"""

def cadastro():
    nome = input("Digite um nome: ")
    nomes.append(nome)
    print("Nome cadastrado")

def listar():
    for i in nomes:
        print(i)

def sair():
    exit()

nomes = []

while True:
    print("Faça sua escolha ai meu bom.")
    print("1 - Cadastrar nome")
    print("2 - Listar nomes")
    print("3 - Sair do programa")
    opcao = int(input("Digita ai: "))

    if opcao == 1:
        cadastro()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        sair()
    else:
        print("Escolhe um cara.")
