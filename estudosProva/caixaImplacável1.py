"""1. O Caixa Eletrônico Implacável (while, match case, if/else)
Crie um programa que simule um caixa eletrônico. Ele deve começar com um saldo de R$ 1000.00.
Utilize um laço de repetição para exibir um menu continuamente até que o usuário escolha a opção de sair.
O menu deve usar match case para as seguintes opções:

1 - Depósito: Pede um valor. Se for maior que 0, soma ao saldo. Se for negativo, exibe erro.

2 - Saque: Pede um valor.
O saque só pode ser realizado se o valor for maior que 0 E houver saldo suficiente na conta.

3 - Saldo: Mostra o saldo atual.

4 - Sair: Encerra o programa.

Caso digite outra coisa: Exibir "Opção inválida"."""

saldo = 1000

while True:
    print("1 - Depósito.\n2 - Saque.\n3 - Saldo.\nOu 'sair' para sair.")
    opcao = input("Digite uma opção para selecionar o que fazer: ")
    if opcao.lower() == "sair":
        print("Saindo do programa...")
        break
    else:
        match opcao:
            case "1":
                print("Depósito")
                valor = int(input("Digite o valor: "))
                if  valor > 0:
                    saldo += valor
                    print(saldo)
                else:
                    print("É necessário um valor positivo/maior que zero...")
            case "2":
                print("Saque")
                saque = int(input("Digite o valor: "))
                if saque > 0 and saque <= saldo:
                    saldo -= saque
                    print(saldo)
                else:
                    print("É necessário um valor positivo/maior que zero e saldo suficiente...")
            case "3":
                print("Saldo")
                print(saldo)
            case _:
                print("Deve escolher alguma opção...")