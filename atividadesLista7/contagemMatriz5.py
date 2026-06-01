"""5. Conte quantos números pares existem em uma matriz."""

matriz = []
count = 0

for i in range(3):
    lista = []
    for j in range(3):
        valor = int(input(f"Digite o valor [{i}][{j}]: "))
        lista.append(valor)
        if valor % 2 == 0:
            count += 1
    matriz.append(lista)
for i in matriz:
    print(i)
print(f"Tem {count} numeros pares")