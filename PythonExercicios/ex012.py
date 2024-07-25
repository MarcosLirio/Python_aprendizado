preco = float(input('Digite o valor da compra: R$'));
novo = preco - (preco * 5/100);
print('O valor total da compra com 5% de desconto agora é: R${:.2f}'.format(novo));