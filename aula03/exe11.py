# 11. Leitura de Dados até Flag
# Objetivo: Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

dados = []

entrada = ''

while entrada.lower() != 'sair':
  entrada = input("Digite uma entrada ou 'sair', para terminar: ")
  dados.append(entrada)

print("Dados de entrada: ",dados)