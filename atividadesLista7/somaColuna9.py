"""9. Some os elementos de cada coluna de uma matriz e mostre os resultados."""

matriz = []
somas = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input("Digite um valor: "))
        linha.append(valor)
    matriz.append(linha)
for linha in matriz:
    print(linha)

for j in range(3):
    soma = 0
    for i in range(3):
        soma += matriz[i][j]
    somas.append(soma)
print(somas)