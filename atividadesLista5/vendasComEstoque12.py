"""Sistema de Vendas com Estoque Reduzido: O Sistema define um estoque inicial de produtos e
a cada venda, retira quantidade do estoque.
O sistema encerra quando não permite vender mais do que o disponível."""

estoque = 20
print(f"Estoque inicial: {estoque}")
venda = int(input("Digite o quanto você quer comprar: "))

while venda < estoque:
    estoque -= venda
    print(f"Venda realizada! Restam {estoque} unidades.")
    venda = int(input("Digite o quanto você quer comprar: "))
print("Já acabou o estoque...")