"""Crie uma função que receba uma lista de números e retorne quantos são pares."""

def pares(numeros):
    par = []
    count = 0
    for i in numeros:
        if i % 2 == 0:
            par.append(i)
            count += 1
    return par, count

numeros = []

while True:
    num = input("Digite o numero ou 'SAIR' para sair: ")
    if num.upper() == "SAIR":
        break
    else:
        numeros.append(int(num))
paresss, count = pares(numeros)
print(f"Então no final, {count} números pares, e foram esses: {paresss}")