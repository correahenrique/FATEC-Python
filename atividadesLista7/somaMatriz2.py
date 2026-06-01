"""2. Some todos os elementos de uma matriz 3x3."""

matriz = []
somar = 0

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite um valor [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)
for i in matriz:
    for soma in i:
        somar += soma
print(somar)