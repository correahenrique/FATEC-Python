"""Peça ao usuário para digitar 5 números e exiba o maior e o menor deles."""

num = float(input("Digite o primeiro de cinco números: "))
maior = num
menor = num
for i in range(2, 5 + 1):
    num = float(input("Digite mais um número: "))
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
print(f"O maior é: {maior} /n O menor é: {menor}")