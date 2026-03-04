emails = ["henrique@gmail.com", "diretor@vilt.com",
          "contato@outlook.com", "suporte@vilt.com", "rh@yahoo.com"]
i = 0
while i < len(emails):
    lista = emails[i]
    separar = lista.split("@")

    if not lista.endswith("@vilt.com"):
        emails[i] = separar[0] + "@CONFIDENCIAL"

    i += 1
print(emails)