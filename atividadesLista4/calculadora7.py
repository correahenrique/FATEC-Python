"""O usuário escolhe uma operação matemática (+, -, *, /) e insere dois números. O programa exibe o resultado."""

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

op = input("Digite a operação que você deseja realizar: (+, -, *, /)   ")

match op:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        print(num1 / num2)
    case _:
        print("Você precisa escolher um caminho válido!!!")