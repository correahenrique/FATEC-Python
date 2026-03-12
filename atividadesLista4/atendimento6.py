"""O usuário seleciona uma opção de atendimento telefônico:
1 - Suporte Técnico
2 - Financeiro
3 - Cancelamento
4 - Falar com um atendente"""

opcao = input("Selecione uma opção (1, 2, 3 ou 4): ")

match opcao:
    case "1":
        print("Encaminhando para o Suporte Técnico. Aguarde na linha...")
    case "2":
        print("Acessando o setor Financeiro. Digite o número do seu boleto.")
    case "3":
        print("Você escolheu Cancelamento. Lamentamos muito, vamos iniciar o processo.")
    case "4":
        print("Aguarde um momento, estamos transferindo para um atendente.")
    case _:
        print("Opção inválida. Por favor, tente novamente.")