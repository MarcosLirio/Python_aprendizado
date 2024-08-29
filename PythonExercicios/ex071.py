'''Crie um programa que simule o funcionamento      Obs: Colnsidere
de um caixa eletrônico. No início, pergunte ao      que o caixa
usuário qual será o valor a ser sacado(número       possui cédulas
inteiro) e o programa vai informar quantas          de R$50, R$20
cédulas de cada valor serão entregues               R$10 e R$1.'''

print('=' * 30)
print('{:^30}'.format('Banco CEV'))
print('=' * 30)
valor = int(input('Que valor voçê quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} de cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao CEV, tenha um Bom dia!')