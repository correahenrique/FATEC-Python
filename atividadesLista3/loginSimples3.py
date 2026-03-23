"""O programa deve pedir ao usuário que informe seu nome de usuário e, com base nisso, conceder um nível de acesso:

Admin → Acesso total

Professor → Acesso ao ambiente acadêmico

Aluno → Acesso ao ambiente de estudos"""

acesso = input("Digite o seu nível de acesso (admin, prof ou aluno): ")

match acesso:
    case "admin":
        print("Você tem todo o acesso!")
    case "prof":
        print("Você tem acesso ao ambiente acadêmico!")
    case "aluno":
        print("Você só tem acesso ao ambiente de estudo!")
    case _:
        print("Você digitou errado!")