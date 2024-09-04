'''Desenvolva um programa que           A)Quantas vezes apareceu o valor 9
leia 4 valores pelo teclado e           B)Em que posição foi digitado o valor 3
guarde-os em um tupla . No final,       C)Quais foram os números pares
mostre:'''

valores = (int(input('Digite um valor: ')),
           int(input('Digite um valor: ')),
           int(input('Digite um valor: ')),
           int(input('Digite um valor: ')))
print(f'Voçê digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O valor 3 foi digitado na posição {valores.index(3)+1}')
else:
    print('Voçê não digitou o número 3')
print('Os valores pares digitados foram: ')
for n in valores:
    if n % 2 == 0:
        print(n, end=', ')