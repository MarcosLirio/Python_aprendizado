n1 = float(input('Digite a primeira nota: '));
n2 = float(input('Digite a segunda nota: '));
media = (n1 + n2) / 2;
print('A sua média foi {:.1f}'.format(media));
#print('Parabéns voçê foi aprovado!' if media >= 6 else 'Voçê foi reprovado, Estude mais!');
if (media >= 6):
    print('Voçê foi aprovado!');
else:
    print('Voçê foi reprovado!');
