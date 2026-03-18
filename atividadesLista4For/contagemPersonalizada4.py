inicio = int(input("Digite o início da contagem: "))
final = int(input("Digite o final da contagem: "))
passo = int(input("De quando vamos contar? (1 em 1, 2 em 2...): "))

for i in range(inicio - 1, final + 1, passo):
    print(i)