'''Faça um que tenha uma função             A)de 1 até 10, de 1 em 1
chamada contador(), que receba três         B)De 10 até 0, de 2 em 2
parâmetros: inicio, fim e passo. Seu        C)Uma contagem personalizada
programa tem que realizr três
contagens através da função criada:'''

from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} pulando de {p} em {p}')
    sleep(2.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont +=p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM ')

#Program principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-= ' * 20)
print(f'Agora é sua vez de personalizar a contagem!')
ini = int(input('Início:  '))
fim = int(input('Fim:     '))
pas = int(input('Passo:   '))
contador(ini, fim, pas)