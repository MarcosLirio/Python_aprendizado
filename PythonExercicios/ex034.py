'''Escreva um programa que pergunte qual é o salário de um funcionário e
calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para inferiores ou iguais,o aumento é de 15%.'''

salario = float(input('Digite o seu salário: R$'))
if salario > 1250:
    aumento = (salario * 10) / 100
    salario = salario + aumento
    print('PARABÉNS! Voçê teve um aumento de 10% e agora o seu salário será: R%{:.2f}'.format(salario))
elif salario <= 1250:
    aumento = (salario * 15) / 100
    salario = salario + aumento
    print('PARABÉNS! Voçê teve um aumento de 15% e agora o seu salário será: R%{:.2f}'.format(salario))