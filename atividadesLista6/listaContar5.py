"""Conte quantas vezes o número 3 aparece em uma lista."""

lista = [1, 3, 4, 3, 5, 3, 2, 8]
tres = 0

for i in lista:
    if i == 3:
        print(f"Esse número({i}) é três!")
        tres += 1
    else:
        print(f"Analisando... ({i})")
print(f"No total, foram {tres} três")