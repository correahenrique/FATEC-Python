"""Crie uma função calcular_desconto(valor, percentual=10) que aplique um desconto percentual ao valor."""

def calcular_desconto(valor, percentual=10):
    desconto = (valor / 100) * percentual
    final = valor - desconto
    return desconto, final

valor = float(input("Digite o valor: "))
descontado, pago = calcular_desconto(valor)
print(f"Desconto: {descontado}")
print(f"Pago: {pago}")