"""Desenvolva um menu de opções para gerenciar uma lista de tarefas:
adicionar, remover, exibir e sair."""

tarefas = []

while True:
    print("1- Adicionar\n2- Remover\n3- Exibir\n4- Sair")
    escolha = int(input("Digite um número para selecionar sua escolha: "))
    if escolha == 1:
        tarefa = input("Digite uma tarefa: ")
        tarefas.append(tarefa)
    elif escolha == 2:
        resultado = ", ".join(tarefas)
        print(f"{resultado}.")
        remover = input("Qual você deseja remover? ")
        for i in tarefas[:]:
            if i == remover:
                tarefas.remove(i)
                resultado = ", ".join(tarefas)
                print(f"Removido!\nOlha ai: {resultado}")
    elif escolha == 3:
        resultado = ", ".join(tarefas)
        print(f"{resultado}.")
    elif escolha == 4:
        print("saindo...")
        break
    else:
        print("Tente novamente...")