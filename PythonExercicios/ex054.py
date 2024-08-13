'''Crie um programa que leia o ano
de nascimento de sete pessoas. No
final, mostre quantas pessoas
ainda não atingiram a maioridade e
quantos já são maiores'''

from datetime import date
ano_atual = date.today().year
cont_maior = 0
cont_menor = 0
for c in range(1, 8):
    nascimento = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = ano_atual - nascimento
    if idade >= 18:
       cont_maior = cont_maior + 1
    else:
        cont_menor = cont_menor + 1
print('''Ao todo temos {} pessoas maiores de idade \ne também {} pessoas menores de idade'''.format(cont_maior, cont_menor))

