larg = float(input('Largura da parede: '));
alt = float(input('Altura da parede: '));
area = larg * alt;
tinta = area / 2;
print('A dimensão da sua parede é de {}x{} e a area é {}m²'.format(larg, alt, area));
print('Para pintar essa parede voçê precisará de {}l de tinta'.format(tinta));