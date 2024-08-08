'''Crie um programa que leia o nome de uma pessoa e diga se ela têm
"Silva" no nome.'''

nome = str(input('Digite o seu nome completo: ')).strip()
print('Seu nome têm silva? {}'.format('silva' in nome.lower()))