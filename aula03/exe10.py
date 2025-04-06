# 10. Agregação de Dados por Categoria
# Objetivo: Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]

soma_categoria = {}

for venda in vendas:
    categoria = venda["categoria"]
    valor = venda["valor"]
    if categoria in soma_categoria:
        soma_categoria[categoria]+=valor
    else:
      soma_categoria[categoria]=valor

print(soma_categoria)