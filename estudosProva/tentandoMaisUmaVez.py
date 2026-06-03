
def create():
	nome = input("Digite o nome do aluno ai: ")
	alunos.append(nome)
	print("Terminou!")

def read():
	for i in alunos:
		print(i)

def update():
	read()
	qual = input("Qual aluno você deseja atualizar? ")
	for i in range(len(alunos)):
		if alunos[i] == qual:
			novo = input("Qual o novo nome dele? ")
			alunos[i] = novo
			print("Atualizado!!!")
			break

def delete():
	read()
	qual = input("Qual aluno você deseja deletar? ")
	for i in range(len(alunos)):
		if alunos[i] == qual:
			alunos.pop(i)
			print("Deletado!!!")
			break

def sair():
	print("Saindo...")
	exit()

def menu(opcao):
	if opcao == 1:
		create()
	elif opcao == 2:
		read()
	elif opcao == 3:
		update()
	elif opcao == 4:
		delete()
	elif opcao == 5:
		sair()
	else:
		print("Tente novamente")

alunos = []

while True:
	opcao = int(input("Digite a opção: 1 = cadastro 2 = ler 3 = atualizar 4 = excluir 5 = sair"))
	menu(opcao)