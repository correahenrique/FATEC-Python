"""O computador escolhe um número aleatório de 1 a 10,
e o usuário tem 3 tentativas para adivinhar. Dê dicas se o número é maior ou menor."""

from random import randint

n = randint(1, 100)
print(n)

for i in range(1, 3):
    c = int(input("Tente adivinhar: "))
    if c == n:
        print("Acertou!!!")
        break
    elif i == 2:
        print("Ultima chance...")
        c = int(input("Tente adivinhar: "))
        if c == n:
            print("Acertou!!!")
            break
        else:
            print("Errou!!! O número era: ", n)