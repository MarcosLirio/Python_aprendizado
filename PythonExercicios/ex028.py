from random import randint;
from time import sleep;
computador = randint(0, 5); #Faz o computador gerar um número
print('-=-' * 20);
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...');
print('-=-' * 20);
jogador = int(input('Em que núemero eu pensei? '));
print('PROCESSANDO...');
sleep(3);
if jogador == computador:
    print('Parabéns! Voçê conseguiu me vencer');
else:
    print('Voçê perdeu, eu pensei no número {} e não no número {}'.format(computador, jogador));