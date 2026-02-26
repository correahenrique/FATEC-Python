"""Peça ao usuário seu peso e altura, calcule o Índice de Massa Corporal (IMC)
e classifique-o como "Abaixo do peso", "Peso normal", "Sobrepeso" ou "Obesidade". """

peso = float(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura? "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso")
elif imc <= 25:
    print("Peso normal")
elif imc <= 30:
    print("Sobrepeso")
else:
    print("Obesidade")