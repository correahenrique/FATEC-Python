print("Vamos falar sobre preços...")
km = float(input("Quantos km você andou?"))
dias = int(input("Quantos dias você ficou com ele?"))
diaria = dias * 90
kmtragem = km * 1.20
valor = diaria + kmtragem

print(f"Cara, ficou meio caro, olha aí: {valor}"
      f"\nÉ que ficou {diaria} reais pelos dias e mais {kmtragem:.2f} pela quilometragem...")