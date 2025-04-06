# Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem medições de temperatura. Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'

temperatura = float(input("Informe a temperatura: "))

if temperatura < 18:
    print("Temperatura Baixa")
elif (temperatura >= 18 and temperatura <= 26):
    print("Temperatura Normal")
else:
    print("Temperatura alta")