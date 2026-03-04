dados = ["Henrique:DEV", "Marina:RH", "Carlos:SUP", "Ana:DEV", "Lucas:SUP", "Mariana:RH"]
time_dev = []
time_sup = []
i = 0

for dado in dados:
    separar = dado.split(":")

    if separar[1] == "DEV":
        time_dev.append(separar[0])
    elif separar[1] == "SUP":
        time_sup.append(separar[0])
    i += 1

print(f"Esses são devs: {time_dev}")

print(f"Esses são suporte: {time_sup}")
