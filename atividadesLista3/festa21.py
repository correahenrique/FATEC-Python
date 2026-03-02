idade = int(input("Digite sua idade: "))
acompanhado = input("Você está acompanhado dos seus pais? (SIM ou NÃO) ")

if idade >= 18 or acompanhado == "SIM":
    print("Liberado!!!")
else:
    print("Pode não!")