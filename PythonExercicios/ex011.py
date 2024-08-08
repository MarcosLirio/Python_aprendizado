'''Faça um programa que leia a largura e altura de uma parede em
metros, calcule a sua área e a quantidade de tinta necessária para
pintá-la, sabendo que cada litro de tinta, pinta uma área de 2 m²'''

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
tinta = area / 2
print('A dimensão da sua parede é de {}x{} e a area é {}m²'.format(larg, alt, area))
print('Para pintar essa parede voçê precisará de {}l de tinta'.format(tinta))