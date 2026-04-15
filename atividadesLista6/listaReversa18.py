"""Faça uma função que recebe uma lista e retorna outra com os
elementos em ordem reversa (sem usar .reverse() ou [::-1])."""

lista = []
novaLista = []

while True:
    valor = input("Digite um valor ou 'sair' para sair: ")
    if valor == "sair":
        break
    else:
        valor = int(valor)
        lista.append(valor)
for i in range(len(lista) -1, -1, -1):
    novaLista.append(lista[i])

print(f"Lista original: {lista}")
print(f"Lista nova: {novaLista}")