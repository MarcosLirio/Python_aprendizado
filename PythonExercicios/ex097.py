'''
Faça um programa que tenha uma função        Ex:
chamada escreva(), que receba um texto          escreva('Olá, Mundo!')
qualquer como parâmetro e mostre uma            Saída:
mensagem com tamanho adaptável.                  ~~~~~~~~~~~~~~~~~~
                                                    Olá, Mundo!
                                                 ~~~~~~~~~~~~~~~~~~
'''


def escreva(msg):
    tamanho = len(msg) + 4
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)


# Programa principal
mensagem1 = str(input('Escreva alguma coisa: '))
mensagem2 = str(input('Escreva outra coisa: '))
mensagem3 = str(input('Escreva a última coisa: '))
escreva(mensagem1)
escreva(mensagem2)
escreva(mensagem3)

