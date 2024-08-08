'''Crie um programa que faça o
computador jogar JOKENPO
com voçê'''
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opçÕes: 
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
if computador == 0: #Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR ganhou!')
    elif jogador == 2:
        print('COMPUTADOR ganhou!')
    else:
        print('Opção inválida!')
elif computador == 1: #Computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR ganhou!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR ganhou!')
    else:
        print('Opção Inválida!')
elif computador == 2: #Computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR ganhou!')
    elif jogador == 1:
        print('COMPUTADOR ganhou!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Opção Inválida!')
