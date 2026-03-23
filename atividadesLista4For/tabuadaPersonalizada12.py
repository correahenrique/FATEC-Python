"""Peça um número ao usuário e exiba sua tabuada de 1 a 10,
mas se for múltiplo de 3, substitua pelo texto "Multiplo de 3"."""

"""num = int(input("Digite um número inteiro para fazermos a tabuada: "))

for i in range(1, 10 + 1):
    resultado = num * i
    if resultado % 3 == 0:
        print(f"{resultado} é múltiplo de 3!!!")
    else:
        print(f"{num} * {i} = {resultado}")"""

num = int(input("Digite um número inteiro para fazermos a tabuada: "))

if num % 3 == 0:
    print("Múltiplo de 3!!!")
else:
    for i in range(1, 10 + 1):
        resultado = num * i
        print(f"{num} * {i} = {resultado}")