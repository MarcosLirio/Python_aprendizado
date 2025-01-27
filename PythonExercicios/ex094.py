'''Crie um programa que leia nome,          A) Quantas pessoas cadastradas
sexo e idade de várias pessoas,             B) A média de idade
guardando os dados de cada pessoa           C) Uma lista com
em um dicionário e todos os dicionários     mulheres.
em uma lista. No final, mostre:             D) Uma lista com idade acima da média'''

cadastros = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MmFf':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    cadastros.append(pessoa.copy())
    while True:
        stop = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if stop in 'SN':
            break
        print('ERRO! Resposta errada, responda apenas S ou N.')
    if stop == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(cadastros)} pessoas cadastradas.')
media = soma / len(cadastros)
print(f'B) A média de idades é de {media:5.2f} anos')
print(f'C) As mulheres cadastradas foram ', end='')
for p in cadastros:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}, ', end='')
print()
print(f'D) Lista de pessoas que estão com idade acima da média: ', end='')
for p in cadastros:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<< ENCERRADO >>>')  