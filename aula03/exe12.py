# 12. Validação de Entrada
# Objetivo: Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

entrada = int(input(f"Digite um valor entre 1 e 10: "))

while entrada < 1 or entrada > 10:
    print("Entrada inválida!!")
    entrada = int(input(f"Por favor digite um valor entre 1 e 10: "))

print("Correto!! Valor informado é: ", entrada)
