senha = input("Digite sua senha: ")
autorizado = input("PC autorizado? (S ou N) ")

if senha == "1234" or autorizado == "S":
    print("Autorizado")
else:
    print("Não autorizado")