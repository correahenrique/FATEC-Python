"""Faça um programa que leia números do usuário até que ele digite 0.
Depois, mostre a lista e a soma dos números."""

numeros = []
soma = 0

while True:
    numero = int(input("Digite um número! (0 para sair): "))
    if numero == 0:
        break
    else:
        numeros.append(numero)
for i in numeros:
    soma += i
print(numeros)
print(f"A soma ficou: {soma}")