# Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha fornecido um email válido. 
# Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.

idade = 64
email = 'renan@mail.com'

if idade >= 18 and idade <= 65:
    if "@" not in email or "." not in email:
      print("Dados inválidos")
    else:
      print("Dados válidos")
else:
  print("Dados inválidos")