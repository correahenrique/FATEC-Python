"""Controle de Votação: Faça um programa que permita cadastrar votos para 3
candidatos. Exibe contagem ao final quando for digitado "fim"."""

candidato1 = 0
candidato2 = 0
candidato3 = 0
print("temos 3 candidatos.\nOs números deles são 1, 2 e 3")
while True:
    votos = input("Seu voto ('fim' para sair): ")
    if votos == "fim":
        print("Fim do programa")
        print(f"Terminado, os votos ficaram: {candidato1}, {candidato2} e {candidato3}")
        break
    else:
        voto = int(votos)
        if voto == 1:
            candidato1 += 1
        elif voto == 2:
            candidato2 += 1
        elif voto == 3:
            candidato3 += 1
        else:
            print("Inválido!, tente novamente ou digite fim")