"""
Implemente um conversor de moedas que permita ao usuário escolher entre Dólar (USD), Euro (EUR) e Libra (GBP)
e converter um valor informado para Reais (BRL).
"""

while True:
    real = float(input("Digite o valor do reais: "))
    moeda = input("Escolha uma moeda para converter, USD = 1, EUR = 2 ou GBP = 3: ")
    match moeda:
        case "1":
            print(f"Seus {real} reais viram {real / 5.21:.2f} dólares")
            break
        case "2":
            print(f"Seus {real} reais viram {real / 6.03:.2f} euros")
            break
        case "3":
            print(f"Seus {real} reais viram {real / 6.99:.2f} libras")
            break
        case _:
            print("É necessário escolher alguma opção")