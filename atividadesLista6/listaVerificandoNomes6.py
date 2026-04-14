"""Verifique se um nome digitado pelo usuário está em uma lista de nomes."""

nomes = ["henrique", "marcos", "maria", "ana", "clara", "joaquim"]
while True:
    hm = input("Digite um nome (Digite 'sair' para sair): ")
    if hm == "sair":
        print("Saindo...")
        break

    if hm.lower() in nomes:
        print(f"Esse nome ja está na lista... ({hm})")
    else:
        print("Ta na lista não...")