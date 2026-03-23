cadastrado = input("Você está cadastrado? (SIM ou NÃO) ")
atraso = input("Você tem algum atraso? (SIM ou NÃO) ")

if cadastrado == "SIM":
    if atraso == "NÃO":
        print(f"Beleza, ta liberado")
    else:
        print(f"Não pô, resolve o atraso aí")
else:
    print(f"Faz teu cadastro antes")