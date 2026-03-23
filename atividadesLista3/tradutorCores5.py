"""O usuário informa uma cor em português (vermelho, azul, verde, amarelo),
e o programa exibe sua tradução para inglês."""

cor = input("Informe uma cor em português (vermelho, azul, verde, amarelo): ").lower()

match cor:
    case "vermelho":
        print("Tradução: Red")
    case "azul":
        print("Tradução: Blue")
    case "verde":
        print("Tradução: Green")
    case "amarelo":
        print("Tradução: Yellow")
    case _:
        print("Cor não encontrada no dicionário.")