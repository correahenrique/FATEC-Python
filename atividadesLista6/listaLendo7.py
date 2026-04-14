"""Faça um programa que leia 10 números e armazene em duas listas: uma com pares e outra com ímpares."""

listaPar = []
listaImpar = []

while True:
    numero = input("Digite um número (sair para sair):")
    if numero == "sair":
        break
    else:
        numero = int(numero)
        if numero % 2 == 0:
            listaPar.append(numero)
        else:
            listaImpar.append(numero)

print("No final, ficou assim:")
for i in listaPar:
    print(f"{i} é par!")
for i in listaImpar:
    print(f"{i} não é par!")