"""Solicite um número ao usuário e exiba o seu fatorial (n!)."""

num = int(input("Digite um número para mostrar seu fatorial: "))
f = 1
for i in range(1, num + 1):
    f *= i
print(f)