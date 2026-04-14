"""Leia 10 números e ordene a lista do maior para o menor."""

listas = []

while True:
    valor = input("Digite um valor ou 'sair' para sair: ")
    if valor == "sair":
        break
    else:
        valor = int(valor)
        listas.append(valor)

listas.sort(reverse=True)
print(listas)