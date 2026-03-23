"""O usuário escolhe uma forma de pagamento (Pix, Cartão de Crédito, Boleto, Parcelado)
e o programa informa se há desconto ou acréscimo."""

pagamento = input("Escolha a forma de pagamento (Pix, Boleto, Crédito ou Parcelado): ").lower()

match pagamento:
    case "pix":
        print("Pagamento via Pix: Você ganhou 10% de desconto!")
    case "boleto":
        print("Pagamento via Boleto: Você ganhou 5% de desconto!")
    case "crédito" | "credito":
        print("Pagamento no Crédito: Sem descontos.")
    case "parcelado":
        print("Pagamento Parcelado: Acréscimo de 2% de juros ao mês.")
    case _:
        print("Tem que ser uma opção válida...")