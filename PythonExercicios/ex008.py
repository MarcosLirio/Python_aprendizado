'''Escreva um programa que leia um valor em metros e exiba
convertido em centímetros e milímetros
km hm dam m dm cm mm'''

medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
dam = medida * 10
print('a medida {}m corresponde a:'
      ' \n{:.0f}cm \n{:.0f}mm'
      '\n{:.0f}dam'.format(medida, cm, mm, dam))