'''Elabore um programa que calcule o valor a ser pago por uma compra,
considerando o seu preço normal e condições de pagamento:
-À vista dinheiro/pix: 10% de desconto      -Em até 2x no cartão: Preço normal
-À vista no cartão: 5% de desconto          -3x ou mais no cartão: 20% de juros'''

print('{:=^40}'.format(' Markinhos Store '))
valor_compra = int(input('Valor da compra: R$'))
print('''FORMAS DE PAGAMENTO: 
[ 1 ] À vista dinheiro/pix (10% desconto)
[ 2 ] À vista cartão (5% desconto)
[ 3 ] 2x no cartão (preço normal)
[ 4 ] 3x ou mais no cartão (20% juros)''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    print('Valor da compra: R${:.2f} \nDesconto: 10%'.format(valor_compra))
    desconto =  10 * valor_compra /100
    valor_final = valor_compra - desconto
    print('Valor final: R${:.2f}'.format(valor_final))
elif opcao == 2:
    print('Valor da compra: R${:.2f} \nDesconto: 5%'.format(valor_compra))
    desconto = 5 * valor_compra / 100
    valor_final = valor_compra - desconto
    print('Valor final R${:.2f}'.format(valor_final))
elif opcao == 3:
    valor_parcelas = valor_compra /2
    print('Valor da compra: R${:.2f} \nParcelas: 2 \nValor das parcelas: R${:.2f}'.format(valor_compra, valor_parcelas))
elif opcao == 4:
    juros = 20 * valor_compra / 100
    valor_final = valor_compra + juros
    parcelas = int(input('Em quantas parecelas? '))
    valor_parcelas = valor_final / parcelas
    print('Valor da Compra: R${:.2f} \nJuros: {:.2f} \nValor Parcelas: {:.2f} \n Valor Final: {:.2f'.format(valor_compra, juros, valor_parcelas, valor_final))
else:
    print('Opção inválida! Tente novamente.')