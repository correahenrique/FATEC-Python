"""Peça ao usuário um número N e exiba todos os números de 1 até N que são múltiplos de 3 e 5."""

n = int(input("Digite um número inteiro: "))

for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i}")