"""Faça um programa que leia uma matriz 4x4
e diga quantos elementos estão acima da média."""

matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
maiores = []

total = 0
for i in matriz:
    for j in i:
        total += j
media = total/16

for i in matriz:
    for j in i:
        if j > media:
            maiores.append(j)
for i in matriz:
    print(i)
print(media)
print(maiores)