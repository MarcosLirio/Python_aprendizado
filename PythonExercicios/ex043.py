'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule o seu IMC e mostre seus status, de acordo com a tabela abaixo:
-Abaixo de 18.5: ABAIXO DO PESO     -25 até 30: SOBREPESO
-Entre 18.5 e 25: PESO IDEAL        -30 até 40: OBESIDADE
                                    -Acima de 40: obesidade mórbida'''

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso /(altura ** 2)
if imc < 18.5:
    print('O seu IMC é {:.1f}, voçê está abaixo do peso'.format(imc))
elif imc < 25:
    print('PARABÉNS! O seu IMC é {:.1f}, Voçê está no peso ideal'.format(imc))
elif imc < 30:
    print('ATENÇÃO! O seu IMC é {:.1f}, Voçê está no SOBREPESO!'.format(imc))
elif imc < 40:
    print('CUIDADO! O seu IMC é {:.1f}, Voçê está com obesidade'.format(imc))
else:
    print('PERIGO! O seu IMC é {:.1f}, Voçê está com OBESIDADE MÓRBIDA precisa se cuidar urgentemente'.format(imc))
