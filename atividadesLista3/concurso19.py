idade = int(input("Digite sua idade: "))
escolaridade = input("Sua escolaridade está adequada?: (SIM ou NÃO) ")

if idade >= 18:
    if escolaridade == "SIM":
        print("Pode participar do concurso!!!")
    else:
        print("Não pode participar!!!")
else:
    print("Não pode participar!!!")