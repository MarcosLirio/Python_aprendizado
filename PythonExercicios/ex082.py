'''Crie um programa que vai ler vários números e colocar em uma
lista. Depois disso, crie duas listas extras que vão conter
apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas
geradas'''

num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resposta = str(input('Deseja continuar? [S/N] '))
    if resposta in 'nN':
        break
for i, v, in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A Lista de ímpares é {impares}')