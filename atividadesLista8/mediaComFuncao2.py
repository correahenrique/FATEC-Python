"""Crie uma função que receba dois números e retorne a média entre eles."""

def media(numeros):
    total = 0
    count = 0

    for i in numeros:
        total += i
        count += 1

    media = total / count
    return media

numeros = []

while True:
    num = input("Digite o numero ou 'SAIR' para sair: ")
    if num.upper() == "SAIR":
        break
    else:
        numeros.append(int(num))
print(f"A média é: {media(numeros)}")