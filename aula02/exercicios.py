import math
# ## Inteiros (int)
#   - Escreva um programa que soma dois números inteiros inseridos pelo usuário.

# valor1 = int(input("Informe um número: "))
# valor2 = int(input("Informe outro número: "))

# soma_valor = valor1 + valor2
# print(f"A soma dos valores é igual a {soma_valor}.")

#   - Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

# DIVISOR = 5
# valor1 = int(input("Informe um número: "))

# resultado = valor1 % DIVISOR

# print(f"O resto da divisao é {resultado}.")

#   - Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

# valor1 = int(input("Informe um número: "))
# valor2 = int(input("Informe outro número: "))

# multiplicacao_valor = valor1 * valor2
# print(f"Os valores multiplicados é igual a {multiplicacao_valor}.")

#   - Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

# valor1 = int(input("Informe um número: "))
# valor2 = int(input("Informe outro número: "))

# divisao_valor = valor1 / valor2
# print(f"A divisao do valor 1 pelo valor 2 é igual a {divisao_valor}.")

#   - Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# QUADRADO = 2
# valor = int(input("Informe um valor: "))

# quadrado_resultado = valor ** QUADRADO

# print(f"O quadrado de {valor} é {quadrado_resultado}.")


# ## Números de Ponto Flutuante (float)
#   - Escreva um programa que receba dois números flutuantes e realize sua adição.

# valor1 = float(input("Informe um valor com ponto flutuante: "))
# valor2 = float(input("Informe outro valor com ponto flutuante: "))

# soma_float = valor1 + valor2

# print(f"A soma dos valores é {soma_float}")

#   - Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

# MEDIA_COUNT = 2

# valor1 = float(input("Informe um valor com ponto flutuante: "))
# valor2 = float(input("Informe outro valor com ponto flutuante: "))

# valor_media = (valor1 + valor2) / MEDIA_COUNT

# print(f"A média dos valores é {valor_media}")

#   - Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

# print("### Exercício Potenciação ### \n")

# base = float(input("Informe um valor para base: "))
# expoente = int(input("Informe outro o expoente: "))

# potencia = base ** expoente

# print(f"A potenciação de {base} elevada a {expoente} é igual a {potencia}")

#   - Faça um programa que converta a temperatura de Celsius para Fahrenheit.

# print("### Conversor Celsius para Farenheit ### \n")

# graus = float(input("Informe a temperatura: "))

# fahrenheit = (graus * 1.8) + 32

# print(f"A temperatura convertida para Fahrenheit é de: {fahrenheit}°F")

#   - Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# print("### Calculadora de Circulo ### \n")

# raio = float(input("Informe um raio: "))

# circulo = math.pi * raio ** 2

# print(f"A área calculada do circulo é de: {circulo}")

# ## Strings (str)
#   - Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# print("### Upper Case ### \n")

# string = input("Informe o texto: ")
# upper = string.upper()

# print(f"{upper}")

#   - Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# print("### Lower Case ### \n")

# string = input("Informe o nome completo: ")
# low = string.lower()

# print(low)

#   - Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# print("### Remove espaços ###")
# frase = input("Insira uma frase: ")

# resultado = frase.strip()

# print(f"{frase}")
#   - Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# print("### Separa data ###")

# data_in = input("Informe uma data no formato: dd/mm/aaaa: ")

# data_split = data_in.split('/')

# dia = data_split[0]
# mes = data_split[1]
# ano = data_split[2]

# print(f"A data separada em lista é esta: {data_split} \n Ou podemos separar desta forma: Dia {dia}, do mês {mes}, do ano de {ano}.")
#   - Escreva um programa que concatene duas strings fornecidas pelo usuário.
# print("### Concatene 2 entradas de string ###")

# string1 = input("Informe uma string: ")
# string2 = input("Informe outra string: ")

# resultado = string1+string2

# print(f"As strings concatenadas, ficam desta forma: '{resultado}'.")

# ## Booleanos (bool)
#   - Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# print("### Resultado Booleanos AND")

# def string_to_bool(s):
#     return s.strip().lower() in [ 'true', 's', 'y', '1']

# bol1 = string_to_bool(input("Informe um booleano, no formato True ou False ou ainda 0 ou 1: "))
# bol2 = string_to_bool(input("Informe outro booleano, no formato True ou False ou ainda 0 ou : "))

# resultado_and = bol1 and bol2
# print("Resultado do AND lógico:", resultado_and)
#   - Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
print("### Resultado Booleanos OR")

def string_to_bool(s):
    return s.strip().lower() in [ 'true', 's', 'y', '1']

bol1 = string_to_bool(input("Informe um booleano, no formato True ou False ou ainda 0 ou 1: "))
bol2 = string_to_bool(input("Informe outro booleano, no formato True ou False ou ainda 0 ou : "))

resultado_and = bol1 or bol2
print("Resultado do OR lógico:", resultado_and)
#   - Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
#   - Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
#   - Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.