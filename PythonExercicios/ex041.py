'''A confederação Nacional de natação precisa de um programa que
leia o ano de nascimento de um atleta e mostre sua categoria, de
acordo com a idade:
-Até 9 anos: MIRIM              -Até 19 anos: JUNIOR
-Até 14 anos: INFANTIL          -Até 25 anos: SÊNIOR
                                -Acima: Master'''

from datetime import date
ano_atual = date.today().year
nascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = ano_atual - nascimento

if idade <= 9:
    print('O Atleta têm {} anos \nClassificação: MIRIM!'.format(idade))
elif idade > 9 and idade <= 14:
    print('O Atleta têm {} anos \nClassificação: INFANTIL!'.format(idade))
elif idade > 14 and idade <= 19:
    print('O Atleta têm {} anos \nClassificação: JUNIOR!'.format(idade))
elif idade > 19 and idade <= 25:
    print('O Atleta têm {} anos \nClassificação: SÊNIOR!'.format(idade))
else:
    print('O Atleta têm {} anos \nClassificação: MASTER!'.format(idade))