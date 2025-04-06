# 6. Contagem de Palavras em Textos
# Objetivo: Dado um texto, contar quantas vezes cada palavra única aparece nele.

texto = "hoje estou fazendo o exercicio exercicio tambem hoje"

palavras = texto.split()

contador_palavras = {}

for palavra in palavras:
    if palavra in contador_palavras:
        contador_palavras[palavra]+=1
    else:
        contador_palavras[palavra] = 1

print("Contador de palavras: \n", contador_palavras)        