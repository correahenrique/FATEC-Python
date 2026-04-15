"""Faça uma função que recebe uma lista de números e
retorna uma nova lista com o fatorial de cada número."""

numeros = []
fatoriais = []

while True:
    valor = input("Digite um valor inteiro ou 'sair' para sair: ")
    if valor == "sair":
        break
    else:
        valor = int(valor)
        numeros.append(valor)
for i in numeros:
    f = 1
    for n in range(1, i + 1):
        f *= n
    fatoriais.append(f)
print(f"Lista original: {numeros}")
print(f"Lista de fatoriais: {fatoriais}")