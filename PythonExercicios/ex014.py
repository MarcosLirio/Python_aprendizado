'''Escreva um programa que leia a temperatura
digitada em ºC e converta para ºF'''

c = float(input('Informe a temperatura em ºC: '))
f = c * 1.8 + 32
print('A temperatura de {}ºC corresponde a {}ºF'.format(c, f))