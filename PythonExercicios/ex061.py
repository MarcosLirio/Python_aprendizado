'''Refaça o desafio 51, lendo o primeiro
termo e a razão de uma PA, mostrando
os 10 primeiros termos da progressão
usando estrutura while'''

print('Gerador de PA')
print('-=-' * 20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo = termo + razao
    cont += 1
print('FIM')
