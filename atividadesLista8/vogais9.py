"""Crie uma função que conte o número de vogais em uma palavra."""

def vogais(palavra):
    count = 0
    for i in palavra.lower():
        if i in 'aeiou':
            count += 1
    return count

texto = input("Digite uma palavra: ")
print(f"Vogais: {vogais(texto)}")