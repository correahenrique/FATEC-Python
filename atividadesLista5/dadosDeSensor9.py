"""Simulação de Dados de Sensor: Crie um programa que simule a leitura de dados
de um sensor e continue capturando dados até que um valor fora do intervalo de
operação seja detectado (por exemplo, fora de 0 a 100)."""

num = int(input("Digite um numero inteiro de 0 a 100: "))
while num >= 0 and num <= 100:
    print("Beleza...")
    num = int(input("Digite um numero inteiro de 0 a 100: "))
print("Parou ai!")