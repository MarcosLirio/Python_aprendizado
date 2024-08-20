'''Melhore o jogo do desafio 28 onde o computador vai
"pensar" em um número entre 0 e 10. Só que agora o
jogador vai tentar adivinhar até acertar, mostrando
no final quantos palpites foram necessários para
vencer.'''

from random import randint
from time import sleep
c = 0
computador = randint(0, 10); #Faz o computador gerar um número
print('-=-' * 20)
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que voçê consegue adivinhar qual foi?''')
print('-=-' * 20)
jogador = int(input('Qual é o seu palpite? '))
while jogador > 10:
    c += 1
    print('Opção inválida. Esse número é maior que 10. Tente novamente')
    jogador = int(input('Qual é o seu palpite? '))
'''
while jogador == ''
    print('Opção inválida. voçê não digitou nenhum número. Tente novamente')
    jogador = int(input('Qual é o seu palpite? '))
'''
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabéns! Voçê conseguiu me vencer')
else:
    if computador > jogador:
        print('Mais...')
    else:
        print('Menos')

    while jogador != computador:
        c += 1
        print('Voçê perdeu. Vamos tentar denovo!')
        print('-=-' * 20)
        jogador = int(input('Qual é o seu palpite? '))
        while jogador > 10:
            print('Opção inválida. Esse número é maior que 10. Tente novamente')
            jogador = int(input('Qual é o seu palpite? '))
        print('PROCESSANDO...')
        sleep(3)
        if computador > jogador:
            print('Mais...')
        elif jogador == computador:
            print('Voçê acertou o número que eu pensei. o Número é {}'.format(computador))
        else:
            print('Menos')
        if jogador == computador:
            print('Parabéns! Voçê conseguiu me vencer')
            print('Para me vencer voçê tentou {} vezes'.format(c + 1))

'''from random import randint
computador = randint(0, 10)
print('Sou seu computador.. Acabei de pensar em um número entre 0 e 10.')
print('Será que voçê consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not in acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
'''