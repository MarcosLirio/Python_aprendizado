'''Crie um programa que leia vários números inteiros pelo teclado. O
programa só vai para quando o usuário digitar 999, que é a
condição de parada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles(desconsiderando o flag)'''

n = s = cont = 0
while True:
    n = int(input('Digite um número(999 para parar): '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'Voçê digitou {cont} numeros, a soma entre os eles é igual à {s}')