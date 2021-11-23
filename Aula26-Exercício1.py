#  Algoritmo que calcule e apresente quanto deve ser pago por um produto

def valida_codigo_pagamento(codigo):
    if not codigo in [1,2,3,4]:
        return False
def calcula_preço_codigo1(preço_etiqueta):
    valor_total = preço_etiqueta - (preço_etiqueta * 0.10)
    return valor_total
def calcula_preço_codigo2(preço_etiqueta):
    valor_total = preço_etiqueta - (preço_etiqueta * 0.05)
    return valor_total
def calcula_preço_codigo3(preço_etiqueta):
    valor_total = preço_etiqueta / 2
    return valor_total
def calcula_preço_codigo4(preço_etiqueta):
    valor_total = (preço_etiqueta + (preço_etiqueta * 0.10)) / 3
    return valor_total

preço_etiqueta =  float(input('Usuário, informe o preço de etiqueta do produto: '))
codigo_pagamento = int(input('Usuário, informe o código da condição de pagamento: '))

if valida_codigo_pagamento(codigo_pagamento) == False:
    print('Código de pagamento inválido!')
elif codigo_pagamento == 1:
    print(f'Usuário, você selecionou à vista em dinheiro ou cheque, com 10% de desconto\nO total da sua compra é: R$ {calcula_preço_codigo1(preço_etiqueta):.2f}')
elif codigo_pagamento == 2:
    print(f'Usuário, você selecionou à vista com cartão de crédito, com 5% de desconto\nO total da sua compra é: R$ {calcula_preço_codigo2(preço_etiqueta):.2f}')
elif codigo_pagamento == 3:
    print(f'Usuário, você selelecionou em 2 vezes, preço normal de etiqueta sem juros\nO total da sua compra é: R$ {preço_etiqueta:.2f}\nO pagamento será efetuado com 2 parcelas de R$ {calcula_preço_codigo3(preço_etiqueta):.2f}')
elif codigo_pagamento == 4:
    print(f'Usuário, você selelecionou em 3 vezes, preço de etiqueta com acréscimo de 10%\nO total da sua compra é: R$ {preço_etiqueta:.2f}\nO pagamento será efetuado com 3 parcelas de R$ {calcula_preço_codigo4(preço_etiqueta):.2f}')



