"""Conversão de Temperatura: Faça um programa que converta uma temperatura de Celsius para Fahrenheit.
Continue pedindo ao usuário para inserir uma nova temperatura em Celsius até que ele digite "sair"."""

c = input("Digite uma temperatura em Celcius (Ou 'sair' para sair): ")
while c != "sair":
    i = float(c)
    fahrenheit = (i * 1.8) + 32
    print(f"Temperatura em Celsius: {c} é {fahrenheit} em Fahrenheit")
    c = input("Digite uma temperatura em Celcius (Ou 'sair' para sair): ")
print("Fim do programa")