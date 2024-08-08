'''Escreva um programa para aprovar um empréstimo bancário para a
compra de uma casa. Pergunte o valor da casa, o salário do comprador
e em quantos anos ele vai pagar.
A prestação mensal, não pode exceder 30% do salário ou então o
empréstimo será negado'''

valor_casa = int(input('Digite o valor da casa: R$'))
anos_pagando = int(input('Em quantos anos será o pagamento? '))
valor_prestacao = valor_casa / (anos_pagando * 12)
minimo = salario * 30 / 100
print('O valor da prestação será R${:.2f}'.format(valor_prestacao))
salario = float(input('Qual é o salário do comprador? R$'))

if valor_prestacao <= minimo:
    print('EMPRÉSTIMO APROVADO! Agora voçê pode ir lá comprar sua casa.')
elif:
    print('Empréstimo NEGADO! O valor da prestação ultrapassa 30% do salário do comprador.')