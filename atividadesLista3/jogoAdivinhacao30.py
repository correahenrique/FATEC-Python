"""
numero = float(input("Digite um número e tente acertar o segredo!!! "))
segredo = 50

if numero == segredo or numero == (segredo - 1) or numero == (segredo + 1):
    print("Acertou!!!")
else:
    print("Errou!!!")
"""
from random import  randint

continuar = input("VAMOS COMEÇAR???? (S ou N) ").upper()
segredo = (randint(0, 1000))
tentativas = 0
print(segredo)

while continuar != "N":
    numero = float(input("Digite um número e tente acertar o segredo!!! "))
    tentativas += 1
    if numero == segredo:
        print(f"Acertou!!! O número era {segredo} e você precisou de {tentativas} tentativas")
        break
    else:
        print("Errou!!!")
        if numero > segredo:
            print("O número que você digitou é maior que o segredo...")
        else:
            print("O número que você digitou é menor que o segredo...")
        continuar = input(f"Quer continuar???? (S ou N) ").upper()
        if continuar == "N":
            print(f"Desistiu!!! O número era {segredo}")
            break