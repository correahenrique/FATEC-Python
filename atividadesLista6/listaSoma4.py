"""Some todos os elementos de uma lista de inteiros digitados pelo usuário."""

numeros = []
soma = 0

while True:
    numero = input("Digite um número inteiro (digite 'sair' para parar de digitar os números):")
    if numero.lower() != "sair":
        numero = int(numero)
        numeros.append(numero)
    else:
        break
for i in numeros:
    soma += i
print(soma)