"""Junte duas listas e remova os elementos repetidos."""

lista1 = [35, 64, 29, 18, 17, 41]
lista2 = [1, 4, 6, 18, 11, 41]
lista3 = []

for i in lista1 + lista2:
    if i not in lista3:
        lista3.append(i)
print(lista3)