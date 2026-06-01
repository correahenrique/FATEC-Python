"""8. Some os elementos de cada linha de uma matriz e mostre os resultados."""

matriz = []
somas = []

for i in range(3):
    linha = []
    soma = 0
    for j in range(3):
        valor = int(input("Digite um valor: "))
        linha.append(valor)
        soma += valor
    matriz.append(linha)
    somas.append(soma)
for o in matriz:
    print(o)
print(somas)