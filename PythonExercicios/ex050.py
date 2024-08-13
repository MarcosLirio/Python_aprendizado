'''Desenvolva um programa que leia seis
números inteiros e mostre a soma
apenas daqueles que forem pares. Se
o valor digitado for impar, desconsidere-o'''

soma = 0
for c in range(1, 7):
    c = int(input('Digite o {}º valor: '.format(c)))
    if c % 2 == 0:
        soma = soma + c
print('A soma de todos os números pares digitado é {}'.format(soma))
