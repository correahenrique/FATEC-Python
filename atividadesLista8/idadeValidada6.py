"""Crie uma função valida_idade(idade) que retorne se a pessoa é maior de idade."""

def valida_idade(idade):
    if idade > 17:
        return True
    return False

idade = int(input("Digite sua idade: "))
if valida_idade(idade):
    print(f"{idade} é maior de idade")
else:
    print(f"{idade} é menor de idade")