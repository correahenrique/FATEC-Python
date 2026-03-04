arquivos = [
    {"titulo": "Contrato_2018", "ano": 2018},
    {"titulo": "Relatorio_2024", "ano": 2024},
    {"titulo": "Nota_Fiscal_2015", "ano": 2015},
    {"titulo": "Projeto_VILT_2026", "ano": 2026}
]
para_arquivo_morto = []

for arquivo in arquivos:
    nome = arquivo["titulo"]
    if arquivo["ano"] < 2020:
        para_arquivo_morto.append(nome)

print(para_arquivo_morto)