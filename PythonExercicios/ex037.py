'''Escreva um programa que leia um número inteiro qualquer e peça
para o usuário escolher qual será a base de conversão:
-1 para Binário
-2 para octal
-3 para hexadecimal'''

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Digite a sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual á {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual á {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual á {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida!!!')