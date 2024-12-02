def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura} x {comprimento} é igual á {a}m².')


# Programa principal
print(' Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
