# Crie um dicionário para armazenar informações de um livro: 
# incluindo título, autor e ano de publicação. 
# Imprima cada informação.

print("Criando livros!!")

livros: list = []
continua = 'y'

while continua == 'y':
  titulo: str = str(input("Qual é o título do livro? \n"))
  autor: str = str(input("Quem é o autor do livro? \n"))
  ano: str = str(input("Qual é o ano da publicação? \n"))

  livros.append({
    "titulo": titulo,
    "autor": autor,
    "ano": ano
  })
  continua = (input("Deseja continuar a inserir livros? (y/n) \n"))

print("Lista impressa: ",livros)

for lv in livros:
  for l in lv:
    print(f"O {l} é: {lv[l]}")
  print("-------------------------")