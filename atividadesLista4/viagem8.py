"""O usuário escolhe um destino (São Paulo, Rio de Janeiro, Curitiba, Salvador)
e recebe o valor da passagem."""

destino = input("Informe o destino (São Paulo, Rio de Janeiro, Curitiba, Salvador): ").lower()

match destino:
    case "são paulo" | "sao paulo":
        print("O valor da passagem para São Paulo é R$ 250,00.")
    case "rio de janeiro" | "rio":
        print("O valor da passagem para o Rio de Janeiro é R$ 300,00.")
    case "curitiba":
        print("O valor da passagem para Curitiba é R$ 180,00.")
    case "salvador":
        print("O valor da passagem para Salvador é R$ 450,00.")
    case _:
        print("Destino não atendido pela nossa frota no momento.")