# 4) Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.

frase = 'Hoje eu criei um programa para somar a quantidade de caracteres em uma string'

strings = frase.replace(" ", "").lower()

ocorrencias = {}

for string in strings:
    if string in ocorrencias:
        ocorrencias[string]+=1
    else:
      ocorrencias[string] = 1

ocorr_sorted = dict(sorted(ocorrencias.items()))

print(ocorr_sorted)