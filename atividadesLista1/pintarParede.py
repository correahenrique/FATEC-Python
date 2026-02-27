print("Vamos pintar uma parede?")
largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))
area = largura * altura
tinta = area / 2

print(f"Uma parede com {largura} de largura e {altura} de altura tem área de {area}"
      f"\nNo total, será necessário {tinta} litros de tinta")