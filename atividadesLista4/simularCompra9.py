"""O usuário escolhe um produto de hardware (RTX 5090, RTX 4060, GTX 1030, RX 7800)
e o programa informa o preço médio de mercado."""

produto = input("Informe o modelo do hardware (RTX 5090, RTX 4060, GTX 1030, RX 7800): ").upper()

match produto:
    case "RTX 5090":
        print("O preço estimado da RTX 5090 é R$ 14.500,00.")
    case "RTX 4060":
        print("O preço médio da RTX 4060 é R$ 2.100,00.")
    case "GTX 1030" | "GT 1030":
        print("O preço médio da GT 1030 é R$ 450,00.")
    case "RX 7800":
        print("O preço médio da RX 7800 XT é R$ 3.600,00.")
    case _:
        print("Tem que digitar algum dos produtos...")