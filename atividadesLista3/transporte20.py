distancia = int(input("Digite a distância da residência (em km): "))
frequencia = int(input("Digite a frequência do aluno (0 a 100): "))

if distancia > 2:
    if frequencia >= 80:
        print("Tem direito ao transporte escolar!!!")
    else:
        print("Não tem direito ao transporte escolar (frequência baixa)!!!")
else:
    print("Não tem direito ao transporte escolar (muito perto)!!!")