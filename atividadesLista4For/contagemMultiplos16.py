"""Peça ao usuário um número N e exiba quantos números entre 1 e N são múltiplos de 3 ou 5."""

m3 = 0
m5 = 0
n = int(input("Digite um número inteiro: "))

for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        m3 = m3 + 1
        m5 = m5 + 1
    elif i % 3 == 0:
        m3 += 1
    elif i % 5 == 0:
        m5 += 1
print(f"No final, de 1 ao número {n}, existem {m3} múltiplos de 3 e {m5} números múltiplos de 5.")