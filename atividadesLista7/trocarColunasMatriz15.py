"""Troque os valores da primeira linha com a última linha de uma matriz."""

matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

ultima = 3
primeira = matriz[0]
matriz[0] = matriz[ultima]
matriz[ultima] = primeira

for i in matriz:
    print(i)