'''Faça um programa que leia o comprimento do
cateto oposto e do cateto adjascente de um
triângulo, calcule e mostre o comprimento
da hipotenusa'''

from math import hypot
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjascente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))