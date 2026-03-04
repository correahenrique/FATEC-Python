listas = ["Henrique Silva", "Debora Oliveira", "Joao Paulo Ramos"]
logins = [nome.lower().replace(" ", ".") for nome in listas]

print(listas)
print(logins)