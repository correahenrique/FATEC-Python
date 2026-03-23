acesso = input("Qual o seu acesso? (aluno, funcionário, público) ")

if acesso == "aluno" or acesso == "funcionário":
    print("Seu acesso é permitido")
else:
    print("Seu acesso é negado")