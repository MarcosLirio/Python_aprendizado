'''Faça um programa que leia nome e média de
um aluno, guardando também a situação
em um dicionário. No final, mostre o
conteúdo da estrutura na tela'''

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input('Média: '))
print('-=' * 50)
if aluno['média'] < 5:
    aluno['situação'] = 'REPROVADO'
elif aluno['média'] >= 5 and aluno['média'] < 7:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = 'APROVADO'
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')