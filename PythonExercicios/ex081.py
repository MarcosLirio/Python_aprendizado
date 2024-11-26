'''Crie um programa que vai ler vários números e colocar em uma
lista. Depois disso mosrtre:
A)Quantos números foram digitados
B)A lista de valores, ordenada de forma decrescente.
C)Se o valor 5 foi digitado e está ou não na lista'''

valores = []
while True:
    valores.append(int(input('Digite um valor numérico: ')))
    resposta = str(input('Deseja continuar? [S/N] '))
    if resposta in 'Nn':
        break
print('-=' * 30)
print(f'Voçê digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores de forma decrescente são {valores}')
if 5 in valores:
    print(f'O valor 5 faz parte da lista')
else:
    print(f'O valor 5 não faz parte da lista')