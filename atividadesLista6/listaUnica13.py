"""Leia uma lista de números e crie uma nova lista apenas com os valores
únicos (sem repetições)."""

listas = []
lista2 = []

while True:
    valor = input("Digite um valor ou 'sair' para sair: ")
    if valor.lower() == "sair":
        break
    else:
        valor = int(valor)
        listas.append(valor)
for i in listas:
    if i not in lista2:
        lista2.append(i)
print(listas)
print(lista2)