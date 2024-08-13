import emoji
from time import sleep
import pygame
p = str(input('Aperte ENTER para iniciar a contagem para o estouro dos fogos de artificios: '))
print('Contagem regressiva iniciada!')
pygame.init()
pygame.mixer.music.load('ex046.mp3')
pygame.mixer.music.play()
#input()
pygame.event.wait()
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize('Pow! Pow! Pow!:fireworks::sparkler::fireworks::sparkles::fireworks::sparkles:'))
sleep(15)
print('FIM! Obrigado por assistir até aqui, até mais, volte sempre')
