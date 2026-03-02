idade = int(input("Digite sua idade: "))
titulo = input("Seu título está válido?: (SIM ou NÃO) ")

if idade > 15:
    if titulo == "SIM":
        print("Pode votar!!!")
    else:
        print("Não pode votar!!!")
else:
    print("Não pode votar!!!")