'''Desenvolva um programa que pergunte a distância de uma viagem
em KM. Calcule o preço da passagem, cobrando R$0,50 por KM para
viagens de até 200KM e R$0,45 para viagens mais longas.'''

from time import sleep
distancia = float(input('Digite a distância em KM da sua viagem: '))
print('processando...')
sleep(3)
if distancia <= 200:
    valor = distancia * 0.50
    print('O valor da sua viagem ficará R${:.2f}'.format(valor))
else:
    valor = distancia * 0.45
    print('O valora da sua viagem ficará R${:.2f}'.format(valor))