# Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar transações suspeitas. 
# Uma transação é considerada suspeita se o valor for superior a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como transacao = {'valor': 12000, 'hora': 20}, verifique se ela é suspeita.

VLR_LIMITE = 10000
HORARIO_COMERCIAL = { 'inicial': 9, 'final': 18 }

transacao = {'valor': 5000, 'hora': 20}

if transacao['valor'] > VLR_LIMITE or transacao['hora'] < HORARIO_COMERCIAL['inicial'] or transacao['hora'] > HORARIO_COMERCIAL['final']:
    print("Transacao suspeita")
else:
    print("transacao dentro da normalidade")
