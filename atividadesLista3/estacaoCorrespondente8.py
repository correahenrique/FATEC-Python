mes = int(input("Qual é o mês atual? "))

if mes < 1 or mes > 12:
    print(f"Mês {mes} é inválido!!! Tem que ser de 1 a 12!!!")
else:
    if mes > 2 and mes < 6:
        print(f"Mês {mes} é outono!!!")
    elif mes > 5 and mes < 9:
        print(f"Mês {mes} é inverno!!!")
    elif mes > 8 and mes < 12:
        print(f"Mês {mes} é primavera!!!")
    else:
        print(f"Mês {mes} é verão!!!")