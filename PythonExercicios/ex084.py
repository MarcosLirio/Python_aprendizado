'''Faça um programa que leia o nome         A)Quantas pessoas foram cadastradas
e peso de várias pessoas,                   B)Uma listagem com as pessoas mais pesadas
guardando tudo em uma lista.                C)Uma listagem com as pessoas mais leves
No final mostre:'''

pessoas = list()
dados = list()
total_pessoas = 0
maior_peso = menor_peso = 0

while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    total_pessoas += 1
    if len(dados) == 0:
        maior_peso = menor_peso = pessoas[1]
    else:
        if pessoas[1] > maior_peso:
            maior_peso = pessoas[1]
        if pessoas[1] < menor_peso:
            menor_peso = pessoas[1]
    dados.append(pessoas[:])
    pessoas.clear()
    continua = str(input('Deseja continuar? [S/N] '))
    print('-=' * 30)
    if continua in 'nN':
        break
print(f'{total_pessoas} cadastros de pessoas foram realizados')
print(f'O maior peso foi de {maior_peso}Kg, que pertence à: ', end='')
for d in dados:
    if d[1] == maior_peso:
        print(f'{d[0]}')
print(f'O menor peso foi de {menor_peso}Kg, que pertence à: ', end='')
for d in dados:
    if d[1] == menor_peso:
        print(f'{d[0]}')