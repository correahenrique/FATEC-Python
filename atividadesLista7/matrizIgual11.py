"""Verifique se duas matrizes 2x2 digitadas pelo usuário são iguais."""

matriz1 = []
matriz2 = []
verdade = 1

for i in range(2):
    linha = []
    for j in range(2):
        valor = int(input("Digite o valor: "))
        linha.append(valor)
    matriz1.append(linha)
print("Aqui está sua matriz1: ")
for i in matriz1:
    print(i)
for i in range(2):
    linha2 = []
    for j in range(2):
        valor2 = int(input("Digite o valor: "))
        linha2.append(valor2)
    matriz2.append(linha2)
print("Aqui está sua matriz2: ")
for i in matriz2:
    print(i)
if matriz1 == matriz2:
    print("As matrizes são iguais!!!")
else:
    print("As matrizes não são iguais!!!")