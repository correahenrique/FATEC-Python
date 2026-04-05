"""Simulador de Caixa Registradora: O usuário digita o preço e
a quantidade de produtos até digitar “sair”.
O Sistema mostra a quantidade de produtos e o valor final da compra."""

precoTotal = 0
quantidadeTotal = 0

while True:
    preco = input("Digite o preço ou 'sair' para sair: ")
    if preco == "sair":
        break
    quantidade = input("Digite a quantidade de produtos ou 'sair' para sair: ")
    if quantidade == "sair":
        break
    i = int(preco)
    j = int(quantidade)
    precoTotal += i
    quantidadeTotal += j

print(f"Parou, o total da compra foi de {precoTotal} e a quantidade final foi de {quantidadeTotal}")