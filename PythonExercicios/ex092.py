'''Crie um programa que leia nome, ano de nascimento e carteira de
trabalho e cadastre-os(com idade) em um dicionário se por
acaso a CTPS for diferente de zero, o dicionário receberá
também o ano de contratação e o salário. Calcule e acresente,
além da idade, com quantos anos a pessoa vai se aposentar'''
from datetime import datetime
trabalhador = dict()
trabalhador['nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano de nascimento: '))
trabalhador['idade'] = datetime.now().year - ano_nascimento
trabalhador['carteira_trabalho'] = int(input('Carteira de trabalho (0 não tem): '))
if trabalhador['carteira_trabalho'] != 0:
    trabalhador['ano_contratacao'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salário: R$'))
    trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['ano_contratacao'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in trabalhador.items():
    print(f'  -{k}: {v}')