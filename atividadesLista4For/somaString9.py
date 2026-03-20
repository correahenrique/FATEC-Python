num = input("Digite um número: ")
soma = 0

for i in num:
    if i.isdigit():
        soma = soma + int(i)
print(f"O resultado fica: {soma}")