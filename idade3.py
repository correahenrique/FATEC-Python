idade = int(input("Qual é a sua idade? "))

if (idade < 0):
    print(f"Ta de brincadeira? Você tem {idade} anos??!")
elif (idade < 13):
    print(f"Você é uma criança!")
elif (idade < 18):
    print(f"Você é um adolescente!")
elif (idade < 65):
    print(f"Você é um adulto!")
else:
    print(f"Você é um idoso!")