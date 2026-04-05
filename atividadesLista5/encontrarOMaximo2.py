"""Encontrar o Máximo: Crie um programa que peça ao usuário para inserir números e encontre o maior número inserido.
O programa deve continuar pedindo números até que o usuário digite "sair"""

num = input("Digite um número (ou 'sair' para sair): ")
if num.lower() != "sair":
    i = int(num)
    maior = i
    menor = i
    while num != "sair":
        i = int(num)
        if maior < i:
            maior = i
        if menor > i:
            menor = i
        num = input("Digite um número (ou 'sair' para sair): ")
    print(f"No final, o maior número foi o: {maior} e o menor foi: {menor}")
else:
    print("Nenhum número foi inserido.")