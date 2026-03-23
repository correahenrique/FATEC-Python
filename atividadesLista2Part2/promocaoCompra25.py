compra = float(input("Digite o valor da compra: "))
cliente = input("Você é VIP? (S ou N) ")

if compra > 100 or cliente == "S":
    print(f"Desconto de 10%, total é {compra:.2f} e ficou {compra * 0.90:.2f}")
else:
    print(f"O total ficou {compra}")