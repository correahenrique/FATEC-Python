"""Crie uma lista com 5 notas de alunos, calcule a média e diga quais alunos ficaram acima da média."""

notas = [10, 5, 7, 9, 3]
media = 0

for i in notas:
    media += i
if (media/5) < 6:
    print(f"Aluno reprovado ({media/5})")
else:
    print(f"Aluno aprovado ({media/5})")