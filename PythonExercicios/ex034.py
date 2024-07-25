salario = float(input('Digite o seu salário: R$'));
if salario > 1250:
    aumento = (salario * 10) / 100;
    salario = salario + aumento;
    print('PARABÉNS! Voçê teve um aumento de 10% e agora o seu salário será: R%{:.2f}'.format(salario));
elif salario <= 1250:
    aumento = (salario * 15) / 100;
    salario = salario + aumento;
    print('PARABÉNS! Voçê teve um aumento de 15% e agora o seu salário será: R%{:.2f}'.format(salario));