'''Crie um programa que leia um número Real qualquer pelo teclado e
mostre na tela a sua porção inteira.
Ex: Digite um número: 6.127
O número 6.127 têm a parte inteira 6'''


from math import trunc;
num = float(input('Digite um número: '));
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, trunc(num)))



