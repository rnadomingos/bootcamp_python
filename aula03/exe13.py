# 13. Consumo de API Simulado
# Objetivo: Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

pagina_atual = 1
total_paginas = 10

while pagina_atual < total_paginas:
    print(f"Processando página {pagina_atual} de {total_paginas} páginas")
    pagina_atual+=1

print("Fim da paginação!")