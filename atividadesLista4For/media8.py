"""Peça 5 notas ao usuário e calcule a média delas."""
total = 0

for i in range(0, 5, 1):
    num = float(input("Digite um número para calcular a média: "))
    total = total + num
media = total / 5
print(f"A média é {media}")