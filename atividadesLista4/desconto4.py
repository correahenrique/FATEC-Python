"""O usuário deve informar o tipo de produto (Eletrônico, Roupas, Alimentos, Móveis),
 e o programa exibirá o percentual de desconto correspondente."""

categoria = input("Informe a categoria do produto (Eletrônico, Roupas, Alimentos, Móveis): ").lower()

match categoria:
    case "eletrônico" | "eletronico":
        print("Desconto de 15% aplicado para Eletrônicos!")
    case "roupas":
        print("Desconto de 20% aplicado para Roupas!")
    case "alimentos":
        print("Desconto de 5% aplicado para Alimentos!")
    case "móveis" | "moveis":
        print("Desconto de 10% aplicado para Móveis!")
    case _:
        print("Categoria não reconhecida. Sem desconto disponível.")