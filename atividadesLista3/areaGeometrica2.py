"""Desenvolva um programa que permita ao usuário escolher entre calcular a área de um quadrado,
retângulo ou triângulo e insira os valores necessários para o cálculo."""

calculo = input("Digite a figura que você deseja calcular a área: (quadrado = 1), (retãngulo = 2) ou (triângulo = 3): ")

match calculo:
    case "1":
        lado = float(input("Digite o lado do quadrado para saber a área dele: "))
        print(f"A área do quadrado é {lado * lado}")
    case "2":
        lado1 = float(input("Digite um lado do retângulo: "))
        lado2 = float(input("Digite o segundo lado do retângulo para descobrir :"))
        print(f"A área do retângulo é {lado1 * lado2}")
    case "3":
        altura = float(input("Digite a altura do triângulo: "))
        base = float(input("Digite a base do triângulo: "))
        print(f"A área do triângulo é {(base * altura) / 2}")
    case _:
        print("Tem que digitar alguma das opções.")