processos = [
    {"arquivo": "nota_fiscal.pdf", "tempo": 15},
    {"arquivo": "contrato_venda.docx", "tempo": 40},
    {"arquivo": "foto_perfil.png", "tempo": 5},
    {"arquivo": "relatorio_anual.pdf", "tempo": 60},
    {"arquivo": "memo_interno.txt", "tempo": 10}
]
soma = 0
rapidos = []
lentos = []

for processo in processos:
    soma += processo["tempo"]
    media = soma / len(processos)
    nome = processo["arquivo"]
    if processo["tempo"] > media:
        lentos.append(nome)
    else:
        rapidos.append(nome)

print(f"A média fica: {media}")
print(f"Os rápidos são: {rapidos}")
print(f"Os lentos são: {lentos}")