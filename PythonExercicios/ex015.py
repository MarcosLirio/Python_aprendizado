'''EScreva um programa que pergunte a quantidade de KM
percorridos por um carro alugado e a quantidade de dias pelos
quais ele foi alugado. Calcule o peço a paga, sabendo que o carro
custa R$60 por dia e R$0,15 por km rodado'''

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km foram rodados? '))
total = (60 * dias) + (0.15 * km)
print('O total a se pagar é {}'.format(total))