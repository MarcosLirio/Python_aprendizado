velocidade = float(input('digite a Velocidade atual do veículo: '));
if velocidade > 80:
    multa = (velocidade - 80) * 7;
    print('MULTADO! Voçê excedeu o limite de 80KM/h nesta via, e irá pagar uma multa de R${:.2f}'.format(multa));
else:
    print('Tenha um bom dia e continue dirigindo com prudência!');
