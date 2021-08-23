#  Algoritmo para calcular o valor a ser pago pelo período de estacionamento do automóvel 

def valida_minutos(minuto_entrada,minuto_saida):
    if minuto_entrada > 60 and minuto_saida > 60 or minuto_entrada < 0 and minuto_saida < 0:
        return False

hora_entrada,minuto_entrada = map (int,input('Usuário, informe a hora e minuto de entrada: ').split(':'))
hora_saída,minuto_saída = map (int,input('Usuário, informe a hora e minuto de saída: ').split(':'))

if valida_minutos(minuto_entrada, minuto_saída) == False:
    print('Minutos inválidos')
elif (hora_saída - hora_entrada) == 1 and (minuto_entrada == minuto_saída): # 1h
    print('Valor a pagar: R$ 4.00')
elif (hora_saída - hora_entrada) == 1 and (minuto_entrada != minuto_saída): #1h com minutos
    print('Valor a pagar: R$ 6.00')
elif (hora_saída - hora_entrada) == 2 and (minuto_entrada == minuto_saída): #2h
    print('Valor a pagar: R$ 6.00')
elif (hora_saída - hora_entrada) == 2 and (minuto_saída - minuto_entrada < 30): #2h com minutos
    print('Valor a pagar: R$ 6,50')
elif (hora_saída - hora_entrada) == 2 and (minuto_saída - minuto_entrada > 30):
    print('Valor a pagar: R$ 7,00')
elif (hora_saída - hora_entrada) > 2 and (minuto_entrada == minuto_saída):
    diferença_horas = hora_saída - hora_entrada
    valor_total = diferença_horas + 6
    print(f'Valor a pagar: R$  {valor_total}')
elif (hora_saída - hora_entrada) > 2 and (minuto_saída - minuto_entrada < 30):
    diferença_horas = hora_saída - hora_entrada
    valor_total = (diferença_horas + 6) + 0.50
    print(f'Valor a pagar: R$ {valor_total:.2f}')
elif (hora_saída - hora_entrada) > 2 and (minuto_saída - minuto_entrada > 30):
    diferença_horas = hora_saída - hora_entrada
    valor_total = (diferença_horas + 6) + 1.00
    print(f'Valor a pagar: R$ {valor_total:.2f}')
