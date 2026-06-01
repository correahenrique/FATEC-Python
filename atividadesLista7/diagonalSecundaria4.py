"""4. Mostre os elementos da diagonal secundária de uma matriz quadrada."""

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
tamanho = len(matriz)

for i in range(tamanho):
    coluna = tamanho - 1 - i
    print(matriz[i][coluna], end=" ")