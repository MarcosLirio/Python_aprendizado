'''Crie um programa que mostre a tabuada de vários números, um de
cada vez, para cada valor digitado pelo usuário. O programa será
interrompido quando o número solicitado for negativo'''
print('-' * 40)
while True:
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 40)
    multiplo = 1
    if tabuada < 0:
        break
    while multiplo <= 10:
        resultado = tabuada * multiplo
        print(f'{tabuada} x {multiplo} = {resultado}')
        multiplo += 1
    print('-' * 40)
print('Programa de tabuada encerrado. Volte sempe!')