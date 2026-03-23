cadastro = input("Tem cadastro? (SIM ou NÃO) ")
valor = float(input("Qual o valor da compra? "))

if cadastro == "SIM":
    if valor >= 500:
        print(f"DESCONTO!!! O total fica {valor * 0.80:.2f} reais.")
    else:
        print(f"Total fica {valor}")
else:
    print(f"Se cadastre primeiro!")