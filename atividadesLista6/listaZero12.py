"""Substitua todos os números ímpares de uma lista por zero."""

listas = []

while True:
    valor = input("Digite um valor (sair para sair): ")
    if valor == "sair":
        break
    else:
        valor = int(valor)
        listas.append(valor)

for i in range(len(listas)):
    if listas[i] % 2 != 0:
        listas[i] = 0
print(listas)