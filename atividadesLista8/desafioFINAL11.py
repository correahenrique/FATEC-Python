"""Simule um sistema de cadastro de produtos com as seguintes opções:

1 - Cadastrar produto
2 - Listar produtos
3 - Buscar produto pelo nome
4 - Sair"""

def cadastro():
    produto = input("Digite o produto: ")
    produtos.append(produto.lower())
    print("Funcionou")

def listar():
    for i in produtos:
        print(i)

def busca():
    nome = input("Digite o nome do produto: ")
    achou = False
    for i in produtos:
        if i == nome.lower():
            print(i)
            achou = True
    if achou != True:
        print("Encontrei nao viu")
def sair():
    exit()

def funcaoDaora(numero):
    if numero == 1:
        cadastro()
    elif numero == 2:
        listar()
    elif numero == 3:
        busca()
    elif numero == 4:
        sair()
    else:
        print("Digita algo daqui po")

produtos = []

while True:
    print("===== SISTEMA DE CADASTRO =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto pelo nome")
    print("4 - Sair")
    print("===============================")
    numero = int(input("Digite um numero: "))
    funcaoDaora(numero)