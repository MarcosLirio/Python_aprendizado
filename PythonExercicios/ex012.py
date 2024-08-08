'''Faça um algoritmo que leia o preço de um produto e mostre seu
novo preço, com 5% de desconto.'''
preco = float(input('Digite o valor da compra: R$'))
novo = preco - (preco * 5/100)
print('O valor total da compra com 5% de desconto agora é: R${:.2f}'.format(novo))