conta = input("Sua conta está ativa? (SIM ou NÃO) ")
saldo = input("Seu saldo é suficiente? (SIM ou NÃO) ")

if conta == "SIM":
    if saldo == "SIM":
        print("Tudo certo")
    else:
        print("Saldo insuficiente")
else:
    print("Crie uma conta antes")