"""Controle de Estoque: Faça um controle de estoque com menu de entrada, saída e exibição."""

estoque = []

while True:
    print("--- Escolhe uma opção ai ---")
    print("1. Entrada de Produto")
    print("2. Saída de Produto")
    print("3. Exibir Estoque")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        id = int(input("Digite o id do produto: "))
        nome = input("Nome do produto: ")
        qtd = int(input("Quantidade de entrada: "))
        estoque.append({"id": id, "nome": nome, "quantidade": qtd})
    elif opcao == "2":
        achei = 0
        remover = int(input("Digite o id do produto que você deseja remover: "))
        for i in estoque:
            if i["id"] == remover:
                estoque.remove(i)
                print("Removido!")
                achei = 1
                break

        if achei == 0:
            print("Não achei...")
    elif opcao == "3":
        print("Itens do estoque: ")
        for i in estoque:
            print(f"Id do produto: {i['id']}, {i['nome']}, Quantidade: {i['quantidade']}")
            print("-------------------------------------")
    elif opcao == "4":
        print("Saindo")
        break
    else:
        print("Digitou errado...")