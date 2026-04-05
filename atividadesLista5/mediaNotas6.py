notas = int(input("Digite a nota (0 a 10): "))
contador = 0
media = 0
n = 0
while notas >= 0 and notas <= 10:
    contador += 1
    n += notas
    media = n / contador
    print(f"Até agora, a média está: {media}")
    notas = int(input("Digite a nota (0 a 10): "))
print(f"A media do aluno foi {media}")