"""Quantidade de valores: Conte quantos valores positivos, negativos e zeros foram digitados."""

zero = 0
positivo = 0
negativo = 0

n = input("Digite um número (Digite 'sair' para sair): ")
while n.lower() != "sair":
    i = float(n)
    if i == 0:
        zero += 1
    else:
        if i > 0:
            positivo += 1
        else:
            negativo += 1
    n = input("Digite um número (Digite 'sair' para sair): ")
print(f"No final, teve {positivo} valores positivos, {negativo} valores negativos e {zero} valores zero")