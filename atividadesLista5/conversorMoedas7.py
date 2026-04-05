"""Conversor de Moeda: Crie um programa que converta uma quantia em dólares para euros.
Continue pedindo ao usuário quantias em dólares para converter até que ele insira "0"."""

valor = float(input("Digite o valor em dólar: "))

while valor != 0:
    print(f"Valor em euro: ${valor * 0.866898:.2f}")
    valor = float(input("Digite um valor: "))
print("Fim")