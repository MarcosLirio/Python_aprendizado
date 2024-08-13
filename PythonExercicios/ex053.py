'''Crie um programa que leia        EX:
uma frase qualquer e diga           Apos a Sopa
se ela é um palíndromo,             A sacada da casa
desconsiderando os                  A torre da derrota
espaços                             O lobo ama o bolo
                                    Anotaram a data da maratona'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
#inverso = ''
'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é palíndromo!')