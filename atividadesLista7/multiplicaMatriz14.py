"""Multiplique todos os elementos de uma matriz por um número dado pelo usuário."""

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in matriz:
    print(i)
multiplicador = int(input("Digite o multiplicador: "))

for i in range(3):
    for j in range(3):
        matriz[i][j] *= multiplicador
print(f"Matriz multiplicada por {multiplicador}:")
for linha in matriz:
    print(linha)