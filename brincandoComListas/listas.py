emails = ["henrique@gmail.com", "diretor@hotmail.com",
          "contato@outlook.com", "suporte@hotmail.com", "rh@yahoo.com"]
i = 0
while i < len(emails):
    lista = emails[i]
    separar = lista.split("@")

    if not lista.endswith("@hotmail.com"):
        emails[i] = separar[0] + "@CONFIDENCIAL"

    i += 1

print(emails)
