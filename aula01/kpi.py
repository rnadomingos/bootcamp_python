# 1. O programa deve começar solicitando ao usuário que insira seu nome.
# 2. Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
# 3. Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
# 4. O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
# 5. Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".

CONST_BONUS = 1000

# 1. O programa deve começar solicitando ao usuário que insira seu nome.
nome = input("Informe seu nome: ")

# 2. Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. 
vlr_salario = float(input("Qual é o valor de seu salário? "))

# 3. Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário
perc_bonus = float(input("Qual é o percentual de bonus recebido? "))

# 4. O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
bonus = CONST_BONUS + vlr_salario * perc_bonus

# 5. O programa deve imprimir uma mensagem
print("Olá "+ str(nome) + ", o seu valor bônus foi de "+ str(bonus)) 