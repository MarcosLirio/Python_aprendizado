'''Faça um programa que conclua a soma
entre todos os números impares que são
múltiplus de três e que se encontram no
intervalo de 1 até 500'''

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
