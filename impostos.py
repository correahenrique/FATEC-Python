print("Vamos falar de impostos...")
fabrica = float(input("Qual o custo de fábrica desse carro?"))
distribuidor = fabrica * 0.28
imposto = fabrica * 0.45
valor = fabrica + distribuidor + imposto

print(f"O valor do carro era {fabrica} na fábrica, no final ficou {valor} com os impostos e distribuidores")