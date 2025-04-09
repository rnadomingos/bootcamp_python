import time
# Processamento de Dados com Condição de Parada
# Objetivo: Processar itens de uma lista até encontrar um valor específico que indica a parada.

lista = [1,2,3,4,"parar",6,7]
#lista = [1,2,3,4,5,6,7]
i = 0

while i < len(lista):
  time.sleep(1)
  if lista[i] == "parar":
    print("Lista interrompida. Aplicação será cancelada")
    break
  print(f"item {i} - {lista[i]} de {len(lista)}")
  i+=1

print("Fim da Lista. Obrigado")