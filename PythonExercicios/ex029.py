'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem
dizendo que ele foi multado.
A multa vai custar R$7,00 por cada KM acima do limite.'''

velocidade = float(input('digite a Velocidade atual do veículo: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('MULTADO! Voçê excedeu o limite de 80KM/h nesta via, e irá pagar uma multa de R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia e continue dirigindo com prudência!')
