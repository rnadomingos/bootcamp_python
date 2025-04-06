# 9. Extração de Subconjuntos de Dados
# Objetivo: Dada uma lista de números, extrair apenas aqueles que são pares.

list_number = [1,2,3,4,5,6,7,8,9,10]

# Modo curto
pares = [num for num in list_number if num % 2]

print(pares)

# Modo extenso
for i, par in enumerate(list_number):
  if par % 2 == 0:
    pares.append(par)

print(pares)