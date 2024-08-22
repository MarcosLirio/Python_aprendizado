'''Faça um programa que leia um número
qualquer e mostre o seu fatorial.
Ex;
5! = 5x4x3x2x1 = 120'''

#De forma simplificada com a biblioteca math importando o módulo factorial
from math import factorial
'''n = int(input('Digite um número para calcular o seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))'''

#De forma tradicional agora
n = int(input('Digite um número para calcular o seu fatorial: '))
c = n
f = 1
print('Calculado {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))