'''Escreva um programa que faça o computador "pensa" em um
número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador. O programa deverá
escrever na tela se o usuário venceu ou perdeu'''

from random import randint
from time import sleep
computador = randint(0, 5); #Faz o computador gerar um número
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que núemero eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabéns! Voçê conseguiu me vencer')
else:
    print('Voçê perdeu, eu pensei no número {} e não no número {}'.format(computador, jogador))