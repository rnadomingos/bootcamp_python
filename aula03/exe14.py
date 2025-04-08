import time
# 14. Tentativas de Conexão
# Objetivo: Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.
print("  ### CONEXAO ###  ")

LIMITE_TENTATIVA = 3

count = 1
start = input("Deseja iniciar a conexão agora? Y/N: ")

while count <= LIMITE_TENTATIVA:

    while start != 'Y':
      start = input("Deseja iniciar a conexão agora? Y/N: ")

    print(f"Tentativa nro {count}")
    time.sleep(1)
    count+=1
    
    if count == 5:
      print("Conexão bem-sucedida")
      break
else:
   print(f"Conexão encerrada por timeout! Tente novamente mais tarde!")
