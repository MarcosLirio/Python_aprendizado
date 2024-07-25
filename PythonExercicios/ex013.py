salario = float(input('Digite o valor do Salário: R$'));
reajuste = salario + (salario * 15/100);
print('Um funcionário que recebia R${:.2f}, com um reajuste de 15% agora passa a receber R${:.2f}'.format(salario, reajuste));