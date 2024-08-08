'''Crie um programa que leia o nome completo de uma pessoa e
mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo(sem considerar espaços)
- Quantas letras têm o primeiro nome'''

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando o seu nome, em letras maiúsculas fica: {}'.format(nome.upper()))
print('Analisando o seu nome, em letras minúsculas fica: {}'.format(nome.lower()))
print('Seu nome ao todo têm {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome têm {} letras'.format(nome.find(' ')))
separa = nome.split()
print(separa)
print('Seu primeiro nome é: {} e ele têm {} letras'.format(separa[0], len(separa[0])))