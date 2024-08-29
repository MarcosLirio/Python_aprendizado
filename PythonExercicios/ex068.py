'''Faça um programa que jogue par ou impar com o computador. O jogo
só será interrompido quando o jogador PERDER,mostrando o total
de vitórias consecutivas que ele conquistou no final do jogo'''

from random import randint
from time import sleep
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar?[P/I]')).strip().upper()[0]
    print(f'Voçê jogou {jogador} e o computador jogou {computador}. Total de {total} ', end='')
    print('Deu PAR' if total % 2 == 0 else 'Deu ÍMPAR!')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voçê VENCEU!')
            v += 1
        else:
            print('Voçê PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voçê VENCEU!')
            v += 1
        else:
            print('Voçê PERDEU!')
            break
    print('Vamos Jogar novamente...')
print(f'GAME OVER! Voçê venceu {v} vezes')