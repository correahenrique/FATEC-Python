"""Solicite o preço de um produto e aplique um desconto de 10% se o preço for maior que R$ 100. Exiba o valor final."""

preco = float(input("Digite o valor do produto: "))

if preco > 100:
    print(f"O seu produto ganhou 10% de desconto!!! No total ficou {preco * 1.10:.2f} reais")
else:
    print(f"O total ficou {preco}")