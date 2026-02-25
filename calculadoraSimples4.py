operacao = input("Digite qual operação você deseja fazer (+,-, * ou /): ")
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if (operacao == "+"):
    print(f"SOMA, o resultado fica: {numero1 + numero2}")
elif (operacao == "-"):
    print(f"SUBTRAÇÃO, o resultado fica: {numero1 / numero2}")
elif (operacao == "*"):
    print(f"MULTIPLICAÇÃO, o resultado fica: {numero1 * numero2}")
elif (operacao == "/"):
    print(f"DIVISÃO, o resultado fica: {numero1 / numero2}")
else:
    print(f"Poxa cara, tinha que ter digitado um dos símbolos")