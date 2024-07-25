medida = float(input('Uma distância em metros: '));
cm = medida * 100;
mm = medida * 1000;
dam = medida * 10;
print('a medida {}m corresponde a:'
      ' \n{:.0f}cm \n{:.0f}mm'
      '\n{:.0f}dam'.format(medida, cm, mm, dam));