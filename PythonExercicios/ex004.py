'''Faça um programa que leia algo pelo teclado e mostre na tela o seu
tipo primitivo e todas as informações possíveis sobre ela'''

digite = input('Digite algo: ')
print('O tipo primitivo desse valor é: ',type(digite))
print('Só tem espaço? ',digite.isspace())
print('É um número?',digite.isnumeric())
print('É alfabético? ',digite.isalpha())
print('É alfanumérico? ',digite.isalnum())
print('Está em maiúsculas? ',digite.isupper())
print('Está em minúsculas? ',digite.islower())
print('Está capitalizada? ',digite.istitle())

