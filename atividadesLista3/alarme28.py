alguem = input("Tem alguêm em casa? (S ou N) ")
porta = input("Tem a porta está aberta? (S ou N) ")

if alguem == "N" or porta == "S":
    print("Alarme disparado!!!")
else:
    print("Alarme desligado")