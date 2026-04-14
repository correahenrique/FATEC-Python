"""Peça ao usuário para digitar 5 nomes e armazene-os em uma lista.
Depois, exiba os nomes um por um."""

nomes = []

for i in range(5):
    nome = input(f"Digite o {i + 1}º nome: ")
    nomes.append(nome)

for a in nomes:
    print(a)




"""
nomes = []
nomesExtenso = ""
for i in range(5):
    nome = input(f"Digite o {i + 1}º nome: ")
    nomes.append(nome)

for a in nomes:
    nomesExtenso += f"{a} "
print(nomesExtenso)
"""