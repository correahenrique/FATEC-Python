"""Remova todos os números negativos de uma lista de inteiros."""

lista = [-1, 2, -72, 35, 54, -3, -63, -9]
r = 0

for i in lista[:]:
    if i < 0:
        lista.remove(i)
print(lista)