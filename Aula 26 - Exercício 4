# Lógica computacional dos caixas eletrônicos

# Resolução 1, com cédulas de 1 real
valor_inicial = int(input())

cedulas_100 = valor_inicial // 100
valor = valor_inicial - cedulas_100 * 100

cedulas_50 = valor // 50
valor = valor - cedulas_50 * 50

cedulas_20 = valor // 20
valor = valor - cedulas_20 * 20

cedulas_10 = valor // 10
valor = valor - cedulas_10 * 10

cedulas_5 = valor // 5
valor = valor - cedulas_5 * 5

cedulas_2 = valor // 2
valor = valor - cedulas_2 * 2

cedulas_1 = valor // 1
valor = valor - cedulas_1 * 1

print(valor_inicial)
print(round(cedulas_100) ,'nota(s) de R$ 100,00')
print(round(cedulas_50) ,'nota(s) de R$ 50,00')
print(round(cedulas_20) ,'nota(s) de R$ 20,00')
print(round(cedulas_10) ,'nota(s) de R$ 10,00')
print(round(cedulas_5) ,'nota(s) de R$ 5,00')
print(round(cedulas_2) ,'nota(s) de R$ 2,00')
print(round(cedulas_1) ,'nota(s) de R$ 1,00')

# Resolução 2, sem cédulas de 1 real

def calcula_milhar(numero):
    unidade = numero % 10
    cnt1 = (numero- unidade) / 10
    dezena = cnt1 % 10
    cnt2 = (cnt1 - dezena) / 10
    centena = cnt2 % 10
    cnt3 = (cnt2 - centena) / 10
    milhar = cnt3 % 10
    return milhar
def calcula_centena(numero):
    unidade = numero % 10
    cnt1 = (numero - unidade) / 10
    dezena = cnt1 % 10
    cnt2 = (cnt1 - dezena) / 10
    centena = cnt2 % 10
    cnt3 = (cnt2 - centena) / 10
    milhar = cnt3 % 10
    return centena
def calcula_dezena(numero):
    unidade = numero % 10
    cnt1 = (numero - unidade) / 10
    dezena = cnt1 % 10
    cnt2 = (cnt1 - dezena) / 10
    centena = cnt2 % 10
    cnt3 = (cnt2 - centena) / 10
    milhar = cnt3 % 10
    return dezena
def calcula_unidade(numero):
    unidade = numero % 10
    cnt1 = (numero - unidade) / 10
    dezena = cnt1 % 10
    cnt2 = (cnt1 - dezena) / 10
    centena = cnt2 % 10
    cnt3 = (cnt2 - centena) / 10
    milhar = cnt3 % 10
    return unidade

valor = int(input('Usuário, informe o valor em reais que deseja sacar: R$ '))
print('Usuário, os caixas eletrônicos do banco possuem cédulas de R$ 2, R$ 5, R$ 10, R$ 20, R$ 50 e R$ 100 reais:')

milhar = calcula_milhar(valor)
centena = calcula_centena(valor)
dezena = calcula_dezena(valor)
unidade = calcula_unidade(valor)

if milhar > 0 :
    valor_mil = calcula_milhar(valor) * 1000
    cedulas = valor_mil / 100
    print(round(cedulas) , 'cedulas de R$ 100 reais')
else:
    print()
if centena > 0:
    valor_cem = calcula_centena(valor) * 100
    cedulas = valor_cem / 100
    print(round(cedulas) , 'cedulas de R$ 100 reais')
else:
    print()
if dezena > 0:
    valor_dezena = calcula_dezena(valor) * 10
    if valor_dezena == 10:
        print('1 cedulas de R$ 10 reais')
    elif valor_dezena == 20:
        print('2 cedulas de R$ 20 reais')
    elif valor_dezena == 30:
        print('1 cedulas de R$ 20 reais e 1 cedulas de R$ 10 reais')
    elif valor_dezena == 40:
        print('2 cedulas de R$ 20 reais')
    elif valor_dezena == 50:
        print('1 cedulas de R$ 50 reais')
    elif valor_dezena == 60:
        print('1 cedulas de R$ 50 reais e 1 cedulas de R$ 10 reais')
    elif valor_dezena == 70:
        print('1 cedulas de R$ 50 reais e 1 cedulas de R$ 20 reais')
    elif valor_dezena == 80:
        print('1 cedulas de R$ 50 reais, 1 cedulas de R$ 20 reais e 1 cedulas de R$ 10 reais')
    elif valor_dezena == 90:
        print('1 cedulas de R$ 50 reais e 2 cedulas de R$ 20 reais')
else:
    print()
if unidade > 0:
    valor_unidade = calcula_unidade(valor)
    if valor_unidade in [2,4,6,8]:
        cedulas = valor_unidade / 2
        print(f'{round(cedulas)} cedulas de R$ 2 reais')
    elif valor_unidade in [5,7,9]:
        cedulas_5_calculo = valor_unidade / 5
        cedulas_5 = round(cedulas_5_calculo - 0.5)
        cedulas_2 = round((valor_unidade - 5) / 2)
        print(cedulas_5 , 'cedulas de R$ 5 reais e', cedulas_2 , 'cedulas de R$ 2 reais')
    elif not(valor_unidade in [2,4,5,6,7,8,9]):
        print('O valor solicitado deve ser múltiplo de R$ 2, R$ 5, R$ 10, R$ 20, R$ 50 ou R$ 100 reais!')
else:
    print()


