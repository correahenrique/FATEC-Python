"""Crie uma função chamada eh_primo(numero) que retorne True se o número for primo."""

def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

num = int(input("Digita o numero ai: "))
if eh_primo(num):
    print(f"O número {num} é primo!!!")
else:
    print(f"O número {num} não é primo!!!")