"""Desenvolva um programa que permita ao usuário escolher uma operação (saque, depósito)
e simule o comportamento de um caixa eletrônico com validações básicas (ex.: saldo insuficiente para saque)."""

escolha = input("Qual o seu escolha (saque ou depósito)? ")

if (escolha == "saque"):
    print(f"O seu saldo é insuficiente")
elif (escolha == "depósito"):
    deposito = float(input("Qual o valor do depósito? "))
    print(f"O depósito de {deposito:.2f} reais foi efetuado com sucesso")
else:
    print("É necessário escolher uma das opções!")