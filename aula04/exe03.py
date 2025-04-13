# Crie um dicionário para armazenar informações de um livro: 
# incluindo título, autor e ano de publicação. 
# Imprima cada informação.

print("Criando livros!!")

# livros = [{'titulo': 'clean code', 'autor': 'uncle bob', 'ano': '1998'}, {'titulo': 'o caso do 10 negrinhos', 'autor': 'agatha christie', 'ano': '1980'}]
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
  for k, v in lv.items():
    print(f"O {k} é: {v}")
  print("-------------------------")