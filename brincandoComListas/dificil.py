faturas = [
    {"servico": "Consultoria ECM", "valor": 1500},
    {"servico": "Suporte Técnico", "valor": 500},
    {"servico": "Migração de Dados", "valor": 3200},
    {"servico": "Treinamento IA", "valor": 2000}
]
valor = 0
maiorValor = 0
servico_mais_caro = ""

for fatura in faturas:
    nome = fatura["servico"]
    valor = valor + fatura["valor"]
    if fatura["valor"] > maiorValor:
        maiorValor = fatura["valor"]
        servico_mais_caro = nome

print(valor)
print(servico_mais_caro)