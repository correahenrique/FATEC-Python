"""Peça ao usuário 10 números e exiba quantos são positivos, negativos ou zero."""
positivo = 0
negativo = 0
zero = 0

for i in range(1, 11):
    num = int(input(f"Digite um número {i}/10: "))
    if num > 0:
        positivo += 1
    elif num < 0:
        negativo += 1
    else:
        zero += 1
print(f"No final, foram {positivo} positivos, {negativo} negativos e {zero} zeros.")

"""    if num > 0:
        print(f"{num} é positivo!")
    elif num < 0:
        print(f"{num} é negativo!")
    else:
        print(f"{num} é zero.")"""