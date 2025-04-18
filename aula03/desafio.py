# Refatorando o Código e forçar o usuário informar o dado corretamente

# Solicita ao usuário que digite seu nome

nome_valido = False
salario_valido = False
bonus_valido = False

while not nome_valido:
  try:
      nome = input("Digite seu nome: ")

      # Verifica se o nome está vazio
      if len(nome) == 0:
          raise ValueError("O nome não pode estar vazio.")
      # Verifica se há números no nome
      elif  nome.isdigit():
          raise ValueError("O nome não deve conter números.")
      elif nome.isspace():
          raise ValueError("O nome não deve conter apenas espacos.")
      else:
          print("Nome válido:", nome)
          nome_valido = True

  except ValueError as e:
      print(e)

# Solicita ao usuário que digite o valor do seu salário e converte para float
while not salario_valido:
  try:
      salario = float(input("Digite o valor do seu salário: "))
      if salario < 0:
          print("Por favor, digite um valor positivo para o salário.")
      else:
          print("Salario válido:", salario)
          salario_valido = True
  except ValueError:
      print("Entrada inválida para o salário. Por favor, digite um número.")


# Solicita ao usuário que digite o valor do bônus recebido e converte para float
while not bonus_valido:
  try:
      bonus = float(input("Digite o valor do bônus recebido: "))
      if bonus < 0:
          print("Por favor, digite um valor positivo para o bônus.")
      else:
          print("Bonus válido: ", bonus)
          bonus_valido = True
  except ValueError:
      print("Entrada inválida para o bônus. Por favor, digite um número.")

bonus_recebido = 1000 + salario * bonus  # Exemplo simples de KPI

# Imprime as informações para o usuário
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")