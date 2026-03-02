preco = float(input("Digite o valor da sua compra: (se for maior que 1000 tem desconto de 10% à vista) "))
pagamento = int(input("Digite quantas vezes deseja fazer o pagamento: "))
desconto = preco * 0.90

if preco > 1000:
    if pagamento == 1:
        print(f"Ficou um total de {desconto:.2f} reais, com 10% de desconto no total de {preco:.2f}.")
    else:
        print(f"O total ficou {preco:.2f} reais.")
else:
    print(f"Ficou um total de {preco:.2f} reais.")