'''Crie um programa que leia varios números inteiros pelo teclado.
O programa só vai para quando o usuário digitar o valor 999, que
é a condição de parada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles(desconsiderando o flag).'''
numero = cont = soma = 0
numero = int(input('Digite um número[999 para parar]: '))
while numero != 999:
    soma += numero
    cont += 1
    numero = int(input('Digite um número[999 para parar]: '))
print('Voçê digitou {} números e a soma entre eles é {}'.format(cont, soma))