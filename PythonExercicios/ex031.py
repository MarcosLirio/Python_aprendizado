from time import sleep;
distancia = float(input('Digite a distância em KM da sua viagem: '));
print('processando...');
sleep(3)
if distancia <= 200:
    valor = distancia * 0.50;
    print('O valor da sua viagem ficará R${:.2f}'.format(valor));
else:
    valor = distancia * 0.45;
    print('O valora da sua viagem ficará R${:.2f}'.format(valor));