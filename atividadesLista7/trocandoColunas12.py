"""Transponha uma matriz 3x3 (trocar linhas por colunas)."""

matriz = []
matriz2 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input("Digite um número: "))
        linha.append(valor)
    matriz.append(linha)
for i in range(3):
    for j in range(3):
        matriz2[j][i] = matriz[i][j]

print("Matriz antiga:")
for i in matriz:
    print(i)
print("Matriz nova:")
for i in matriz2:
    print(i)