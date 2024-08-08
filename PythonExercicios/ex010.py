'''Crie um programa que leia quanto dinheiro uma pessoa têm na
carteira e quantos dolares ela pode comprar.
considere US$1 = R$3,27'''

real = float(input('Quanto de dinheiro voçê têm na carteira?'))
dolar = real / 3.27
print('Com R${} voçê pode compar U${:.2f}'.format(real, dolar))