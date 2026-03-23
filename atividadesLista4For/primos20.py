"""Crie um programa que solicite ao usuário um número e informe se ele é primo ou não.
Lembre-se de que um número primo é aquele que é divisível apenas por 1 e por ele mesmo."""

n = int(input("Digite um número inteiro: "))
primo = 0

for i in range(1, n + 1):
    if n % i == 0:
        primo += 1
if primo != 2:
    print(f"{n} não é primo...")
else:
    print(f"O {n} é primo!!!")