estudante = input("Você é estudante? (SIM ou NÃO) ")
idade = int(input("Qual a sua idade? "))

if estudante == "SIM" or idade < 18:
    print("Meia entrada permitida!!!")
else:
    print("Meia entrada não permitida!!!")