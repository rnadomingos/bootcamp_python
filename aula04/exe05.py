# Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

lista = ["maçã", "banana", "cereja"]
compras = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
total_compras: float = 0

for l in lista:
  if l in compras:
    total_compras+=compras[l]

print("Total das Compras: ", total_compras)