'''Crie um programa que leia a idade e o
sexo de várias pessoas. A cada
pessoa cadastrada, o programa
deverá perguntar se o usuário quer
ou não continuar. No final mostre:
A) Quantas pessoas têm mais de 18 anos
B) Quantos homens foram cadastrados.
C) Quantas mulheres têm menos de 20 anos'''

cont_idade_mais18 = cont_homens = cont_mulheres_menos20 = 0
while True:
    print('---' * 10)
    print('Cadastre uma pessoa')
    print('---' * 10)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('---' * 10)
    if idade > 18:
        cont_idade_mais18 += 1
    if sexo == 'M':
        cont_homens += 1
    if sexo == 'F' and idade < 20:
        cont_mulheres_menos20 += 1
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
print('---' * 10)
print(f'Total de pessoas com mais de 18 anos: {cont_idade_mais18}')
print(f'Homens cadastrados: {cont_homens}')
print(f'mulheres com menos de 20 anos: {cont_mulheres_menos20}')