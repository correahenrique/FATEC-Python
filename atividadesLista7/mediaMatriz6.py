"""6. Calcule a média de todos os elementos de uma matriz."""

matriz = []
count = 0
total = 0
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite um valor [{i}][{j}]: "))
        linha.append(valor)
        count += 1
        total += valor
    matriz.append(linha)
for i in matriz:
    print(i)
print(f"A média ficou {total / count} com {count} numeros")