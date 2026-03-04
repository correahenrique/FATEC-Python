documentos = [
    {"titulo": "Manual de Integração", "formato": "pdf", "acesso": 1},
    {"titulo": "Folha de Pagamento", "formato": "xlsx", "acesso": 5},
    {"titulo": "Planejamento 2026", "formato": "docx", "acesso": 4},
    {"titulo": "Lista de Ramais", "formato": "txt", "acesso": 2},
    {"titulo": "Contrato Social", "formato": "pdf", "acesso": 3}
]
conta = 0
publicos = []
restritos = []

for documento in documentos:
    nome = documento["titulo"]
    if documento["acesso"] > 2:
        conta += 1
        restritos.append(nome)
    else:
        publicos.append(nome)

print(f"A conta fica: {conta}")
print(f"Os públicos são: {publicos}")
print(f"Os restritos são: {restritos}")