nota = int(input("Qual a sua nota? (0 a 100) "))
presenca = int(input("Qual a sua presença? (0 a 100) "))

if nota >= 60:
    if presenca >= 75:
        print(f"Aprovado!!!")
    else:
        print(f"Reprovado por falta pai!!!")
else:
    print(f"Reprovado!!! Nem chegou na média :C")