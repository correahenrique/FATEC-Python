"""Peça um número ao usuário e some separadamente os pares e os ímpares de 1 até esse número."""

num = int(input("Digite um número inteiro: "))
pares = 0
impares = 0

for i in range(1, num + 1):
    if i % 2 == 0:
        pares = i + pares
    else:
        impares = i + impares
print(f"{pares} pares e {impares} impares")