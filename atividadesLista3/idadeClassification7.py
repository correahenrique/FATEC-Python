idade = int(input("Digite sua idade: "))

if idade < 18:
    print(f"Você é uma criança {idade}")
elif idade < 24:
    print(f"Você é um adolescente {idade}")
elif idade < 60:
    print(f"Você é um adulto {idade}")
else:
    print(f"Você é um idoso {idade}")