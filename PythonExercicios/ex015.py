dias = int(input('Quantos dias alugados? '));
km = float(input('Quantos km foram rodados? '));
total = (60 * dias) + (0.15 * km);
print('O total a se pagar é {}'.format(total));