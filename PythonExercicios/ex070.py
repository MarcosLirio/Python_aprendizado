'''Crie um programa que leia o nome e o         A) Qual é o total gasto na compra
preço de vários produtos. O programa            B) Quantos produtos custam mais de R$1000
deverá perguntar se o usuário vai               C) Qual é o nome do produto mais barato
continuar. No final, mostr:'''

total = acima1000 = maisbarato = cont = 0
maisbarato_nome = ''
print('{:=^70}'.format(' Loja Super Baratão '))
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if cont == 1 or preco < maisbarato:
        maisbarato = preco
        maisbarato_nome = produto
    if preco > 1000:
        acima1000 += 1
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
print('{:=^70}'.format(' Fim do Programa '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {acima1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {maisbarato_nome}')