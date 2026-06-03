"""Crie uma função que receba o nome de um aluno e exiba uma mensagem de boas-vindas."""

def bemVindo(nome):
    print(f"Bem vindo {nome}!")

nome = input("Digite o seu nome: ")
bemVindo(nome)