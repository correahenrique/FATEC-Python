senhas = ["12345", "fiec#2026", "senha123", "acesso#global", "fiec#7"]
seguras = []
naoSeguras = []
i = 0

while i < len(senhas):
    senha = senhas[i]

    if len(senha) < 8 or "#" not in senha:
        print(f"{senha}: Insegura")
        naoSeguras.append(senha)
    else:
        print(f"{senha}: Segura")
        seguras.append(senha)


    i += 1
