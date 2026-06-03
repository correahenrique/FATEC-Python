"""📝 O Desafio de Prova
"Crie um sistema de gerenciamento de alunos (CRUD). O sistema deve permitir:

Cadastrar um aluno (Create)

Listar todos os alunos com seus respectivos números de chamada/índice (Read)

Atualizar o nome de um aluno informando o seu número (Update)

Excluir um aluno informando o seu número (Delete)

Sair do programa."""


def cadastro():
    nome = input("Digite o nome do aluno: ")
    alunos.append(nome)
    print("Nome do aluno: ", alunos, " | cadastrado.")

def listar():
    for i in alunos:
        print(i)

def atualizar():
    listar()
    qual = input("Digite o nome do aluno pra modificar: ")
    for i in range(len(alunos)):
        if alunos[i] == qual:
            novo = input("Digite o novo nome do aluno: ")
            alunos[i] = novo
            print("Novo aluno: ", alunos)
            break

def excluir():
    listar()
    qual = input("Digite o nome do aluno pra excluir: ")
    for i in range(len(alunos)):
        if alunos[i] == qual:
            alunos.pop(i)
            print("Aluno morreu: ", alunos)
            break

def sair():
    print("Saindo do sistema...")
    exit()

def menu(opcao):
    if opcao == 1:
        cadastro()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        atualizar()
    elif opcao == 4:
        excluir()
    elif opcao == 5:
        sair()
    else:
        print("Tente novamente")

alunos = []

while True:
    opcao = int(input("Digita ai\n1-Cadastrar | 2-Listar | 3-Atualizar | 4-Deletar | 5-Sair"))
    menu(opcao)