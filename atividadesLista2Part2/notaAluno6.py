nota = int(input("Digite a nota do aluno: (0 a 100) "))

if nota < 0 or nota > 100:
    print(f"Nota inválida ({nota})")
elif nota < 60:
    print(f"Sua nota foi F ({nota})")
elif nota < 70:
    print(f"Sua nota foi D ({nota})")
elif nota < 80:
    print(f"Sua nota foi C ({nota})")
elif nota < 90:
    print(f"Sua nota foi B ({nota})")
else:
    print(f"Sua nota foi A ({nota})")