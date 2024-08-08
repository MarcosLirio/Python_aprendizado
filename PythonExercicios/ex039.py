'''Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que
passou do prazo'''

from datetime import date
ano_atual = date.today().year
nascimento = int(input('Digite o seu ano de nascimento: '))
idade = ano_atual - nascimento

if idade < 18:
    falta = 18 - idade
    print('Voçê têm {} anos, faltam {} anos para voçê se alistar'.format(idade, falta))
elif idade > 18:
    passou = idade - 18
    print('Voçê já têm {} anos, seu alistamento deveria ser feito á {} anos'.format(idade, passou))
else:
    print('Voçê já está com {} anos, está na hora do seu alistamento!'.format(idade))
