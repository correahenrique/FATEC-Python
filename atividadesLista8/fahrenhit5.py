"""Crie uma função converter_para_fahrenheit(celsius) que converta graus Celsius para Fahrenheit."""

def converter_para_fahrenheit(celsius):
    farenheit = (celsius * 1.8) + 32
    return farenheit

celsius = float(input("Digite o valor da celsius: "))
print(f"Ficou {converter_para_fahrenheit(celsius)} fahrenheit")