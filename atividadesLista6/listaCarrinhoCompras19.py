"""Simule um carrinho de compras:
adicione produtos até que o usuário digite 'fim' e, no final, mostre o carrinho."""

carrinho = []

while True:
    valor = input("Digite um valor ou 'fim' para sair: ")
    if valor == "fim":
        break
    else:
        carrinho.append(valor)
resultado = ", ".join(carrinho)
print(f"Carrinho de compras: {resultado}.")