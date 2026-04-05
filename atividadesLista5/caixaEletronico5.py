"""Simulador de Caixa Eletrônico: Crie um programa que simule um caixa eletrônico,
que continue pedindo ao usuário para inserir um valor de
saque até que o saldo da conta seja zero ou negativo."""

conta = 2500
while conta > 0:
    print(f"Conta do caixa: {conta}")
    saque = float(input("Digite o valor do saque: "))
    conta -= saque
print(f"O valor na conta ficou: {conta}")