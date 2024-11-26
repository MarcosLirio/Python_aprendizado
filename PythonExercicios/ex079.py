'''Crie um programa onde o usuário possa digitar vários valores
numéricos e cadastre-os em uma lista. Caso o número já exista
lá dentro, ele não será adicionado. No final, serão exibidos
todos os valores únicos digitados, em ordem crescente.'''
lista = []
while True:
    numero = int(input('Digite um número:  '))
    if numero not in lista:
        lista.append(numero)
        print('Valor adicionado com sucesso!...')
    else:
        print('Valor duplicado! Não vou adicionar')
    continua = ' '
    while continua not in 'sSnN':
        continua = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continua in 'nN':
        break
print('-=' * 30)
print(f'Voçê digitou os valores: {sorted(lista)}')