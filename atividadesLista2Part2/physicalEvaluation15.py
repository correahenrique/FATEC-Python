idade = int(input("Digite sua idade: (0 a 100) "))
performance = int(input("Digite sua performance: (0 a 100) "))

if idade >= 18:
    if performance >= 70:
        print("Aprovado")
    else:
        print("Reprovado")
else:
    print("Reprovado")