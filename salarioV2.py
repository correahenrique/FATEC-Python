print("Qual o seu salário?")
dias = int(input("Quantos dias você trabalhou nesse mês? (coloca mais de 31 não, quero colocar if aqui não)"))
horas = dias * 8
salario = horas * 25

print(f"O seu salário é {salario} e você trabalhou {horas} horas, precisa de uma folga!")