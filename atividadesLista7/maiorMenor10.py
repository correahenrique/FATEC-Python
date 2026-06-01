"""10. Encontre o maior e o menor elemento de uma matriz."""

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input("Digite um valor: "))
        linha.append(valor)
    matriz.append(linha)
for i in matriz:
    print(i)

maior = matriz[0][0]
menor = matriz[0][0]
for i in range(3):
    for j in range(3):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
        if matriz[i][j] < menor:
            menor = matriz[i][j]
print(f"O menor é o {menor}")
print(f"O maior é o {maior}")