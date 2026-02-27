"""Faça um programa que leia a idade
e a categoria de um jogador de futebol (juvenil, adulto, veterano) e calcule a sua classificação no time."""

idade = int(input("Digite sua idade: "))
categoria = input("Digite sua categoria (juvenil, adulto ou veterano): ")

if categoria == "juvenil":
    if idade < 18:
        print("Ta em dia ne")
    else:
        print("Ta meio atrasado ne,c nao é juvenil mais nao")
elif categoria == "adulto":
    if idade < 30:
        print("Ta em dia ne")
    else:
        print("Ta meio atrasado ne pai, vc deveria ser veterano ja")
elif categoria == "veterano":
    if idade > 50:
        print("Ta na hora de aposentar ja ne")
    else:
        print("Ta em dia ne")
else:
    print("Tem que escolher uma categoria ne")